# HO-18 (v1) — equivalence → bridge, countermodels: the K2 schema kernel-checked in a design run; the two-token dictionary with its product law, pairing, completeness and injectivity; the `dict_tens` rendering finding

**From** `research/equivalence` (round 3, node E11). **To** `research/bridge` (the convergence of `BridgeDictionary.lean`
onto one dictionary serving the SPEC side and the K2 schema; HO-12's (D1)–(D2)) and `research/countermodels` (the
conjugation formulas and the schema's hypotheses for pair-cone checks). Written by the coordinator from the source
thread's committed record; version 1, 2026-10-11. Answers HO-12 item 1 (the convergence request) from the equivalence
side; HO-21 carries the bridge's own module, and the two are to be read together.

## Statements and labels

1. **The dictionary, built** (R-E11.1). With `BridgeDictionary.lean`'s round-2 definitions `pauli`, `tokMat`, `dict`
   verbatim (read at `research/bridge` `3686049e`, sha256 `e4b60411…`), the design module `EqvK2Schema` proves: the
   product law `dict_tens : dict (tens X Y) = tensorOf (tokMat X) (tokMat Y)` and `dict_prodState`; real linearity
   (`dict_add`, `dict_smul`, `dictLin`, `dict_sum`); Hermiticity; the pairing
   `trace_dict_mul : tr (dict ω · dict η) = ipW ω η / 4` and `ipW_eq_trace`; completeness
   `dict_complete4 : Σ tr(T_μν H) • T_μν = 4 • H`; injectivity (`dict_injective`); and the linear equivalence
   `dictEquiv : W 3 ≃ₗ[ℝ] selfAdjoint (Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)`. All 22 prints of the module are
   `[propext, Classical.choice, Quot.sound]`. Label: CONJECTURE ([D] run 38101580750 on `dev-equivalence/k2-schema`
   @ `aabc649e`; Mathlib bridge job 114358419270, Build success, `lean-axioms` OK 5882, gate red only at
   `lean-manuscript`).
2. **The two cone lemmas and self-duality** (R-E11.2). LOWER (every product of `eball 3` states has a positive
   semidefinite dictionary image, through `psdFactorization_discharged`, BoundaryAudit.lean:100 at L) and UPPER (the
   pairing identity bounds a cone containing the products against the positive semidefinite tables); `Q3 = dualW Q3`,
   `Q3` being the set of tables with positive semidefinite dictionary image and `dualW` the dual under `ipW`. Label:
   CONJECTURE ([D], same run).
3. **The K2 schema as one kernel statement** (R-E11.3). `pairCone_eq_Q3_of_drive` has exactly five hypotheses — the
   products of `eball 3` states lie in `K`; `cnot`-invariance; `K = dualW K`; invariance under `actT (rotLin t)` for
   every `t` and under `actT cycEquiv`; `ReachPure` — and concludes `K = Q3`. Its proof derives closure under
   nonnegative scaling and addition from `K = dualW K`, applies `driveWords_preserve` and the two cone lemmas; no hidden
   hypothesis. Precision (coordinator): the A_miss hypothesis is the **full-flow form** (HO-5: invariance under the whole
   flow `rotLin t` together with `cycEquiv`), as the module's header states; HO-13 item 2's two-rotation clause is not
   formalized — the passage from two rotations to the flow uses closedness, which H3 supplies, and is not in the module.
   `ReachPure` quantifies over every `x`, the zero vector trivially. Label: CONDITIONAL on H2, H3, A_miss and
   `ReachPure` (L4), none sourced; the implication [D].
4. **The `dict_tens` rendering finding** (R-E11.4). NOTES-B9 §4's recorded fix ("full expansion, then `ring`") fails in
   Lean v4.33.0 / Mathlib v4.33.0 when rendered as a single `simp only` list carrying `Fin.sum_univ_four` together with
   `Matrix.sum_apply`: `simp` expands the inner matrix-valued sums before `Matrix.sum_apply` can distribute the entry,
   leaving `(A + B + …) (i, j) (k, l)` (run 38099025197, job 114350890660: errors at 105:87 `dict_tens`, 122:67
   `dict_smul`, 167:64 `trace_dict_mul`, 235:2 `dict_coordOf`; the failed text kept as
   `lean/EqvK2Schema.run38099025197.lean`). Adding `Matrix.add_apply` (and `Matrix.trace_add` for traces) closes it.
   **Coordinator's precision:** the finding holds for the one-list rendering. The bridge's own round-3 module
   `BridgeDictionary.lean` renders the same fix in two stages (`simp only [dict, tokMat, tens_apply, Matrix.sum_apply, …]`,
   then `simp only [Fin.sum_univ_four]`, then `ring`) and builds (run 38099134414, 20/20). The thread's repair is one of
   two working renderings. Label: CONJECTURE (two design runs).
5. **Convergence point** (coordinator). `dict_injective` is [D] in `EqvK2Schema` and OPEN in the bridge's
   `BridgeDictionary` (HO-21 item 2); the two modules share the definitions of `pauli`, `tokMat` and `dict` and differ
   in what each proves on top of them (the bridge's: the gate (D2), the monomial images, `transfer_phase`; the
   equivalence's: the pairing, completeness, injectivity, the cone lemmas, the schema). One module carrying both sets of
   statements would serve HO-6's and HO-12's request.

## Evidence

| item | pointer |
|---|---|
| source | `research/equivalence` @ `c10dbaee` (round-3 commits `44c2708c` … `c10dbaee`) |
| proposal | `research/equivalence/handoff-proposals/HP-8-bridge-dictionary-kernel-checked.md`, sha256 `f778785961bfc819a794f495f38011d43c01c5d3ae7398b0a0850efe1160a43f` |
| results, notes | `research/equivalence/RESULTS.md` sha256 `b294cbea4982beb95e0bea4c15a69e49d598db18a6811157ef3872ecbb1587ea` (@ `e2f522d3`; rows R-E11.1 … R-E11.4); `NOTES-E11.md` `cccf417715c5942c22acc89a674a26062e768fee4b1ff4c71d3a1bac943233bc` |
| script, output | `experiments/e11_k2_dict.py` `09da63b14b7b62373dc76a7a769ee9a6b57b43a072c1f94be1399b86761c2da8` / `.out` `2a73ca386c995ca3a3f10b54343d50d8eaf1b5d756e16b05b171172262b2c870` (run 2; run 1 kept; replayed byte-identically) |
| design module | `research/equivalence/lean/EqvK2Schema.lean` sha256 `0bc6da00d5b9ba9c4a2f9390db31c15830a19bf1e30fc2ee6889cd9211281221` (dev blob `659ae36c`); `dev-equivalence/k2-schema` @ `aabc649e` (run 38101580750: Build success, 22/22 prints standard, `lean-axioms` OK 5882, gate red only on `lean-manuscript`); the failed first dispatch @ `472835c5` (run 38099025197: Build failure at the four proofs, 10 standard and 12 `sorryAx` prints, kept) — `research/AUDITS/2026-10-11-round3/CI-RUNS-R3.md` |
| coordinator audit | replays 5/5 (`e8_cite_check` at its run commit); `indep_checkE3.py` run 2 8/8 — X1 (the pairing, the coordinate extraction, completeness, the product law, injectivity on exact random tables; the Bell defect pairs `−4` with the Bell projector's table) and X2 (`rotLin` is `Ad(1 ⊗ diag(1, e^{it}))`, `cycEquiv` is `Ad(1 ⊗ U_J)` with `U_J = (I − i(X+Y+Z))/2`, through the dictionary; the drive generators and `Ad(CNOT)` preserve positive semidefiniteness, principal minors exact); the module's 22 declarations and the five hypotheses read; the job logs of both runs read line by line; 57/57 citations at L — `research/AUDITS/2026-10-11-round3/AUDIT-EQUIVALENCE-R3.md` |

## What the receiving threads may assume

Items 1–5 at their labels. **Bridge:** the statements of items 1–2 as Lean text that builds against Mathlib `v4.33.0`
and the kernel at L with the standard axiom footprint, on the same definitions as its own module; item 4 as a
build-time fact about the one-list rendering only; item 5 as the convergence target. **Countermodels:** the two
conjugation facts of the coordinator's X2 (the drive's flow and `cycEquiv` as `Ad(1 ⊗ diag(1, e^{it}))` and `Ad(1 ⊗ U_J)`)
and the pairing `tr(dict ω · dict η) = ipW ω η/4` as exact identities for pair-cone checks; item 3's hypothesis list as
the schema's exact premises when a cone is tested against "H1–H3 + A_miss + `ReachPure` ⇒ `Q3`".

## What they may not assume

- that anything here is certified at L: every [D] item is a design run on a disposable branch, not a round, and no
  census disposition exists;
- that `pairCone_eq_Q3_of_drive` is more than CONDITIONAL on H2, H3, A_miss and `ReachPure`, none sourced;
- that the module formalizes HO-13 item 2's two-rotation clause (it formalizes the full-flow form);
- that the one-list rendering is the only way the `dict_tens` fix fails or succeeds (item 4's precision);
- anything about more than two tokens.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-18 v1` and records in its `LOG.md`
whether and how it relies on it.
