# O-RET Phase A: implementation notes for the test tool and workflow

**Status.** WIP / UNVERIFIED. The tool and workflow were written under the owner's authorization of 2026-11-04
(#1032). They implement the preregistration frozen at `F = 49f0bd41c5323d2191b580460c8703740dd01b30`. This revision
applies the independent review of `5ca342fc` (ACCEPT WITH CHANGES: S1 self-test coverage, S2 binding of the executed
head to the reviewed commit), the owner's choice of the reviewed-PR launcher route (§4), and the two optional
self-test additions SF1 and SF2 of the delta review of `6133e0eb`. Not run. A dispatch is a
separate owner approval (PREREG §7, AGENTS.md §A.43 item 4).

- `phaseA/phasea.py`: the tool. Standard library only, with exact `fractions.Fraction` arithmetic throughout.
- `.github/workflows/oret-phasea.yml`: the workflow, triggered by `workflow_dispatch` only, with a required
  `confirm_commit` input.
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
| §6 one pass; the run tied to the reviewed commit (review S2) | workflow launch guard; `record_identity` (`--record-identity`) |

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
    - A launch guard runs before checkout. It fails unless the event is `workflow_dispatch`, the input
      `confirm_commit` is exactly 40 lowercase hex characters and equals `github.sha`, and `github.run_attempt` is 1.
      The input reaches the shell only as the env var `CONFIRM_COMMIT`, never by interpolation into a script.
    - `--record-identity out` then writes `out/phase-a/run-identity.json`: event, ref, sha, `confirm_commit`, run id
      and attempt, workflow ref, and the checkout `HEAD`. It exits nonzero unless the same conditions hold and
      `HEAD = github.sha`.
    - `--check-summary` re-verifies the frozen inputs, regenerates `verdict_text` and re-applies §4 in one step.
      `check.json` records each check separately.
    - `actions/checkout` runs with `persist-credentials: false`. A concurrency group prevents parallel runs.

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

## 4. Launch procedure: the reviewed-PR launcher route (owner's choice)

GitHub offers `workflow_dispatch` only for a workflow file on the repository's **default branch**, and it runs the
file **at the dispatched ref**. The owner chose this route; a push-triggered launch branch is not used.

1. **The workflow file reaches `main` through a reviewed PR.** The copy on `main` and the copy at the reviewed tool
   commit should be byte-identical. If they differ, the dispatched ref's copy is the one that runs.
2. **The dispatch is a separate, owner-authorized special launch.**
   - `ref` is the reviewed tool branch, or a tag, held at the reviewed commit. The dispatch API takes a branch or
     tag name, not a bare commit.
   - `confirm_commit` is that commit's full SHA.
   - The guard refuses the run unless `github.sha = confirm_commit`. A branch that has moved past the reviewed commit
     is therefore refused before checkout.
3. **The result reviewer** does all of the following:
   - reads the job conclusion and `head_sha` from the host's API;
   - checks `head_sha`, `run-identity.json` (`sha`, `confirm_commit`, `checkout_head`, `run_attempt = 1`) and
     `summary.json` `run.commit` against the reviewed commit;
   - lists every run of the workflow. A second dispatch is a new run with attempt 1, which no in-job check can see.
4. **No push launches the workflow.** It has no `push` or `pull_request` trigger.
   - Of the existing workflows, `bg2-orientation-design.yml` and `bridge-compatibility-research.yml` push-trigger
     on paths outside this directory, and `hidden-sector-replay.yml` and `verify.yml` on `main` only.
   - A push of the tool branch therefore launches no workflow. An open PR runs `verify.yml`, not this workflow.
   - A dispatch with `ref=main` before the tool is on `main` fails at the guard or at the tool's absence. It would
     still be a recorded launch.

## 5. Local checks run (static only, PREREG §7)

| Command (from the worktree root) | Exit | Result |
|---|---|---|
| `python3 -m py_compile …/phaseA/phasea.py` | 0 | compiles (Python 3.13 locally; CI pins 3.12) |
| `python3 -I …/phaseA/phasea.py --help` | 0 | usage printed |
| `python3 -I …/phaseA/phasea.py --self-test` | 0 | 33 of 33 synthetic checks pass, in about 1.5 s |
| `python3 -I …/phaseA/phasea.py --verify-inputs --expect-F 49f0bd41…` | 0 | four blob ids match at `F` |
| `python3 -I …/phaseA/phasea.py --verify-inputs --expect-F 0000…` | 3 | wrong `F` refused |
| `git rev-parse F:<path>` and `git hash-object <path>`, for each frozen file | 0 | equal to the tool's ids |
| `git diff 49f0bd41 -- <the four frozen files>` | 0 | empty |
| the launch-guard script under `bash`, with synthetic env values | 0 / 1 | accepts only the valid case; refuses push, attempt 2, uppercase, 39 characters, embedded newline and `$(…)` |

**What the self-test covers.** Synthetic models only. Sizes and parameters are outside the frozen set: HC-SK-model
cases at `(k, T) = (2, 4)` and `(1, 7)`, and non-dyadic biases `1/40` and `3/40`.
- *Rows.* 5 and 6 (exact). 5 (DIL∃-η). 2a, 2b, 3, 1 (J-i, J-ii and carrier-return failures), 7, 8, I-9 and I-3.
  Each is re-applied from its JSON fields.
- *Branches.* The HC-SK `w`/`w_chg` branch. `method_for` at `|S| = 2¹⁶` and `2¹⁷`. The MD-xor-prefixed sweep (a
  biased junk bit, sweep `1/4`). All eight cell constructors. The frozen order rule.
- *Mutant-targeted cases.*
  - `𝓛` including the last window tick.
  - The recurrence rule at `ε = ε*`.
  - `τ` starts under `μ^P` (an unfired preparation would shorten `τ`).
  - (R-a) on `A ∩ Σ ≠ ∅`.
  - SCH over the read cells only.
  - The support conditioning, and `Q` built from `A`.
  - Sequential failures (a re-entering cell, two non-product laws, a forced disagreement, and a computed `Q` cell,
    SF2).
  - `G_status_T = inconsistent` through the real code path (SF1).
- *Exits and outputs.* Exits 2, 3 and 5. Exit 4 through real dynamics (SF1) and by injection. Exit 6 by injection. The
  `check_summary` prefix and halt-at-last tampers. Run identity, with each condition violated.
- *End-to-end.* A six-tuple run (PASS; exits 1, 2 and 5), and a two-tuple run with a `full+sequential` HC-SK-model
  tuple.

**Mutation campaign.** Every mutant was run on a copy outside the worktree, against the synthetic self-test only.

| Set | Mutants | Detected | Not detected |
|---|---|---|---|
| reviewer M1–M20 (`mutate.py`) | 20 | 15 | M3, M5, M14, M16, M19: equivalent (below) |
| reviewer N1–N6 (`mutate2.py`) | 6 | 6 | none |
| author's original A01–A24 | 24 | 24 | none |
| new paths B1–B8, C1–C2 (re-application rows 7, 8, 5-approx and 1 in both modes; order rule; `sequential_check`; declared method; product test; readback row) | 10 | 10 | none |
| run identity I1–I6 | 6 | 6 | none |
| reviewer P1–P10 (`mutate3.py`) | 10 | 8 | P4, P6: equivalent (below) |
| SF1 and SF2: `g_star` never inconsistent; the t₀-cell rejection dropped | 2 | 2 | none |

The equivalent mutants:
- **M3**, η under `μ`: `μ^P(·|σ) = μ(·|σ)` for `σ ∈ P`.
- **M5**, the sequential used set dropped: every earlier `Q` origin lies in `R`'s dependency set, which is still
  checked.
- **M14**, exit 4 after ST: exact DIL∃ forces a consistent `G*`.
- **M16**, `C_t` over `Par(A)`: SCH reads only `Par(read) ∩ C_t`.
- **M19**, the TR/EX observed-failure assertion: the re-applied row implies it.
- **P4**, step 4 over `W_{T′}`: step 3 already catches any failure on `W_{T′} ∖ W_T`.
- **P6**, τ checking the repeat before the hit: a repeated family cannot carry a new hit.

P10 (`G_status` always consistent) and P5 (provenance kept for computed cells) are now detected, by SF1 and SF2.

**No frozen tuple was evaluated locally.**
- No model, law, decoder or expected value of `PHASEA-TUPLES.json` or `PHASEA-EXPECTED.json` was computed.
  `--run` was never invoked.
- The only reads of the frozen data were reading the files and one read-only structural comparison. That
  comparison checked that every expected entry's key set equals its mode's compared-field list, that the ids match,
  and that the orders are 1–49.
- The synthetic cases reuse the frozen cell layouts only through the constructors, with other rules, laws and
  parameters.

## 6. Known limitations

- **Re-application** reads only the serialized fields, but it is written by the same author in the same file.
- **The self-test's expected values** are my own hand derivations on synthetic models. They test the implementation,
  not the frozen hand algebra.
- **Exit 4** is exercised through real dynamics by one synthetic case (SF1) and by injection. Row 4 is the declared
  constant `false` (PREREG §9).
- **The `g_star` "inconsistent" branch** is covered by SF1, a 3-bit copy-code register with two masked inputs, each
  consistent alone, that chain `001 ~ 011 ~ 111` together. On that case the test establishes four things:
  - the tool classifies `G_status_T` as `inconsistent`, and `g_star` gives the same classification on the pooled sets
    directly;
  - η and the bound are `null`;
  - the tuple halts with exit 4 at step 6, its record written with row `null`;
  - a mutant that never reports `inconsistent` fails the self-test.

  This establishes the classification on that synthetic case, not on every input. A wrong `consistent` in a frozen
  tuple would still need the frozen expected value to be wrong in the same way before it could pass.
- **The sequential method** uses syntactic provenance for freshness. It is exact where it accepts, and it may reject
  a valid rule.
- **Paths a line trace of the final `--self-test` still does not reach.** The frozen run uses none of them on a
  correct input. Each is a rejection: it can only turn a run red (void), and none can produce a PASS by itself.
  - The wrappers that call git on the real checkout: `git_run`, `repo_root`, the real file read, and `run_info`.
    `--verify-inputs` exercises them locally.
  - The exit-3 sub-branches "absent at F" and "unreadable".
  - The single schema rejections (exit 2) in the parsers and validators, and the summary write's exit-2 fallback.
  - The internal guards (exit 7): `f_R` factorization, an unknown expression node, `Par` outside `A ∪ Q`, missing
    presence bits, and the generic handler.
  - Some exit-5 sub-conditions:
    - a shared-origin `Q` cell (the computed-cell rejection is covered by SF2);
    - an oversized support or law;
    - the full-versus-sequential disagreement on the exit-4 condition.
  - Row 4, a declared constant.
  - The unreadable-file branches of `check_summary`.
- **The workflow** was parsed as YAML and its guard script run under `bash` locally. It was not run on the host, and
  no `actionlint` was available.
