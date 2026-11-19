# Q-C2-1 (ARP-2-QC21): what the scripts must change to match r14b

WIP / UNVERIFIED. Model-written. For the implementer; nothing here was run.

- **Scripts checked** (read only): `wt-impl/verification/programmes/oi-qm/reconstruction/round-arp2-qc21-20261108/`,
  worktree head `d87547a4a` ("C-IFACE STAB rule matches the whole word", local, unpushed):
  - `qc21_check.py`, sha256 `1f9283348ed9ffb932602186b5d9c1ed4ea5143c6fbb4721bd0b114277f8aed2`, 3715 lines;
  - `controls.py`, sha256 `ce343d6f7992a3d0c98ef3cf93acb38f835e2bbbcad93f979357b2ae39954ca4`, 2196 lines.
- **Target:** r14b `preregistration.draft.md`. Part D is r14a's, with I1–I4 of `review/REVIEW-QC21-r14a.md`
  (`f30841ba…`) applied in place (D2, D16, D17, D20); Part E adds what r14b requires. Parts A–C are r14's delta,
  unchanged except the line correction below; their section, C.8-item and row references are r14's and hold in r14a (r14a adds rows 86–98 and changes no
  r14 row number). Part D adds what r14a requires (re-review `REVIEW-QC21-r14.md`, and the shared-method items found
  via Q-C2-2 r14). Line numbers in Part D marked "r14a" are the preregistration's.
- **Line numbers** are the scripts' at the head above.
- **Authorization** (c.6740078002): script updates and fixture-only, non-scientific self-tests. No step below needs a
  decisive family, the design run, or an LP on OI data. ST-BP is implemented, not run.

Each item: **where → what r14 requires → status checked against the script.**

## Part A. The r13 lag items named in the brief (each checked)

| # | item | script and lines | finding | change required |
| --- | --- | --- | --- | --- |
| A1 | **replay format** (C.8 3; rows 50, 51, 54, 66) | `controls.py` `replay_compare` 1403–1415; `main` replay branch 2156–2160 | **Partly lagging.** The comparison is right (parse, drop `parameters.dispatch_sha`, canonical JSON). The absent-file case prints a sentence, not `{"replay":"not-applicable"}`; a mismatch or parse error exits 1, not 3 | print exactly `{"replay":"not-applicable"}` and exit 0 when `evidence/measurements.json` is absent; exit 3 on a mismatch or unparseable input; keep the `"rb"` reads. Self-test both exits |
| A2 | **`h_sha256`** (C.8 4; row 61) | `qc21_check.py` `sha256_hex` 123–152; uses 646, 2795, 3637, 3639 | **Lagging.** Named `sha256_hex`, outside an `h_*` namespace; the self-test has two FIPS vectors (empty, `abc`), not three | rename to `h_sha256` (and any helper to `h_*`); add the 448-bit vector `abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq` → `248d6a61…db06c1`; C-INDEP (controls) must reject a `v_*` call to `h_*` |
| A3 | **`s_entry` / `s_refusal` signatures** (C.8 5, 6; rows 61–64) | `qc21_check.py` `run_entry` 3684; `s_refusal(name)` 3163–3170; `DECISIVE_BUILDERS` 51; `BUILDER_CALLS` 53; `t_mguard_checker` 3441–3472; `controls.py` `static_checker` 625–725 (accepts `run_entry`, requires a one-argument refusal, a tuple of strings) | **Lagging.** Entry named `run_entry`; refusal takes a name argument; `DECISIVE_BUILDERS` is a tuple of strings; `t_builder_refuses` runs `len(cases) + 1` times (3471) | rename `run_entry` → `s_entry(argv, environ)`; make `s_refusal()` argument-free, its first statement the call in `s_decisive` and each builder (expression statement `s_refusal()`); keep one module counter incremented in `s_refusal()` (M-GUARD asserts a zero delta in each fixture-mode case; `t_builder_refuses` accounts for exactly one); `DECISIVE_BUILDERS = (s_build_p, s_build_repinv, s_build_b, s_build_c)` as names; run `t_builder_refuses` once. Update `static_checker` to the r14 forms (`s_entry`; `s_refusal()` with no args; `s_refusal` referenced only in its `def` and those first statements; `DECISIVE_BUILDERS` of `Name` nodes) and its mutations |
| A4 | **the A3b marker** (C.2 A3b; C.3; C.8 7; rows 48, 49, 52, 53, 55, 56, 60, 67–69) | `controls.py` `FROZEN_JOBS` 299–352 (no A3b step); `STEP_*` 38–43 (no A3b name); `main` 2140–2193 (no `fixture-mode-check`); `run_class_rule` (d) 1649–1658 reads `rec["fixtures_mode"]` and falls back to `order-s1` on "artifact missing" | **Missing.** | add step A3b "ARP-2-QC21 fixture output is fixture mode" running `controls.py fixture-mode-check "$RUNNER_TEMP/arp2-qc21/fixtures.json"` after A3/A4 per C.2; add the mode (exit 0 iff schema v1, `mode: "fixture"`, `complete: false`, every decisive field the placeholder; else 3); rule (d) reads A3b's conclusion from the jobs record (`success` required), records `A3b_conclusion` and `fixtures_artifact_digest` (provenance only), and no longer needs an artifact or `order-s1` fallback; W's self-test removes A3b and must fail |
| A5 | **`approvals.json`** (C.8 9; *The objects*; R) | `controls.py` `E_FILES` 76–77; `main` `order`/`verdict` stub 2188–2191 | **Missing.** `E_FILES` lacks `evidence/approvals.json`; no schema `arp2-qc21-approvals` v1 reader; `order` and `verdict` are stubs that exit 1 | add `evidence/approvals.json` to `E_FILES` (R at `E`); implement the schema (`run_id`, `run_attempt`, `head_sha`, `stage`, `approval_comment_id`, `approval_created_at`, `approval_updated_at`, `approval_author`, `quoted_words`) and its checks (C.3); implement `order` and `verdict` fully, with post-`F` inputs as arguments (stage commits by `a_ok` HEX40; `T_repo` read live; `T0` a frozen constant, `PENDING`); exercise both on synthetic records in the self-test only |
| A6 | **`--fixture-output`** (C.8 10) | `qc21_check.py` docstring line 12; `run_entry` 3696–3698 | **Lagging.** It is a checker flag | remove the flag and its branch; the design run uses `--event fixture` |
| A7 | **B-S4F missing** (B-S4F row; row 59; adaptation table) | `qc21_check.py` `FIXTURE_EXPECT` 3244–3247; `fixture_fragments` 3250–3252; `t_mutations` M-MODEL (≈3597) | **Missing.** No B-S4F fixture; M-MODEL's step-4 case uses F10 only | add B-S4F (`Ω = F_2²`; four point laws; effects unit, `ξ_1 = 3/8 + [ω_0 = 0]/4`, `ξ_2 = 3/8 + [ω_1 = 0]/4` and complements; expect feasible, step 4, `T = 3`, model verified); add it to M-MODEL (step-4 `T > 0`) and to the fixture-mode list |

Other r13 lag items found while checking (not in the brief's list):

| # | item | where | change required |
| --- | --- | --- | --- |
| A8 | A3 and B4 `mkdir -p` form (rows 46, 47; C.8 11) | `FROZEN_JOBS` A3 and B4 use a two-line `run: \|` block | W compares the whole file with the frozen splice; make the splice text match C.2's frozen lines (`mkdir -p "$RUNNER_TEMP/arp2-qc21" && python3 -I -S -B …`), or record the exact YAML the preregistration freezes before `F` |
| A9 | `"workflow_dispatch"` only in `SPLICE_*` constants and `run_class_*` (C.8 8; row 65) | `ON_SPLICE`, `FROZEN_JOBS`, `B4_EXPR`, `B6_IF`, `JOB_B_IF` (264–352) | rename the constants holding the splice to `SPLICE_*`; make B's rule enforce the C.8 8 placement |
| A10 | CC-NAT gating after the r12 reviews (*Proof reviews*; CC-NAT row) | `qc21_check.py` `LEMMA_P_REVIEW = "pending"` 3173 (CC-NAT is then excluded from `c_red` at 3209); `CONE_REVIEW` 3174 | Lemma P is PROVED (conditional); CC-NAT gates C. Remove the review switch, or set it to the recorded verdicts; CC-NAT red ⇒ C-VOID |
| A11 | STAB-FALSE gating (C.8 12) | `controls.py` `R12_STAB = False` 75 ("absent copies are skipped") | make A9 require both pinned certificates from the design run onward (no skip) |
| A12 | C.8 2's stress-fixture shapes | `qc21_check.py` `stress_fixture` 1095–1123 | SF-1 is 8 product laws × 4 copies, three seeds mixed into one fragment; SF-2 is 13 laws × 7 copies. r14: one instance per seed; SF-1 32 distinct coset-uniform laws on `F_2⁵` (dims 2–4), the 51 effects of `Acc(B-P)`; SF-2 91 coset-uniform laws on `F_2⁴` (dims 1–3), `f_z`, `f_x`, `f_y`. See B2 |
| A13 | Appendix D.6's orbit forms of CC-DYAD, C-XB and C-FRAME | `c_r5_controls` 2901–2953 runs only the Appendix B forms (C-FRAME on `L_scope(0)`, CC-DYAD on `L_scope`, C-XB on `S_0`) | add the orbit forms on `O_12` / `O_11` as D.6 states; keep the Appendix B forms as the diagnostic forms (depth 1; B12) |
| A14 | B-C's horizon | `s_build_c` 2776 always takes `orbits[name][:13]` (`O_12`) | B-C uses `O_K` at the larger `K` whose conjunction flags the instance (`O_6` for an instance flagged only at `K = 6`) |
| A15 | stale docstrings | both files say "Preregistration r11b" (lines 4 and 2) | cite r14 |

## Part B. Changes required by r14's decisions

### B1. D19 (0)(c): extreme rays, certified (C.8 1, 15; B-RAY; M-RAY)

- `qc21_check.py` `s_generators` 290–299 and `s_decide` 584–655:
  - after factorization and step 1, apply the caps on effects before reduction and on `d`; then the **extreme-ray
    reduction**: rows in frozen order; remove a row when a phase-1 simplex finds `λ ≥ 0` with `Σ_q λ_q a_q = a_p` over the
    rows still retained other than `p`; step 5's rules; the work draws on the fragment's budget (`Budget`);
  - then the caps on `n` (= retained rows) and `C(n, d − 1)`;
  - record `n_distinct` and `n_extreme`;
  - put the retained indices and the removal certificates, in removal order, into the certificate bytes;
  - "effects before reduction" counts only outcomes with positive probability under some preparation, plus the unit
    (today `len(all_reads)` counts every listed read).
- `v_verify` 866–923 and `v_facets` 813–840: check each removal in order (`λ ≥ 0`, exact equality, each `q ≠ p` not
  removed earlier), then enumerate facets over the retained rows only. A failed removal ⇒ `undecided`. Keep C-INDEP:
  certificate data only.
- Fixtures: add **B-RAY-S** (B-STAB plus `½Z+ + ½Z−`) and **B-RAY-P** (B-POS's four plus the mixture of its first two);
  expect 5 distinct rows, 4 extreme rays, one verified removal, and the verdict and step of B-STAB (feasible, 2) and
  B-POS (infeasible, 4). Add both to `FIXTURE_EXPECT`, `fixture_fragments` and the fixture-mode control list.
- Mutation **M-RAY** on B-RAY-P: one removal multiplier altered; the first row removed with a fabricated certificate.
  Each must fail C-CERT.

### B2. D19 (i)(a): ST-BP, two cap sets, two budget triples (C.8 1, 2; C.7)

- `qc21_check.py` constants 38–46: add `S_MAX = None` (`PENDING`, owner, before the design run); B-P's caps
  `CAP_BP_N`, `CAP_BP_D`, `CAP_BP_SUBSETS` and budget `P_MAX_BP`, `B_MAX_BP`, `W_MAX_BP` (`None` until fixed); keep the
  general caps (16, 16, `10^5`, 200) and `P_MAX`, `B_MAX`, `W_MAX`.
- `s_build_b` 1996–2031: B-P is decided under B-P's caps and budget; every other fragment (construction A of B,
  completions, B-C and its completion, QM-P's restricted fragment) under the general ones. Today one `budget_vals`
  is passed to all.
- `stress_output` 3401–3420 (`--stress`): generate SF-1/20261108, SF-1/1, SF-1/2 and SF-2/… per A12. For each SF-1
  instance: factor, step 1, the reduction (no budget), record `n_distinct`, `n_extreme`, `d`, `c = C(n, d − 1)`; if
  `c > S_MAX`, record `over_maximum: true` and do not decide; otherwise decide (no budget), verify, record verdict,
  step, pivots, `max_bits`, work (reduction included). Record `S_max` once. The facet enumeration must count subsets
  and stop at `S_max`, so an over-maximum instance costs only its reduction.
- `controls.py` `stress_check` 1379–1400: accept ST-BP records with `over_maximum: true` and no certificate; require
  `certificate_verified` only for decided fragments; check the new fields.
- `controls.py` `check --freeze` (`check_mode` 1517–1530, stage `None`): recompute from the pinned `stress.json`:
  the general budget (C.1's 3× rule, ST-BP instances excluded); the reference instance (passing instances by
  decreasing `c`, ties in seed order; the first for which the timeout test holds); B-P's caps
  `max(16, n_ref)`, `max(16, d_ref)`, `max(10^5, c_ref)`, 200; B-P's budget `max(general, 3 × ref)`; the failure rule
  (no reference ⇒ copied caps and the general budget); the timeout test
  `σ × (W_max^BP + 1203 · W_max + 2·W_fix + W_stress) + t_810 ≤ 1200`. Fail on any difference from the constants in
  the pinned checker, or on a failed timeout test.
- C.5a `budget`: both triples, B-P's caps and `S_max`.

### B3. D19 (ii)(b), (iii)(c): reported-only fragments (C.8 13; *Decision rule B*)

- `qc21_check.py` `k_decide_b` 1226–1248 and `controls.py` `decide_b` 918–935: steps 1–3 read **B-P alone** and the B
  controls. Remove `"B-C"` from the token roles; construction A of B, completions and B-C never void or decide.
  Self-test "decide-b VOID A-of-B out_of_scope" (in `t_decide_paths`) must invert: the token is unaffected.
- `assemble_decisive` 3192–3240: `over` (3204–3206) adds C-BUDGET to `b_red` for any `out_of_scope` fragment. Per
  rows 73–75: an `out_of_scope` B-P gives B-VOID through `decide-b`; reported-only `out_of_scope` voids nothing;
  C-BUDGET is red only if an over-budget fragment is given a verdict. `budget.respected` stays per fragment.
- `decide-b` step 1 adds the SG-1 check: B-P's record has `preps == 32` and its settings are exactly `Acc(B-P)`'s nine.
- Schema (C.5a): per fragment `role` ∈ {`B-P`, `A-of-B`, `completion`, `B-C`}, `n_distinct`, `n_extreme`, the cap or
  budget exceeded.
- Note (`controls.py` `make_note` 1335 ff.): the B-VOID texts of *Test B*, with the `out_of_scope` and `undecided`
  sentences; the C texts print each flagged instance's B-C status (verdict, `out_of_scope` or `undecided`; "not built"
  no longer occurs).

### B4. D19 (iv)(a)

- `s_build_c` 2766–2777 already flags on the step 2/3/4 conjunctions. No change beyond A14.

### B5. D20 (b): depth-1 diagnostics (D.2, D.6)

- `qc21_check.py` `l_scope` 2818–2836 (`for _ in range(2)`): the diagnostics' `L_scope(g)` at depth 1 (one round from
  `S_0`). Use it in `r5_diagnostics` 2880–2898 and in the diagnostic forms in `c_r5_controls` (CC-DYAD's closure,
  C-AFFB); C-SCOPE's diagnostic clause checks depth 1.
- Label every diagnostic record `"depth 1"` (today `"diagnostic (D1(a)); no token reads it"`, 2897). No SF-D, no A5d,
  no `--stress-diag`.

### B6. D21 (b): test-level VOID and the S1 binding (rows 72–85; C.8 3, 7, 14)

- `qc21_check.py` `run_entry`/`s_entry` 3707–3709: in decisive mode exit 0 when the output is complete. Red controls
  and `out_of_scope`/`undecided` fragments are recorded with codes and void only their own token. Remove the
  `red or over` ⇒ 3 rule.
- Red decisive-mode controls void the tokens of their `for` column ("all" ⇒ every token). Check `assemble_decisive`'s
  lists (3195–3214): CW-P, QM-P and ATTR-FIX feed `p_red`; QM-P also `b_red`; REP-PLANT (`for` P, all) voids every
  token. Fixture-mode exit rule unchanged (A3 still exits 3 on a fixture mismatch: a round halt at S1 or `E`).
- `controls.py`:
  - `CONTROLS_IMPORTS` 80: add `io`, `zipfile`. `MOD_ATTRS` 81–83: `io: {"BytesIO"}`, `zipfile: {"ZipFile"}`.
  - B's rule: a `ZipFile` is built only as `zipfile.ZipFile(io.BytesIO(<x>))` (one argument), and only `.namelist()`
    and `.read("measurements.json")` are called on it.
  - `GH_TEMPLATES` 90: add `actions/artifacts/{DEC}/zip`. `gh_get` must return bytes for it (no `text=True`).
  - M-GUARD's B variants ZIP-1 to ZIP-3 (`ZipFile(io.BytesIO(b), "w")`; `extractall`/`open` on a `ZipFile`;
    `ZipFile(<path>)`) must fail B.
  - `verdict_mode` 1751–1778:
    - add the **S1 binding**: list S1 run's artifacts (every page); exactly one with B5's frozen name, whose
      `workflow_run.id`/`head_sha` are S1's; download its zip; `sha256(zip) == digest`; members exactly
      `["measurements.json"]`; compare with the committed file by `replay_compare`. Any failure, or a missing or
      expired artifact ⇒ VOID; a rate-limit or 5xx ⇒ failed capture;
    - stop treating VOID tokens as a verdict failure: `decide(meas)` VOID only for schema, mode, completeness,
      placeholder or flag disagreement; the token line carries P, B, C tokens (VOID ones included) and the level;
    - keep "every step of job B `success`" (B6 included at `E`).
  - Self-test **S1-BIND** on in-memory synthetic lists and zips (match; changed token; extra member; wrong digest;
    other run's id or `head_sha`; no artifact). No file written.
  - `check --stage E` (`check_mode` 1546–1549) keeps `X` for schema VOID only; a P, B or C VOID token is not an `X`
    error.

### B7. D22 (a): the QM-P restricted fragment (*Test B*; QM-P row)

- `qc21_check.py` `qm_p_fragment` 1550–1574 and `bp_restricted_equals_qmp` 2034–2061: for the restricted fragment use
  the arms off (marker `|0⟩`, no CNOT), on (CNOT, `|0⟩`), SH-0 (CNOT, `|+⟩`), SH-K (CNOT, `I/2`), path as control;
  `QM_SLOT_BASIS = {0: "X", 1: "Z"}` stays; equality is exact, column by column, for all four arms (drop the
  "up to relabelling" branch for SH-0). `qm_run` 1455–1482 keeps the P arms (off, CNOT, `X` on E, `Z^w`, purified)
  for QM-P's P control. The writer's probe `probes-r13/qmp_marker.py` (`efd583bd…`) gives the QM-side tables.
- `controls.py` `c_iface` 821–864: add the rules that no `decide_*`/`k_decide_*` or `decide_levels`/`k_decide_levels`
  references `bp_equals_qmp`, and that `decide_b`/`k_decide_b` read only B-P's record and the B controls; add the two
  mutations (decide-b reading construction A of B; decide-levels reading `bp_equals_qmp`) to the self-test.

### B8. D23 (c): `pred_change` pair

- `qc21_check.py` `p_ablation_fields` 1821–1837: for ABL-SA1b, `pred_change = {"common": <bool over quantities in both
  read sets>, "added": <sorted names of OLC quantities: conditional V and Pz per joint subset, OLC.joint>}`. Today the
  `OLC` is merged into `abl_obs` and compared whole (1826–1828), which gives option (b). Class ablations keep one
  boolean. Self-test: `common` false and `added` non-empty on a synthetic SA1b record.

### B9. Safeguard checkpoints (SG-1 to SG-4; invariants table)

- `decide-levels` self-tests: C-VOID with P-COMPLEMENTARITY ⇒ Level 1; B-VOID with P-COMPLEMENTARITY ⇒ Level 1.
- `decide-b` self-tests: a 16-preparation B-P record ⇒ B-VOID; an `out_of_scope` and an `undecided` B-P ⇒ B-VOID,
  with the limitation sentences in the note.
- `verdict` self-test: VOID on each provenance failure listed under D21 (crash/incomplete output, failed check, red
  fixture-mode step, replay mismatch, failed S1 binding, host VOID without retake, authorization violation).
- Mirror every `decide-*` change in `controls.py` (`decide`, 990–1026) so X's flag agreement holds.

## Part C. Not to change

- The C token rule and flags (already (iv)(a)); P's model and tokens; REP-INV; the STAB machinery; the ledger.
- No value of `S_max`, B-P's caps, the budgets, `T0` or any pin may be filled before the authorized design run and the
  owner's recorded `S_max`.

## Part D. Changes required by r14a (each checked read-only against `wt-impl` at `d87547a4a`)

No item here needs a decisive family, the design run, an LP on OI data or a run of ST-BP. Constants that r14a leaves
`PENDING` (`S_MAX`, B-P's caps and triple, the general triple, pins, `T0`) stay `None` or unset. Where a rule is an
owner ruling's draft default (R1–R8, precondition 2), the script implements the default and keeps it in one place, so
a different ruling is a local change.

| # | finding | script and lines | change required |
| --- | --- | --- | --- |
| D1 | **R14-B1** (control P; `S_max`) | `controls.py` `pending_unbackticked` 1433–1440; `check_mode` 1517–1530 | **Control P's rule is unchanged** (r14a writes placeholders unbackticked). Add self-test cases: the line ``- **`S_max`** = PENDING`` and ``at most PENDING extreme rays; `d ≤` PENDING`` are refused; a line naming `` `PENDING` `` only passes. In `check --freeze` (stage `None`): parse the one line of the preregistration whose stripped form starts ``- **`S_max`** = ``; fail unless it occurs exactly once, its value is a decimal integer `≥ 10^5`, and it equals `qc21_check.py`'s `S_MAX` (read from the pinned blob by AST, no import) and the single `S_max` field of the pinned `stress.json`. Self-test on synthetic preregistration text and synthetic `stress.json`: equal ⇒ pass; each of missing line, two lines, `99999`, file ≠ checker, checker ≠ `stress.json` ⇒ fail |
| D2 | **N2** C-CERT aggregation | `qc21_check.py` `assemble_decisive` 3192–3240. The `C-CERT` in `b_red` at 3201 is the fixture section's (`fx["controls"]`); **a decisive-mode C-CERT over B-P and the reported-only fragments does not yet exist** (r14a-I3) | Add the decisive-mode C-CERT. `unverified` keeps counting fragments whose certificate failed (reported). C-CERT enters `b_red` only if a fragment whose certificate failed was **given a verdict**; a failed certificate makes the fragment `undecided` (B-P ⇒ B-VOID through `decide-b`; reported-only ⇒ reported). Fixture mode unchanged (any failed certificate ⇒ exit 3; M-SOLVER still sees `unverified > 0`). Self-test: an undecided reported-only fragment leaves C-CERT green and B's token unaffected; a verdict given over a failed certificate turns it red |
| D3 | **N3** `verdict` token line | `controls.py` `verdict_mode` 1751–1778 | The token line is already `"%s %s %s level %s"` (P, B, C, level). Change: `decide(meas)` VOID only for schema, mode, completeness, placeholder or flag disagreement (round level); P/B/C VOID tokens are printed in the token line, not a `verdict` failure; print `none` for no Level. `VERDICT VOID` and exit 1 only on a failed C.3 condition. Mirror in `make_note`'s token line. Same as r14's B6 bullet, now frozen by rows 89–90 |
| D4 | **N4** B-RAY-F | `qc21_check.py` `FIXTURE_EXPECT` 3244–3247, `fixture_fragments` 3250–3252; fixture-mode list | Add B-RAY-F: B-S4F's four point laws plus the mixture (½, ½) of the first two, B-S4F's effects. Expect 5 distinct rows, 4 extreme rays, one verified removal, feasible, step 4, `T = 3`, model verified. `v_verify` (866–923) must check reproduction of its own `N` on **every** preparation, removed ones included; the step-4 model's `μ_p` for a removed row is computed from `a_p` (`μ_p(j) = (g_j · a_p) s_j`), not dropped. Self-test: drop the removed row from the model ⇒ C-CERT fails |
| D5 | **N7** ADA claim | `controls.py` `c_iface` 821–864; `make_note` 1335 ff. (ADA section at 1372) | Move every ADA status computation into functions named `ada_*` (the note only formats their results). C-IFACE: no `ada_*` function references `bp_equals_qmp`; add the mutation "an `ada_*` function reads `bp_equals_qmp`" ⇒ self-test red |
| D6 | **N10** early-ST-BP guard | `qc21_check.py` `stress_output` 3401–3420; constants 38–46 | `--stress` exits 4 with no output while `S_MAX is None`. The self-tests of item 2's rule (reference instance, caps, budgets, timeout test, failure rule) in `controls.py` use synthetic `stress.json` records built in memory; none calls `stress_output` or generates SF-1 |
| D7 | **N11** artifact names | `controls.py` `upload()` 289–297 | **Defect:** `name.split()[-1]` gives `arp2-qc21-output` for both "the fixture output" and "the stress output", a duplicate name within one run, which `upload-artifact@v4` rejects. Use the frozen names `arp2-qc21-fixtures` (A4), `arp2-qc21-stress` (A6), `arp2-qc21-measurements` (B5), passed explicitly. `verdict`'s S1 binding filters by `arp2-qc21-measurements` |
| D8 | **N14** SF-2 in `--stress` (R3 default) | `stress_output` 3401–3420 | Decide each SF-2 instance under no cap and no budget (as the other stress fixtures); record its counters; include it in the general budget's maxima in `check --freeze`'s recomputation |
| D9 | **N19** S1 binding record | `controls.py` `derive_run` 1677 ff.; `verdict_mode`; `GH_TEMPLATES` | `derive-run` on S1's run also records, for the artifact named `arp2-qc21-measurements`: `id`, `name`, `digest`, `workflow_run.id`, `workflow_run.head_sha`, `expires_at`, and the archive's member list (zip read in memory under the same `ZipFile` rule: `namelist()` only). `verdict` requires its fresh read to equal `evidence/s1-run/results.json`'s record. S1-BIND self-test gains the mismatch case (`id`, `digest` or member list differs). The zip template is used only by `verdict` and `derive_run` |
| D10 | **N20** completion statuses | `make_note` | B-CONTEXTUAL text: print each completion's result (`out_of_scope`/`undecided` by name), name the first restoring completion with a verified certificate, or print the frozen "No completion in the frozen list restored a model within this round's frozen caps and budget: {…}" sentence |
| D11 | **N6** REP-INV table change (R7 default) | `qc21_check.py` `s_build_repinv`; `decide_levels` (both scripts) | A B-P or B-C table that differs beyond the alternative's own relabelling is not re-decided: record it among the changed inputs and treat it as a change of contextuality in the reclassification rule. Self-test on synthetic REP-INV records |
| D12 | **N13** labels | `verdict` self-test (r14's B9) | Name the crash and timeout cases "incomplete-output halt" in the self-test and note; each still gives `VERDICT VOID` |
| D13 | **N15** | — | Already r14's B8 self-test; r14a names it as D23's checkpoint. No further change |
| D14 | **N12**, **N16**, **N17**, **N8**, **N18**, **N9** (beyond D1) | — | Text only; no script change |
| D15 | **"the sum covers both"** (found via Q-C2-2 r14) | — | Text only (C.8 item 2 reading). `check --freeze`'s inequality is unchanged |
| D16 | **C-SYM** (via Q-C2-2) | `qc21_check.py` `s_decide_effect_facet` 656 ff.; `fixture_section` 3316–3342 (not `assemble_decisive`; r14a-I2) | The transposed step 4 exists. **Missing** (r14a-I2): `s_decide_effect_facet` discards its certificate (`verdict, _ = s_step4(…)`, 665); it decides under a fresh `Budget()`, not the fragment's; no verifier with the roles exchanged exists. Check against row 92: its certificates are verified by `v_*` with the roles exchanged (infeasible `W h_k = Σ_p y_{kp} a_p`, `tr W < 0`; feasible model `μ_p(k) = (κ′_k · a_p)(h_k · b_u)`, `ξ_e(k) = (h_k · b_e)/(h_k · b_u)`); C-SYM is green only if every C-SYM certificate verifies; each C-SYM decision draws on the fragment's budget, its counters enter the budget maxima and its work `W_fix` (`--stress` decides it too). Add all three |
| D17 | **No sets** (via Q-C2-2) | `qc21_check.py`: by AST count 38 `set`/`frozenset` calls, 4 set displays and 6 set comprehensions (r14a-I4; `review/probes-r14a/script_facts.out`; e.g. 901, 941, 1296, 1319, 1416); `controls.py` C-INDEP whitelist 753 | Replace every `set`/`frozenset` call, set display and set comprehension in `qc21_check.py` with lists or `dict` keys (insertion order), keeping each output's order as now (most sites are already `sorted`). Control B: refuse any of them in `qc21_check.py`; M-GUARD variant. Remove `"set"` from C-INDEP's builtin whitelist (753). `controls.py` is not covered by the rule (as in Q-C2-2) |
| D18 | **rule (e) f-string** (via Q-C2-2) | `controls.py` 429–438 (`JoinedStr` admitted when every `FormattedValue` is an `a_ok` call) | Implementation already matches row 98. Add the M-GUARD variant (row 95): a `gh` path f-string with a formatted value that is not `a_ok(...)` must fail B |
| D19 | **synthetic merges** (via Q-C2-2) | `derive_run` 1677 ff.; `check_mode` (6′ and design-run checks) | `derive-run` records each `pull_requests` entry's base and head `sha` from the runs API. `check --freeze` fails unless `design-run.json`'s and `confirmation-run.json`'s entry has base `sha` = `D` and head `sha` = the run's `head_sha`; a missing entry fails. Self-test on synthetic run records |
| D20 | **`approvals.json` and `E`'s entry** (via Q-C2-2; R8 default; R14A-B1, r14a-I1) | `controls.py` `GH_TEMPLATES` 90; `gh_get`; `verdict_mode`; `order`; `E_FILES`; approvals schema | **Add `"issues/comments/{DEC}"` to `GH_TEMPLATES`** (rule (g), edit row 99; r14b), with its `{DEC}` filled by an `a_ok` DEC value, so that `verdict` and `e-entry` can read comments; the M-GUARD f-string rule (D18) applies to it. `verdict` reads every approval comment (`approvals.json`'s entries and `E`'s), the designation of `E`, and under R8's default the ratification, each through this template, and checks author, author association, `created_at`, `updated_at` and the quoted words (C.3). `approvals.json` holds the entries of dispatches before `E` (S1, retakes). `verdict` takes the `E` approval comment id (`a_ok` DEC) and builds and checks `E`'s entry (C.3's binding, order and edited-comment rules) and prints it in its record. R8's default: `verdict` also takes the owner's ratification comment id and prints `VERDICT VOID` unless that comment quotes the canonical-JSON sha256 of the entry it builds and passes the authorship checks. Self-test on synthetic comments: entry built; wrong sha256, missing ratification, edited comment ⇒ VOID |

## Part E. Changes required by r14b (each checked read-only against `wt-impl` at `d87547a4a`)

Nothing here needs a decisive family, the design run, an LP on OI data or a run of ST-BP. Where a rule is an owner
ruling's draft default (R1–R9, precondition 2), the script implements the default in one place, so that a different
ruling is a local change. Line numbers marked "r14b" are the preregistration's.

| # | finding | script and lines | change required |
| --- | --- | --- | --- |
| D21 | **R14A-B1** `verdict`'s entry condition (r14b C.3, rows 101 and 105) | `controls.py` `verdict_mode` 1751–1778 | `verdict` fails (`VERDICT VOID`, exit 1) unless every approval entry holds, `E`'s included: each entry of `approvals.json`, and `E`'s entry built from the `E` approval comment's id, checked by the same function. Inputs (C.8 item 9): the `E` approval comment id, the designation-of-`E` comment id and, under R8's default, the ratification comment id, each an `a_ok` DEC argument. Self-test on synthetic comments and runs: all entries hold ⇒ the token line; `E`'s entry failing any C.3 check (author, association, edited after its run, comment after the run's `created_at`, reused comment, quoted commit ≠ `head_sha`) ⇒ `VERDICT VOID` |
| D22 | **r14a-N3** the `e-entry` mode (r14b C.5 modes, row 100; C.8 item 9) | `controls.py` `main` 2140–2193 (no such mode) | Add `e-entry <E> <comment id>`: it builds `E`'s entry with the function `verdict_mode` uses, applies C.3's checks, and prints the entry as canonical JSON (`sort_keys=True`, `separators=(",", ":")`, `ensure_ascii=False`, UTF-8) with its sha256. It prints no `VERDICT` line. Control B's rules apply as to any mode. Self-test: `e-entry` and `verdict` give byte-identical entries on the same synthetic records |
| D23 | **R8** draft default (ratification comment) | `verdict_mode` | Under R8's default, `verdict` reads the ratification comment through `issues/comments/{DEC}`, applies C.3's authorship checks, and requires its body to contain the sha256 of the entry `verdict` builds; otherwise `VERDICT VOID`. Keep the ratifying act in one function, so that R8's alternative (the designation quotes the sha256) is a local change. Self-test: wrong sha256, missing ratification, edited ratification ⇒ VOID |
| D24 | **r14a-N4** R1's floor and lowering rule (r14b C.8 item 2) | `controls.py` `check_mode` 1517–1530 (D1's `S_max` check) | Keep the floor `10^5` as one named constant, used only by the `S_max` check, so that removing it after a red design run at `10^5` (R1's draft default) or under R1's alternative is a one-line change made before that design run. D1's self-test cases stand under the default |
| D25 | **r14a-N13** R9, UPR-BC (r14b *The representation ledger*; UPR-BC control) | `controls.py` and `qc21_check.py` `decide_levels`; `make_note` | Under R9's default, UPR-BC fires only when the completion "every slot of every cell, registered jointly" restores a model with a verified certificate; when it is `out_of_scope` or `undecided`, no label, L-UPRIME not reclassified, and the note prints the completion's status. Add the UPR-BC self-test's third case (contextual; that completion `out_of_scope` ⇒ no label, status printed) |
| D26 | **r14a-N11** `derive-run` reads S1's archive before `E` is committed (r14b rule (g), row 82; C.8 items 3 and 7) | `derive_run` 1677 ff. | No change beyond D9: `derive-run` on S1's run, before `E` is committed, records the binding's inputs in `evidence/s1-run/results.json`. Docstrings and comments say "before `E` is committed", not "at `E`" |
| D27 | **r14a-I5** DS's inputs (pre-existing) | `controls.py` `INPUTS` 52–66 | `INPUTS` lacks QA, FB, M2D, MI-R, SUB, RCH and DSN, and maps `tools/v3_verifier.py` to `None`, so DS does not re-check rows that the preregistration's *Inputs* section says it re-checks. Add every Inputs row (Appendix D.1 and the *Inputs* table) with its blob at `D`; rows whose blob is PENDING in the preregistration (RCH, DSN) stay unset and fail DS until filled. For `tools/v3_verifier.py`, rule (h) says the inputs pin its blob, but *Inputs* has no row for it (precondition 1 gives its sha256 at `fd539e15` only); `INPUTS` keeps `None` until the text gives that pin (noticed in r14b, not changed: DISPOSITIONS-r14b §4). Self-test: an unset or wrong blob fails DS |
| D28 | **r14a-N1, N2, N5, N6, N7, N8, N9, N10, N12** | — | Text only (labels, ruling statements, the PENDING markers, the copies of the cap values, the sketch-review item, typography, provenance); no script change. N7: `check --freeze` already compares the checker's constants with its recomputation (B2); it does not parse the preregistration's copies |
