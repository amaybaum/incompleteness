# Reconstruction round KT4-PREM-1 — premise audit of the Pauli-free four-copy theorem: countermodels hypothesis by hypothesis, the pair-level completion and action route, and the source map: PREREGISTRATION

**Status: candidate freeze.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted
on its pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The questions, the decision rules, the earned reading, the non-inference rule, the frozen probe, the workflow edit, the
controls, the stages and the outcomes below are fixed; the predicted execution tree is recorded before `F`.

```v3-round
round KT4-PREM-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-kt4-prem-1-premise-audit/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-kt4-prem-1-premise-audit/
record AM verification/receipts/KT4-PREM-1.json
execution A verification/lean/kt4_prem1_probe.py
execution M .github/workflows/verify.yml
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/KT4-PREM-1.json`. Every other path the round changes is an execution path listed
above. **No manuscript, no built artifact, no Lean module, `verification/ROADMAP.md`, the census and no other round's
record change under any outcome.**

## The objects

- **`D`** = `bcbc516fe78eb7aa303a41e7bc9cc106dd63bd58`, the head of `main` after round RELC-SELECT-1 landed (merge of
  `Q` `eecdecdf`), certified by push run 37755552123.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

## What the round is

The round audits the five hypotheses of one theorem: which implications among them and the theorem's conclusion fail,
what certified `main` supplies toward each, and what each would still need. It proves no theorem in the kernel and adds
no Lean module. Its exact layer is one probe, replayed in CI; its written layer is stated in the result note beside the
checks it rests on; the two layers are reported separately and neither stands in for the other.

### The audited statement

The theorem is `OIBridge.FourCopy.kt4_forward_ie1` of the design module `FourCopyHeadline` at the design commit
`ff9c3a358c57ce938978f15f2915d2145ae7b4a5` (blob `a254873d8d8fccf59bdd63444e64ef0ef3c5084f`), on the branch
`claude/network-tool-access-8jtdhm`. It is not on `D`. Its vocabulary is in the design modules `FourCopyDefs`
(`2346e7d9`), `FourCopyCore` (`6a17a420`), `FourCopyBridge` (`7e19f5a5`), `FourCopyBipolar` (`0e080e5f`) and
`FourCopyIE1` (`65cc5bcb`) at the same commit. In design run 37948419430 at that commit `#print axioms` reports
`[propext, Classical.choice, Quot.sound]` for the theorem; the run's release gate failed on modules outside the
theorem's dependency closure, so the theorem is kernel-checked in a design run and is not certified. The round audits
the mathematical statement below, which it states from that text; it does not certify the design modules, and nothing
in it depends on their landing.

For four pair cones `K_p ⊆ W 3` (`p = 01, 23, 02, 13`), gates `N_p` and one-copy linear maps `A_p, B_p, A'_p, B'_p`:

| name | statement |
|---|---|
| `hcls` | `N_p = actC A_p ∘ actT B_p ∘ cnot ∘ actC A'_p ∘ actT B'_p` with the four maps orthogonal (`NClass`) |
| `hadm` | `K_p` contains `prodState x y` for all `x, y ∈ eball 3`, lies in `maxCone (eball 3)`, and is a convex cone (`PairAdm`) |
| `hcl` | `K_p` is closed |
| `hgate` | `N_p` maps `K_p` into `K_p` |
| `H` | a `KT4Core` structure on `(K_01, K_23, K_02, K_13)` over a real normed carrier `V` |

The conclusion `C`: every `K_p` is invariant under `actC R` and `actT R` for every rotation `R` (`IE1`), and the number
of pairs with `det A_p · det B_p = −1` is even (`EvenCycle`). `cnot`, `actC`, `actT`, `prodState`, `maxCone` and the
tables `phiW`, `idW`, `chainW` are the landed definitions of `CompositeDimension` and `K2Guard` at `D`.

### The three questions

- **Q1 — the countermodels.** For the closedness foil `M_cl` and the maximal-cone model `M_max`, does each of the five
  hypotheses hold or fail, at which verification layer, and which implication does each model refute? For the
  remaining models `M_D`, `M_refl`, `M_id`, `M_class`, `M_mix`, `M_int`, `M_tok` and `M_tokC`, the same. Does a
  written argument with exactly checked finite steps make `hcl` necessary relative to `hcls`, `hadm`, `hgate` and the
  conclusion?
- **Q2 — the pair-level completion and action route.** Does `D` imply closedness or gate preservation for a composite
  of two balls, and what would a pair-level completion and action route need, stated so that it introduces neither
  gate preservation nor idle extension without naming it?
- **Q3 — the source map.** For `hcls`, `hadm` and the token clauses (and, from Q2, `hcl` and `hgate`): which landed
  declarations bear on each, which additional principles a route needs, and which exact countermodels apply?

### The cells

Each cell is read by its own frozen rule (below) from the probe's output at `E` and, for Q2 and Q3, from the landed texts
at `D`. No rule reads another cell's outcome.

| cell | question | positive outcome |
|---|---|---|
| `Q1-CL` | `M_cl` satisfies `hcls`, `hadm`, `hgate` and `H`, and fails `hcl` and IE₁ | `CLOSEDNESS-FOIL-VERIFIED` |
| `Q1-MAX` | `M_max` satisfies `hcls`, `hadm`, `hcl`, `H` and `C`, and fails `hgate` | `MAXCONE-MODEL-VERIFIED` |
| `Q1-MAP` | the remaining models satisfy and fail the clauses their rows state | `COUNTERMODEL-MATRIX-VERIFIED` |
| `Q1-NEC` | the finite steps of the classification argument hold exactly | `CLASSIFICATION-STEPS-VERIFIED` |
| `Q2` | the composite interface at `D` admits a non-closed body and bodies `cnot` does not preserve, and the completion layer at `D` is typed for one system | `PAIR-ROUTE-GAP-VERIFIED` |
| `Q3` | the landed declarations the source map cites resolve at `D` | `SOURCE-MAP-CITATIONS-VERIFIED` |

Each cell's other outcome is its token with `-NOT-ESTABLISHED` in place of the last word (`CLOSEDNESS-FOIL-NOT-ESTABLISHED`,
and so on).

### The earned reading (frozen)

> The hypothesis hcl cannot be dropped from the Pauli-free four-copy theorem: the closedness foil satisfies hcls, hadm,
> hgate and H and fails IE1. The hypothesis hgate is not necessary relative to hcls, hadm, hcl, H and the conclusion:
> the maximal-cone model satisfies all of them and fails hgate; this does not show that hgate can be removed, and the
> D-gate model refutes the implication without it. Each of hcls, hadm, hgate and the token clauses cannot be dropped,
> and each of hcls, hadm and the token clauses of the given data is not necessary, by the models of the matrix. Under
> hadm, H is equivalent to the cone-level interface FCC, one direction by Lemma B1 of the design modules and the other
> by an explicit carrier. Certified main supplies neither closedness nor gate preservation for a composite of two
> balls; a pair-level completion supplies closedness only from a new premise, and gate preservation only from a
> premise that states it on preparations.

The result note states this reading in these words exactly when all six cells are positive, and not otherwise.

### The non-inference rule (frozen)

> This round adopts no premise, sources none of the five hypotheses, and makes no manuscript claim and no ROADMAP claim.
> Its countermodels are models of the hypothesis sets they are stated for and of nothing more; none is a physical
> theory. The necessity of hcl relative to hcls, hadm, hgate and the conclusion rests on a written argument with one
> standard input from Lie theory and is not kernel-checked; the probe checks its finite steps only. The audited
> theorem is kernel-checked in a design run and is not certified. Nothing here says that the observational axioms force
> quantum cones: the classification of a pair cone as Q3 or its twin holds relative to N-CLASS gates, admissible cones,
> gate preservation and IE1, none of which is sourced.

The result note states this rule in these words under every outcome.

### The decision rules (frozen; implemented by `controls.py verdict`)

`P(ids)` means: the probe blob at `E`, run by `controls.py` with `python3 -I` from a checkout of `E`'s tree, prints a
`PASS` line for every check id in `ids` and no `FAIL` line for any of them. `S0` is the transcription set `S0.sgn`,
`S0.pc`, `S0.pt`, `S0.phiW`, `S0.idW`, `S0.chainW`, `S0.reflY`; `DICT` is `D1`–`D7`; `CARRIER` is `H1`–`H10`.

| cell | positive iff |
|---|---|
| `Q1-CL` | `P(S0 ∪ DICT ∪ CARRIER ∪ {F0, F1, F2, F3, F2v, F2s, M_cl.1, M_cl.5, M_cl.6, M_cl.7, M_cl.8, M_cl.9, M_cl.10, M_cl.11, M_cl.12})` |
| `Q1-MAX` | `P(S0 ∪ DICT ∪ CARRIER ∪ {F4, F5, F6, M_max.2, M_max.3, M_max.4, M_max.6, X6})` |
| `Q1-MAP` | `P(S0 ∪ DICT ∪ CARRIER ∪ {F7, F8, F9, F10, M_D.1, M_D.2, M_refl.1, M_id.1, M_class.1, M_class.2, M_class.3, M_class.4, M_mix.1, M_int.1, M_int.2, T1, T2, T3, T4, X5})` |
| `Q1-NEC` | `P(S0 ∪ {D1, D7, C1, C2, C3, C4, C5, C6, M_max.4})` |
| `Q2` | `P(S0 ∪ {I1, I2, M_cl.7, M_cl.8, M_cl.9, M_max.3, M_max.4})`, and the landed texts at `D` contain the frozen COMP-1 scope sentence and the frozen completion-layer declarations (below) |
| `Q3` | every declaration of the frozen citation list resolves at `D` in its frozen file |

The probe's countercontrols `X1`–`X4` are read by every cell: a cell is positive only if they pass as well.

**The frozen COMP-1 scope sentence**, whitespace-normalized, in `CompositeInterface.lean` at `D`: "The stage-level
product of two `DirectedStages` and the bridge from completed product towers to this interface are not part of this
module." **The frozen completion-layer declarations** at `D`: `body` in `StageCompletion.lean` (the closed convex hull
of the preparation vectors), `body_isClosed`, `OpDatum`, `Undoes` and `preservesBody_inducedEquiv` in
`CompletionAction.lean`, each with the statement embedded in `controls.py`; and the only declarations of the form
`noncomputable def <name> : DirectedStages where` in `verification/lean-mathlib/OIBridge/` at `D` are `badD`,
`bitTower` and `midD`, each a system of one copy's stages.

**The frozen citation list** (Q3), by file at `D`: `CompositeDimension.lean` — `cnot`, `phiW`, `prodState`, `pairVal`,
`prodEffVal`, `maxCone`, `actT`, `actC`, `IsNot`, `NativeGate`, `nativeGate_cnot`, `cnot_prodState_xplus_z3`;
`K2Guard.lean` — `CandidateCone`, `idW`, `chainW`, `cnot_idW`, `chain_eq`, `chain_value`,
`no_candidateCone_cnot_reflY`, `prodState_mem_maxCone`, `actT_reflY_phiW`; `CompositeInterface.lean` — `ProductData`,
`PreComposite`, `Composite`, `LocallyTomographic`, `minBody`, `maxBody`, `subset_maxBody`, `JointReversible`,
`modelData_ext`, `prodEff_eq_of_eff_eq`, `minComposite`, `maxComposite`, `ball3MinComposite`, `ball3MaxComposite`;
`StageCompletion.lean` — `body`; `CompletionAction.lean` — `OpDatum`, `AffineRespect`, `Undoes`, `body_isClosed`,
`induced_mem`, `preservesBody_inducedEquiv`; `RelcSelectBlock.lean` — `CtrlGate`, `dim_of_ctrlGate`,
`three_of_ctrlGate`.

The round's outcome is `KT4-PREM-1-READ` when all six cells are assigned, each by its own rule. The design run below
already exhibits a probe read by these rules as all six positive tokens; the rules, not that reading, are what this
file freezes, and the cells at `E` are those `controls.py verdict E` prints.

## The frozen probe

`verification/lean/kt4_prem1_probe.py`, blob **`<PROBE_BLOB>`**, is written before `F` and added at S1 unchanged. It
imports the Python standard library (`re`, `sys`, `itertools`, `pathlib`) and `sympy`, pinned at `1.14.0` in its
workflow shard. Exact arithmetic only: sympy rationals, Gaussian rationals and symbolic identities. It reads
`CompositeDimension.lean` and `K2Guard.lean` read-only, to check its transcription of `sgn`, `pc`, `pt`, `phiW`, `idW`,
`chainW` and `reflY`. It runs every check, prints one `PASS` or `FAIL` line per check, and ends with
`kt4_prem1_probe: OK -- 79 checks` or with `kt4_prem1_probe: FAILED -- …` and exit status 1. Each check is labelled with
its kind — `identity`, `witness`, `enumerate`, `source`, `sample` or `countercontrol` — and every written step is printed
as a `NOTE [written]` line beside the checks it rests on.

What the probe establishes at each layer, and what it does not, is fixed here:

- **The carrier for `H`** (S2): `V = ℝ^{17×17} × ℝ^{17×17}` with `stA x y = (x̂ŷᵀ, 0)` and `stB x y = (0, x̂ŷᵀ)`.
  - Exact identities: the evaluation laws, bilinearity, the 256 token identities of each kind, and the cross values as
    four-copy contractions.
  - Written: an effect on a pair body of a cone inside `maxCone` is a table of the dual cone, so FCC, the maxCone bound
    and scaling give every field of `KT4Core`.
- **FCC for `Q3` and for `maxCone`** (S3).
  - Exact bookkeeping identities: the contraction is the trace pairing of the Kronecker-ordered operators.
  - Written, with a standard input: the Kronecker product of positive semidefinite matrices is positive semidefinite.
  - For `maxCone`: exact identities, the Lagrange identity, and a written self-duality step.
- **The models** (S4–S7): exact witnesses for every failing clause, exact identities for the reductions, and written
  steps where a clause quantifies over an infinite set.
- **The classification** (S8): its finite steps only. The step from the generated Lie algebra to the generated group
  is a standard result of Lie theory and is not checked.

## The workflow edit (frozen)

`.github/workflows/verify.yml` changes by one edit in five places. The round's probe runs in a shard of its own,
`probes_kt4prem1`, `Numerical probes / KT4-PREM-1 premise audit`, inserted after the KINF-2 shard. It installs `sympy`
at the pinned version `1.14.0` and runs `python3 kt4_prem1_probe.py` from `verification/lean`. In the aggregate
`Numerical probes` job:

- `probes_kt4prem1` is added after `probes_kinf2` in `needs`;
- `KT4PREM1_RESULT: ${{ needs.probes_kt4prem1.result }}` is added after `KINF2_RESULT`;
- `echo "kt4prem1=${KT4PREM1_RESULT}"` is added after the KINF-2 echo;
- `test "${KT4PREM1_RESULT}" = success` is added after the KINF-2 test.

`controls.py` checks that the workflow at `E` is `D`'s with exactly that edit.

## The controls (in `controls.py`)

- **L landed.** The texts read at `D` are the frozen ones: the COMP-1 scope sentence, the completion-layer
  declarations, the `DirectedStages` census, the citation list, and the definitions the probe transcribes.
- **P probe.** The probe at `S1` and at `E` is the frozen blob.
- **W workflow.** The workflow at `S1` and at `E` is `D`'s with exactly the frozen edit.
- **R record.** At `E`, the record directory holds exactly `preregistration.md`, `controls.py` and `result.md`. This
  preregistration is unchanged from `F`, and `F` is `D` plus this file alone.
- **G governed paths.** `delta(D, E)` is exactly the record paths and the two execution paths.
- **V verdicts.** Each cell yields one outcome by its own rule. At a commit carrying the result note:
  - the note contains exactly the six computed tokens and no other;
  - it states the frozen earned reading exactly when all six are positive;
  - it states the frozen non-inference rule;
  - it carries the probe's summary line from the run at `E`.
- **S8 phrases.** Outside the two frozen texts, the result note contains none of the frozen phrases (case-insensitive,
  backticks removed, whitespace-normalized). They are: "observational axioms force", "OI forces", "forces quantum",
  "is sourced", "are sourced", "adopt", "hgate can be dropped", "hgate can be removed", "hgate is redundant",
  "hgate is unnecessary", "without hgate the theorem", "hcl is redundant", "proves that hcl is necessary",
  "kernel-checked necessity", "certified theorem" and "physical theory".
- **Self-test.** `controls.py --self-test` drives a mutation through each control; every mutation must fail with its
  named code. The mutations are:
  - a probe with one check id renamed;
  - a probe with one witness value changed;
  - a workflow without the aggregate `test` line;
  - a result note with an extra token;
  - a result note with the earned reading altered;
  - a result note carrying "hgate can be dropped";
  - a landed scope sentence that differs;
  - a third `DirectedStages` definition at `D`;
  - a citation that does not resolve.

## Design evidence

Design runs on the disposable branch `claude/network-tool-access-8jtdhm`. That branch carries the design commits of the
audited theorem, whose release gate fails on modules outside this round, so the evidence read from these runs is the
probe shard and the aggregate probe job.

| run | commit (probe blob) | workflow run | result |
|---|---|---|---|
| 1 | `<C1>` (`<PROBE_BLOB>`) | `<RUN1>` | `<to be recorded>` |

### The predicted execution tree

`<to be recorded: a single-parent child of D carrying the record directory less the result note, the probe and the
workflow edit, with its exact-head run>`

## Stages

1. **C1** adds `controls.py`, blob `<CONTROLS_BLOB>`, to the record directory. Acceptance: the blob is the frozen blob,
   and `controls.py --self-test` passes.
2. **S1** adds the probe and the workflow edit in one commit. Acceptance:
   - `controls.py check S1 --freeze F` passes;
   - the exact-head run at S1 has every job green, the KT4-PREM-1 shard printing `kt4_prem1_probe: OK -- 79 checks`.
3. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F` passes,
   the result note included in S8 and V, and the exact-head run at `E` has every job green.

A repair after S1 may change nothing in the probe's checks, values or kinds; a probe that fails at S1 halts the round.

## Outcomes

- **`KT4-PREM-1-READ`**: all of the following hold.
  - `controls.py check E --freeze F` prints `controls: OK`.
  - `controls.py verdict E` prints exactly one outcome for each cell.
  - The exact-head run at `E` is green on every job.
  - The result note states each cell's outcome, the earned reading in its frozen words when all six cells are
    positive, and the non-inference rule.
- **`KT4-PREM-1-HALTED`**: anything else. The round halts under the specification's `S12`, and the result note names
  the failing check or job.

No outcome adopts a premise, sources a hypothesis, or edits the ROADMAP or a manuscript. Correctness bands are unchanged
by either outcome: the round is consistency-axis work.
