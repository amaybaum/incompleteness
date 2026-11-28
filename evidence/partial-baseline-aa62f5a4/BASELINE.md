# Bounded tool-acceptance baseline at aa62f5a4: partial local reconstruction

**This is RECONSTRUCTED evidence, produced in this session (2026-11-28) on a local detached worktree. It is not
the recovered original workspace evidence of the previous writer, and it is not a full baseline.** It is a
partial run: the steps that need the tool-acceptance fixture snapshot could not run, because the snapshot is
not available (section 2). Nothing was written to GitHub, and nothing was dispatched.

- Subject: `aa62f5a47454983d0b3ac771450a78118fbaaab7`, tree `60fbb0789dc5a3ba1ece60c83e22fcc24ee8b175`. HEAD was
  verified and the status was clean before and after the run (0 entries).
- Worktree: `SP/a11-baseline-aa62f5a4/wt`, created with `git worktree add --detach` from the shared store. The
  store is shallow (22 shallow roots). No fetch was needed: `9be526b6` (origin/main), the merge base `d7794dc9`,
  and the fixed commits `8e9b8334`, `14ac71b4` (T1') and `4c79be64` (P) are all present.
- The preview merge (`merge-tree --write-tree` and `commit-tree`) wrote its objects only to the private directory
  `SP/a11-baseline-aa62f5a4/preview-objects`, which used the store as a read-only alternate. Preview
  `4e85cb9a1ddded8a4b365d1221dd0d01648d2c25` (tree `08116b08a7a8f721606317892c970484af380c1a`) is absent from the
  shared store.

## 1. Procedure (source: `.github/workflows/ledger-coverage.yml`, job `suite`, `job=tool-acceptance`)

`run.sh` repeats the workflow's suite job step for step.

1. Inputs: `F` is the reviewed fixture snapshot S, `CFG` is the configuration path in it, `M` is the
   representative anchor (the synthetic M_rep), and `S=F`.
2. Suite guard: pins `CFG`'s `tool.files` against the checkout and writes `staged-config.json`.
3. Engine self-test (`tools/ledger_coverage.py self-test`).
4. `engine_controls.py`.
5. `staged_purity_lint.py`. Needs `F:CFG`.
6. `synthetic_fixture.py OUT .`.
7. `conformance_controls.py`, without `--native-tr5` at tool acceptance.
8. `obl29`, `custody`, `adjudication`, `staging` and `sessions` controls.
9. `a1_conformance.py --config F:CFG --tool-revision HEAD --tool-acceptance`. Needs F.
10. `a1_controls.py --config F:CFG --main M --rep-template HEAD:<tool audit>/rep/control-instance.json
    --rep-snapshot F --rep-descriptor-sha256 sha256(F:${CFG%/*}/a1-staging-transition.json) --tool-candidate HEAD`.
    Needs F.
11. Control gate: `--records` for each job, then `--tool-candidate HEAD --fixed-config F:CFG --repo .
    --tool-base origin/main --tool-preview <merge-tree preview>`.
12. Evidence digest.

**SW1/SW2.** The workflow has no separate mutation step. SW1 and SW2 are recorded by `a1_controls.py`, which runs
its sweeps unless it is given `--skip-sweeps`. The workflow omits that flag, so the sweeps are on the CI route. The
plan (IMPLEMENTATION-PLAN-r6.md sec. 9) puts the mutation run, which takes hours, in CI only. In this run SW1 and
SW2 are blocked anyway, because `a1_controls.py` needs F.

## 2. Inputs that could not be reconstructed

- **The tool-acceptance F (fixture snapshot S), its CFG, its first-parent base B and the synthetic M_rep.** The
  previous writer's objects (for example B `1cf0c02b`, S `2cca4002` and M `5312bb2b` at 34009af6, and the
  "rebuilt" fixture used at 9cef4d22) are not in the local store. None of the 2,269 refs that origin advertises
  points to them.
- **The configuration itself.** No `retirement-config.json`, `execution-control-config.json` or
  `a1-staging-transition.json` exists in the branch tree or on main at `9be526b6`. The README's local recipe names
  `a1exit-deletion-20261121/retirement-config.json`, which is also absent.
- **Can it be regenerated from the branch?** No. No tool on the branch builds S, B or M. `rep_instance.py` only
  fills the template's holes from an existing S and M, and `staging_controls.py` builds in-memory synthetic worlds
  only. Building S would mean writing new class records, an allow root, a transition descriptor, an execution
  control configuration and review records, which would be invented inputs.
- **Not used.** `origin/staging/a1-allow-root-20261127` (`8f668f55`) carries unreviewed WIP drafts of the live
  staging files, with no configuration. It is not the synthetic fixture.
- **Lost row tables.** The per-row tables of the recorded runs (`GATE-9cef4d22.json` and the aa62f5a4 scoped
  packets) were in the lost workspace. Only the aggregate counts and the named rows in the PR comments survive.

## 3. Execution (local, 4 CPUs, 15 GB RAM; about 12 GB free disk)

| step | exit | wall | peak RSS |
|---|---:|---:|---:|
| self-test | 0 | 0.3 s | 28.9 MB |
| engine | 0 | 8.7 s | 31.5 MB |
| purity | blocked (needs F) | - | - |
| synthetic | 0 | 26.7 s | 58.2 MB |
| conformance | 0 | 35.2 s | 68.0 MB |
| obl29 | 0 | 6.2 s | 41.5 MB |
| custody | 0 | 13.9 s | 53.0 MB |
| adjudication | 0 | 0.2 s | 30.7 MB |
| staging | 0 | 3.5 s | 54.4 MB |
| sessions | 0 | 0.3 s | 33.3 MB |
| a1-conformance | blocked (needs F) | - | - |
| a1-controls | blocked (needs F; includes SW1/SW2) | - | - |
| gate (partial, no `--fixed-config`) | 20 GATE_FAIL | 2.0 s | 84.4 MB |

The F-independent part ran in about 100 s. The engine self-test passed 97 of 97 controls. The auxiliary suites
recorded these cases:

| suite | PASS | FAIL |
|---|---:|---:|
| obl29 | 161 | 4 |
| custody | 123 | 0 |
| adjudication | 43 | 0 |
| staging | 120 | 0 |
| sessions | 12 | 0 |

The four obl29 FAILs are FINDING-FORM, FINDING-KEYS, FINDING-LINEAGE and REASSESS-KEYS, and the obl29 suite still
exited 0. The two auxiliary fixture regressions reported at 9cef4d22 now PASS here: OBL-29 N-BRANCH-DRAFT and
custody LIVE-SELECTOR. A second gate run over the same records gave byte-identical results.

## 4. Row results of this partial gate

| scope | PASS | NOT RUN | FAIL |
|---|---:|---:|---:|
| all 619 rows | 323 | 114 | 182 |
| 484 retained A1 rows (AMENDMENT-8 kept list) | 295 | 7 | 182 |
| recorded full result at 9cef4d22 (7237112421) | 377 | 191 | 51 |
| expected at aa62f5a4 (9cef4d22 + 8 PASS + TR45 trio NOT RUN) | 384 | 194 | 41 |

FAIL findings (rows can carry more than one finding):

| finding | rows |
|---|---:|
| missing-id | 170 |
| status-not-allowed | 13 |
| raw-evidence-missing | 12 |
| status-actual-inconsistent | 2 |

The FAIL rows fall into three groups.

- **Missing records from blocked steps (147).** The `a1_controls.py` rows (95) and the `a1_conformance.py`
  rows (47). Z9-STAGED comes from the purity lint. S11-7, REPRO-DOUBLE and RT-O9-L2 come from `a1_controls`. The
  composites S11-2, RT-D and V27 inherit missing components. This group includes K1-GRAPH, REP-BUILD, RT-L2,
  RT-O9, S1r, S11-57d, SW1, SW2, V3-countercontrol and Z9g.
- **Missing records, no runner on the branch (23).** CONFIG-REFS, CTX-INDICATOR, DELEG-RECDIR, DELEG-REGEN,
  HIT-REPLACEMENT, HP-RECORDS, HP-SEMCLASS, LC-7, OUT-ADAPTERS, OUT-EXPLAIN, PROF-LANDING-LIST, PROF-PARAMS-LINT,
  RECON-FIELDS, RECON-SCHEMA, REPRO-PYVER, RESOLUTION-SCHEMA, REVIEW-SCHEMA, RT-M, RT-SHIFT, SUPERSEDES-RESOLVE,
  VD2-HP-SEARCH, VD3-CONTEXT and VD3-COUNT. No adapter emits these ids, so they would also be missing in a full
  run.
- **A record is present, but the predicate or raw evidence fails (12).**
  - Raw evidence is missing and the status is not allowed: BLOCK-KEY, FINDING-FORM, FINDING-KEYS,
    FINDING-LINEAGE, O3-FILTER (missing the oracle output), REASSESS-KEYS, RECON-ENUM, RECON-OVERLAP, RECON-TRIAL
    and RTL2-BIND.
  - Raw evidence is missing and the status is inconsistent with the runner: RDIR-25 (the
    `existing_conformance_controls_unchanged` invariant is not attested; the runner reports PASS) and TT14
    (`evaluated_in` is not attested; the runner reports PASS).

### Rows named in the records, checked here

- **Agrees with 7237880887.** ANCH-OVERRIDE, OUT-FROZEN, OUT-CONFINED, PIPE-CHAIN, PIPE-PRIOR, PIPE-REPO,
  PIPE-STAGES and SCAN-PARSE are all PASS. TR45-opB, TR45-opC and TR45 are all NOT RUN. RDIR-25, TT14 and
  O3-FILTER remain FAIL for the reasons that record states.
- **Agrees with 7237112421.** CANON-JSON, CLASS-RETAINED, CLASS-SCHEMA and MIGRATION-RECORD are PASS. The
  RECON-ENUM, RECON-OVERLAP, RECON-TRIAL and RTL2-BIND failures match the earlier review's list. RECON-FIELDS and
  RECON-SCHEMA have no record.
- **Not checkable here, because they need F.** S11-7, Z9-STAGED and Z9g (recorded as PASS at 9cef4d22), RT-L2 and
  RT-O9-L2 (scheduled NOT RUN), K1-GRAPH, S11-57d, REPRO-DOUBLE, S1r, V3-countercontrol, SW1 and SW2.
- **No contradiction found.** Every row that the F-independent runners decide agrees with every named status in
  the records. A full row-by-row comparison is impossible for two reasons: the recorded per-row tables are lost,
  and this run lacks the three F-dependent steps.

## 5. Proposed route to a full baseline (nothing dispatched)

The local run is cheap. The F-independent part takes about 100 s, and the sweeps run in CI only. The blocker is
the missing input, not cost. A full baseline needs three things:

- The reviewed fixture snapshot S, its CFG and the synthetic M_rep, either recovered or rebuilt and independently
  reviewed, then pushed to a ref.
- An owner-approved dispatch of `ledger-coverage.yml` with `job=tool-acceptance`, `freeze=S`, `config=CFG` and
  `m=M_rep`, on the exact tool commit. Per §A.39/§A.40, the dispatch is a launch.
- Alternatively, a local run of `run.sh WT OUT S CFG M_rep` once S exists in the store, with SW1/SW2 left to that
  CI run.

## 6. Files (`SP` = `<records>`)

| file | sha256 |
|---|---|
| `SP/a11-baseline-aa62f5a4/run.sh` | `b9b4f6aa83c89ec76ae9af247b63aff2f36dfa5edaf7fed5807375292021cc57` |
| `SP/a11-baseline-aa62f5a4/suite/gate/gate-result.json` (replay identical) | `5ea5fc9bbe38289c6242f680d0eeac27baa983a14dcaecf0ec1072cb2d3207f0` |
| `SP/a11-baseline-aa62f5a4/suite/evidence-digest.txt` (18,103 files) | `83bbfb11e8f04ba83573d59e90e5f3f7d0e1878b3db24be515bdeeaee88ae348` |
| `SP/a11-baseline-aa62f5a4/rows.tsv` (619 rows) | `de462b6c0da6ea598dbc68a188bee6cb021c2432846d9054773cdeadcf92acc1` |
| `SP/a11-baseline-aa62f5a4/kept484.txt` (from AMENDMENT-8.md line 338) | `c15555969fca8c11ba809b88b0bdc808f9ea97e88db1b39fe6a1b61feee9dd91` |

Per-step logs and timing are in `SP/a11-baseline-aa62f5a4/timing/`.
