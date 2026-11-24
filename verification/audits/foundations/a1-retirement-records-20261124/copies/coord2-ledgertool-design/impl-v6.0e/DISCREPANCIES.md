# Design-code discrepancies, readings and blockers (implementation of v6.0e)

Each item is escalated, not decided. "Implemented as" states what the commits do now, so that a reviewer or the
owner can accept or redirect it. None of them reopens a settled design decision.

## Escalations

**D-1. Placement of the pinned workflow (blocker for any real run of TR5, EI14 on the host).** Inventory table 3d
says the pinned workflow "is written with the implementation"; design sec. 12.3 says "the tool's landing may add
paths only under `tools/` and its audit directory" (control R14); GitHub runs workflows only from
`.github/workflows/`. Implemented as: the workflow text in the audit directory
(`verification/audits/foundations/ledger-coverage-tool-20261123/workflow/ledger-coverage.yml`), pinned in the staged
A1 configuration as `tool.workflow = {path: .github/workflows/ledger-coverage.yml, blob_sha256: <that text's
sha256>}`; the EI controls extract the pre-run program from that text. A run needs a byte-identical copy at
`.github/workflows/ledger-coverage.yml` on `main`, which this landing does not add. Owner decision needed: add the
copy in the tool landing (an exception to sec. 12.3 and a class-record entry), in the plan amendment's landing, or in
its own landing.

**D-2. How a plan check's arguments reach the entry point.** Sec. 6.3 point 5's checklist fixes "the exact run
lines: the fetch of F, the pre-run check, and the entry point's command", with inputs reaching the shell only through
`env:`. The design does not say how the per-check arguments of P's sec. 11 commands (operation, `--commit`, `--check`,
`--final`, ...) are given. Implemented as: a third `workflow_dispatch` input `operation`, passed as `OPERATION` and
expanded unquoted (`python3 -I -B tools/ledger_coverage.py $OPERATION --freeze "$F" --config "$F:$CFG" --out
"$RUNNER_TEMP/out"`), so the dispatcher's string is word-split and glob-expanded. Alternatives for the workflow's
review: one workflow (or job) per plan check with fixed arguments; `set -f` before the command. The trigger is
`workflow_dispatch` only (flag F-19 left this to the workflow's review).

**D-3. Purity allowlist: a fourth category for `PREREG.md`.** Design sec. 6.3 fixes the pin-table file name
`PREREG.md`; the staged purity lint (Z9 with the A1 configuration's profiles) flags that literal, because the A1
deny profile `register-caps` (P's `CAPS`) matches `PREREG`. Sec. 16.1 lists three allowlist categories (field names,
schema ids, enumerations). Implemented as: a fourth category `interface_names = frozenset(['PREREG.md'])` in
`engine/purity.py`, linted to be one `*.md` file name (as v5.5.9's implementation had a fourth category for the
authority record's path). Alternative: a design amendment naming the category, or treating the name as an engine
enumeration. Every other new engine string was reworded instead (commit 0e14261c).

**D-4. `controls.json`: TR, LN and WB entries.** Inventory 3c: "the TR, LN and WB expectations as in table 2; GV1-GV7
and EI1-EI15 added". The file at 443e871f holds only A1 controls (RT, V, A, S11, L, N-W, G1-G3, X1, SW); it has no TR,
LN or WB entry, so nothing was modified for them (their expectations live in the runners' `expected` strings, which
were updated). GV1-GV7 and EI1-EI15 were added verbatim from sec. 10.4 with `operations: []` (tool-level), and the
header names DESIGN-v6.0e with its sha256.

**D-5. GV4, "although `git cat-file -p` prints the content".** With git 2.43, `cat-file -p` prints a corrupted blob
or commit but refuses a corrupted tree ("hash mismatch"); `git cat-file <type>` and `--batch` (what the store
serves to a reader that does not verify) return the substituted bytes in every case. The control asserts the served
bytes and records `-p`.

**D-6. GV4, the class for a corrupted commit of E..H.** For the configured HP merge commit, the configuration
loader's retained `hp_chain_check` reports `CONFIG_INCONSISTENT` ("merge ... is not resolvable") before any other
read, not the unresolvable-object class; both are ERROR 65 and no PASS. The control corrupts the segment's first
commit (also a commit of E..H, read through the verified reader), which gives `UNRESOLVABLE`. If the design intends
the unresolvable-object class for a corrupted merge commit too, `hp_chain_check` (inventory: retain) would change.

**D-7. EI6, "the interpreter's standard library".** On this host the isolated interpreter imports
`_distutils_hack` from the system package directory through a `.pth` file at startup. The control's predicate allows
the directories of the interpreter's own isolated `sys.path` (its standard library and installed packages), none
inside the checkout, in line with flag F-15 (the runner image is trusted); a narrower reading (standard library only)
would fail on such hosts without any checkout file executing.

**D-8. The class record is re-pinned in place.** Inventory 3c says "modify (re-pin)" and "a new version pins the v6.0
landing". The record is an unreviewed draft never landed; as S1 did, `records/side-change-classes-v1.json` is
re-pinned in place (53 pins, equal to `git ls-files -s` of the landing paths). A `-v2` record with `supersedes` would
be the alternative if "a new version" means a new file.

**D-9. TR45, op-C part.** As at 443e871f, only the op-B/D replay (TR45-opB) is a local control; the op-C replay from
recorded delegated evidence needs native delegated runs at `X` and `C` (G-A1) and stays for CI.

**D-10. Changes beyond inventory table 3a's "retain".** `engine/outcome.py` (schema `/5`; the `class_meaning` table
and its quotation in every item, site state and file state, which sec. 5 "Class meanings" requires and table 3a does
not list), `engine/schema.py` (the renamed schema file) and `engine/selftest.py` (the self-test result annotated).

**D-11. O-3 (inventory open item 8) implemented without a local control.** The delegated clones run `git clone` and
`git checkout` with the runner's global and system configuration disabled. No filter driver is installed here, so
the effect is not exercised; it belongs with G-A1 in CI.

**D-12. Runtime of the A1 sweeps.** The A1 control step took 4647 s against S1's 1208 s (sweeps 4182 s); peak 1.2 GB.
Not a defect of the guarantees: objects are verified once and cached; the cost is `GitRepo.paths()` rebuilding its
dict on every call (EXACT-DELTA, "Runtime and memory"). Within the default 360-minute hosted-job limit; not
optimized now, by owner instruction.

## Readings (implemented, stated for review)

- **R-1.** `is_ancestor` decides from parsed parents; a negative answer walks the second commit's whole history, so
  in a shallow store it is an unresolvable object (GV5). The A1 runs ask it only for commits that are ancestors of the
  rules' `recorded_at` or in memory (answered without a walk); the A1 controls pass on the shallow shared store.
- **R-2.** TR14's "a consumer that runs in a fork" is simulated as the consumer's host reporting the fork as the run's
  repository; EI14's branch dispatch as `GITHUB_REF=refs/heads/feature` on the materialized tree.
- **R-3.** The entry point's isolation refusal is plain text on stderr (exit 65): no module may be imported before
  the check, so no JSON encoder is available.
- **R-4.** The tool's execution identity compares the run's `workflow_path` with `tool.workflow.path` and reads the
  workflow blob at that path in `T`; the `uses:` rule runs at the tool and at the consumer.
- **R-5.** Control ids TR28 and TR29 are reported in two halves (`TR28-tool`/`TR28-consumer`, `TR29-tool`/`TR29`) and
  EI2, EI7, GV7 with a consumer half; Z6b (implementation id) now asserts that `--config-sha256` is USAGE.

## Not blockers, recorded

- `RestHost` reads `/repositories/{id}/...` paths; S1 observed that this session's proxy refuses numeric-id paths.
  No real-host read was made here (none was required: every host read has an in-memory control).
- The A1 configuration (staged, outside the repository) pins every tool file at the final commit; it must be
  regenerated whenever a tool file changes.
