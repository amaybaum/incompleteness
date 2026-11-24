# Implementation inventory: design v6.0e -> code -> controls (revision 2)

Revision 2, 2026-11-24, made under correction 1 (owner `amaybaum`, decision 2: "D-4 and D-10: correct the inventory";
nit N-3). It supersedes `IMPLEMENTATION-INVENTORY.md` (sha256 e87cde6c…f301, kept as written). Changes from that file:
the dangling reference "D-18" is D-10 (N-3); the rows for `engine/outcome.py`, `engine/schema.py` and
`engine/selftest.py` are "modify", not "retain" (D-10); section 4 corrects the statement of discrepancy D-4; the rows
touched by correction 1 (commit 3184c7f9075948d8474197eee03ba5b94ba85db5) are updated and section 5 lists them.
Every other row is as in revision 1.


Design `DESIGN-v6.0e.md` (sha256 4024a31c…5131), inventory `INVENTORY-v6.0e.md` (ce3abd51…20f0). Branch
`tools/ledger-coverage-20261123`, base 443e871f225a414f69bef3f1e3cab45cb30d6594, final commit as in `EXACT-DELTA.md`, corrected by 3184c7f9 (`CORRECTION-1.md`).
Paths are relative to `tools/` unless they start with `verification/`. "conf" = `ledger_coverage/adapters/conformance_controls.py`,
"syn" = `adapters/synthetic_fixture.py`, "self-test" = `engine/controls_engine.py` via `ledger_coverage.py self-test`,
"a1" = `adapters/a1_controls.py`, "a1c" = `adapters/a1_conformance.py`. Status is the local run of `logs/repro.sh`
(see `logs/controls-table.md`).

## 1. Inventory table 3a (entry point and engine)

| Inventory row | Action | Code (final commit) | Controls |
|---|---|---|---|
| `ledger_coverage.py` wrapper | modify | `ledger_coverage.py` (run as `python3 -I -S -B`, correction 1, D-7): isolation check (`_inside`, `sys.flags.isolated`) before `import json`, exit 65 with a plain-text refusal; `_load_package` (spec_from_file_location with submodule_search_locations); no `sys.path` insert; INTERNAL result carries `class_meaning` | EI6 (conf), X2, X7, X8 (syn) |
| `engine/authority.py` (everything but the three functions below) | remove | file deleted | retired ids (sec. 10) |
| `authority.read_pin_table`, `admitted_by_table`, `snapshot_sha` | move | `engine/config.py`: `read_pin_table` (strict: last `### N.N Record pins` subsection, header/separator, malformed or duplicate rows raise `PinTableError`), `admitted_by_table` (regular files only); `snapshot_sha` replaced by `util.fingerprint` where used | TR2, TR3, EI4 (conf) |
| `engine/host.py` retained parts | retain / modify | `RestHost.detect` (job's own run id and repository id; None without either), `_run` (repository id, head repository id, event, head branch, workflow path, `head_sha`; incomplete record raises), `run_record`, `runs_for` (incomplete listing raises), `artifact_sha256` (incomplete listing raises) | GV7-tool, GV7-consumer (conf) |
| `engine/host.py` removed parts | remove | `first_line`, `_graphql`, `repository`, `main_head`, `file_at`, `paths_at`, `entries_at`, `first_parent_chain`, `on_first_parent_chain`, `_tree`, `_entry`, `file_history`, `comments`, `deletion_events`, `b64` deleted | host reads limited (sec. 6.3) |
| `engine/host.py` `MemoryHost` | modify | runs, per-commit host runs, artifacts, `fail` and `incomplete` sets only | GV7 |
| `engine/gitobj.py` `_batch`, `_commit`, `read_blob`, `paths` | modify | `_batch`: full id only, `git --no-replace-objects` with `GIT_NO_REPLACE_OBJECTS`, `GIT_NO_LAZY_FETCH`, `GIT_ALLOW_PROTOCOL` (no transport), id recomputed (`object_id`); `_commit`: tree and parent lines parsed from verified bytes; `_tree`: entries and modes parsed; `entries`, `paths`, `mode`; `read` refuses a non-regular entry | GV1, GV2, GV3, GV4, GV5, GV6, GV6-disk (conf) |
| `gitobj.resolve`, `tree_id`, `is_ancestor` | modify | `resolve`: full id, verified; `tree_id` from parsed trees; `is_ancestor` walks parsed parents (missing parent is unresolvable); `Overlay` likewise, with non-regular in-memory entries | GV1, GV3, GV5 |
| `gitobj.diff_u0` | retain | runs with `--no-replace-objects` (diagnostic only) | |
| `engine/cli.py` `build_parser` | modify | `--plan`, `--round`, `--config-sha256` removed; no pin-table option | EI4 (b) (USAGE 64), Z6b (syn) |
| `cli.admission` | modify | `admission` (replay / control harness / chain); `freeze_admission` (points 1-2); `disk_checkout`; `execution_identity` (points 1, 2, the `uses:` rule of point 5, point 6); snapshot fields of sec. 6.3 | TR1-TR3, TR5-sim, TR13-TR15, TR28-tool, TR29-tool, TR48, TR50-TR52, EI1, EI2, EI4, EI7-tool, GV6, GV7-tool (conf) |
| `cli.engine_identity` | modify (design) | unchanged function (engine blob hash from disk); `T` and every tool blob are recorded in the snapshot by `execution_identity` (`tool_commit`, `tool_blobs`, `workflow`) | TR48 |
| `cli.stages`, `finish_snapshot` | modify | no `owner_id`; admission record passed through | TR5-sim |
| `cli.resolve`, `split_ref` | modify | `resolve` uses the verified reader (full ids only) | GV1 |
| `cli.RecordSet`, `rule_files`, `op_execution`, `native_env` | retain / modify | no owner argument; a record at a non-regular entry is `record-invalid`; `native_env` reads host-run evidence in the configuration's `repository_id` | GV6, G4-G9 (conf) |
| `engine/config.py` owner, forbidden list, authorization lookups | remove | `forbidden` and `retirement.owner` removed (`retirement_fields = ('name', 'issue')`), no owner timeline, admitted set = records + reviews | Z1-Z8, Z10 (syn), A12 mutant |
| `config.py` fields `tool`, `repository_id` | add | `required` lists them; `tool_layout` (entry point and package directory derived from the module's location, no literal); `tool_problems` (sec. 16.2 lint); widening by the generic rule of `non_widening` | X10 (syn), TR5-sim, TR28 |
| `config.py` records of an undefined kind | add (sec. 16.2) | a `records` entry whose JSON `schema` is not a defined record kind is `CONFIG_INVALID` | mutant A13 |
| `config.py` scans | modify | `scan` and the harness neighbour read take regular-file entries only | GV6 |
| `engine/records.py` owner parts | remove / modify | `auth_schema`, `_owner`, `_comment`, `OwnerTimeline` and the authorization loop removed; `owner` parameters removed from `lint_chain`, `supersedes_problems`, `predecessor_problems`, `widening_review_problems`, `widening_review_ok` | O1-O3, O5-O9 (self-test), LN1-LN8, LN10, R6-G6, A12r (conf) |
| `engine/checker.py` `accept` | modify | schema `/5`; pins `{config, adapters, freeze, pin_table, tool}`; snapshot `freeze`, `pin_table`, `configuration`, `tool_blobs`, `workflow` compared | X10, X11, EI3 |
| `checker.accept_with_host` | modify | run record by run id in `repository_id`: repository and head repository ids, event, `head_sha == T`, workflow path; `T`'s tool entries from the consumer's verified store (exact set, regular, sha256), workflow blob and `uses:` rule, `T` on `M`'s first-parent chain, evaluated commits, artifact digest | TR14, TR15, TR28-consumer, TR29, TR30, EI2-consumer, EI3, GV7-consumer |
| `checker.uses_line_problems` | add (sec. 6.3 point 5, R-a) | the three refusal clauses on the raw text; the owner component a GitHub account name, `[A-Za-z0-9](?:-?[A-Za-z0-9])*`, so `./` and `../` are refused with a 40-hex suffix (correction 1, B-1) | EI7-tool (22 forms), TR28-consumer (four EI7 cases), mutants U01-U05, C01-C04 |
| `checker.resolve_main` | add (sec. 13.4) | `git ls-remote` output check (exit, one main line, full id, readable, equal to `L`'s first parent) | EI5 (the readability clause isolated by the case of an id equal to the given first parent; correction 1, N-1) |
| `engine/replay.py` | modify | the admission is re-derived from `F` (`freeze_admission`) and compared with the snapshot's pin table; INTERNAL/ERROR docs annotated | TR45-opB |
| `engine/delegation.py` `host_runs` | modify | keeps runs with event push or workflow_dispatch and both ids equal to `repository_id`; failed or incomplete read is None (missing evidence) | GV7-tool (host-run class), G7 |
| `delegation.Native.clone` | modify (inventory open item 8, O-3) | clone and checkout run with `GIT_CONFIG_NOSYSTEM=1`, `GIT_CONFIG_GLOBAL=/dev/null` | O3-FILTER (conf; correction 1, D-11): the global configuration's smudge filter |
| `engine/purity.py` | modify | schema ids: `/5`, no `oi-owner-authorization/1`, `oi-tool-authority/2`, `oi-freeze-ledger/1`; `tool_paths` removed; fourth category `interface_names = {'PREREG.md'}` (discrepancy D-3) | Z9a-Z9h, staged purity lint (step 2) |
| `engine/controls_engine.py` | modify | `chain_world`, `chain_probs`, `o_controls` without authorization; O4 removed | self-test O1-O3, O5-O9 |
| output schema | modify | `schemas/oi-ledger-coverage-5.schema.json` (`/4` removed) with `class_meaning` const and required; `config.admission` required wherever `config` is present (correction 1, N-2) | S7-schema-and-checker (syn) |
| `engine/outcome.py` | modify (inventory 3a: retain; D-10) | `result_schema` `/5`; `class_meaning`; `annotate` (discrepancy D-10) | O01, O02 mutants; schema validation |
| `engine/schema.py`, `engine/selftest.py` | modify (inventory 3a: retain; D-10) | the schema file name; self-test result annotated | self-test |

## 2. Inventory table 3b (adapters and runners)

| Inventory row | Action | Code | Controls |
|---|---|---|---|
| `staged_purity_lint.py`, `a1_conformance.py`, `a1_controls.py`, `conformance_controls.py`, `host_fixture.py`, `synthetic_fixture.py` | modify | package loaded by location (no `sys.path` insert) | all runners |
| `host_fixture.py` | modify | reduced: `World` (tool commit `T` with the fixture tool and workflow, run record, `checkout`), `tool_pins`, `pin_table` (with an optional earlier subsection), `freeze` | TR*, GV7, EI1-EI7 |
| `rest_fixture.py` | remove | deleted | |
| `synthetic_fixture.py` | modify | no authorization records, no `retirement.owner`; `tool` and `repository_id` in the configuration; `Runner.cli` runs the simulated chain through `host_fixture`; Z6b checks that `--config-sha256` is USAGE; X10 against the `tool` pins | Y1-Y10, Z1-Z10, X2-X10, M10 |
| `a1_controls.py` | modify | `k1_graph` without authorization records; `chain_refusal` (also with the stand-in `F`); `rev_parse` for the runner's own ref arguments; no `--config-sha256` | K1-GRAPH, CHAIN-REFUSAL, all A1 controls |
| `conformance_controls.py` | modify | rewritten TR, GV, EI groups; retained groups with authorization removed (R3-F2, R4-B3, R4-B3-DUP, R5-N6, R6-G6, LN1-LN8, LN10, G4-G9, R16, R17, A12r, Z11, S4a, X11, TR30, TR45, TR46); removed groups as inventory 3b lists | see section 3 |
| `a1_conformance.py` | modify | WB wording "fingerprinted" (N-3); package loading | WB1-WB15, S11-*, N3-N18, R18, R19 |

## 3. Controls of the S13 acceptance list and the new controls

| Control | Where | Local status |
|---|---|---|
| Z1-Z8, Z10, Y1-Y10, X2-X10, M10 | syn | PASS (Y8: engine hash recorded; the two-configuration CI run is CI only) |
| Z9a-Z9f | syn; Z9g, Z9h a1 | PASS |
| N2-N18, R18, R19 | a1c (N3-N18, R18, R19), self-test (N2) | PASS |
| S4a, Z11 | conf | PASS |
| LN1-LN8, LN10 | conf | PASS |
| S11-56, S11-57a-d, S11-58a-k, WB1-WB15 | a1c | PASS |
| G4-G9 | conf | PASS; G-A1 NOT RUN (CI) |
| TR1-TR3, TR13-TR15, TR28-TR30, TR48, TR50-TR52 | conf | PASS |
| TR5 | conf | NOT RUN (CI only); TR5-sim PASS |
| TR45 | conf (op B) | PASS for op B; the op-C part is not implemented locally (as at 443e871f) |
| TR46, X11 | conf | PASS |
| GV1-GV7 | conf (GV1-GV5, GV6-disk on disk; GV6, GV7 in memory); GV4 with the corrupted HP merge (correction 1, D-6) | PASS |
| EI1-EI15 | conf (EI6, EI8-EI15 as subprocess runs on trees under OUT_DIR) | PASS; EI10 needs a C compiler (SKIP without one) |
| R16, R17, A12r | conf | PASS |
| K10 | self-test | PASS |
| every A1 control of sec. 10-11 | a1, a1c | see `logs/controls-table.md`; RT-T NOT RUN (no reviewed records) |

## 4. Discrepancy D-4, corrected statement

`DISCREPANCIES.md` D-4 lists the families in `controls.json` at 443e871f as "RT, V, A, S11, L, N-W, G1-G3, X1, SW". The
file holds 80 entries: RT (14: RT-A, RT-E, RT-H0, RT-T0, RT-T, RT-C, RT-D, RT-DR, RT-DR3W, RT-I7, RT-I7A, RT-X, RT-L,
RT-L2), X1, SW1-SW2, L1-L4, V (28), N-W, A1r-A11r, S1r, S2r, G1-G3 and S11-1 to S11-14, so the families are V, S, RT,
A, L, G, SW, X and N, as the review found. D-4's conclusion stands: there is no TR, LN or WB entry; their expectations
live in the runners' `expected` strings; GV1-GV7 and EI1-EI15 were added verbatim from sec. 10.4. Correction 1 leaves
`controls.json` unchanged: its GV and EI rows remain the design's verbatim text, and the cases added by correction 1
(EI7's three suffixed forms, GV4's HP merge, EI5's unreadable first parent) are stated in the runner's case text.

## 5. Rows changed by correction 1

| Item | Code | Controls |
|---|---|---|
| B-1 | `engine/checker.py` `_uses` (owner component) | EI7-tool, TR28-consumer; mutants C01-C04 |
| D-1 | the workflow moved to `.github/workflows/ledger-coverage.yml`; `adapters/conformance_controls.py` `WORKFLOW`; `adapters/a1_controls.py` `WORKFLOW_PATH` among the landed files; class record pins it as one exact path; README | EI6, EI8-EI15 (extraction from the moved file), RT-L2 (landed paths) |
| D-2 | the workflow: `check` (choice), role inputs `h`, `x`, `e`, `m`, `l`, all through `env:`; one fixed `case` arm per plan check, every expansion quoted; `exit 64` after `esac` | line rule and R-e extraction on the workflow (`logs/corr1/probe/`) |
| D-6 / N-5 | GV4 case "the HP merge m1" | GV4; mutants C09, C10 |
| D-7 | the workflow's entry command `python3 -I -S -B`; EI harness entry flags; `_interpreter_dirs` under `-I -S` | EI6; mutants C11, C12 |
| D-11 / N-4 | `adapters/conformance_controls.py` `o3_controls` | O3-FILTER; mutants C07, C08 |
| N-1 | EI5 case | EI5; mutant C06 |
| N-2 | schema `config.required` gains `admission` | ACCEPT-SCHEMA; mutant C05 |
