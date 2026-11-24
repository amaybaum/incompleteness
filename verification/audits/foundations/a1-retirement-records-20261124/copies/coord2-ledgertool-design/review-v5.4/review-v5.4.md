Independent review of DESIGN-v5.4 (ledger and terminology verification tool)

Verdict: REVISE

Reviewer: the independent, non-author session that wrote review-v5.2 and review-v5.3.

Limits kept:
- read-only;
- no repository, git or GitHub write, and no host call of any kind;
- no workflow run;
- the Stage 1 worktree was not touched;
- all new files are under `D/review-v5.4/`;
- the scripts are mine, and import P's frozen `edits_check.py` only after verifying its blob hash.

I did not read or run `work-v54/`. Date 2026-11-23.

Goal link (sec. A.47): A1-EXIT (#1169). This review decides whether DESIGN-v5.4 closes review-v5.3's W1-W4 under the owner's decisions A-D1 to A-D5 and the trust-root addendum. It adopts nothing and authorizes nothing.

Inputs (sha256, verified first; all match the coordinator's values)

- DESIGN-v5.4.md a980251709485e7c1b26c91c32a18d8fdf412adb6f6d8058c382892bc29b9cb3
- CHANGES-v5.4.md d1e5c04858050d61a30b3b9135a6a729c4186d3878ffe3b91d129cbac15033a5
- review-v5.3/review-v5.3.md 20f2c0c3e867cecdbc161dee88df12973f64101acbb15ae1d8a31b6ba1b88b66

Summary

W1 (parity) is resolved in substance. My own implementation of v5.4's selection rule equals P's `variant()`/`check`/`apply_edits` in all 20,000 random cases and all crafted cases, provided "occurs exactly once" is read as Python's non-overlapping `str.count`, which is what P uses. The design does not state that reading, and under an overlapping reading the rule differs from P in 260 of the 20,000 cases (V1). On A1, all 401 edits applied in order bind the 399 splices and the 2 retained edits exactly.

The authority design (A-D1 to A-D5) is largely sound: a numeric owner id, the repository id, the workflow pinned by content hash, exact forms fixed outside `F`, the whole thread read, and edits invalidating a designation. It still fails pass condition 4 and leaves the acceptance predicate unsatisfiable:

- **(V2) The acceptance predicate cannot be met as written.** It requires the run's `head_sha` to be the evaluated commit, and the workflow file at `head_sha` to hash to `A.workflow.sha256`. The tool (`tools/ledger_coverage/`) does not exist at H, T1' or current main, and `X` may change nothing outside the ledger. So no run with `head_sha = X` can contain the pinned tool or its workflow.
- **(V3) The code that produced the result is not bound.** The engine and adapter blob hashes are read from the result itself, which is self-reported.
- **(V4) A non-owner can change the state of a round.** Deleting a withdrawal or supersession comment, or editing one so that it no longer starts with a form, reinstates an earlier designation. That is invisible to "relevant comments only" edit checks and to a count check against the current listing.

These are bounded corrections. They need owner decisions on the points listed at the end.

***

1. Parity (W1, pass condition 2)

Measured (`rv54_variant.py`): my implementation of sec. 6.1 compared with P's own functions.

- **The rule as written.** For every edit, selection at `H` must succeed (P's `check` first loop). The edits are then applied in list order on a running copy, each selecting against the running copy and replacing the first occurrence (P's `check` simulation and `apply_edits`).
- **Random cases.** 20,000 random cases over the alphabet "ab " with 1-3 edits, 60% of them with a second variant. Overlaps and interactions between edits are frequent.
  - With non-overlapping counting (Python `str.count`, as P uses), the selected pair, the refusal and the final text equal P's in **all 20,000 cases**, and in the 6 crafted cases: overlap, empty `old`, `old == old_step2`, an edit whose `old` an earlier edit creates, a variant reachable only after an earlier edit, and overlap in the variant choice.
  - With overlapping counting (a find loop advancing by one), the rule differs from P in **260 of the 20,000 cases** and in 2 crafted ones, for example `old = "aa"` in `"xaaay"`.
  - Sec. 6.1 says only "occurs exactly once". This needs precision (V1).
  - A harness check of my transcription against P's own `check()` uniqueness verdict gives 0 mismatches. My first run reported mismatches because my test edits lacked the `site` and `part` fields that P's failure message formats. With those fields added there are none.
- **A1** (`rv54_a1bind.py`):
  - applying P's 401 edits in list order with P's `variant()` on running copies at `H` binds 399 edits to their splices at their exact byte offsets;
  - the 2 retained edits (D032, D039) are identity and have no splice;
  - nothing is lost.

  My first run showed 2 mismatches (D247, D360). They came from my offset mapping, which used stale running offsets; after the fix all 399 bind. The design's phrase "mapped back to byte offsets at `H`" should state the mapping precisely (V1).

**Judgement on the refusals P does not make.** Three kinds exist; the writer lists two:

- (i) a splice built for the unselected variant (S11-58g);
- (ii) one splice covering two edits (S11-57c);
- (iii) **not listed by the writer:** chained edits, where a later edit's selected occurrence lies in, or overlaps, text an earlier edit created. P applies them, but no set of disjoint splices at `H` can represent them, so the binding refuses. This is my crafted case "edit 2 old created by edit 1".

In all three the tool still computes and records P's per-edit items 5 and 6, so the result of items 5 and 6 never differs from P's. What the tool adds is an ERROR (`SOURCE_CHANGED`) on the ledger, an input P does not have. A ledger that misrepresents P's application, as in (i), must be refused. In (ii) and (iii) the ledger cannot represent P's application at all.

My judgement: these are fail-closed integrity refusals, not a parity defect under condition 2, because no item-5 or item-6 verdict differs from P. None occurs on A1. The owner should confirm this reading. Sec. 6.1 should name (iii) and give it a control (V1).

2. Identity (A-D1)

| Attempt | Outcome | Holds? |
|---|---|---|
| Same login, another numeric id | the comment is not the owner's, so the designation is missing and the run is refused (TR20) | yes |
| Fork owner | repository id differs or the repository is a fork, so the tool refuses and the consumer does not accept (TR14) | yes |
| Owner account renamed | the numeric id is unchanged and still matches; the login is for readers only | yes |
| Owner login released and taken by another account | new numeric id, so not the owner | yes |
| Owner identity supplied by the caller | not read (TR9) | yes |

The numeric id is the right choice: logins can be renamed and reused, and ids cannot.

3. Comment edits, hidden and deleted comments, pagination (A-D2)

| Case | Outcome under v5.4 | Holds? |
|---|---|---|
| Designation edited; edited and then restored | permanently invalid (TR11) | yes, if the host reports every edit (unverified, no host call) |
| Designation deleted | missing, so refused (TR19) | yes |
| A relevant comment hidden or minimized | unverifiable, so refused (TR19) | yes |
| Superseding comment on a later page | the whole thread is read and the count checked (TR12, TR21) | yes |
| **Withdrawal or supersession comment deleted** (by the owner, or by anyone the host lets delete comments in the thread) | it disappears from the listing, and the count check compares against the current count, so it passes. The earlier designation becomes live again, and the withdrawn or superseded `F` is admitted | **no** (V4) |
| **Withdrawal or supersession edited so that its first line no longer starts with a form** | point 3 classifies relevance by the current first line, and point 4 reads edit status only for relevant comments. The comment becomes irrelevant and its edit history is not read, so the earlier designation becomes live again | **no** (V4) |
| **A comment edited into a withdrawal or supersession** | for these kinds point 4 says only that a designation with an edit is invalid; it does not state what an edited withdrawal or supersession means | **unspecified** (V4) |
| First line with CRLF (the host's web interface submits `\r\n`) | "first line is exactly" does not define the line terminator. A trailing `\r` makes an exact designation a "near form", which is refused (fail-closed). A sloppy implementation could instead strip other characters | precision (V5) |

4. Withdrawal and supersession: ordering and ambiguity (A-D3)

The ordering is defined and deterministic: creation time, then comment id. Conflicts fail closed: two live designations, a withdrawal or supersession of a commit never designated, or a re-designation of a withdrawn commit. Apart from V4, I found no ambiguous ordering.

A relevant comment whose first line is a valid form for another plan sharing the same thread refuses as "ambiguous". That is acceptable, because each plan has its own authorized thread. It should be stated.

5. Workflow substitution (A-D4)

| Attempt | Outcome | Holds? |
|---|---|---|
| Same path, different content | hash mismatch (TR15) | yes |
| Same content, different path | path mismatch (TR15) | yes |
| Same-named workflow in a fork | repository id (TR14) | yes |
| **Pinned workflow content, but the tool code it runs taken from a modifiable tree** | the pinned workflow runs whatever tool it checks out. If that is the run's `head_sha` or `main`'s moving head, the tool is caller- or later-chosen. The result's engine hash is self-reported, and nothing in the acceptance predicate reads the executed engine's blobs from the host | **no** (V3) |
| **`head_sha` must be the evaluated commit** | the tool (`tools/ledger_coverage/`) is absent at H, T1' and current main 8e9b8334. `X` = H plus the ledger, and any other change at `X` is FAIL `unauthorized-change`. So `X` cannot carry the pinned tool or workflow, and the acceptance predicate cannot be met for op B or op C at `X` | **contradiction** (V2) |

6. Trust root and bootstrap

- **No circularity.** `A` is data. Its authority rests on three things:
  - the host's attestation of the run's repository;
  - reading `A` only from `main` of that repository through the host API;
  - acceptance only by landing in the canonical repository.

  The bootstrap merged-by check is stated honestly as a consistency check.
- **Refusals.**
  - Caller-supplied `A`: refused (TR24).
  - Another ref or repository: refused (TR25).
  - `F` without `A`: refused (TR27).
  - A copy of `A` in `F` that differs: refused (TR23).
  - The retirement configuration cannot carry authority fields.
  - A configuration changed after `F`: impossible, because the configuration is admitted only from `F`'s pin table, which `F` fixes.
- **The chain of later `A` changes.** Each must be a reviewed, owner-authorized merge, merged by the id the previous `A` pins (TR23, TR26). This is sound. It also means a lost owner account cannot be recovered without an out-of-band act; fail-closed is acceptable, and the owner should confirm it.
- **Changes to `A` between `F` and execution** are admitted when reviewed and authorized, and the current `A` then governs. Sound, and recorded in the result.

7. Residual trust assumptions

The list is incomplete. Add:

- **who the host lets delete, hide or edit comments in the authorized thread** (V4): the owner, and collaborators with the permissions the host grants. Today this is not a stated assumption, and V4's mitigation would make it unnecessary;
- **the integrity of the code the pinned workflow executes** (V3), unless V3's binding makes it host-attested;
- **the runner executing the pinned workflow faithfully**: part of "the host's attestations", but it should be named.

Points the writer asks the owner to confirm, with my judgement

| Choice | Sound? |
|---|---|
| Path `tools/ledger_coverage/authority.json` | Sound. It is the tool's own data, outside the engine's purity scope and covered by the tool's landing review. The tool must read exactly that path on `main` and nothing else |
| Exact comment wording (three first-line forms) | Sound and unambiguous, once the line terminator is defined (V5) |
| A change to `A` must be merged by the previous `A`'s owner id | Sound. It is fail-closed against takeover; owner loss is unrecoverable within the tool (owner decision) |
| Numeric id over login; a login mismatch with the right id is not a refusal | Sound (renames). The mismatch should be reported in `result.json`, which the design says |

***

Required corrections

V1. Parity precision (pass condition 2). In sec. 6.1:
- Define "occurs exactly once" as P's count: non-overlapping, left to right (Python `str.count`) over the file's decoded text. A byte-level count over valid UTF-8 is equivalent.
- Define the mapping from running-copy offsets back to `H` offsets.
- Name the third refusal kind, chained edits that disjoint splices at `H` cannot represent, and give it a control.
- Add a control with an overlapping occurrence (`old = "aa"` in `"xaaay"`): selected, as P selects.

V2. The run's commit (acceptance, blocking). Restate the acceptance predicate and admission point 1 so that they can be met:
- The run's `head_sha` is a commit that carries the pinned tool and workflow, for example the run's ref on `main` of the canonical repository.
- The evaluated commits (`X`, `C`, `L`, `M`) are explicit inputs, which the tool resolves from the object store and records.
- The consumer checks them against the landing record.
- `A.workflow`'s content hash is checked at that `head_sha`.

Without this, no result for an `X` = H plus the ledger can be accepted.

V3. The executed code (pass condition 4 and acceptance, blocking). The consumer must establish, from the host API and not from `result.json`, which engine and adapter blobs ran. For example:
- the pinned workflow obtains the tool only from the run's `head_sha` tree;
- that tree's `tools/ledger_coverage*` blobs must equal the pinned engine and adapter hashes, read by the consumer through the host API at that `head_sha`;
- and/or the pinned workflow verifies those hashes before executing.

State this requirement on `A.workflow`'s content, so that the review of `A` checks it. Add a refusal control: the pinned workflow at a `head_sha` whose tool blobs differ from the pins.

V4. The round's state cannot be changed by deletion or edit (pass condition 4, blocking).
- Read the edit status of **every** comment by the owner in the thread, not only the currently relevant ones. Any owner comment whose edit history contains a first line starting with a form, or any edited withdrawal or supersession, makes the state unverifiable: refuse.
- Make a withdrawal or supersession durable against deletion. Options:
  - require each designation to be re-confirmed in the durable landing record at acceptance time, together with every withdrawal and supersession comment id;
  - or let a withdrawal also be recorded through an owner-merged change on `main`, so that deleting a comment can never revive a designation;
  - or, if the host exposes deletion events for the thread, refuse on any deletion event.

  Otherwise state it as a residual trust assumption, and name who can delete comments in the thread.
- Add controls:
  - a withdrawal deleted after it was posted: refused, or the stated residual;
  - a withdrawal edited into an irrelevant comment: refused;
  - an old owner comment edited into a designation: refused.

V5. Define "first line": the bytes up to the first LF, with one trailing CR removed and no other normalization. Add a control: a designation submitted with CRLF is recognized, and one with a trailing space is refused.

Optional

- O1. State that a thread holds exactly one plan, or that forms naming another plan are ignored rather than refused.
- O2. The committed `result.json` is about 1.26 MB. If it is compressed, commit the compressed bytes with the sha256 of both forms (sec. A.42 item 4).

Owner decisions needed

1. Whether refusals on a ledger that P's model has but the splice model cannot express (kinds i-iii above) are acceptable fail-closed additions under pass condition 2. My view is yes, because items 5 and 6 equal P's in every case.
2. How a withdrawal or supersession is made durable against comment deletion (V4), or acceptance of it as a stated residual, with the list of who can delete comments.
3. Which commit a tool run executes from, and how the executed tool is bound (V2, V3).
4. The writer's choices: the `authority.json` path, the exact forms (with V5), the previous-owner merge rule including unrecoverable owner loss, and the numeric id over the login. My judgement on each is above: all sound.
5. Committing the 1.26 MB result (O2).

Not verified

- No host call was made. The host's semantics for edit history (`updated_at`, `lastEditedAt`, `userContentEdits`), hidden comments, deletion visibility, the comment count, merged-by and fork status are assumed by the design and were not exercised.
- No v5.4 implementation exists.
- The owner decisions reached me through the coordinator, without comment ids.

Files (D/review-v5.4/; MANIFEST.sha256 covers them)

- `rv54_variant.py` and `out54-variant.txt`: the selection rule against P, random and crafted cases.
- `rv54_a1bind.py` and `out54-a1bind.txt`: the A1 in-order binding.
- `data/`: P's `edits_check.py`, `edits.json` and `ledger.json`.
- `diff-v53-v54.txt`.
