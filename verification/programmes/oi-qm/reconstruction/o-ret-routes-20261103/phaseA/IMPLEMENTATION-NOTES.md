# O-RET Phase A: implementation notes for the test tool and workflow

**Status.** WIP / UNVERIFIED. The tool and workflow were written under the owner's authorization of 2026-11-04
(#1032). They implement the preregistration frozen at `F = 49f0bd41c5323d2191b580460c8703740dd01b30`. Not reviewed
and not run. Dispatch is a separate owner approval (PREREG §7, AGENTS.md §A.43 item 4).

- `phaseA/phasea.py`: the tool. Standard library only, with exact `fractions.Fraction` arithmetic throughout.
- `.github/workflows/oret-phasea.yml`: the workflow, triggered by `workflow_dispatch` only.
- The four frozen inputs in the parent directory are read and hash-checked. They are never written.

## 1. Where each PREREG section lives in the code

| PREREG | Code |
|---|---|
| §2.0 conventions: `ε* = 1/20`, `W_T`, `H_T`, window convention | `EPS_STAR`, `gt_eps` (exact `>`), `compute_record` (`hold`, `win`, `holdp`, `winp`) |
| §2.0 independence and support conditioning under `μ^P` | `compute_record`: `tabP`, `J1`, `C_cells`, `suppQ`, `suppR`, `eta` |
| §2.0 metrics `ε_max`, `TV`; D-MET item 4 `failures` | `eps_with`, `tv`, `failures` |
| §2.0 dependence `B = Q = Par(A)∖A` from `φ` on all of `S` | `FullMethod.__init__` (φ table), `par_restricted` (sequential), `build_fR` |
| §2.0 arithmetic, exactness | `exact`, `rat`, `parse_rat`, `no_float`, `load_json_bytes` (float literals rejected) |
| §2.0 full method, injectivity (exit 5) | `FullMethod` |
| §2.0 sequential method and its two conditions (exit 5) | `SequentialMethod`, `product_marginals`, `Model.provenance_step`, `_origins` |
| §2.0 validation on orders 32–43 (exit 5) | `evaluate_tuple` for `full+sequential`; `method_for` derives the method from §2.0 |
| §2.3, §2.4 pooled `𝒬`, `τ`, `T′` | `compute_record`, `compute_tau` |
| §2.5 `w`, `w_chg` | `compute_record` (`is_sk` branch) |
| §2.8 `write_min_eps`, MD-xor sweep | `compute_record` (`decoders`, `sweep`) |
| §3 models, laws, cell order, simultaneous steps | `Model`, `CELL_SPECS`, `arith`, `subst`, `expand_conj`, `parse_ranges`, `parse_expr`, `validate_law`, `law_support` |
| §3.2 `D` | `d_bits` |
| §4 computed objects, `G`-rule | `classes_of`, `consistent`, `g_star`, `compute_record` |
| §4 steps 0–8 (exit 4 at step 6 only) | `assign_row`; readback rows in `compute_record` |
| §4 PASS (the three in-job signals) | run step exit status; `--check-summary` (regenerated `verdict_text`); marker step on `summary.json` |
| §5 outputs, encodings, verdict texts, exits | `build_output`, `check_record_schema`, `render_verdict`, `run`, `write_json` |
| §5 F and the frozen-input check (exit 3) | `check_frozen_inputs`, `blob_id`, `--verify-inputs`, `--expect-F` |
| §6 re-application of §4 to the JSON fields | `reapply`, called in `run` on the serialized record and again in `--check-summary` |
| §6 order, prefix, halt on first red | `validate_docs`, `run`, `check_summary` |

## 2. Choices where the PREREG and the data files are silent

1. **Output paths.** PREREG §5 names `phase-a/<tuple_id>.json` and `phase-a/summary.json`. The tool writes them under
   `--out DIR`, so the workflow produces `out/phase-a/…` and uploads `out/`. `--check-summary` adds
   `out/phase-a/check.json`.
2. **Extra output fields.** The PREREG schemas are kept; these are added:
   - in the summary: `schema` (`oret-phase-a-summary/1`), `exit`, `eps_star`, `w_star`, `T_star`, `run`,
     `frozen_inputs`, and `tuples` (each tuple's id, order, mode, row, match and computed compared fields);
   - in each record: `schema`, `row_step`, `reapplied_row`, `reapply_problems`, and `sequential_check` (on
     `full+sequential` tuples);
   - in noext records, the uncompared `w`, `w_chg` and `sweep_min_max_eps`.
3. **Exit codes in "other nonzero".** 6 means the re-application of §4 disagrees with the assigned row or an implied
   property fails. 7 means an unexpected internal error. Both render as "Phase A halted with exit N."
4. **Order inside one tuple.** The checks run in this order: record schema (exit 2), then the pending exit 4, then
   re-application (exit 6), then comparison (exit 1). Every comparison is recorded, and `first_failure` is the first
   mismatching field in the mode's list order.
5. **The `<expected>` and `<computed>` values in the exit-1 text** are rendered as canonical compact JSON: sorted keys,
   no spaces, ASCII.
6. **`F` present.** `F` must be a commit object (`git cat-file -e F^{commit}`) and must appear in
   `git log --format=%H HEAD`. An `--expect-F` that differs from the tool's constant exits 3. The exit-3 `detail` is
   the file path, or `F <sha> (absent from the checkout)` / `(not in the history of HEAD)`.
7. **Blob id of the bytes read.** The tool computes it in Python, as SHA-1 over `blob <len>\0` + bytes, from the very
   bytes it then parses. It equals `git hash-object`, which was checked locally for all four files.
8. **Cell lists.** `PHASEA-TUPLES.json` gives them as prose. Each of the eight descriptions is matched by exact
   string to a constructor, and its stated constraint (`L = m+3`, `L = 3`, `L = T+1`) is checked. An unknown
   description exits 2.
9. **Expression grammar.** The precedence of `^` against `&` is not stated, so an unparenthesized chain that mixes
   them exits 2. No frozen rule has one. In index arithmetic, `mod` has the lowest precedence and a nonnegative
   remainder.
10. **`Par` in the sequential method.** `φ_i` is constant in cells outside its syntactic support, so `Par(i)` is found
    exactly by enumerating that support. On orders 32–43 this result is cross-checked against the full φ table
    through `Q_cells`.
11. **`f_R`.** It is evaluated with every cell outside `R ∪ Q` set to 0. In the full method its factorization through
    `(R, Q)` is checked on all of `S` (exit 7 if it fails).
12. **`C_t`** is computed only for the cells of `Par(read cells)`, which are the only cells SCH reads. They lie in
    `R ∪ Q`.
13. **`TV` with more than two preparations** would be the maximum over pairs. Every tuple has `|P| = 2`.
14. **noext `T_prime`** is `null` for I-9 and `T` otherwise. That includes a row-1 verdict at step 1, which no frozen
    tuple takes.
15. **Step 6.** Exit 4 is raised on reaching step 6 with `G_status_T = inconsistent`, before ST is evaluated. Exact
    DIL∃ forces a consistent `G*`, so this matches reading the condition after ST. ST also re-tests `ε ≤ ε*` on `W_T`
    explicitly.
16. **HC-SK is identified by model `trigger-channel`.**
    - `w = μ(p0_1 = … = p0_k = 1 at t₀)` under the unconditioned law.
    - `w_chg = μ(f_R(R_{t₀}, Q_{t₀}) ≠ R_{t₀})`.
17. **MD-xor is identified by the tuple id prefix `MD-xor`.** The data file has no flag for the decoder sweep.
18. **Decoders.** For `write_min_eps` and the sweep, they range over every `{0,1}`-valued truth table of `A`.
19. **The sequential conditions** are checked at every hold tick the method evaluates, `H_{T′}`. This equals `H_T`
    when `τ ≤ T`. Each such tick must satisfy all of the following:
    - every `Q` cell is an unmodified copy of a `t₀` cell, tracked syntactically through bare-cell assignments, which
      can only reject;
    - the copies have distinct origins;
    - the origins lie outside `Σ ∪ A ∪ Q_{t₀}`, outside the origins of earlier hold ticks, and outside the dependency
      set of `R`.

    The law must be a product over cells, which is checked exactly.
20. **Validation.** Every field of the record except `method` must agree, plus `Q_cells`. Then
    `method = "full+sequential"`. `injective` is `null` on sequential-only tuples.
21. **Readback records** have `Q_cells`, `classes_T` and `Wr` set to `null`, since readback computes only `ε`, `TV`
    and the flags (§4).
22. **Start-up schema checks (exit 2).**
    - Each expected entry's keys must equal its mode's list exactly.
    - The ids must match; orders must run 1–49 in sequence; and the HC-SK `(n_bits, k)` order rule is re-checked.
    - Probability strings must match the regex in lowest terms.
    - Float literals and duplicate JSON keys are rejected.
    - A `P` element with `μ(σ) = 0` is rejected.
23. **The Lemma H bound** may exceed 1. The §5 regex has no upper bound, and only negatives are rejected.
24. **`B_def`** is the one-backslash string `Par(A)\A on S`, reading PREREG §5's `"Par(A)\\A on S"` as JSON
    escaping.
25. **Workflow.**
    - A first step fails when `github.run_attempt ≠ 1`, so a rerun is red before any tuple runs. The PREREG names only
      the host record as the checkpoint; this is an added mitigation.
    - `--check-summary` re-verifies the frozen inputs, regenerates `verdict_text` and re-applies §4 in one step.
      `check.json` records each check separately.
    - A concurrency group prevents parallel dispatches.

## 3. Points in the PREREG that need the reviewer's decision

- **(a)** No flag marks which tuple carries the decoder sweep, or which carries `w` and `w_chg`. The tool identifies
  them by id prefix and model name (§2, items 16 and 17).
- **(b)** PREREG §5 says `phase-a/`, while the task brief says `out/summary.json`. The tool writes
  `out/phase-a/summary.json` (§2, item 1).
- **(c)** The sequential conditions are stated over `H_T`. If a sequential tuple ever had `T′ > T`, the tool would
  also require them on `H_{T′} ∖ H_T`, or exit 5 (§2, item 19).
- **(d)** The noext `T_prime` for a step-1 row-1 verdict is not specified (§2, item 14). No frozen tuple is affected.
- **(e)** The `^`/`&` precedence is not stated (§2, item 9). No frozen tuple is affected.
- **(f)** "Write trigger fires" is computed as the presence-bit conjunction (§2, item 16). For these tuples it equals
  `μ(σ ∈ P)`.
- **(g)** The PREREG's three in-job signals are the run step, the regeneration step and the marker. The re-application
  of §4 shares the regeneration step.

## 4. Open point for the dispatch gate: `workflow_dispatch` needs the file on the default branch

GitHub offers `workflow_dispatch` (UI, API or `gh workflow run`) only for a workflow file that exists on the
repository's **default branch**. A file that lives only on this disposable branch cannot be dispatched as it stands.
Two options are recorded here without a choice between them; the owner decides:

- **(i)** Land `.github/workflows/oret-phasea.yml` on `main` first, through a reviewed PR, then dispatch it with `ref`
  set to this branch. The job checks out that ref, and the tool verifies `F` against it.
- **(ii)** Add a `push` trigger restricted to a dedicated launch branch, so that the push itself is the special
  launch. That push would need the same separate owner approval (§A.43 item 4). The workflow would then need a
  reviewed edit, and the reviewed tool commit would have to be the one pushed.

**Push-trigger inspection (§A.43 item 4).**
- Of the existing workflows, `bg2-orientation-design.yml` and `bridge-compatibility-research.yml` push-trigger on
  paths outside this directory.
- `hidden-sector-replay.yml` and `verify.yml` push-trigger on `main` only.
- So a push of these files to a research branch launches no workflow by push.
- An open PR from the branch runs `verify.yml` (`pull_request`). It does not run this workflow.

## 5. Local checks run (static only, PREREG §7)

| Command (from the worktree root) | Exit | Result |
|---|---|---|
| `python3 -m py_compile …/phaseA/phasea.py` | 0 | compiles (Python 3.13 locally; CI pins 3.12) |
| `python3 -I …/phaseA/phasea.py --help` | 0 | usage printed |
| `python3 -I …/phaseA/phasea.py --self-test` | 0 | 17 of 17 synthetic checks pass |
| `python3 -I …/phaseA/phasea.py --verify-inputs --expect-F 49f0bd41…` | 0 | four blob ids match at `F` |
| `python3 -I …/phaseA/phasea.py --verify-inputs --expect-F 0000…` | 3 | wrong `F` refused |
| `git rev-parse F:<path>` and `git hash-object <path>`, for each frozen file | 0 | equal to the tool's ids |

**What the self-test covers.** Synthetic models only. Gated hold (row 5) and gated swap (row 6). One-cell shift and
three-cell pulse (2a, I-9 in noext). A pulse whose `𝒬` grows on `W_{T′}`, and a gated conveyor where
`G*_{W_T} = ∅ ≠ G*_{W_{T′}}` (2b). An unbiased-pad completion (J-ii fails), a static carrier input (J-i fails), and a
static Σ input (support under `μ^P` differs from `μ`). A partial read set, and an (R-a)/(R-b) failure.
Methods and exits:
- A Toffoli-written channel, by full, sequential and both methods, with hand values.
- The sequential failures: a re-entering cell, a non-product law, and a forced disagreement (each exit 5).
- A non-injective sequential 2-cycle (exit 5).
- Frozen-input mismatches with an injected git (exit 3).
- Floats in input, record, serialization and comparison (exit 2).
- The precedence of steps 1–8, including exact `≤` at `ε*` and exit 4 at step 6 only.
- Re-application.
- End-to-end runs on a five-tuple synthetic document: PASS, exit 1, exit 2 and exit 5, with `verdict_text`
  regenerated and a tampered `verdict_text` detected.

**Other local runs.**
- *Mutation runs of the self-test.* Twenty-four single mutations were run, on scratch copies outside the worktree,
  against synthetic inputs. In the final run, each mutation was detected. Seven survived their first run; synthetic
  cases were added until each was detected.
- *A timing probe.* A 15-cell synthetic Toffoli channel at `T = 6`, run by both methods, took about 1.3 s. That
  suggests the run fits well inside the 30-minute timeout. It is not a measurement of the frozen set.
- *One hand error.* One of my synthetic hand values was wrong (`ε = 1/2` where it is 1). It was corrected after
  re-derivation.

**No frozen tuple was evaluated locally.**
- No model, law, decoder or expected value of `PHASEA-TUPLES.json` or `PHASEA-EXPECTED.json` was computed.
  `--run` was never invoked.
- The only reads of the frozen data were reading the files and one read-only structural comparison. That
  comparison checked that every expected entry's key set equals its mode's compared-field list, that the ids match,
  and that the orders are 1–49. It computed nothing about any tuple.

## 6. Known limitations

- **Re-application** reads only the serialized fields, but it is written by the same author in the same file. Its
  independence from `assign_row` is one of representation, not of authorship.
- **The self-test's expected values** are my own hand derivations on synthetic models. They test the implementation,
  not the frozen hand algebra.
- **Exit 4** is exercised only at the level of `assign_row`. No synthetic dynamics reaching step 6 with an
  inconsistent `G*` was constructed. Row 4 is the declared constant `false` (PREREG §9).
- **The sequential method** uses syntactic provenance for freshness. It is exact where it accepts, and it may reject a
  rule that is valid. It is built for channel-type rules such as `trigger-channel`.
- **Equivalent mutant.** Computing the sequential `Par` syntactically is equivalent on `trigger-channel`. It is
  detected only on a synthetic rule with a dead dependence.
- **The workflow** was parsed as YAML locally but not run, and no `actionlint` was available. The Python version
  differs between local runs (3.13) and CI (3.12).
- **`run.commit`** is the checkout `HEAD` at dispatch. A run on a disposable branch is provenance only until its
  `summary.json` lands on `main` (PREREG §7, §A.42).
