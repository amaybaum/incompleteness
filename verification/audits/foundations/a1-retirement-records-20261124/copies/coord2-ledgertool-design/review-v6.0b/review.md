# Independent review of design v6.0b of the ledger coverage tool

Reviewer: independent, non-author. Review only. Nothing was written in the repository or in the
tool worktree, and there was no commit, push, GitHub write, GraphQL call or CI run. No host read
was needed. Every file this review wrote is under `review-v6.0b/`; throwaway probe trees were made
under the session workspace (`rv60b<tmp>/`). The permission system refused no operation.

## Objects verified

| Object | sha256 / id | Result |
|---|---|---|
| `DESIGN-v6.0b.md` | f87dd8bee2c0a9d20beaf462351245f4735eaf056ad0485616fe391dacceb452 | match |
| `INVENTORY-v6.0b.md` | 7efa6bd2614d77a239a7816c219a96e37e7713fad4a0df31ec31444cf4ea630b | match |
| `CHANGES-v6.0b.md` | 1a939950db6104178389cf43e328d9c64bae91bb9fc137080aedba16323033dc | match |
| `CHANGES-v6.0b-from-v6.0a.diff` | a15f68c4d04b8ba9d92ecd37fd20575cfac72b3536fb58da4f3370a42693ea29 | match; regenerated with `diff -u DESIGN-v6.0a.md DESIGN-v6.0b.md`: byte-identical (`cmp`, header lines included) |
| `CHANGES-v6.0b-from-v5.5.9.diff` | c9564ad32b5b85720bada12d819866a79e5943c4fd9c68c1d147ddaa83b3d1cb | match; regenerated: byte-identical (`cmp`) |
| `DESIGN-v6.0a.md` | 105db5efe8803876107e525f868051593227f0cc20f0bd2fb7600ea312113585 | match |
| `review-v6.0a/review.md` | f5f4f57b6c028f0b995984be74be0c1a799e9cd3875dc4c82097a9a0167e9f2a | match |
| `review-v6.0/review.md` | 43cfe728198588eb4f01a38dd817f4d207e50494bb98c5bb20c895df4fddb0ec | match |
| `DESIGN-v5.5.9.md` | cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9 | match |
| `coord2-impl-wt` | HEAD 443e871f225a414f69bef3f1e3cab45cb30d6594 | match; clean |
| `P` | 4c79be642ca631573f06b444903be75ec4f5e2b6 | read with `git show` |
| `AGENTS.md` at 9deb6956 | blob sha256 43a28e2653843e8a8ba87e38778cacd6815b71ee54d7977af945303d1783ce27 | read with `git show`; equals the inventory's input row |

## Verdict: ACCEPT-WITH-NITS

R-1 is fixed as the prior review proposed: TR29's first case is back with its v5.5.9 meaning, and
the import path no longer holds the checkout. CX-1 to CX-4 are refused. I found no route by which
the revised design accepts a result that v5.5.9 would have rejected for technical reasons. No
authorization machinery remains or was added, and no added mechanism is unnecessary.

I found no blocking finding under the stopping rule. The nearest candidate, Q-1 below, is
demonstrated:

- Point 5's sentence "no file outside `tool.files` ... executes in the job, before or after the
  tool's own checks" is false for a `T` whose tool directory differs from the pins.
- Such a `T` is refused by the consumer from its own store in every case I constructed, and is
  bounded to `main` by TR29.
- At any `T` that can be accepted, the property holds.

I therefore classify Q-1 as a precision nit with an optional five-line hardening, and put one
reading of the owner's sentence back to the owner (open item O-1). If the owner reads that sentence
as also covering a `T` that fails the pins, Q-1 becomes blocking. The smallest fix is then stated
there.

## The key question

*"Could an incorrect scientific result pass under the revised design when it would have been
rejected under v5.5.9 for technical reasons?"*

**No.** I found no such case. Each route I tried, and what refuses it:

| Route | v5.5.9 | v6.0b |
|---|---|---|
| CX-1: engine module changed at `T'` | refused (pins in `A`) | refused: TR28, X10 at the tool; at the consumer from its own verified store |
| CX-2: changed workflow writes a forged result | refused (TR15, TR50) | refused: TR15, TR50 against `tool.workflow` |
| CX-3: unpinned `tools/hashlib.py` at a branch `T'` | refused (TR29: `T'` off `main`) | refused: TR29 at the consumer. In addition, the file never executes. Probe P1: no marker under `-I -B` with the v6.0b entry point. Countercontrol P1c: the 443e871f entry point executes it |
| CX-3 at an on-`main` `T` that legitimately holds a `tools/hashlib.py` | **accepted, file executed** (bounded only by `main`'s review) | not executed (P1); strengthened |
| CX-4: `./` local action or reusable workflow; script in `T` | refused off `main` (TR29); on `main`, review only | refused off `main` (TR29); `./` refused mechanically (EI7); scripts by review of the pinned workflow (F-14) |
| Branch-only `T` with pins equal | refused (TR29) | refused at the consumer (TR29 against `M`, EI5) |
| `__pycache__/*.pyc` (unchecked-hash), extension module `*.so`, or symlink inside `tools/ledger_coverage/`, or a symlinked entry point | code executes before checks; refused (extra file, non-regular entry, off `main`) | same: executes in that run (P4, P7, P9, P10), refused at the consumer (TR52, TR51, point 2 "symlink", TR28) and by TR29. See Q-1 |
| `site`/`sitecustomize`/`usercustomize`, `.pth`, `PYTHONSTARTUP`, `PYTHONPATH` | not addressed | user site, `PYTHON*` and script dir are excluded by `-I` (P1, P2). Image `site-packages` and `.pth` are runner-image trust (F-15). The checkout cannot place `.pth` files on the path |
| Interpreter without `-I` | n/a | ERROR 65 (P2). Implementation note N-g (P2b): the check must precede the wrapper's module-level `import json` |
| `python3` from `PATH`, `LD_PRELOAD`, `GIT_*`, `container:`, `setup-*` actions, composite or docker actions pinned by sha but fetching mutable content, self-hosted runner | review of the workflow content only | the same: review of the pinned workflow (F-14), fixed by TR15/TR50. Not weakened; N-b tightens the checklist |
| Git hooks, `core.fsmonitor`, aliases, `includeIf`, filter drivers | `.git/config` and hooks are written by checkout, not taken from the tree; a `.gitattributes` filter needs a driver defined in config; the verified reader recomputes every object id | unchanged (GV1-GV6 strengthen it). A pre-existing observation on delegated clones of `X` is O-3 |
| Artifact substitution across runs or attempts | bound to the run id and sha256 | unchanged. A re-run keeps `head_sha` and the workflow file, so every attempt is pinned code |
| Off-`main` `T` in the landing record's recipe (§A.42 items 1, 3, 8) | impossible | impossible again (TR29) |

There is one place where v6.0b is weaker than v5.5.9 at the tool, but not in acceptance (nit N-c).
TR29's first case is non-acceptance at the consumer only. v5.5.9 also listed an ERROR at the tool.
A branch run can therefore print PASS with `admission: "chain"`. The consumer never accepts that
result, so no incorrect result passes.

## Blocking findings

None.

## Findings, nits and open items

### Q-1 (precision; optional hardening; demonstrated). Point 5's universal sentence holds only at a `T` that satisfies point 2

**Evidence.** Probes run against a copy of 443e871f, with the entry point rewritten as the design
and inventory table 3a specify (`probe/entry_v60b.py`):

- no `sys.path` insert;
- refuse unless `sys.flags.isolated` and no `sys.path` entry lies in the checkout;
- load `tools/ledger_coverage/` by `spec_from_file_location` with `submodule_search_locations`.

Each probe writes a file into a fresh tree. Results (`probe/run_probes.out`, Python 3.13.18):

| Probe | Tree | Result |
|---|---|---|
| P4 | `tools/ledger_coverage/engine/__pycache__/util.cpython-313.pyc` as a PEP 552 unchecked-hash pyc | its code runs **instead of** the pinned `engine/util.py`, before any check. Countercontrol P4c: a checked-hash pyc is ignored |
| P7 | an extension module `engine/util.so` beside the pinned `util.py` | its init runs. Extension modules take precedence over source in the path finder, so `-X pycache_prefix` does not help |
| P9 | the pinned path `engine/util.py` as a symlink to `payload.py` outside the package | the payload runs |
| P10 | the entry point as a symlink to `tools/evil.py` | `evil.py` runs as `__main__`. No check inside the tool can precede it |

**Why this is not an acceptance route.**

- Each of these trees fails point 2 as the consumer repeats it from its own verified store:
  - an extra file under `tools/ledger_coverage/` (TR52);
  - a symlink entry (TR51; point 2 covers the entry point too);
  - a blob that differs from its pin (TR28).
- The code that ran in the job cannot touch the consumer's own store.
- TR29 further requires `T` on `main`.

The same holds, and was already accepted for v6.0a, for CX-1: a changed pinned module at `T'`
also executes before the tool's checks. Anyone who can push a branch can already run arbitrary code
in CI through a workflow file on that branch. Preventing pre-check execution only inside the pinned
workflow at a `T` that fails the pins therefore protects no accepted result.

At a `T` that passes point 2 (exact file set, regular files, pinned blobs):

- no bytecode, extension or symlink can exist under the package;
- with `-I` and by-location loading, nothing outside the package is imported (P1, P3);
- so nothing unpinned executes, which is the property the owner's rationale states ("other,
  unverified files can influence what actually runs").

**Smallest fix (wording, needed).** Scope point 5's first sentence and G23a:

- "At a `T` that satisfies point 2, no file outside `tool.files`, the pinned workflow and the
  interpreter's standard library executes in the job."
- Add one sentence: "At a `T` that fails point 2, its tool files may execute in that run before the
  tool's checks; such a run is never accepted, because the consumer repeats point 2 from its own
  store and TR29 holds."
- Correct "the only files of the checkout that can be imported are the pinned files under that
  directory": cached bytecode, extension modules and symlinks under the package are importable,
  and point 2 refuses them.
- EI1's "a compiled-bytecode file" case is detected at the tool after import, so it may be
  pre-empted; the consumer's TR52 is the binding refusal.

**Optional hardening (about five lines, no infrastructure, demonstrated in P8).** Before importing
the package, the entry point walks `tools/ledger_coverage/` with `os.lstat` and refuses (ERROR 65)
on:

- any `__pycache__` directory;
- any name ending in `importlib.machinery.BYTECODE_SUFFIXES + EXTENSION_SUFFIXES`;
- any symlink.

P8 refuses both the P4 and the P7 trees, and the clean tree (P8c) runs unchanged. P10, a symlinked
entry point, cannot be refused from inside the tool. It is refused at the consumer.

### Nits (non-blocking)

- **N-a. `CHANGES-v6.0b.md` size table.**
  - v6.0a to v6.0b removes **30** lines, not 29.
  - v5.5.9 to v6.0b removes **596** lines, not 520 (`diff -u` count; 3152 - 596 + 457 = 3013).
  - The added counts (86, 457) and the hunk counts (18, 45) are correct.
- **N-b. F-14 checklist.** Make the review rule for the pinned workflow an explicit list, and make
  the `uses:` check fail-closed on the raw text: any occurrence of a `uses` key in a form other
  than `^\s*(- )?uses: <owner>/<repo>[/<path>]@<40 hex>\s*$` refuses.
  - Why fail-closed: a stdlib line check otherwise misses YAML forms such as quoted keys, flow
    mappings, block scalars and aliases.
  - Checklist items:
    - triggers;
    - `permissions` read-only except artifact upload;
    - a GitHub-hosted `runs-on`;
    - no `container:` or `services:`;
    - no `env`, `GITHUB_ENV` or `GITHUB_PATH` change of `PATH`, `LD_*`, `GIT_*` or `PYTHON*`;
    - no `shell:` override;
    - allowed actions named, with no `setup-*`, composite or docker action that installs or
      downloads executables or refers to other actions by tag;
    - the exact run line.
  - Point 5's "executes only the entry point and fixed `git` commands" should also say "and the
    named pinned actions".
- **N-c. TR29 at the tool.** Either restore v5.5.9's tool-level ERROR for a `head_sha` off `main`,
  or state in the class-meaning table that a `"chain"` PASS from a run says nothing about `T`'s
  place on `main` until the consumer checks it. The second is the simpler and enough.
- **N-d. Consistency.** Sec. 5 says the consumer repeats "points 1-3, 5 and 6"; point 4 says
  "points 1-3 and the `uses:` check of point 5". The import-path part of point 5 cannot be
  repeated by the consumer. Use point 4's wording in sec. 5.
- **N-e. Stale "EI1-EI5" in the inventory** (four places):
  - table 1a "10 retired-identifier paragraph";
  - table 2 row S13 (line 923);
  - table 3b `conformance_controls.py` (`tr_controls` rewritten for "... EI1-EI5");
  - table 3c `controls.json`.

  EI6 and EI7 are assigned to no control runner. Name the runner that implements EI6 (a
  subprocess run of the entry point on a materialized tree, as in `probe/run_probes.sh`) and EI7.
- **N-f. G23a.** Record that v5.5.9's workflow clause "verify the tool blobs against
  `engine_pins` before executing" (v5.5.9 sec. 6.3, `A.workflow`) becomes the tool's first step
  plus the consumer's repetition. In acceptance it is not weakened (see Q-1), but the inventory
  should state the disposition. It currently cites only the "run the tool only from that tree"
  half.
- **N-g. Implementation ordering** (inventory table 3a, entry point). The isolation check must
  run before the wrapper's module-level `import json`; only `sys` and `os`, which are already
  loaded at startup, may precede it. P2b: without `-I`, a `tools/json.py` executes before the
  refusal in a literal implementation. This has no effect on acceptance, because the pinned
  workflow fixes `-I`, but EI6's second case should be read as "before any import from outside
  `sys.modules`".
- **N-h. Delegated runs.** Point 5's sentence should exclude the delegated checker processes of
  sec. 7:
  - F's checker blobs, pinned by `checker_sha256`;
  - for `coverage-ledger`, `X`'s own `tools/proof_census.py`, by design.

  Both run in clones under `--out` with `-I -B`. They are not in `tool.files`, and are
  unchanged from v5.5.9.

### Open items

- **O-1 (owner reading).** "An unverified file must not execute, even before the tool performs
  its own integrity checks." Under the reading this review applies, the sentence covers runs that
  can be accepted, and Q-1's wording fix is enough. If the owner means every run of the pinned
  workflow, including at a `T` that fails the pins, the smallest fix is v5.5.9's own clause.
  - The fix: one fixed inline step in the pinned workflow, `python3 -I -S -B -c '<~15 lines>'`.
    It reads the configuration at `F` with `git cat-file`, and compares the on-disk entry point and
    package (exact set, regular files, sha256) with `tool.files` before the entry point runs.
  - It is pinned with the workflow (TR15/TR50), so it adds no new trust root.
  - I judge it unnecessary, for the push-access reason in Q-1, but it is the owner's call.
- **O-2.** `P` (4c79be64) is not an ancestor of `main` 9deb6956. The reachability of `F` from
  `main` at landing is a §A.42 item 8 question that is unchanged from v5.5.9 and outside v6.0b.
- **O-3** (pre-existing, inferred, not checked on a hosted runner). The delegated clones of `X`
  are checked out with the runner's global git configuration. If the image configures a
  `filter.lfs` driver, a `.gitattributes` in `X` could make the working tree differ from `X`'s
  blobs for checkers that read files. This is unchanged from v5.5.9 and outside v6.0b; noted for
  the implementation's clone step (for example `-c filter.lfs.smudge= -c filter.lfs.process=`, or
  comparing the checked-out files with the blobs).

## Hunk map against v6.0a (task A)

18 hunks, each read in the regenerated diff. `CHANGES-v6.0b.md`'s table is accurate.

| Hunks | Source | Verified |
|---|---|---|
| 1 | owner bullets 1-6 (status bullet quoting decision and review) | yes |
| 2, 4, 5, 12 (inventory name), 16 | traceability; owner bullet 6 (fresh review) | yes; only pointers moved, no claim changed |
| 3 | identifiers EI6, EI7; TR29 restored (owner bullets 1, 3) | yes |
| 6 | wrapper loads by location after isolation check (R-1; owner bullets 2, 3) | yes |
| 7, 8 | consumer predicate repeats point 5's `uses:` check and point 6 (R-1; owner bullet 1) | yes (see N-d) |
| 9 | N2 (configuration path in procedural confirmation) | yes |
| 10 | R-1 (points 4-6), N3 (no option sets `tool`/`repository_id`), N5 (`uses:` by full id); owner bullets 1-3 | yes |
| 11 | N6 (residual-trust sentence conditional on point 5) | yes |
| 12 (EI1-EI7), 18 (S13) | owner bullet 3 | yes |
| 13 | TR29 first case (R-1; owner bullet 1) | yes; the first case is byte-identical to v5.5.9's text |
| 14 | EI6 (the hashlib.py control; owner bullet 3), EI7 (N5) | yes |
| 15 | N4 (`ls-remote` against `repository_id`'s repository), R-1 | yes |
| 17 | plan item P8: the pinned workflow meets point 5 | yes |
| N1 | applied in `INVENTORY-v6.0b.md` table 6 (twelve subsections, list through §31.31) | yes |

Nothing else changed. The row comparison by my script (`rows/rows_cmp.py`,
`rows/rows-v60a-v60b.txt`) shows 2 rows modified (TR29, S13), 3 added (the 0.2 row, EI6, EI7) and
none removed, which matches CHANGES. The correction is bounded.

## Guarantee table against v5.5.9 (task B)

Enumerated from v5.5.9 sec. 5, 6.3 (including the `A.workflow` clause) and the control tables.

| # | v5.5.9 technical guarantee (controls) | v6.0b | Judgment |
|---|---|---|---|
| 1 | Outcomes, exit codes, wrapper (X1-X9) | unchanged; wrapper loads by location | intact |
| 2 | Acceptance predicate with S7 recomputation; harness never acceptable (X10, X11) | X10 against `tool` pins | intact |
| 3 | Executed engine equals pins; extra files refused (TR28, TR48, TR51, TR52, K7) | `tool.files` at `F`, at tool and consumer | intact |
| 4 | Workflow equals reviewed pin (TR15, TR50) | `tool.workflow` | intact; event rule (EI2) strengthened |
| 4a | Workflow "verifies the tool blobs ... before executing" | tool's first step plus consumer repetition | modified, with no acceptance consequence (Q-1, N-f, O-1) |
| 4b | Workflow "runs the tool only from that tree" | point 5: `-I`, by-location load, EI6; `uses:` rule EI7; content review | intact, strengthened on `main` (P1 versus P1c) |
| 5 | Canonical repository, not a fork (TR14) | `repository_id` and `head_repository` | strengthened |
| 6 | `head_sha` on `main`'s first-parent chain (TR29 first case) | consumer against `M` (EI5), verified reader | intact in acceptance; tool-level ERROR dropped (N-c) |
| 7 | Evaluated commits explicit and equal to the landing record's (TR29 second case, TR30) | kept | intact |
| 8 | Result is the run's artifact by sha256; deterministic gzip (TR46) | kept | intact |
| 9 | Configuration only from `F` via the fixed pin table (TR1-TR3) | derived pin table (EI4); configuration path compared (EI3) | intact; F-2 procedural residual |
| 10 | Identity values not caller-overridable (TR9 technical part) | in the configuration at `F`; no option (N3) | intact |
| 11 | Local runs never `"chain"` (TR13) | kept | intact |
| 12 | Offline replay (TR45) | kept; recipe's `T` on `main` again | intact |
| 13 | Object integrity | verified reader (GV1-GV6) | strengthened |
| 14 | Host-read failure never falls back (TR21) | GV7 | intact |
| 15 | Landing against current `main` | EI5 fail-closed; N4 | strengthened |
| 16-28 | review chain, lineage, widening, edit completeness, side changes, landing and reconciliation, HP, context, profiles, delegated classes, corpus and mirrors, purity, fail-closed config, determinism | byte-identical or wording only (row table) | intact |
| — | `A`, designation, forms, thread, freeze ledger, authority changes | removed | authorization only (owner decision) |

**Failure cases constructed for modified or removed rows with a technical part:**

- **TR8 and TR10** (a different or caller-built `F`). Constructed: a run with another `F` → EI3
  non-acceptance (its `F` differs from the landing record's). Which `F` the landing record names is
  procedural (owner decision).
- **TR9** (override of repository id or workflow pin). Constructed: an option or environment value
  → no such input exists (N3); a field in another configuration → EI3.
- **TR21** (host failure). Constructed: failing REST → GV7.
- **TR29 first case.** Constructed: branch `T'` with equal pins (CX-3, CX-4) → consumer
  non-acceptance.
- **4a.** Constructed: `T'` with a pyc or changed module → executes, then the consumer refuses
  (Q-1).
- **TR3, TR51, O5, O7, O9, A12r, LN4.** Only their authorization halves are dropped; I read each
  modified row against v5.5.9.

## Row table (task B)

My keying by first cell (`rows/rows-v559-v60b.txt`):

- 439 rows retained, 34 modified, 71 removed, 32 added.
- Control ids: 28 modified and 58 removed, which matches inventory table 2's control counts
  exactly.
- The 58 removed control ids are exactly the retired list: O4, TR4, TR6-TR12, TR16-TR27, TR31-TR44,
  TR47, TR49, TR53-TR70, LN9, LN11, LN12.
- I read TR8, TR9, TR10 and TR21 in full; their technical parts are covered as above.
- The other removed TR/O/LN rows test `A`, designations, forms, the thread or the freeze ledger.

The inventory's table-row figures (40 modified, 65 removed, 21 added) come from line-by-line
keying and differ from mine only by method.

## Flag verdicts (task C)

| Flag | Verdict |
|---|---|
| F-14: run steps not parsed mechanically | **Acceptable.** The workflow blob is pinned and compared at the tool and the consumer (TR15, TR50), its content is reviewed once with the configuration, TR29 bounds `T` to `main`, and v5.5.9 also checked workflow content only in review. Parsing shell would be infrastructure. Apply N-b's checklist and the fail-closed `uses:` rule (both are text checks of a blob already read) |
| F-15: runner image trust | **Acceptable.** It is the same host-runner trust as v5.5.9, now stated. It must also cover what any allowed action installs, or N-b must forbid such actions |
| F-2: record directory | **Acceptable procedural residual.** N2 is applied: sec. 6.3 names the configuration path in the owner's confirmation |
| F-10: N14 "approved text" | Acceptable (design wording of a reconciliation record, not tool output) |
| F-11: purity value set | Acceptable as an implementation item |
| F-12: event rule for `ci` and `pdf` | Acceptable; a strengthening |
| F-13: `CONFIG_UNREVIEWED` breadth | Acceptable (an identifier, glossed) |

## Simplicity (task D)

Added mechanisms:

- `-I` plus loading by location;
- one refusal on `sys.flags` and `sys.path`;
- one line check of `uses:` in a blob already read;
- one first-parent walk with the existing verified reader against the `M` that EI5 already
  resolves.

None of these is unnecessary infrastructure, and there is no new host read. The missing simplest
protections are Q-1's optional five-line package scan and N-b's fail-closed `uses:` rule. Nothing
should be removed.

## Residual authorization machinery (task E)

None.

- The added lines that mention the owner are the quoted decision, the procedural confirmation of
  `F` and the configuration path, and the review requirement.
- TR29 is a fact about the object graph.
- No added wording implies that a PASS or `"chain"` means approval. N-c asks that `"chain"` also
  not be read as "on `main`".

## Governance (task F)

AGENTS.md at 9deb6956:

- **§A.42 items 1, 3, 8.** Satisfied for `T` again: `T` is on `main`'s first-parent chain, so the
  recipe's commit is reachable and the run's code is merged content. The run id and logs remain
  provenance; the result is committed (gz). The reachability of `F` (O-2) is unchanged from v5.5.9.
- **§A.43 item 4.** If the pinned workflow keeps the `push` trigger, a push to `main` launches a
  run.
  - For a run that uses the A1 plan's records, that launch is a trial needing per-instance approval
    under §A.50 item 2.
  - Recommendation (nit, procedural): the workflow that runs plan configurations is
    `workflow_dispatch`-only.
  - EI2 already admits both events, so this restricts nothing the tool needs.
- **§A.50.** Items 2 and 5 are cited correctly as procedural.
- **§A.49.** Rule 4 is unaffected.
- **No AGENTS.md amendment is needed.**

## Inventory and the A1-plan list (task G)

Spot-checked against 443e871f:

- **Entry point.** The `sys.path.insert` is at line 51. The new import rule is as in table 3a; see
  N-g.
- **`a1_conformance.py` and `staged_purity_lint.py`.** The module-level inserts are at lines 20-21
  and 18-19, as stated. Both are script-run control and lint runners, not code that the acceptance
  run imports.
- **Other inserts.**
  - `rest_fixture.py`, `host_fixture.py`, `a1_controls.py`, `conformance_controls.py` and
    `synthetic_fixture.py` also insert `tools/` and are listed (removed or modified).
  - `python_frozen_replay.py` runs its driver with `-I -B` and sets `sys.path` to the
    materialization, as stated.
- **Adapters.** They are admitted by blob and executed in memory (`config.admit_module`), so no
  file import is involved.
- **Delegated runs.** Checkers from `F` blobs and `X`'s census run with `-I -B` in clones (N-h).
- **Counts.** Modify 21, remove 2, retain 32, total 55: recounted, correct.
- **A1-plan items.** P1-P8 are complete; P8 now states twelve `Record pins` subsections (N1).
- **Stale identifiers.** The stale EI1-EI5 references are listed in N-e.

## Identifiers (task H)

- **TR29.** Its first case is byte-identical to v5.5.9's ("a run whose `head_sha` is not on
  `main`'s first-parent chain (a branch)"). Its second case is v5.5.9's. Its third case is v6.0a's
  addition, which is consistent with the same meaning.
  - The outcome for the first case moved from tool-and-consumer to consumer only (N-c). That is not
    a change of meaning.
- **EI6, EI7.** They are new. They appear in no earlier design, and in none of the v5.5.10 or
  v5.5.10a designs, changes or reviews.
- **v5.5.10 and v5.5.10a ids.** TR71-TR87, HV1-HV12 and HS-1 to HS-7 occur only in the sentence
  that says they are not used.
- **Retired ids** are not reused.

## Verified vs inferred

**Verified:**

- all hashes; both diffs regenerated byte-identical;
- the hunk map and both row comparisons (my script);
- the removed-id set;
- probes P0-P10 and P2b on a copy of 443e871f with the simulated v6.0b entry point (Python
  3.13.18, gcc for P7);
- the implementation facts cited in task G;
- AGENTS.md §A.42, §A.43, §A.49 and §A.50 at 9deb6956;
- `P` not an ancestor of 9deb6956;
- the `CHANGES` line counts.

**Inferred (not executed):**

- the behaviour of the GitHub-hosted runner and actions: actions/checkout creates symlinks and
  writes `.git/config` itself; the runner image's git and lfs configuration; artifact scoping per
  run; re-run semantics;
- that `setup-*`, composite and docker actions can fetch mutable content;
- the end-to-end host run of any probe (the probes are in-process only).

## Probes run

- `probe/run_probes.sh <impl-wt> <probe dir>`, which uses `PROBE_TMP` for its throwaway trees.
  - Each case: a fresh `git archive 443e871f` of the tool, the simulated entry point
    (`entry_v60b.py`, or `entry_v60b_fix.py` for P8), and one planted file.
  - Each case runs `python3 [flags] tools/ledger_coverage.py self-test --help`, which imports the
    CLI and its engine modules.
  - Marker bodies: `marker_mod.py`; the pyc writer: `make_pyc.py`; the extension: `ext_util.c`.
  - Output: `probe/run_probes.out`.
- Row comparison: `rows/rows_cmp.py` and its outputs.
- Early probe runs wrote throwaway trees under `<tmp>/tmp.*`. Those created by this review were
  removed, and the final run used the workspace.

## Files

`review.md`; `probe/` (`entry_v60b.py`, `entry_v60b_fix.py`, `marker_mod.py`, `make_pyc.py`,
`ext_util.c`, `run_probes.sh`, `run_probes.out`); `rows/` (`rows_cmp.py`, `rows-v559-v60b.txt`,
`rows-v60a-v60b.txt`); `MANIFEST.sha256`.
