# Log summary: run 37718803221, job 113121430254 ("Mathlib bridge")

Head sha `f062fcffc930cbffc034c7119e079dc5cf343768`. Source: `mcp__github__get_job_logs` (owner `amaybaum`, repo `incompleteness`, job_id 113121430254, return_content true). Raw text received: `raw.log` in this directory.

## Coverage of the retrieved text (read first)

- The tool reported `original_length: 37338` (a line count — the 5000 returned lines alone are 427,446 characters) and returned **5000 lines** — the last 5000 lines of the log (full-log lines 32339–37338). Calls with `tail_lines` 20000 and 40000 returned byte-identical responses, so the tool caps at 5000 lines and has no offset parameter; the first 32338 lines could not be obtained through it.
- Fallbacks, all read-only: the built-in `gh api .../actions/jobs/113121430254/logs` refuses the redirect to the log host, and a direct download of the signed log URL (host `productionresultssa7.blob.core.windows.net`) was refused by the session egress proxy (`connect_rejected`, organization policy). Not retried or routed around. The check run's annotations (2) hold only a runner Node.js 20 deprecation warning and an ubuntu-latest migration notice — no Lean messages.
- The window opens at `2026-10-08T02:41:00.3411980Z` in the middle of `OIBridge/DitaTorusLocus.lean` output: window lines 1–4894 are all DitaTorusLocus messages (110 axiom reports, 808 warnings with their hint/note bodies). The build-progress lines in the window are only `[3640/3643]`, `[3641/3643]`, `[3642/3643]`.
- **Consequence:** the output of `OIBridge.RelcSelectParity` and `OIBridge.RelcSelectBlock` (build lines, warnings, axiom reports) is not in the retrieved text. Items (a) and (b) below are complete only for RelcSelectSqueeze and RelcSelectC5.

## (a) Every line mentioning `RelcSelect` (verbatim, in order)

29 lines, window lines 4895–4923:

```text
2026-10-08T02:41:14.0943431Z ℹ [3640/3643] Built OIBridge.RelcSelectSqueeze (14s)
2026-10-08T02:41:14.0944476Z info: OIBridge/RelcSelectSqueeze.lean:487:0: 'OIBridge.RelcSelect.frame_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.0945807Z info: OIBridge/RelcSelectSqueeze.lean:488:0: 'OIBridge.RelcSelect.relT_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.0947157Z info: OIBridge/RelcSelectSqueeze.lean:489:0: 'OIBridge.RelcSelect.relC_symm_of_relT' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.0948792Z info: OIBridge/RelcSelectSqueeze.lean:490:0: 'OIBridge.RelcSelect.gateRel_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.0950074Z info: OIBridge/RelcSelectSqueeze.lean:491:0: 'OIBridge.RelcSelect.gSq_frame' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.0951342Z info: OIBridge/RelcSelectSqueeze.lean:492:0: 'OIBridge.RelcSelect.gateRel_gSq' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.0952942Z info: OIBridge/RelcSelectSqueeze.lean:493:0: 'OIBridge.RelcSelect.pairVal_gSq_prodState' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.0954179Z info: OIBridge/RelcSelectSqueeze.lean:494:0: 'OIBridge.RelcSelect.gSq_core' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.0955289Z info: OIBridge/RelcSelectSqueeze.lean:495:0: 'OIBridge.RelcSelect.gSq_posFwd' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.0956317Z info: OIBridge/RelcSelectSqueeze.lean:496:0: 'OIBridge.RelcSelect.gSq_symm_value' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.0957328Z info: OIBridge/RelcSelectSqueeze.lean:497:0: 'OIBridge.RelcSelect.gSq_not_posInv' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.0958350Z info: OIBridge/RelcSelectSqueeze.lean:498:0: 'OIBridge.RelcSelect.not_nativeGate_gSq' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.0959395Z info: OIBridge/RelcSelectSqueeze.lean:499:0: 'OIBridge.RelcSelect.not_nativeGate_gSqInv' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.0960399Z info: OIBridge/RelcSelectSqueeze.lean:500:0: 'OIBridge.RelcSelect.gSq_sep' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.0961394Z info: OIBridge/RelcSelectSqueeze.lean:501:0: 'OIBridge.RelcSelect.gSqInv_sep' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.1944013Z ℹ [3641/3643] Built OIBridge.RelcSelectC5 (15s)
2026-10-08T02:41:14.1945088Z info: OIBridge/RelcSelectC5.lean:404:0: 'OIBridge.RelcSelect.isNot_nC5' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.1946548Z info: OIBridge/RelcSelectC5.lean:405:0: 'OIBridge.RelcSelect.gC5_frame' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.1947759Z info: OIBridge/RelcSelectC5.lean:406:0: 'OIBridge.RelcSelect.gC5_relT' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.1948964Z info: OIBridge/RelcSelectC5.lean:407:0: 'OIBridge.RelcSelect.gC5_not_relC' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.1950273Z info: OIBridge/RelcSelectC5.lean:408:0: 'OIBridge.RelcSelect.selC5_target' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.1951502Z info: OIBridge/RelcSelectC5.lean:409:0: 'OIBridge.RelcSelect.selC5_core' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.1953022Z info: OIBridge/RelcSelectC5.lean:410:0: 'OIBridge.RelcSelect.prodEffVal_gC5_prodState' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.1954349Z info: OIBridge/RelcSelectC5.lean:411:0: 'OIBridge.RelcSelect.gC5_posFwd' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.1955584Z info: OIBridge/RelcSelectC5.lean:412:0: 'OIBridge.RelcSelect.gC5_posInv' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.1956458Z info: OIBridge/RelcSelectC5.lean:413:0: 'OIBridge.RelcSelect.c5_sep' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.1957359Z info: OIBridge/RelcSelectC5.lean:414:0: 'OIBridge.RelcSelect.not_nativeGate_gC5' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-08T02:41:14.1958340Z info: OIBridge/RelcSelectC5.lean:415:0: 'OIBridge.RelcSelect.relT_not_dimension_selecting' depends on axioms: [propext, Classical.choice, Quot.sound]
```

- Distinct `OIBridge.RelcSelect.*` names with an axiom report in the retrieved text: **27** (15 from `RelcSelectSqueeze.lean` lines 487–501, 12 from `RelcSelectC5.lean` lines 404–415); each name is reported once.
- Axiom lists: **all 27 are exactly `[propext, Classical.choice, Quot.sound]`**. Names that differ: none. Lines reading "does not depend on any axioms": 0.
- Cross-check against the source at `f062fcf` (repository file, not the log): the 27 reports match the 27 `#print axioms` commands in those two files exactly (file, line, name). The same source has 7 further RelcSelect `#print axioms` commands whose output is **not in the retrieved text**: `RelcSelectParity.lean:365` `OIBridge.RelcSelect.finrank_plus_eq_finrank_minus_relC`, `RelcSelectParity.lean:366` `OIBridge.RelcSelect.not_even_of_relC`, `RelcSelectBlock.lean:761` `OIBridge.RelcSelect.ctrlGate_of_nativeGate`, `:762` `OIBridge.RelcSelect.actT_slice_ctrl`, `:763` `OIBridge.RelcSelect.blockData_of_ctrlGate`, `:764` `OIBridge.RelcSelect.dim_of_ctrlGate`, `:765` `OIBridge.RelcSelect.three_of_ctrlGate`. Their axiom lists cannot be stated from this log.

## (b) Warning lines mentioning a RelcSelect file

- Lines containing "warning" that mention a RelcSelect file, in the retrieved text: **0**.
  - `RelcSelectSqueeze.lean`: 0 (build line `ℹ [3640/3643] Built OIBridge.RelcSelectSqueeze (14s)`, followed only by `info:` axiom lines)
  - `RelcSelectC5.lean`: 0 (build line `ℹ [3641/3643] Built OIBridge.RelcSelectC5 (15s)`, followed only by `info:` axiom lines)
  - `RelcSelectBlock.lean`: **not determinable** — its output is outside the retrieved window, so the expected 7 warnings can be neither confirmed nor refuted from this text.
  - `RelcSelectParity.lean`: not determinable, same reason.
- For context, the only Lean warnings in the window (808 `warning:` headers) are all from `OIBridge/DitaTorusLocus.lean`: 586 unused-variable, 110 unused simp argument, 56 "this tactic is never executed", 56 unused-tactic linter.
- Errors: no Lean `error:` line, no `##[error]` line and no failed-build (✖) marker in the retrieved text (0 such lines). The only line containing the substring "error" is a Node deprecation message in post-job cleanup:

```text
2026-10-08T02:42:13.2716513Z (node:24803) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
```

  The first 32338 lines of the log were not retrieved and were not checked for errors.

## (c) `sorryAx`

- Lines mentioning `sorryAx` in the retrieved text: **0** (none). No line reads "declaration uses 'sorry'". The only line containing "sorr" is the gate's lean-axioms line:

```text
2026-10-08T02:42:10.4428231Z   PASS  lean-axioms      lean_axiom_check: OK (5860 named result(s) reported, no sorr
```

  Its detail text stops at "no sorr" because `tools/release_gate.py` (at `f062fcf`) prints each check's detail as `tail[:60]`; the truncation is in the log itself, not introduced by retrieval.

## (d) Release gate output (verbatim)

Step header (the second line carries ANSI colour escapes; the ESC byte is shown here as `\x1b`, otherwise verbatim):

```text
2026-10-08T02:41:22.5594734Z ##[group]Run python3 tools/release_gate.py
2026-10-08T02:41:22.5595279Z \x1b[36;1mpython3 tools/release_gate.py\x1b[0m
2026-10-08T02:41:22.7198699Z shell: /usr/bin/bash -e {0}
2026-10-08T02:41:22.7199044Z ##[endgroup]
```

Gate output, window lines 4951–4975:

```text
2026-10-08T02:42:10.4413864Z release gate
2026-10-08T02:42:10.4415795Z ====================================================================
2026-10-08T02:42:10.4416740Z   PASS  toolchain        toolchain_check: OK (build entry present, unicode-fix.tex co
2026-10-08T02:42:10.4417730Z   PASS  staleness        staleness_check: OK (13 matched, 0 unstamped)
2026-10-08T02:42:10.4418626Z   PASS  baseline-label   baseline_label_check: OK (no baseline archives named)
2026-10-08T02:42:10.4419568Z   PASS  voice            voice_check: OK (no manuscript-voice history narration; 40 m
2026-10-08T02:42:10.4420499Z   PASS  voice-scope      voice_scope_test: OK (6 scope case(s); the checker scans the
2026-10-08T02:42:10.4421900Z   PASS  ci-gate-presence ci_gate_presence_test: OK (CI runs the real release gate)
2026-10-08T02:42:10.4423157Z   PASS  artifact-placement artifact_placement_check: OK (no unaccounted root artifact; 
2026-10-08T02:42:10.4423832Z   PASS  manifest-drift   build_migration_manifest --check: OK (91 artifacts; both gen
2026-10-08T02:42:10.4424439Z   PASS  claims           claims_check: OK (no withdrawn result asserted unconditional
2026-10-08T02:42:10.4425037Z   PASS  duplicate        duplicate_check: OK (no paragraph repeated within a file)
2026-10-08T02:42:10.4425543Z   PASS  mirror           mirror_check: 0 chapter line(s) absent from FULL.md
2026-10-08T02:42:10.4426032Z   PASS  citation         citation_check: 112 citation(s), 0 broken, 0 duplicate bib n
2026-10-08T02:42:10.4426568Z   PASS  architecture     architecture_check: 259 invariant(s), 0 violation(s), 0 self
2026-10-08T02:42:10.4427133Z   PASS  dependency-label dependency_label_check: OK (no stale dependency label, 41 fi
2026-10-08T02:42:10.4427704Z   PASS  coverage         coverage_check: OK (129 canonical statements, 19 unattached 
2026-10-08T02:42:10.4428231Z   PASS  lean-axioms      lean_axiom_check: OK (5860 named result(s) reported, no sorr
2026-10-08T02:42:10.4428782Z   PASS  lean-manuscript  lean_manuscript_census: OK (every cited identifier and path 
2026-10-08T02:42:10.4429330Z   PASS  legacy-records   LEGACY  303 record(s) in 75 closed namespace(s), all intact
2026-10-08T02:42:10.4429832Z   PASS  v3-self-test     v3_verifier: self-test OK
2026-10-08T02:42:10.4430220Z   PASS  v3-corpus        CORPUS  140 vector(s), exact and as expected
2026-10-08T02:42:10.4430638Z   PASS  v3-receipts      RECEIPTS  41 receipt(s), all hold
2026-10-08T02:42:10.4431000Z ====================================================================
2026-10-08T02:42:10.4431493Z release gate: PASS  (note: --label bNNN not given, so the baseline check ran in relative mode only)
```

- 21 checks, all PASS. Key lines: `lean-axioms` → "5860 named result(s) reported, no sorr" (cut at 60 characters by the gate); `v3-receipts` → "RECEIPTS  41 receipt(s), all hold"; `legacy-records` → "LEGACY  303 record(s) in 75 closed namespace(s), all intact" (303, as expected); `lean-manuscript` → "OK (every cited identifier and path " (cut at 60); final line `release gate: PASS` with the relative-mode baseline note.

## (e) Job conclusion

End of the Build step:

```text
2026-10-08T02:41:22.4313733Z Build completed successfully (3643 jobs).
2026-10-08T02:41:22.5146822Z TIMING lake-exe-cache-get 88s
2026-10-08T02:41:22.5147441Z TIMING lake-rehash-build 27s
```

Final lines of the log (post-job steps, window lines 4976–5000):

```text
2026-10-08T02:42:10.9449895Z Post job cleanup.
2026-10-08T02:42:11.2519117Z (node:24803) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-10-08T02:42:11.2520427Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-10-08T02:42:11.2719851Z [command]/usr/bin/tar --posix -cf cache.tzst --exclude cache.tzst -P -C /home/runner/work/incompleteness/incompleteness --files-from manifest.txt --use-compress-program zstdmt
2026-10-08T02:42:13.2716513Z (node:24803) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
2026-10-08T02:42:14.2602035Z Sent 0 of 142399406 (0.0%), 0.0 MBs/sec
2026-10-08T02:42:15.2599546Z Sent 75290542 of 142399406 (52.9%), 35.9 MBs/sec
2026-10-08T02:42:15.4399020Z Sent 142399406 of 142399406 (100.0%), 62.3 MBs/sec
2026-10-08T02:42:15.6024583Z Cache saved with key: oibridge-Linux-324962b2357195e1544c06a1936656a7dafa7cf303e07c9c08c1e5a3b289622d-450b74934fafa98d8efb2396cf9012f612f953ee930ddb1c34797c3a20f51f86
2026-10-08T02:42:15.6227975Z Post job cleanup.
2026-10-08T02:42:15.7173560Z [command]/usr/bin/git version
2026-10-08T02:42:15.7224830Z git version 2.55.0
2026-10-08T02:42:15.7297889Z Temporarily overriding HOME='/home/runner/work/_temp/801da142-9300-4eeb-b0ff-b46d4b7137e6' before making global git config changes
2026-10-08T02:42:15.7299270Z Adding repository directory to the temporary git global config as a safe directory
2026-10-08T02:42:15.7305764Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/incompleteness/incompleteness
2026-10-08T02:42:15.7349249Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-10-08T02:42:15.7387199Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-10-08T02:42:15.7706874Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-10-08T02:42:15.7736592Z http.https://github.com/.extraheader
2026-10-08T02:42:15.7749621Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
2026-10-08T02:42:15.7795649Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-10-08T02:42:15.8060242Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-10-08T02:42:15.8104427Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-10-08T02:42:15.8516784Z Cleaning up orphan processes
2026-10-08T02:42:15.8818707Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/cache@v4, actions/checkout@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```

The raw log has no explicit conclusion line. The REST API (`GET /repos/amaybaum/incompleteness/actions/jobs/113121430254`, saved as `job_api.json`) reports: status `completed`, conclusion **`success`**, started `2026-10-08T02:38:51Z`, completed `2026-10-08T02:42:18Z`; steps: 1 Set up job = success; 2 Run actions/checkout@v4 = success; 3 Install elan = success; 4 Restore the OIBridge build cache = success; 5 Build = success; 6 Release gate = success; 11 Post Restore the OIBridge build cache = success; 12 Post Run actions/checkout@v4 = success; 13 Complete job = success.

## Notes

- Missing from the retrieved text: everything before full-log line 32339, including all RelcSelectParity and RelcSelectBlock output. Nothing in the retrieved text is anomalous: every visible RelcSelect axiom report is the standard three, no RelcSelect warning, no error, no `sorryAx`, gate PASS, job success.
- `wait.txt` in this directory predates this extraction (mtime 02:53:01Z) and was left untouched.
