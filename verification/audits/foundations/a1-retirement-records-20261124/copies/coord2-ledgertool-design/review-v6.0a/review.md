# Independent review of design v6.0a of the ledger coverage tool

Reviewer: independent, non-author. Review only. Nothing was written in the repository, and there
was no commit, push, GitHub write, GraphQL call or CI run. Host reads were one REST
`GET /repos/amaybaum/incompleteness` (id 1156244443, `fork: false`) and one docs.github.com fetch
(reusing workflows). The permission system refused no operation. Every file written is under
`review-v6.0a/`.

## Objects verified

| Object | sha256 / id | Result |
|---|---|---|
| `DESIGN-v6.0a.md` | 105db5efe8803876107e525f868051593227f0cc20f0bd2fb7600ea312113585 | match |
| `INVENTORY-v6.0a.md` | b5ada0da953962710ca043b66c8a356a11ceb14965d538c70b5df2dd561039ae | match |
| `CHANGES-v6.0a.md` | 4953171d9cfda38669462d1bee680fc894db7a2d63aec09815172e4012c9a1ae | match |
| `CHANGES-v6.0a-from-v6.0.diff` | 50e5ba13e1225d6d730e5beeb7ece5c7646bf13e9e7089facfc41ec1e30ba098 | match. Regenerated with `diff -u DESIGN-v6.0.md DESIGN-v6.0a.md`: byte-identical after the two header lines (`cmp`), and the header timestamps equal the files' mtimes |
| `CHANGES-v6.0a-from-v5.5.9.diff` | fb0aefc7315a73176ed3285bc9b614cfe42abb46305de3f69ac3eae324b9e2c9 | match. Regenerated: byte-identical (`cmp`) |
| `DESIGN-v6.0.md` | 5d4ddf784164c496d98b3194030524b20353cfcd5695fbf102eae68ced85e145 | match |
| `review-v6.0/review.md` | 43cfe728198588eb4f01a38dd817f4d207e50494bb98c5bb20c895df4fddb0ec | match |
| `DESIGN-v5.5.9.md` | cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9 | match |
| `coord2-impl-wt` | HEAD 443e871f2 | match |
| `P` | 4c79be642ca631573f06b444903be75ec4f5e2b6 | read with `git show`; nothing fetched |

## Verdict: REJECT (narrow: one blocking finding with a small fix; the rest is accepted)

v6.0a applies B-1 to B-4, the nits and owner item 4 as directed, within the stated bounds. CX-1
and CX-2 are now refused. No authorization machinery remains, and none was added. One technical
binding that v5.5.9 had, and that the prior review accepted as removable, turns out to be
load-bearing. The pinned file set is not the set of files the run executes, so dropping the
requirement that `T` lie on `main` lets unpinned code from an arbitrary commit run inside the
tool. That is a reproducible counterexample, and it also opens a §A.42 reachability gap. The fix
is one restored check plus one restored control id. Neither adds any authorization machinery or
any new host read.

## The key question

*"Could an incorrect scientific result pass under the revised design when it would have been
rejected under v5.5.9 for technical reasons?"*

**Yes, as v6.0a is written:** by CX-3 (demonstrated) and its workflow variant CX-4 (design-level).
Both are refused under v5.5.9 by TR29's first case (`head_sha` on `main`'s first-parent chain).
Once R-1 below is applied, I found no remaining case. CX-1 and CX-2 are closed (details below).

## Blocking finding

### R-1. The executed code is wider than the pinned set, and `T` may lie off `main` (inventory G23, flag F-1)

**Evidence (design).**

- Sec. 6.3, execution identity point 2, binds only `tools/ledger_coverage.py` plus
  `tools/ledger_coverage/**` (`tool.files`) and the workflow blob.
- The paragraph after point 4 says: "Whether `T` lies on `main` is not checked: the tool and
  workflow are fixed by the pins at `F`, whichever commit holds them."
- TR29 lost its first case, and inventory G23 records the guarantee as "not kept".
- The residual-trust list states that "the code that ran is the code whose blobs were read and
  compared". That statement is false for CX-3.

**CX-3 (demonstrated: `review-v6.0a/cx3/run_cx3.sh`, output in `run_cx3.out`).**

- Mechanism: the entry point at 443e871f runs `sys.path.insert(0, <dir of tools/ledger_coverage.py>)`,
  which is `tools/`, before it imports the engine. The engine then imports `hashlib`, `re`,
  `subprocess`, `gzip`, `urllib` and other stdlib modules. Several adapters insert `tools/` again.
- Construction: take `T'` = the landed tool commit plus a file `tools/hashlib.py`. That file is
  outside `tools/ledger_coverage/` and is not the entry point.
- Result: running `python3 -I -B tools/ledger_coverage.py` on that tree executes `tools/hashlib.py`
  in-process. The probe printed `CX3-SHADOW-LOADED`. `-I` does not prevent this, because the path
  is inserted explicitly.
- The shadow module runs arbitrary code before any check. For example, it can patch the outcome
  computation, or patch the self-comparison (EI1) itself.

How the attack passes v6.0a:

1. Push `T'` to a branch and dispatch the pinned workflow on that branch (`workflow_dispatch`), or
   simply push.
2. Every v6.0a clause then holds:
   - repository and head repository equal `repository_id`;
   - the event is allowed;
   - `tool.files` are exact and equal their pins;
   - the workflow blob equals its pin;
   - the checkout equals `T'`;
   - `F`, pin table, configuration and evaluated commits equal the landing record's;
   - the artifact digest matches;
   - S7 recomputes PASS from the forged items.
3. Accepted.

Under v5.5.9, `T'` is not on `main`'s first-parent chain, so TR29 refuses it. Getting
`tools/hashlib.py` onto `main` would need a reviewed merge.

**CX-4 (design-level; the workflow is not yet written).**

- The pinned workflow may use a local action (`./.github/actions/…`), a same-repository reusable
  workflow (`./.github/workflows/…`), or a script in `T`.
- docs.github.com, "Reusing workflows": "When you reference a reusable workflow in the same
  repository using … `./` …, the called workflow is from the same commit as the caller workflow."
- Any of these files can then differ at an arbitrary `T'` while the pinned workflow blob is
  unchanged. This is CX-2 through an unpinned file.
- v5.5.9 bounded this by on-`main`, and also required the workflow's content to "run the tool only
  from that tree". v6.0 dropped that sentence, and v6.0a has no counterpart.

**Governance (§A.42 items 1, 3, 8).**

- The landing record's reproducibility recipe names `T` (sec. 5, durable evidence), and the
  consumer's verdict reads `T`'s tree.
- Under v6.0a, `T` may be a branch commit that is never reachable from `main`. The landed claim
  then names, as support, a commit off `main`. §A.42 item 8 adds: "copying their files to main
  does not make them reachable from it".
- v5.5.9's first-parent rule guaranteed reachability.

**Why this is technical, not authorization.** Ancestry of `T` is a fact about the object graph,
like `H` on `M`'s first-parent chain (R1), which v6.0a keeps. It involves no owner, comment, form
or ledger. The prior review's verdict on F-1 ("acceptable once 3-5 are bound to `F`") assumed that
the pinned set was the executed set. CX-3 shows it is not.

**Smallest fix.**

1. **Restore TR29's first case with its v5.5.9 meaning.** The consumer requires `T` to be on the
   first-parent chain of `M`. `M` is already resolved by `git ls-remote` under EI5's fail-closed
   rules, and the chain is walked by the verified reader. That needs no new host read.
   - Replace the "Whether `T` lies on `main` is not checked" paragraph accordingly.
   - Keep G23 as kept.
   - Add `T` to TR29's case list with its v5.5.9 text: "a run whose `head_sha` is not on `main`'s
     first-parent chain (a branch)".
   - This restores v5.5.9 parity for CX-3 and CX-4 and closes the §A.42 gap.
2. **Recommended, in the same edit: one sentence restoring v5.5.9's workflow-content requirement
   in its reduced form.** The pinned workflow executes nothing from `T` outside `tool.files` and
   itself: no local action, no `./` reusable workflow, no script. The tool's import path holds only
   pinned files, for example by loading the package by location instead of inserting `tools/` on
   `sys.path`.
   - Control: `T'` = pins plus `tools/hashlib.py`; expected, the file is never executed (or the run
     is refused).
   - With this, "what actually ran" holds even for unpinned files on `main`, which v5.5.9 left to
     main's review.

## Hunk map against v6.0 (task A)

The 29 hunks were checked one by one against the regenerated diff. `CHANGES-v6.0a.md`'s table is
accurate.

| Hunks | Source | Verified |
|---|---|---|
| 1, 3, 16, 29 | owner items 1-6 (status, ids, retired list, S13) | yes |
| 2, 6, 11, 14 (first part), 23 | N-4, one normative sentence (sec. 1); owner login removed | yes |
| 7, 12, 13, 14 (second part), 15, 17, 18 (TR5, TR14, TR15, TR28, TR48, TR50, TR52), 19 (EI1, EI2), 24-28 | B-1, B-2 | yes |
| 12, 18 (TR2, TR13), 19 (EI4), 22 | B-3, owner item 4 | yes |
| 8 | B-4 (meaning table; no lint) | yes |
| 9, 10, 18 (WB rows) | N-3 (wording only) | yes; the WB rows' expected outcomes are byte-identical |
| 19 (EI3, EI5), 20 | N-1, N-2 | yes |
| 4, 5, 21 | traceability; owner item 6 | yes |

Nothing else changed. Row comparison by my own script (`rows_cmp.py`, `rows-v60-v60a.txt`):

- 19 rows modified, 17 added, 1 replaced (the 0.2 V3 row).
- These match CHANGES' "Row changes" exactly. The class-meaning header row accounts for the one
  extra row.

## Guarantee table against v5.5.9 (task B)

Enumerated independently from v5.5.9's sec. 5, 6.3 and the control tables.

| # | v5.5.9 technical guarantee (controls) | v6.0a | Judgment |
|---|---|---|---|
| 1 | Outcomes, exit codes, wrapper (X1-X9) | unchanged | intact |
| 2 | Acceptance predicate with S7 recomputation; harness never acceptable (X10, X11) | X10 against the `tool` pin | intact |
| 3 | Executed engine equals reviewed pins; extra files refused (TR28, TR48, TR51, TR52, K7) | `tool.files` at `F` | intact for the pinned set; **weakened for files outside it** (R-1, CX-3) |
| 4 | Workflow equals reviewed pin and runs only from that tree (TR15, TR50) | `tool.workflow`; event rule (EI2) | pin intact, event rule strengthened; "only from that tree" lost (R-1, CX-4) |
| 5 | Canonical repository, not a fork (TR14) | `repository_id` and `head_repository` at tool and consumer | strengthened (the fork `pull_request` case is now refused) |
| 6 | `head_sha` on `main`'s first-parent chain (TR29 first case) | removed | **weakened** (R-1) |
| 7 | Evaluated commits are explicit inputs and match the landing record (TR29 second case, TR30) | kept | intact |
| 8 | Result is the run's artifact by sha256; deterministic gzip (TR46) | kept | intact |
| 9 | Configuration only from `F` via the pin table; the pin table is fixed (TR1-TR3, TR9 via `A`) | derived pin table (EI4); config path is a caller input recorded and compared (EI3) | intact for the pin table; record directory is a procedural residual (flag verdict below) |
| 10 | Identity values not caller-overridable (TR9 technical cases) | values live in the config at `F`; no option exists; the pin-table option is USAGE (EI4b) | intact (nit N3) |
| 11 | Local runs never `"chain"` (TR13) | kept | intact |
| 12 | Offline replay (TR45) | kept | intact, except that its recipe may name an off-`main` `T` (R-1) |
| 13 | Object integrity | verified reader (GV1-GV6) | strengthened |
| 14 | Host-read failure never falls back (TR21) | GV7 | intact |
| 15 | Landing against current `main` | EI5 makes `ls-remote` fail-closed | strengthened |
| 16-28 | Review chain, lineage, widening (now also covers `tool` and `repository_id`), edit completeness, unrelated changes, landing and reconciliation, HP, context, profiles and fingerprints, delegated classes (event rule added: strengthened), corpus and mirrors, purity, fail-closed config, determinism | byte-identical or modified only in wording | intact |
| — | `F` designation, `A`, forms, thread, freeze ledger, authority changes | removed | authorization only; the owner's decision |

**Row coverage** (`rows-v559-v60a.txt`; my keying by first cell, so counts differ from the
inventory's line-by-line counting):

- 71 rows removed, 34 modified, 29 added.
- Each removed TR/O/LN row was read in full. O4, TR4, TR6, TR7, TR11, TR12, TR16-TR20, TR22-TR27,
  TR31-TR44, TR47, TR49, TR53-TR70, LN9, LN11 and LN12 are authorization-only or `A`-specific.

Technical parts of the remaining removed rows, and what covers them now:

| v5.5.9 row | Technical failure | Covered in v6.0a by |
|---|---|---|
| TR8, TR10 | run of a different `F` | EI3 |
| TR9 | override of repository id or workflow pin | the config at `F` holds them; no input exists |
| TR21 | fallback on host failure | GV7 |
| TR28 | blobs differ from pins | TR28 (CX-1 refused) |
| TR15, TR50 | workflow differs from pin | restored (CX-2 refused) |
| TR14 | fork | TR14, strengthened |
| TR29 first case | `T` off `main` | **nothing (R-1)** |

The modified rows TR3, TR51, O5, O7, O9, A12r and LN4 drop only their authorization halves. Their
technical cases are kept.

**CX-1 re-test.** `T'` with a changed engine module: `tool.files` pin mismatch. Refused at the tool
and the consumer by TR28 and X10. **Closed.**

**CX-2 re-test.** A changed workflow writes a forged `result.json`: workflow blob ≠ pin. Refused by
TR15 and TR50. **Closed.** CX-4 reopens the same route only through unpinned files the pinned
workflow calls.

**Other probes:**

- **`pull_request` events:** refused (EI2).
- **Reusable workflows called by another workflow:** the run's `path` is the caller's, so
  `tool.workflow.path` must be the top-level workflow. That case is covered. Called files are CX-4.
- **Re-runs (`run_attempt`):** a re-run uses the same `head_sha` and workflow file, so its
  artifacts come from the same pinned code. No gap.
- **Artifact substitution between runs:** the artifact is bound to the run id and sha256, and an
  upload can target only its own run. No gap.
- **`git ls-remote` failure:** refused (EI5).
- **Landing record vs result:** EI3.
- **Forks:** TR14.
- **Second `PREREG.md` in `F`:** see the flag verdicts.

## B-4 (task C)

The meaning table plus the terminology requirement is sufficient. I grepped the engine's string
literals at 443e871f for `approv`, `authoriz` and `owner` outside the class identifiers. Every hit
lies in code that v6.0a removes (`authority.py`, the owner and authorization controls,
`retirement.owner`) or is an unrelated field name (sitemap `carried.owner`, an HTTP
`Authorization` header). The output strings will be rewritten under review anyway. **No concrete
need for lint machinery was found.**

## Simplicity (task D)

Nothing unnecessary was added:

- `tool` and `repository_id` are two config fields;
- EI1-EI5 are controls;
- no new host read (`head_repository` and `event` are fields of the run record already read).

`--pin-table` and `--config-sha256` were removed, which is a simplification. The R-1 fix adds one
check over objects already read.

## Residual authorization machinery (task E)

None. Every remaining hit for `approv` or `authoriz` is one of:

- an owner quotation;
- a procedural statement placing approval outside the tool;
- a retired-schema refusal;
- a class identifier (glossed by the meaning table);
- N14's "approved text" (F-10).

No wording says that a PASS implies approval.

## Flag verdicts (task G)

| Flag | Verdict |
|---|---|
| B-3 residual (F-2): a second `PREREG.md` and config directory in `F` | **Acceptable procedural residual.** The configuration path stands exactly where `F` stands: a caller input that is recorded, compared with the landing record (EI3), and confirmed by the owner. A technical fix would need a reference outside `F` and the caller, which is what `A` was. A uniqueness rule over `F`'s tree would break once a second retirement plan exists. Nit N2: the procedural confirmation should name the configuration path (record directory) as well as `F`. |
| F-10, N14 "approved text" | Acceptable. It is design-control wording for a reconciliation record, not tool output, and sec. 5's terminology rule governs the tool's strings. Optional: change to "expected text". |
| F-11, purity value set | Acceptable as an implementation item. The entry-point path can be derived from `__file__` or allowlisted under sec. 16.1. |
| F-12, event rule for `ci` and `pdf` | Correct, and a strengthening: a `pull_request` run with `head_sha = X` tests the merge commit, not `X`. P §26.3 dispatches `verify.yml` with `workflow_dispatch` on a branch whose head is exactly `T1` (PREREG lines 5378, 5600), so it complies. P's `a1exit-trial-verify.yml` is dispatched from `main` with the commit as an input, so its `head_sha` is not `X`. That is pre-existing and unaffected. |

## Governance (task F)

AGENTS.md at 9deb6956:

- **§A.25, §A.39, §A.43-§A.48:** no violation (consistent with inventory table 5).
- **§A.42 items 1, 3, 8:** violated by the off-`main` `T` that v6.0a explicitly permits (R-1).
  The R-1 fix removes the violation.
- **Amendment:** with the fix, **AGENTS.md needs no amendment**. The on-`main` check is not an
  authorization record, and §A.49 rule 4 stays conditional.

## Inventory and the A1-plan list (task H)

P1-P5 and P8 are complete as items. One factual error, inherited from the prior review:

- P8 and the B-3 text say P's PREREG has **nine** `Record pins` subsections ending at §31.25.
- It has **twelve**: §26.4, §31.11, §31.14, §31.16, §31.18, §31.20, §31.21, §31.23, §31.25, §31.27,
  §31.29 and §31.31 (`git show 4c79be64:…/PREREG.md`, lines 5383-7354). The pins in force are
  §31.31's.
- The derived rule ("last subsection") gives the right answer either way. Only the count and the
  list need correcting (nit N1).
- Inventory table 3 now lists the `gitobj.py` members from prior nit N-5.
- P's §31.31 rows have the `` | `file` | `sha256` | `` form that the derived reader expects.

## Identifiers and register (task I)

- **TR15 and TR50** carry their v5.5.9 meaning (workflow blob ≠ pin; the workflow at its path
  modified by one byte), with the pin now held by the config.
- **TR28, TR48 and TR52** keep their v5.5.9 meaning against `tool.files`.
- **EI1-EI5** are new. EI and GV appear in no earlier design.
- No TR71-TR87, HV1-HV12 or HS-* ids are used.
- Retired ids are not reused.
- **With the R-1 fix**, TR29 regains its v5.5.9 first case, so its meaning returns to v5.5.9's;
  this is not a reuse.
- §A.32 and §A.33 govern `papers/` prose; the design is not paper prose, and no caps emphasis or
  self-narration that would matter was found.

## Nits (non-blocking)

- **N1.** Correct "nine" to twelve, and the list, in P8 (inventory table 6).
- **N2.** In sec. 6.3, name the configuration path in the owner's procedural confirmation,
  alongside `F`.
- **N3.** Say in one line that no option, environment value or other field sets `tool` or
  `repository_id` (TR9's technical cases).
- **N4** (pre-existing). The `git ls-remote` remote should be the repository that `repository_id`
  names.
- **N5** (pre-existing). Third-party actions in the pinned workflow should be pinned by full
  commit id.
- **N6.** The residual-trust sentence "the code that ran is the code whose blobs were read" is true
  only once R-1 is fixed.

## Verified vs inferred

**Verified:**

- all hashes and both diff regenerations;
- the hunk map and row comparisons (my script);
- the CX-3 execution against the 443e871f implementation (Python 3.13.18);
- repository id 1156244443 (REST GET);
- the docs quotation on `./` reusable workflows;
- P's twelve `Record pins` subsections and its §26.3 dispatch procedure;
- the engine string scan.

**Inferred (not executed):**

- CX-3 end to end through a host run (the in-process execution is demonstrated; the acceptance
  clauses were checked against the design text);
- CX-4, which depends on a workflow not yet written;
- that a re-run reuses the original commit and workflow file, and that an artifact upload is
  scoped to its own run (standard Actions behaviour, not re-fetched).

## Files

`review.md`; `rows_cmp.py`; `rows-v559-v60a.txt`; `rows-v60-v60a.txt`; `cx3/hashlib_probe.py`;
`cx3/run_cx3.sh`; `cx3/run_cx3.out`; `MANIFEST.sha256`.
