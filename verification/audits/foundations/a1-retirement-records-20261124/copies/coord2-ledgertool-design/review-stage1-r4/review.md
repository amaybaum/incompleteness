# Independent review r4: the ledger coverage tool at 28f7e37c (trust chain, adversarial)

Reviewer: independent. I wrote none of the code and none of the earlier reviews. I worked read-only on the subject.
All runs used my own detached worktrees under `review-stage1-r4/`: `wt` at 28f7e37c and `wt-old` at 6babcea4. Both
were removed at the end with `git worktree remove`. Scripts are in `scripts/` and outputs in `out/`.

Verdict: **REJECT**. There are 2 BLOCKING findings, 2 DESIGN-ISSUE and 8 NON-BLOCKING. The r3 findings B1, B2 and B3
are fixed, and there is no regression.

## 0. Inputs verified

- `DESIGN-v5.5.3.md` sha256 99e9ce3a...3379 matches.
- `review-stage1-r3/review.md` sha256 4e72be61...c9d8 matches.
- `impl-stage1-r4/MANIFEST.sha256` sha256 5af160fa...4003 matches, and `sha256sum -c` passes on all 46 entries.
- The staged draft configuration has sha256 a0bd0568...e706. It differs from r3's staged draft only in the two
  references to the class record's blob: cd231be2... became d526eaa2..., which is that record at 28f7e37c.
- Subject history: 6babcea4 -> 6b0c00dd -> b654c8f3 -> 28f7e37c, linear, with no merges. 28f7e37c descends from
  4fb2c1ee.

## 1. Scope (focus 8): CONFIRMED

- `git diff --name-status 4fb2c1ee 28f7e37c` lists 58 entries. All of them are `A`, and all lie under
  `tools/ledger_coverage*` or `verification/audits/foundations/ledger-coverage-tool-20261123/`. No pre-existing file is
  modified.
- I grepped the added lines for `<tmp>/`, `/home/`, `workspace`, e-mail addresses, `noreply` and model ids. Nothing
  matched.
- `authority.json` engine pins: 44 entries, equal to the 45 tool files less `authority.json`, and every hash matches.
  The workflow draft hashes to `A.workflow.content_sha256`.
- The class record pins all 57 other landed paths. sha256 and git blob both match, with no extra pins.
  `out/pins-check.txt`.
- The plan branch `research/a1exit-deletion-20261121` is at 4c79be642ca631573f06b444903be75ec4f5e2b6, both by the
  local ref and by `git ls-remote origin`.
- The configuration is not in the landing.

## 2. Regression suite (focus 7)

I ran the writer's steps 1-7 in my own worktree at 28f7e37c with the r4 staged configuration: `scripts/repro.sh`,
output in `out/repro/`. Step 6 took 1175 s.

| Step | My outcome | Same as the writer? |
|---|---|---|
| 1 self-test | 87 PASS, exit 0 | yes |
| 2 staged purity lint | PASS, 0 findings, exit 0 (config a0bd0568) | yes |
| 3 synthetic fixture | 36 PASS, exit 0 | yes |
| 4 conformance | 75 PASS, 2 NOT RUN (TR5, G-A1), exit 0 | yes |
| 5 A1 conformance | 46 PASS, exit 0 | yes |
| 6 A1 controls | 90 PASS, 1 NOT RUN (RT-T), exit 1 (N4) | yes |
| 7 release gate | exit 1: lean-axioms, legacy-records, v3-corpus, v3-receipts, citation-roles | same five failing steps as r3 |

**Totals: 335 PASS, 0 FAIL, 3 NOT RUN** (TR5, G-A1, RT-T). This reproduces the writer's claim.

- **Control-by-control comparison.** `scripts/compare_controls.py` reads the raw outputs of three runs: the r3
  reviewer's run at 6babcea4, the writer's r4 run, and mine. Output in `out/control-comparison.md`.
  - No control that passed in r3 fails to pass here, and none is absent.
  - Seven controls were added: R4-B1, R4-B1-GUARDS, R4-B2, R4-B2-PROV, R4-B3, R4-B3-DUP and R4-N2.
  - My run and the writer's agree on every control.
- **NOT RUN.** TR5, G-A1 and RT-T need GitHub or CI, and are reported honestly as NOT RUN.
- **Release gate.** The step-7 failures are the shallow-repository and missing-Lean-toolchain conditions already
  recorded in r2 and r3. The diff touches only the tool's own prefixes.

## 3. The r3 counterexamples, before and after (focus 6)

I reproduced these independently with the r3 reviewer's unmodified probe scripts, run against both of my worktrees
(`out/r3probes-old/`, `out/r3probes-new/`), plus my consumer probe. Everything ran on the simulated host, in memory,
over real synthetic git objects.

| Counterexample | 6babcea4 | 28f7e37c |
|---|---|---|
| R1 approval replay across A->B->A (both forms) | ACCEPTED, exit 0 | refused: "is not an append" |
| R2 replay with no owner change (both forms) | ACCEPTED, exit 0 | refused: "is not an append" |
| R3 a different change with no approval | refused | refused |
| P9 approval after a direct push (no merge record), both forms | ACCEPTED, exit 0 | refused: "has no merge record" |
| P1-P8, P10-P12 | as in r3 | identical to 6babcea4 (the owner-in-force rule is unchanged) |
| C9 second class lacking an id, one record-level verdict | classified, exit 10 | record-invalid, exit 20 |
| C8 every class lacking an id | uncaught `KeyError` | record-invalid, exit 20 |
| C0-C7, C10 | as in r3 | identical |
| Consumer binding: forged bytes, landing quotes the genuine hash | accepted (True) | rejected (False) |
| Consumer binding: same JSON, different bytes | accepted (True) | rejected (False) |

The two guards of B1 are each shown to work alone by the writer's R4-B1-GUARDS. I read the stub mechanism and accept
it.

On their own, my probes show this:

- A reverted or re-applied change is refused by append-only.
- Within one history, single use is defence in depth. Append-only already makes every (from, to) pair unique, and the
  hash spaces of A and of the ledger are disjoint.

## 4. BLOCKING findings

### K1 (BLOCKING): a committed snapshot designates a freeze that no owner comment designates

**Code path.** `authority.admit` reads every `landings/*/snapshot.json` on `main` under the ledger directory:
`snap_events`, `authority.py` near line 450. No check of any kind is applied to those files: no approval, no merger
check, no review. A `withdraw` or `supersede` event among them is "bound". When its `comment_id` is not in the thread,
it is appended to the event list unchecked. When it is in the thread, only its author id and first line are compared,
not the owner. In the state machine, a bound `supersede` then sets `state[by] = 'designated'`.

**Counterexample.** `scripts/r4_snapshot_probes.py`, output in `out/snap-new.txt` and `out/snap-old.txt`, simulated
host.

- **S1.** The owner designates F. A file `syn/freeze/landings/forged/snapshot.json` lands on main, merged by account
  31337, with no approval of any kind. It holds one event: `supersede commit=F by=F2`, with `comment_id 777777`, which
  does not exist in the thread. A run for F2 is admitted, exit 0, with `designation_comment_id: 777777`. No owner
  comment names F2 anywhere.
- **S2.** The same, but the event is bound to a real comment in the plan thread written by the non-owner account 31337
  (`oi-freeze/1 supersede ... by=F2`). F2 is admitted, exit 0, with `designation_comment_id` set to that non-owner
  comment.
- S0 is the positive control. S3 shows that the snapshot cannot create a first designation on its own. S4 shows that
  a forged withdrawal only refuses, which is the restrictive direction.
- The behaviour is identical at 6babcea4, so it is pre-existing and was missed by every earlier review.

**Requirements violated** (sec. 6.3):

- Reconciliation: "a designation must be present and verifiable in the thread now; a ledger entry alone never
  designates".
- Admission point 6: the pin table's "content is authenticated by the owner's designation of exactly `F`".
- Points 3 and 4: forms are read only from comments whose author is `A.owner.id`.
- The bound-event rule exists "so it can never silently reactivate an earlier freeze". It is restrictive: it lets a
  withdrawal outlive its comment. It does not license a designation.

**Effect.** Any account able to land a file on `main` can redirect the round to its own `F2`. That `F2`'s pin table
then admits an arbitrary configuration, which defeats the whole chain. The design's trust in the host's access control
on `main` does not cover this, because the design states for A and the ledger that "the merge alone authorizes
nothing".

**Fix, local.** A bound `supersede` revokes `commit` only. `by` becomes designated only through an owner form in the
thread, and the snapshot event alone never designates. A bound event that names a comment present in the thread
should also require that comment's author to be `A.owner.id`. Add S1 and S2 as controls.

### K2 (BLOCKING): the two ledger-approval forms are treated as alternatives; an append needs only an `oi-authority/1 approve`, and neither route checks the review or the merger

**Code path.** In `verify_history`, kind `ledger`, any single fresh approval suffices: either an `oi-authority/1
approve` in the authority thread, or an `oi-freeze-ledger/1 append` in the admitted plan's thread. Neither route checks
`merged_by_id` or an independent review record. The comment's `plan=` and `round=` are ignored: the loop variables
`(plan, rnd)` are unused.

**Counterexample.** `scripts/r4_chain_probes.py`, output in `out/chain-new.txt`, simulated host.

- **L2 [authority].** An append that adds events is approved only by `oi-authority/1 approve` in the authority thread.
  There is no `oi-freeze-ledger/1 append` comment in the plan thread. The change is merged by account 31337, and no
  review record exists. Result: **admitted, exit 0**.
- **L2 [append].** Only the plan-thread append comment exists, the change is merged by 31337, and there is no review.
  Result: **admitted, exit 0**.
- **L3.** An append comment in the plan thread naming `plan=other-plan round=r9`, a plan A does not list, authorizes
  the append, exit 0. So does `round=r9`.
- Identical at 6babcea4, so pre-existing.
- The writer's own R4-B1 control expects the authority-thread route to be admitted ("appends, each approved
  [authority]: exit 0"). It therefore encodes this behaviour.

**Requirements violated** (sec. 6.3, "The freeze ledger"; and N3 as adopted in `CHANGES-v5.5.2.md`):

- N3 states: "Every append to the freeze ledger, including an acceptance landing's append, needs its own explicit
  owner approval comment. The comment must: be in the plan's authorized thread; use the versioned first line
  `oi-freeze-ledger/1 append plan=<plan_id> round=<round_id> ...`". TR47 requires refusal when the append comment is
  absent or outside the plan's thread. L2 [authority] has no such comment and is admitted.
- "Every change lands through the authority-change procedure, with an `oi-authority/1 approve` comment". That
  procedure also requires "an independent review record (sec. 6.3) [that] names both blobs" and a pull-request merge
  whose "merged-by id must equal the previous owner id". Neither route checks either.
- `plan=<plan_id> round=<round_id>` names the plan whose thread carries the comment. L3 accepts other values.

**Uncertain point.** Reading the two sentences together, every append needs both the authority-change procedure and
the N3 comment. Under the narrowest reading I can defend, the authority-thread comment alone is not the N3 comment.
That alone suffices for the counterexample L2 [authority]. Whether the procedure's review and merged-by checks apply to
ledger changes is the only interpretive question. If the owner reads them as not applying, that part becomes a
DESIGN-ISSUE. The N3 part stands either way.

**Fix, local.**

- Require for every ledger change that adds events an `oi-freeze-ledger/1 append` comment in the thread of the plan
  its events name, with `plan=` and `round=` equal to those events.
- Require the authority-change procedure's approval, review record and merged-by check, as the owner confirms.
- The first, empty ledger, which lands with A, stays under the authority procedure alone.

## 5. Owner criteria (a), (b1), (b2)

**(a) Duplicate class ids: confirmed.**

- The design requires ERROR `CONFIG_INCONSISTENT` for this case:
  - sec. 13.1: "definitions of one id, in one record or several, are ERROR `CONFIG_INCONSISTENT` (S7, control Z11)";
  - the Z11 row;
  - the sec. 16.6 error table.
- `config.py` near line 227 raises it at configuration load, before any record is used, over every class record the
  configuration references. `cli.py` line 1061 raises it again over the classes gathered with `--classify`.
- E3 (`out/records-new.txt`): two classes with one id in one record give exit 65, `CONFIG_INCONSISTENT`. No result is
  produced and nothing is classified. The probe's `classified=True` only means that no unclassified item exists,
  because the run stopped.
- Duplicates in other record kinds, and duplicate verdicts, are `record-invalid`. E4, E4b and E5 each give exit 20 and
  the side change stays unclassified.
- In neither case is the duplicate used. ERROR (exit 65) stops the run and is never acceptable, so it is at least as
  strict as FAIL (exit 20).

**(b1) Merge times: no bypass within the design's trust model. NON-BLOCKING, documented.**

Besides the time, the tool checks (`_provenance_problem`):

- commit identity: the merge record's `merge_commit_sha` must equal the version's commit;
- ancestry: the commit must be on `main`'s first-parent chain;
- introduction: the commit holds the version, and its first parent holds the previous version;
- monotonicity: merge times strictly increase along the history;
- approval timing: comment `created_at` strictly before the merge time (L9: an equal time is refused).

Approval timing has no independent source. It compares two host attestations: the pull request's `merged_at` and the
comment's `created_at`.

- **T1** (`scripts/r4_b1b2_probes.py`, `out/b1b2-new.txt`): a ledger change merges, the owner approves afterwards, and
  the host reports a `merged_at` later than the approval. The change is admitted, exit 0, in both forms.
- **T2**, the same with the true time, is refused.
- So a host that reports a later-than-true merge time defeats the timing rule.

I could not construct that on the real host. GitHub sets `merged_at` itself, and a user cannot choose it.

- A direct push to `main` produces no merged pull request whose `merge_commit_sha` equals the pushed commit: P9 is now
  refused.
- The one real-host route I can see is GitHub's after-the-fact detection of a manually merged pull request. That needs
  a push to `main` that bypasses protection, followed by an owner approval inside the detection lag. Even then the
  approval is still the owner's, quotes the exact hashes, and is single-use.

This is the design's stated residual: "The host's API and its attestations ... `main`'s head and history; a pull
request's merged-by id". It was not executed on GitHub (NOT RUN).

**(b2) Path-filtered history: fail-closed. NON-BLOCKING, documented.**

- `RestHost.file_history` lists `commits?sha=<main>&path=<p>` and keeps only commits on `main`'s first-parent chain.
- GitHub applies default history simplification to that listing. A true merge commit whose result is TREESAME to its
  second parent for the path is pruned, and the branch commits are listed instead. Those are then dropped as off-chain.
  So a merge-commit-style landing can vanish from the listing (reasoning only, NOT RUN on GitHub).
- The continuity check makes any such omission fatal rather than skippable:
  - the first listed version's parent must hold no file;
  - each version's first parent must hold the previous listed version;
  - the last version must equal `main`'s.
- Blobs cannot recur:
  - the ledger is append-only;
  - A's `supersedes` names the previous blob, so a hash cycle would be needed.
- Therefore no omitted transition can be bridged.
- Probes on the simulated host:
  - O (ledger) and P (authority), with the listing omitting the first, a middle or the last change: refused in all six
    cases;
  - the control with nothing omitted: admitted;
  - L7, a true two-parent merge whose second parent changed the ledger, listed as the in-memory host lists it:
    admitted.
- The cost is liveness. On GitHub, a merge-commit landing of A or the ledger whose listing is simplified away makes
  every later admission refuse, so squash or rebase merges are needed. That is fail-closed, with no requirement
  violated. NON-BLOCKING (N8).

## 6. The trust chain by focus area

1. **Approval lifecycle.**
   - Each ledger approval is single-use, unedited, visible, by the owner of the A in force at the merge (the latest A
     merged strictly before it on the first-parent chain), and created strictly before a recorded merge.
   - P1-P12 match r3.
   - L5: a 4242 approval created before 4242->5555->4242, with the change merged after the change-back, is accepted.
   - L6: 5555 approves while not yet owner, 4242->5555, then the merge: accepted past the ledger.
   - Both match the design's letter, "authored by `A.owner.id`", "created before the merge". The design sets neither
     an approval expiry nor a requirement that the author be owner when the comment was written. See DESIGN-ISSUE
     DI-1.
   - Authority changes (L13): no merge record is now refused. The co-approval of the new owner is consumed as well.
   - Withdrawal and supersession: K1.
2. **Ledger history.** Continuity, append-only, unique approvals across both histories and timing all hold (sec. 3,
   O, P, L8-L11). Missing (P9), altered (L8, R4-B2-PROV), off-first-parent and non-introducing merge records
   (R4-B2-PROV, O) are refused. K2 remains.
3. **Record integrity** (`out/records-new.txt`):
   - E1, E2: an empty or non-string id is record-invalid.
   - E3: a duplicate class id is CONFIG_INCONSISTENT.
   - E4, E4b, E5: duplicate or conflicting verdicts are record-invalid.
   - E7: a supersedes naming a record that never existed is record-invalid.
   - C1-C7 (r3 probes): reviewer equal to author, a reject verdict, a missing per-item verdict, an authorization not
     listing both blobs, and a wrong owner are each record-invalid.
   - E6: a supersedes that names a same-schema record of another lineage (another `record_id`) is accepted. DI-2.
   - E8: `classes` as an object rather than a list makes the configuration loader raise `AttributeError`. That is
     INTERNAL, exit 71, with no result. N6.
4. **Combinations.**
   - Approval reuse after an owner change, and a revert with a late approval: refused (R1, R2, P8).
   - A re-targeted approval: the ledger-append comment's plan and round are ignored (K2, L3). Designation forms are
     plan- and round-bound.
   - An authority change re-legitimizing a stale approval: allowed by the letter (L5, DI-1).
   - A record valid in one mode used in another: harness and replay results carry `harness` or a non-`chain` mode and
     are never accepted. Harness mode cannot be selected from the command line.
5. **Acceptance.**
   - `checker.accept_with_host` is the only acceptance predicate; `accept` is its offline part.
   - It now refuses non-bytes and hashes the raw bytes itself. That hash must equal both the run's artifact and
     `landing.result_sha256`, and the document is parsed from exactly those bytes.
   - The landing record cannot override this. Forged bytes are refused whatever hash the landing quotes (B, C), and a
     differing `evaluated` is refused (G).
   - The K7 allowlist and admission pins still hold on the consumer side:
     - an extra file is refused (K1');
     - a second copy of A is refused (K2');
     - a one-byte change to A is refused (K3');
     - an unrelated change is accepted (K4').
   - `landing.artifact_name` is not pinned (F). Any artifact of the attested run whose bytes hash correctly is
     accepted. The pinned workflow uploads one artifact, so this needs the pinned run itself to upload forged bytes,
     which is within the host-runner trust. N7.
   - The landing check that composes `verify_compressed` with this predicate does not exist in this landing. NOT RUN.

## 7. DESIGN-ISSUE

- **DI-1. Owner identity is evaluated by the current owner, not by the owner when a comment was written.**
  - D1: a former owner's designation stops counting after an owner change, so the round needs re-designating.
  - D2: a former owner's withdrawal that never reached the ledger is ignored, so the new owner can re-designate the
    withdrawn F (admitted past state, stopping only at point 7).
  - D3: comments the new owner wrote before becoming owner count as designations.
  - L5 and L6 are the ledger analogue.
  - All of these follow the design's text ("every comment whose author numeric id is `A.owner.id`"). Whether forms
    should bind to the owner in force at their creation is the owner's decision.
  - Probes: `out/chain-new.txt`, D1-D3.
- **DI-2. "Lineage" is undefined for records other than the configuration.**
  - Sec. 6.3 requires `supersedes` to name a record "of the same kind, schema and lineage". The code checks lineage
    only for the configuration (`config_id`). E6 is accepted.
  - The design names no lineage field for the other kinds. I report the gap; I do not demonstrate a violation.

## 8. NON-BLOCKING

- **N1.** (b1): approval timing rests on two host attestations. This is the stated residual.
- **N2.** Multiple plans (L4). Admission of plan P reads only P's thread. An append approved in another plan's thread
  therefore makes every admission of P refuse. This is fail-closed. A1 lists one plan, so A1 is unaffected, but it
  limits the engine's generality, and the fix for K2 should read the thread of the plan each append names.
- **N3.** Two fresh approvals for one change are refused, even though both are the owner's (L12). Fail-closed.
- **N4.** `a1_controls.py` exits 1 when the only non-PASS control is the NOT RUN control RT-T. Carried from r3.
- **N5.** The delegation contract is not chain-linted. Carried from r3.
- **N6.** E8 crashes (INTERNAL 71) instead of giving record-invalid. Fail-closed.
- **N7.** The consumer does not pin the artifact name (F).
- **N8.** (b2): merge-commit landings may be invisible to GitHub's path-filtered listing, which fails closed.
  Recommend squash merges for A and the ledger, or a first-parent walk in place of the path listing.

## 9. Control and probe status

- **Independently tested by me on real git objects:**
  - steps 1-7 in my own worktree at 28f7e37c with the r4 staged configuration;
  - the scope and pin checks.
- **Simulated host only**, in memory over synthetic git objects:
  - the r3 probes at both commits;
  - `r4_chain_probes` (L0-L13, O, D1-D3);
  - `r4_b1b2_probes` (T1, T2, P);
  - `r4_snapshot_probes` (S0-S4);
  - `r4_record_probes` (E0-E9);
  - `r4_consumer_probe`;
  - all TR and R4-* conformance controls.
- **NOT RUN** (they need GitHub or CI, or reviewed records):
  - TR5, G-A1, RT-T;
  - the landing check composed with acceptance;
  - (b1) and (b2) on the real host.

## 10. Verdict

**REJECT.**

- **K1:** a committed snapshot, needing no approval, designates a freeze that no owner comment designates (S1, S2).
- **K2:** an append is admitted with only an authority-thread approval, contrary to N3 and TR47. Neither ledger route
  checks review or merger, and the append comment's plan and round are ignored (L2, L3).

Both are pre-existing, present at 6babcea4. Both have local fixes. B1, B2, B3, N2 and N3 of r3 are fixed. The
duplicate-id handling meets the design (a). Merge times and path-filtered listings give no bypass within the trust
model (b1, b2).
