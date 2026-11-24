# Independent review of design v6.0 (reduced design) of the ledger coverage tool

Reviewer: independent, non-author. Review only: nothing written in the repository, no commit,
push, GitHub write, GraphQL call or CI run. Host reads: one REST `GET` attempted on a third-party
repository (refused by the session's access policy before reaching GitHub; nothing else was
attempted on GitHub) and two docs.github.com fetches. No operation was refused by the permission
system.

## Objects verified

| Object | sha256 / id | Result |
|---|---|---|
| `DESIGN-v6.0.md` | 5d4ddf784164c496d98b3194030524b20353cfcd5695fbf102eae68ced85e145 | match |
| `INVENTORY-v6.0.md` | 2b4006ddafcf9be6dbfdc048953bf729f7005ea4ca6f6f8f78bd50852593953c | match |
| `CHANGES-v6.0-from-v5.5.9.diff` | 7be43780ef43c50ce8632d947a5f63ccf935369ecbd61157a4e39de15b5cbcf2 | match; regenerated with `diff -u DESIGN-v5.5.9.md DESIGN-v6.0.md`: byte-identical (`cmp`) |
| `DESIGN-v5.5.9.md` | cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9 | match |
| `coord2-impl-wt` HEAD | 443e871f225a414f69bef3f1e3cab45cb30d6594 | match; 55 tracked landed paths, as the inventory states |
| `P` | 4c79be642ca631573f06b444903be75ec4f5e2b6 | present locally; read with `git show`; nothing fetched |
| `AGENTS.md` | at 9deb69568d8231210c7f39cb65be943dea566371 (blob sha256 43a28e26...) | read with `git show`; §A.49-§A.51 present. (The local `main` ref is 416f546d, which is not a descendant of 9deb6956; the review uses the commit named in the task.) |

## Verdict: REJECT (narrow; four bounded corrections, then re-check)

The removal of the authorization machinery itself is clean: every removed row I examined that
tested only owner authorization (designations, forms, threads, edits, freeze ledger, Owner at
creation, authority changes, authorization records) is correctly retired. No comment, thread,
GraphQL or repository-history read remains. The record review chain, lineage, edit completeness,
unrelated-change detection, landing composition, HP, context, rules, delegation, purity,
fail-closed validation, replay and determinism are unchanged or strengthened.

But in removing the authority record `A`, v6.0 also removed the only fixed reference value for
three technical facts that `A` carried alongside the owner identity: **which tool code runs**,
**which workflow runs it** and **which repository/event produces the run**, and it made the
**governing pin table** a caller choice. Each of these is a technical binding, not an approval,
and each now admits a concrete wrong result that v5.5.9 rejected.

**The owner's key question.** *Could an incorrect scientific result pass verification under v6.0
when it would have been rejected under v5.5.9?* **Yes**, as v6.0 is written. Counterexamples
CX-1 and CX-2 below are accepted by every clause of v6.0's acceptance predicate (sec. 5) and
rejected under v5.5.9 by TR28/TR29 and TR15/TR50 respectively. The fixes are small, purely
technical, and add no authorization machinery: they bind these values to `F`, the plan commit the
owner already confirms procedurally, exactly as v6.0 already binds the configuration and the
adapter modules.

## Blocking findings

### B-1. Tool code and workflow are bound only to the run's own `T`, not to any fixed reference (flags F-1, F-4)

**Evidence.** v5.5.9: the executed blobs must equal `A.engine_pins` (independently reviewed, sec.
6.3 trust root point 3), the workflow content must equal `A.workflow.content_sha256` (whose
reviewed content "must check out exactly the run's `head_sha`, verify the tool blobs ... and run
the tool only from that tree"), and `head_sha` must be on `main`'s first-parent chain; controls
TR15, TR28, TR29 (first case), TR50, X10 (second case). v6.0 (sec. 5 and 6.3 execution identity):
`T` is whatever the run's `head_sha` is; the consumer checks only that the result's recorded tool
blobs equal `T`'s blobs ("its recorded tool commit `T`, engine blobs and adapter module blobs
equal the blobs the consumer reads itself at `T`"); adapter modules are pinned by the
configuration at `F`, the engine and entry point are pinned by nothing; the workflow blob at `T`
is "recorded", never compared. The modified TR28/X10 now test only checkout tampering and
internal inconsistency; the v5.5.9 failure case ("tool blobs differ from the pins") has no
counterpart.

**CX-1 (unreviewed engine).** Let `T'` = the landed tool commit plus a one-line engine change
(for example, `outcome.py` drops FAIL items of class `unauthorized-change`, or the preflight
controls are skipped). Adapters are untouched. Run the workflow on a branch at `T'` with the true
`--freeze F --pin-table ... --config F:...`. Result: PASS, recording `T'` and its blobs. Consumer:
run reported in the repository; `head_sha = T'`; `T'`'s tree equals the recorded tool blobs;
adapter blobs equal the configuration's pins; configuration, `F`, pin table and evaluated commits
equal the landing record's (the landing record is written from the same run); artifact digest
matches; S7 recomputes PASS from the (filtered) items. **Accepted.** v5.5.9: refused (TR28 blobs
differ from `A.engine_pins`; TR29 `head_sha` not on `main`).

**CX-2 (forged result, genuine tool).** Let `T''` = the landed tool, unmodified, plus a changed
workflow file whose step writes a hand-made `result.json` (PASS, consistent items, recording
`T''`'s genuine tool blobs and the real `F`, configuration and commits) and uploads it. The tool
never runs. Every consumer clause holds, including "the result file is that run's uploaded
artifact". **Accepted.** v5.5.9: refused (TR15/TR50 workflow content differs from the pin).
Neither the offline replay (not part of the acceptance predicate) nor S7 (recomputes from the
forged items) catches it.

**Additionally (F-4):** for a `pull_request` run the host executes the workflow from the merge
commit (`GITHUB_SHA` is the merge commit, verified from docs.github.com "Events that trigger
workflows"), while the run record's `head_sha` is the PR head. So "the workflow file's blob at
`T`" is not necessarily the workflow that ran.

**Why this is technical, not approval.** The property lost is "the result was computed by the
specified tool code, run by the specified workflow". Reviewing the tool is an independent
technical review; which code computed a verdict is a fact about the computation (§A.44: verdicts
read structured evidence of what the check did). The owner's model is "the tool verifies which
exact plan was executed; the owner confirms that it was the approved plan". v6.0 does not verify
that the plan's checks were executed by the specified code: the identity of the code is reported,
but nothing, technical or stated as procedural, compares it with anything. P itself binds its
checker's code to the plan commit ("preserve_check.py, run from the designated plan commit
(`git show <plan>:…/preserve_check.py`, never the candidate's copy)", P PREREG line 5180).

**Owner's assessments tested.** "F1 acceptable if the tool commit's exact identity and integrity
are verified": identity and integrity of `T` are verified, but that is not sufficient, because
`T` is chosen by the run (CX-1). "F4 acceptable only if the actually executed workflow is verified
against that commit": necessary, not sufficient (CX-2: the executed workflow is `T''`'s and is
still forged).

**Smallest fix (technical, no authorization machinery).** Add to the configuration at `F` (sec.
16.2, admitted through `F`'s pin table like the adapters) a field `tool`:
`{files: [{path, blob_sha256}], workflow: {path, blob_sha256}}` covering the entry point, every
file under `tools/ledger_coverage/` and the producing workflow. The tool (execution identity point
2) and the consumer (sec. 5) require `T`'s tree to hold exactly these files under
`tools/ledger_coverage/` plus the entry point, and the run record's `path` to be `workflow.path`
with that blob at `T`; and they require the run's `event` to be `push` or `workflow_dispatch`
(events for which the executed workflow is the one at `head_sha`). Controls: restore the v5.5.9
failure cases as TR28 (a `T` whose tool blob differs from the configuration's pin) and TR15/TR50
analogues under their existing ids or new ids (a `T` whose workflow blob differs; a run with event
`pull_request`). The owner's single procedural confirmation of `F` then covers the tool and
workflow, and F-1 (on-`main`) becomes unnecessary. Alternative, if the owner prefers it: state in
sec. 5 and 6.3 that the landing record names `T` and the workflow blob, and that the owner's
procedural confirmation covers them as well as `F`; plus the event restriction. That alternative
leaves the binding procedural, which is an owner choice.

### B-2. Repository check is relative to wherever the consumer runs, and fork `pull_request` runs are reported in the base repository (flag F-3)

**Evidence.** v6.0 sec. 5: "the host's REST API reports the run, by its run id, in the repository
in which the consumer runs"; no repository id is fixed anywhere (inventory: "no configured
repository id"). TR14 (modified) expects "non-acceptance at the consumer: the host does not report
that run in the consumer's repository". That expectation is false for a run triggered by
`pull_request` from a fork: such runs execute in, and are listed under, the base repository
(docs.github.com: "For pull requests from a forked repository to the base repository, GitHub
sends the `pull_request` ... events to the base repository. No pull request events occur on the
forked repository"; the REST run object carries `repository` and `head_repository` separately,
verified from the REST reference). A consumer running in a fork of the repository would likewise
accept that fork's runs. v5.5.9 refused both at the tool (`A.repository` id, `fork: false`) and
required `head_sha` on `main`. Combined with B-1, a fork contributor's PR can produce an
acceptable result from arbitrary code.

**Owner's assessment tested.** "F3 acceptable only if the consumer's repository check is mandatory
before accepting results": v6.0 makes the consumer re-check mandatory before landing ("re-checked
from the committed data before the landing merges"), but the repository it checks against is not
fixed and does not exclude fork-head runs, so the condition is not met.

**Smallest fix.** A `repository_id` in the configuration at `F` (technical identity, compared,
never an approval). The tool and the consumer require `run.repository.id ==
run.head_repository.id == repository_id` (both fields are in the run record already read; no new
host read). Correct TR14's case and expectation accordingly (a fork-PR run in the base
repository: refused because `head_repository` differs). With B-1 fixed this also becomes
defence in depth rather than the only guard.

### B-3. The governing pin table is a caller choice and the design text names a superseded section (flag F-2)

**Evidence.** v5.5.9 fixed `pin_table_path` per plan in `A`, which the caller could not override
(TR9). v6.0 takes `--pin-table F:<path>` from the caller and says the pin table is read "(the sec.
26.4 mechanism)". P does not have two "Record pins" sections: it has nine (§26.4, §31.11,
§31.14, §31.16, §31.18, §31.20, §31.21, §31.23, §31.25; P PREREG lines 5383-6828), and P's own
rule is "The pins in force are always the last `Record pins` subsection" (line 6582; preserve_check
reads the last one). The implementation (`authority.py:498-500`) reads the last `### N.N Record
pins` subsection; the design text does not say so, and "the sec. 26.4 mechanism" can be read as
§26.4, which holds P\*'s superseded pins. Separately, any other file in `F`'s tree with such a
subsection (another round's PREREG, a draft copy) can be named, and the configuration path is also
a caller input, so `F` alone does not determine which configuration is admitted. The inventory's
"more than one ... (§26.4, §31.11)" understates the count.

**Owner's assessment tested.** "F2 potential ambiguity — the tool must identify the intended table
unambiguously": confirmed as a real ambiguity.

**Smallest fix.** State the rule in sec. 6.3 point 2: the pin table is the last `Record pins`
subsection (by the heading pattern the implementation uses) of the plan's `PREREG.md`, and that
file is the one in the same record directory as the configuration (so the pin-table path is
derived from the configuration path, not a separate input), with refusal if that directory has no
such file or the subsection's table is malformed. Record both paths (already done). Add a control:
a second PREREG in `F` listing a different configuration, named by the caller: refused.

### B-4. Owner decision F6 is not yet met in the text

**Evidence.** F6: "retain existing test identifiers ... Clearly document their technical meaning
and ensure that human-readable results never imply owner authorization." v6.0 documents the
meaning of `authorized-replacement`, `authorized-removal`, `unauthorized-edit`,
`unauthorized-change` once, in "Status and authority". The output form (sec. 5: items,
fingerprints, explanations with `resolution_needed`, stderr JSON) carries these names with no
rule that human-readable text glosses them, and no control checks that no message, reason or
explanation text uses "authorized", "approved" or "unauthorized" outside the identifier (the
implementation's `segments.py:180` reason text is neutral today, but nothing fixes that).
(F6 was decided after v6.0 was written; this is a gap, not a writer error.)

**Smallest fix.** In sec. 5 "Output form": the result's schema carries a fixed `class_meaning`
table (identifier -> "specified by the frozen ledger" / "not specified by the frozen ledger"),
every explanation of an item in these classes quotes it, and no free-text field contains
"approv", "authoriz" or "owner" except inside a class identifier; one control (a lint over the
engine's message strings and a sample result) enforces it.

F5 is met: owner acceptance condition 8 keeps the review lint for rules, PIN_OK reasons,
reconciliation records and other records, and only the authorization lint is removed (sec. 0.1
row 8, sec. 6.3).

## Required non-blocking corrections and nits

- **N-1 (controls).** The predicate's clause "names the same `F` and the same pin table as the
  landing record" has no negative control (TR8/TR10 covered it through the designation in
  v5.5.9; TR30 covers only evaluated commits). Add one: result `F` or pin table differing from the
  landing record's: non-acceptance.
- **N-2 (fail-closed).** Sec. 13.4: a failed or empty `git ls-remote` should explicitly refuse the
  landing (unchanged from v5.5.9; state it).
- **N-3 (wording).** Sec. 6.2 and WB rows call the fingerprinted sentence "the exact approved
  text", "approved location". This is rule-review language, not owner approval, but it is the
  only approval vocabulary left in tool semantics; "fingerprinted text/location" would avoid it.
- **N-4 (simplicity).** `retirement` keeps an optional informational owner login "never compared
  with anything": removing it entirely is simpler. `--config-sha256` (optional, "never a
  substitute") could go. The "no approval implied" statement is repeated in Status, sec. 1, 5, 6.3
  (three places) and the snapshot; one normative sentence plus the B-4 control suffices.
  `CONFIG_UNREVIEWED` now also names failures unrelated to review (run record unreadable, a
  corrupt object); harmless identifier, noted only.
- **N-5 (inventory).** Table 3 omits several `gitobj.py` members (`Unresolvable`, `_git`,
  `parents`, `subject`, `blob_id`, `read`) and `authority.py`'s nested `designate`/`revoke`; all
  fall within the stated module actions. "P's PREREG has more than one Record pins section
  (§26.4, §31.11)" should say nine (B-3).
- **N-6 (pre-existing, not a regression).** The `ci` and `pdf` host-run classes accept any run on
  `X` with the named workflow/job names; a fork `pull_request` with head `X` executes the merge
  commit's workflows. With head pinned to `X` this is narrow and unchanged from v5.5.9; if B-2's
  `head_repository`/event check is added, applying it to these reads costs nothing.
- **N-7.** Status: the 2026-11-24 owner decisions still lack a comment id (sec. 15 item 1), as the
  design states.

## Guarantee table (built from v5.5.9's text and control tables, then compared with the inventory)

| # | v5.5.9 guarantee (controls) | v6.0 | Judgment |
|---|---|---|---|
| 1 | Outcomes, exit codes, wrapper, precedence; interpreter codes non-acceptance (X1-X9) | sec. 5 unchanged | intact |
| 2 | Acceptance predicate: exit 0, schema, S7 recomputation, harness never acceptable (X10 first case, X11) | sec. 5 (`/5`) | intact |
| 3 | Executed engine/entry point equal independently reviewed pins; extra files refused (TR28, TR48, TR52, X10 second case, K7) | bound to self-selected `T` only | **weakened** (B-1, CX-1) |
| 4 | Producing workflow content equal reviewed pin (TR15, TR50) | recorded only | **weakened** (B-1, CX-2) |
| 5 | Producing run in canonical repository, not a fork (TR14) | consumer-relative lookup | **weakened** (B-2) |
| 6 | `head_sha` on `main`'s first-parent chain (TR29 first case) | removed | approval-adjacent; acceptable once 3-5 are bound to `F` (F-1) |
| 7 | Evaluated commits explicit inputs, recorded, never `head_sha`, equal landing record (TR29 second case, TR30) | execution identity 3 | intact |
| 8 | Result = producing run's artifact by sha256; deterministic gzip (TR46, R4-N2) | sec. 5 | intact |
| 9 | Configuration only from `F`, admitted only via `F`'s pin table; files beside it never admitted (TR1-TR3, O6) | sec. 6.3 admission 1-3 | intact for `F`; pin-table selection **weakened** (B-3) |
| 10 | Identity values not caller-overridable (TR9, TR24, TR25) | authority values gone; `--pin-table` new caller input | weakened only through B-3; rest moot |
| 11 | Local runs never `"chain"` (TR13) | admission 4 | intact |
| 12 | Offline replay byte-equal except admission (TR45) | sec. 5 | intact |
| 13 | Integrity of objects read (integrity errors; host-served contents trusted) | verified reader, GV1-GV6 | strengthened (F-8) |
| 14 | Host-read failure never falls back (TR21 technical part) | host reads, GV7 | intact |
| 15 | Independent review of every record, bound to exact blob, full verdict coverage, no role from tool output (O1-O3, O5-O9) | sec. 6.3 | intact |
| 16 | Record lineage, cycles, heads, predecessor lint (S4a, LN1-LN8, LN10) | sec. 6.3, 13.2 | intact; LN4's third case re-covers LN11/LN12's technical part |
| 17 | Widening requires a second non-author widening review covering every changed item, bound to both blobs (A12r, A3r, Z10) | sec. 6.3, 16.2 | intact |
| 18 | Edit completeness, P's selection, splice correspondence, stricter refusals (S11-56..58k) | sec. 6.1 unchanged | intact |
| 19 | Unrelated-change detection (R16, R17, H4, row 14) | unchanged | intact |
| 20 | Four trees, landing composition, reconciliation R1-R13 (N2-N18, R18, R19, Z11) | unchanged | intact |
| 21 | HP provenance and regions (H1-H7, RT-H0, RT-T0) | unchanged; parents from verified reader | intact |
| 22 | Context rule and indicators (K1-K10) | unchanged | intact |
| 23 | Profiles, deny/allow rules, fingerprints, allowances (V1-V27, WB1-WB15, L, A, S) | unchanged | intact |
| 24 | Delegated/native classes in clones at `X` and `C`, re-derivation, exact-head host evidence (G1-G9) | sec. 7 | intact (N-6 pre-existing) |
| 25 | Corpus/mirror consistency, census, Lean docstring-only (sec. 11 rows 8-13) | unchanged | intact |
| 26 | Engine purity (Z9a-Z9h) | allowlist minus retired schema ids | intact |
| 27 | Fail-closed configuration validation (Z1-Z11) | unchanged; retired kind is `CONFIG_INVALID` | intact |
| 28 | Determinism (CI double run, Y1-Y10) | unchanged | intact |
| 29 | `F` designated, not withdrawn/superseded; authority-change and ledger integrity (TR4, TR6-TR12, TR16-TR27, TR31-TR44, TR47, TR54-TR70, LN9, LN11, LN12, O4) | removed | authorization only; removal is the owner's decision |

The inventory's table 4 matches this list except at rows 3-5 and 9, where it says "kept"; G2's
definition ("the code that ran is the code whose blobs were read") is narrower than v5.5.9's.

## Row coverage (script `rows.py`, output `rows-out.txt`)

Every table row of both documents, keyed by table header and first cell: 527 rows in v5.5.9,
469 in v6.0; 431 unchanged, 73 removed by key, 23 modified in place, 15 added by key (six of the
removed/added pairs are first-cell rewrites). This reconciles with the inventory's 431 retained /
29 modified / 67 removed / 9 added, and the inventory accounts for all 527 v5.5.9 row lines
(checked by line number: none missing, none extra).

Removed or modified rows that touched a technical property, with the failure case constructed:

| v5.5.9 row | Technical failure it caught | v6.0 replacement | Catches it? |
|---|---|---|---|
| TR28 | `head_sha` whose tool blobs differ from the reviewed pins | TR28 (checkout ≠ `T`; result blobs ≠ `T`) | **no** (CX-1: blobs equal `T'`'s) |
| X10 (2nd case) | result recording an engine blob ≠ pin | X10 (≠ blob at recorded `T`) | **no** for a self-consistent `T'` |
| TR15, TR50 | workflow content ≠ reviewed pin; same-named workflow at another path | none (workflow blob recorded) | **no** (CX-2) |
| TR29 (1st case) | run from a branch, not `main` | removed | not needed if B-1 fix binds tool to `F`; otherwise **no** |
| TR14 | run in a fork / other repository | TR14 (consumer lookup) | **no** for fork `pull_request` runs (B-2); yes for runs in other repositories when the consumer runs in the canonical one |
| TR9 | caller override of identity values (pin-table path among them via `A`) | none; `--pin-table` is caller input | **no** (B-3) |
| TR8, TR10 | run of a different `F` (technical part: `F` mismatch) | predicate clause "same `F` as landing record" | rule yes, control missing (N-1) |
| TR21 | host-read failure falls back | GV7 | yes |
| TR25 | `A` from another ref | GV1 (refs never consulted) | yes, for the technical part |
| TR48, TR51, TR52 | K7 positive; non-regular/extra entries | TR48, TR51, TR52 (against `T`) | yes for checkout tampering; inherits B-1 |
| TR49, TR53 | authority-file tampering/duplication | none needed | authorization only |
| TR3, TR5, TR13 | beside-config files, positive chain, local run | modified rows | yes |
| O5, O7, O9 | role from tool result; correction without review; positive chain | modified rows | yes (authorization half dropped only) |
| A12r | widening review incomplete | A12r (omits item; names other blob) | yes |
| LN4 | predecessor failing lint | LN4 (plus widened predecessor) | yes |
| LN11, LN12 | widened predecessor across owner change | LN4 third case | yes for the technical part (widening review validity) |
| sec. 0.1 row 8, 0.2 rows, 8.1 row, 16.2/16.4 rows, S13 | traceability text | modified | consistent; S13 acceptance list matches the retained/new ids |

All other removed rows (O4, TR4, TR6, TR7, TR11, TR12, TR16-TR20, TR22-TR24, TR26, TR27,
TR31-TR44, TR47, TR54-TR70, LN9) test only the authorization machinery; I agree with the
inventory's "authorization only".

## Residual authorization machinery (search: authoriz, approv, owner, comment, thread, form, ledger, GraphQL; `residual-hits.txt`)

- **Unnecessary machinery: none.** No read of comments, threads, Issues, PRs, branches, file
  contents or GraphQL; no authority, form or ledger record. The only host reads are Actions REST
  (run record, artifact list/digests, host-run class runs and jobs) and `git ls-remote` for `M`.
- **Necessary technical identity:** run id, repository, workflow path, `head_sha`, `T`, `F`, pin
  table, configuration (after B-1/B-2: plus pinned tool files, workflow blob, repository id,
  event).
- **Harmless naming:** sitemap `carried.owner` (ledger row owner), `CONFIG_UNREVIEWED`, the four
  retained class identifiers (subject to B-4), "ownership chain (R11)" as the name of the
  writer/reviewer chain, the informational owner login (N-4), the retired-kind refusal in
  `records`, procedural sentences (sec. 11 note 1, 12.2, Status) stating that approvals are the
  owner's.
- **Wording rule** ("the tool never states or implies approval"): met by the design's normative
  text, except the output-rendering gap (B-4) and the "approved text" vocabulary (N-3).

Host reads (task 6): each is necessary (run identity; result binding; host-run class evidence;
landing against current `main`) and fail-closed (GV7: no `"chain"`, non-acceptance,
`delegated-evidence-missing`), except `ls-remote`, whose failure handling is unstated (N-2).

## Flag verdicts

| Flag | Verdict |
|---|---|
| F-1 tool commit off `main` | On-`main` itself is approval-adjacent and may go, **but only** with tool identity bound to a fixed reference; as written it is a technical weakening (B-1, CX-1). |
| F-2 pin-table path | Technical; ambiguity confirmed; P has nine pin sections; blocking (B-3). |
| F-3 fork runs at consumer only | Technical; TR14's expectation is false for fork `pull_request` runs; blocking (B-2). |
| F-4 workflow not pinned | Technical; forged-result counterexample; executed workflow may not be `T`'s for `pull_request`; blocking (B-1, CX-2). |
| F-5 condition 8 | Meets owner decision F5. |
| F-6 class names | Identifiers retained correctly (no migration needed, §A.48 item 3); output-rendering part of owner decision F6 not yet met (B-4). |
| F-7 §A.49 rule 4 | Agree: conditional, no amendment needed. |
| F-8 verified reader | Agree: strengthening; shallow/partial stores holding every needed object are acceptable because missing parents error and nothing is fetched. |
| F-9 landing documents | Agree: README and `side-change-classes-v1.json` must change with the implementation; ESC-6 separate. |

## Exact-commit binding (task 5)

A run records `F`, the pin table, the configuration and its review, `T` and every tool blob, the
workflow blob at `T`, the evaluated commits, the run id and the artifact digest, and all repository
objects are read through the hash-verifying reader. An outside reader can compare `F` (and any of
the others) with the hashes an owner's procedural approval names. Substitution that goes
undetected by the tool and the consumer: `T` (B-1), the workflow (B-1), the producing repository
via a fork PR (B-2), and the pin-table file within `F` (B-3); in each case the substituted value is
recorded, so detection rests on a human comparing it with a reference that the design does not
require to exist. With the fixes, every one of these is fixed by `F`, so the owner's one
confirmation of `F` covers all inputs.

## Governance (AGENTS.md at 9deb6956)

| Rule | Check | Result |
|---|---|---|
| §A.25 | Design is not manuscript; propagation applies to the tool's own records (README, class pins) | handled by F-9; no violation |
| §A.39 | P §25.2 places the deletion outside a native V3 round; the tool reads no V3 chronology | no violation |
| §A.42 | item 7: approvals quoted with author and time in the relying record, tool does not check; item 2: run ids provenance only; item 8: Status cites `coord2-q10/...` and scratch files, acceptable for an unlanded design, to be traced at landing | no violation; N-7 open |
| §A.44 | Acceptance reads exit status, schema file, REST run/job/artifact records | no violation |
| §A.45 | Design states it authorizes nothing; implementation needs its own authorization | no violation |
| §A.46 | No established claim; records strengthen nothing | no violation |
| §A.48 | Retired ids not renumbered or reused; class identifiers kept (owner F6); no migration | no violation |
| §A.49 | Tool writes nothing to GitHub; rule 4's "authority record" alternative is conditional | no violation; no amendment needed |
| §A.50 | Merge, freeze/designation, plan execution and trials remain owner approvals, procedural | no violation |
| §A.51 | Work packages unaffected | no violation |

The writer's conclusion that AGENTS.md needs no amendment is **correct**, and remains correct with
the fixes B-1 to B-4 (all are technical bindings to `F`, not authorization records).

## A1-plan dependencies (P1-P5)

Searched P's PREREG, `preserve_check.py`, `edits_check.py`, `guards_check.py` for authority,
forms, freeze ledger, GraphQL, comments, the tool path and designation: P relies on none of the
removed machinery; its "designated" inputs are explicit arguments (P6 correct). P1-P5 are complete
for v6.0 as written. If B-1 to B-3 are adopted, add: **P8**, the amended plan's frozen configuration
carries the tool file pins, the workflow pin, the repository id, and (B-3) the configuration lives
beside the `PREREG.md` whose last `Record pins` subsection lists it.

## Identifiers and register

- No v6.0 use of TR71-TR87, HV1-HV12, HS-1..HS-7, sec. 10.5 or sec. 15 items 7-9; sec. 15 resumes
  at item 10; `GV` appears in no earlier design (grep over every `DESIGN*.md`). Retained ids keep
  their meaning; removed ids (O4, TR4, TR6-TR12, TR15-TR27, TR31-TR44, TR47, TR49, TR50,
  TR53-TR70, LN9, LN11, LN12, item 0a, schema ids) are listed as retired. No renumbering or reuse.
- §A.32/§A.33 govern `papers/` prose; the design is not paper prose. No caps emphasis or
  self-assessment found that would matter if they applied.

## Verified vs inferred

Verified: all hashes; diff regeneration; row counts and inventory line coverage (script); the
text of every removed/modified row; v6.0 sec. 5, 6.3, 7.2, 16.2, 16.6-16.8 against v5.5.9; P's nine
`Record pins` subsections and its last-subsection rule; P's checker bound to the plan commit; the
implementation's last-subsection reader and module/function list; absence of any workflow file in
the implementation; docs.github.com: fork PR events go to the base repository, `GITHUB_SHA` is the
merge commit for `pull_request`, and the run object has `repository`, `head_repository`, `event`,
`head_sha` and `path`.

Inferred (not executed): CX-1 and CX-2 were constructed against the design's predicate text, not
run; that a `pull_request` run uses the merge commit's workflow file (consistent with `GITHUB_SHA`,
not quoted verbatim from the docs); that the REST API lists a fork-PR run under the base repository
(follows from where the event is delivered and the run object's separate `head_repository`; a
REST GET on a public repository was refused by session policy, so not observed directly).
