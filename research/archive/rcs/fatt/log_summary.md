# Job log summary: job 113148584104 ("Mathlib bridge"), run 37727395526

Source: `mcp__github__get_job_logs` with owner `amaybaum`, repo `incompleteness`, job_id `113148584104`, return_content `true`, tail_lines `5000`. Every count and quoted line below was computed by Python (`scripts/summarize.py`, run with `python3 -I`) over `raw.log`; line numbers are 1-based positions in `raw.log`.

## Provenance

| file | sha256 |
|---|---|
| `raw.log` | `b72496fae8e4057c022e6a767426f89dedcb665602aebfc1179ac38b2a70c508` |
| `raw_tool_response.json` | `e37a7657efe9192c9a2005a9c8aa481f4e53bf5993a43773a66efcdb23d1bab9` |
| `job_api.json` | `b2e780c36c6a43c5dd77631f1f0df29bcab7748d70311424783680a28899af03` |

- `raw.log` is byte-identical to the decoded `logs_content` field of `raw_tool_response.json`: **True**.
- Tool message: `Job logs content retrieved successfully`.
- Job API (`job_api.json`): name `Mathlib bridge`, run_id `37727395526`, head_sha `1003b029b4949516e615cea8fbf0531c0ced583b`, head_branch `claude/relc-select-1`, run_attempt `1`, status `completed`, conclusion `success`, started `2026-10-08T04:25:20Z`, completed `2026-10-08T04:28:27Z`.
- Job API steps (number | name | conclusion | started -> completed):
  - 1 | Set up job | success | 2026-10-08T04:25:21Z -> 2026-10-08T04:25:22Z
  - 2 | Run actions/checkout@v4 | success | 2026-10-08T04:25:22Z -> 2026-10-08T04:25:37Z
  - 3 | Install elan | success | 2026-10-08T04:25:37Z -> 2026-10-08T04:25:37Z
  - 4 | Restore the OIBridge build cache | success | 2026-10-08T04:25:37Z -> 2026-10-08T04:25:41Z
  - 5 | Build | success | 2026-10-08T04:25:41Z -> 2026-10-08T04:27:34Z
  - 6 | Release gate | success | 2026-10-08T04:27:34Z -> 2026-10-08T04:28:23Z
  - 11 | Post Restore the OIBridge build cache | success | 2026-10-08T04:28:23Z -> 2026-10-08T04:28:24Z
  - 12 | Post Run actions/checkout@v4 | success | 2026-10-08T04:28:24Z -> 2026-10-08T04:28:24Z
  - 13 | Complete job | success | 2026-10-08T04:28:24Z -> 2026-10-08T04:28:24Z
- Read-only git context: `git rev-list --parents -n 1 1003b029` -> `1003b029b4949516e615cea8fbf0531c0ced583b e2426ba4109dcd719d518aefbd3c417b7c6fdc5b`; `git diff --name-status e2426ba4 1003b029` -> `A	verification/programmes/oi-qm/reconstruction/round-relc-select-1/preregistration.md`; `.lean` paths in that diff: 0.

## 0. Coverage

- Reported original length (`original_length` field of the tool response): **37219**.
- Lines returned: **5000** (4999 newline characters, no trailing newline; 429461 characters). Lines without a timestamp prefix: 0.
- Read as a line count (the unit of `tail_lines`), the window is original lines 32220-37219; the first 32219 lines of the job log are not in it.
- First timestamp (line 1): `2026-10-08T04:27:34.4659997Z`. Last timestamp (line 5000): `2026-10-08T04:28:24.6980845Z`. Min/max over all lines: `2026-10-08T04:27:34.4659997Z` / `2026-10-08T04:28:24.6980845Z`.
- Step layout inside the window: lines 1-4951 are the tail of the **Build** step's output (timestamps `2026-10-08T04:27:34.4659997Z` to `2026-10-08T04:27:34.5483230Z`; the job API puts Build at 2026-10-08T04:25:41Z -> 2026-10-08T04:27:34Z); lines 4952-4980 are the **Release gate** step; lines 4981-5000 are post-job cleanup.
- The window opens inside one module's messages: lines 1-4846 (before the first progress line) carry 892 Lean diagnostics citing `OIBridge/DitaTorusLocus.lean` (892), plus their continuation and blank lines; that module's own `[k/n]` line precedes the window, so whether it was built or replayed is not visible here.
- Build-progress lines `[k/n]` in the window: **5** (status glyphs: `ℹ` 4, `⚠` 1; verbs: `Replayed` 5; lines with `] Built`: 0):

```text
 4847 | 2026-10-08T04:27:34.5442683Z ℹ [3633/3639] Replayed OIBridge.TrackBQfbBridge
 4875 | 2026-10-08T04:27:34.5454892Z ℹ [3635/3639] Replayed OIBridge.ProductAdmission
 4882 | 2026-10-08T04:27:34.5458400Z ⚠ [3636/3639] Replayed OIBridge.ProductStrictLift
 4923 | 2026-10-08T04:27:34.5473127Z ℹ [3637/3639] Replayed OIBridge.ProductOffLocusUniqueness
 4929 | 2026-10-08T04:27:34.5475983Z ℹ [3638/3639] Replayed OIBridge
```

- Final lake line (1 match; lines matching `Build failed`/`build failed`: 0):

```text
 4949 | 2026-10-08T04:27:34.5482898Z Build completed successfully (3639 jobs).
 4950 | 2026-10-08T04:27:34.5483129Z TIMING lake-exe-cache-get 94s
 4951 | 2026-10-08T04:27:34.5483230Z TIMING lake-rehash-build 4s
```

  (the two `TIMING` lines that follow it are included for context.)

## (a) `RelcSelect`

- Lines containing `RelcSelect` (case-sensitive): **0**.
- Supplementary: lines containing `relcselect` case-insensitively: 0; containing `relc` case-insensitively: 0. (The window holds no checkout output; the branch name `claude/relc-select-1` above comes from the job API.)

## (b) Errors and failure markers

- Lean `error:` lines (post-timestamp body starts with `error:`): **0**.
- `##[error]` lines: **0**.
- Failed-build marker lines (contain `✖`, U+2716): **0** (total occurrences: 0).
- Supplementary: lines containing `error:` anywhere: 0; lines containing `error` case-insensitively anywhere: 0; non-table lines with the word `fail`/`failed`/`failure`: 0.
- Context: Lean `warning:` lines 799; Lean `info:` lines 178; `##[warning]` lines 1:

```text
 5000 | 2026-10-08T04:28:24.6980845Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/cache@v4, actions/checkout@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```

## (c) `sorry`

- Lines containing `sorryAx`: **0**.
- Lines containing `declaration uses 'sorry'`: **0**.
- Supplementary: lines containing `sorry` case-insensitively: 0; `depends on axioms: [...]` lines: 178; `does not depend on any axioms` lines: 0. Distinct axiom lists in the window:
  - `[propext, Classical.choice, Quot.sound]`: 178

## (d) Release gate

Step header (the runner's group for the step, then the gate's own title and rule):

```text
 4952 | 2026-10-08T04:27:34.5527704Z ##[group]Run python3 tools/release_gate.py
 4953 | 2026-10-08T04:27:34.5527866Z \x1b[36;1mpython3 tools/release_gate.py\x1b[0m
 4954 | 2026-10-08T04:27:34.5637182Z shell: /usr/bin/bash -e {0}
 4955 | 2026-10-08T04:27:34.5637286Z ##[endgroup]
 4956 | 2026-10-08T04:28:23.9503589Z release gate
 4957 | 2026-10-08T04:28:23.9504012Z ====================================================================
```

Per-step table, every row verbatim (ANSI escapes would appear as `\x1b`; none occur in these rows):

```text
 4958 | 2026-10-08T04:28:23.9505098Z   PASS  toolchain        toolchain_check: OK (build entry present, unicode-fix.tex co
 4959 | 2026-10-08T04:28:23.9505953Z   PASS  staleness        staleness_check: OK (13 matched, 0 unstamped)
 4960 | 2026-10-08T04:28:23.9506592Z   PASS  baseline-label   baseline_label_check: OK (no baseline archives named)
 4961 | 2026-10-08T04:28:23.9507110Z   PASS  voice            voice_check: OK (no manuscript-voice history narration; 40 m
 4962 | 2026-10-08T04:28:23.9507611Z   PASS  voice-scope      voice_scope_test: OK (6 scope case(s); the checker scans the
 4963 | 2026-10-08T04:28:23.9508234Z   PASS  ci-gate-presence ci_gate_presence_test: OK (CI runs the real release gate)
 4964 | 2026-10-08T04:28:23.9508802Z   PASS  artifact-placement artifact_placement_check: OK (no unaccounted root artifact; 
 4965 | 2026-10-08T04:28:23.9509388Z   PASS  manifest-drift   build_migration_manifest --check: OK (91 artifacts; both gen
 4966 | 2026-10-08T04:28:23.9509907Z   PASS  claims           claims_check: OK (no withdrawn result asserted unconditional
 4967 | 2026-10-08T04:28:23.9510450Z   PASS  duplicate        duplicate_check: OK (no paragraph repeated within a file)
 4968 | 2026-10-08T04:28:23.9511162Z   PASS  mirror           mirror_check: 0 chapter line(s) absent from FULL.md
 4969 | 2026-10-08T04:28:23.9511855Z   PASS  citation         citation_check: 112 citation(s), 0 broken, 0 duplicate bib n
 4970 | 2026-10-08T04:28:23.9512364Z   PASS  architecture     architecture_check: 259 invariant(s), 0 violation(s), 0 self
 4971 | 2026-10-08T04:28:23.9512893Z   PASS  dependency-label dependency_label_check: OK (no stale dependency label, 41 fi
 4972 | 2026-10-08T04:28:23.9513430Z   PASS  coverage         coverage_check: OK (129 canonical statements, 19 unattached 
 4973 | 2026-10-08T04:28:23.9513923Z   PASS  lean-axioms      lean_axiom_check: OK (5826 named result(s) reported, no sorr
 4974 | 2026-10-08T04:28:23.9514457Z   PASS  lean-manuscript  lean_manuscript_census: OK (every cited identifier and path 
 4975 | 2026-10-08T04:28:23.9514983Z   PASS  legacy-records   LEGACY  303 record(s) in 75 closed namespace(s), all intact
 4976 | 2026-10-08T04:28:23.9515416Z   PASS  v3-self-test     v3_verifier: self-test OK
 4977 | 2026-10-08T04:28:23.9515816Z   PASS  v3-corpus        CORPUS  140 vector(s), exact and as expected
 4978 | 2026-10-08T04:28:23.9516223Z   PASS  v3-receipts      RECEIPTS  41 receipt(s), all hold
```

Closing rule and final verdict line:

```text
 4979 | 2026-10-08T04:28:23.9516579Z ====================================================================
 4980 | 2026-10-08T04:28:23.9517077Z release gate: PASS  (note: --label bNNN not given, so the baseline check ran in relative mode only)
```

- Table rows: **21**; PASS **21**; FAIL **0**; lines between the rules that are not PASS/FAIL rows: 0.
- Row details are limited to 60 characters by the gate itself: `tools/release_gate.py` at `1003b029` prints `print(f"  {'PASS' if ok else 'FAIL'}  {n:16s} {tail[:60]}")`. Rows whose detail sits at exactly the 60-character limit: 12; longer than 60: 0. So the truncated rows are truncated in the job log as printed, not by the fetch.

Requested rows (verbatim):

```text
 4973 | 2026-10-08T04:28:23.9513923Z   PASS  lean-axioms      lean_axiom_check: OK (5826 named result(s) reported, no sorr
 4974 | 2026-10-08T04:28:23.9514457Z   PASS  lean-manuscript  lean_manuscript_census: OK (every cited identifier and path 
 4978 | 2026-10-08T04:28:23.9516223Z   PASS  v3-receipts      RECEIPTS  41 receipt(s), all hold
 4975 | 2026-10-08T04:28:23.9514983Z   PASS  legacy-records   LEGACY  303 record(s) in 75 closed namespace(s), all intact
 4964 | 2026-10-08T04:28:23.9508802Z   PASS  artifact-placement artifact_placement_check: OK (no unaccounted root artifact; 
 4965 | 2026-10-08T04:28:23.9509388Z   PASS  manifest-drift   build_migration_manifest --check: OK (91 artifacts; both gen
```

- `lean-axioms` named results, as printed: **5826**.
- `v3-receipts` receipt count, as printed: **41** (`all hold`).
- `legacy-records` count, as printed: **303** record(s) in **75** closed namespace(s) (`all intact`).
- Final verdict line body: `release gate: PASS  (note: --label bNNN not given, so the baseline check ran in relative mode only)`
- Job API conclusion of the `Release gate` step: `success`.
