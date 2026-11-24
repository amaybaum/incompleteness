Independent review of DESIGN-v5.3 (ledger and terminology verification tool)

Verdict: REVISE

Reviewer: the independent, non-author session that wrote review-v5.2. Limits kept:

- read-only;
- no repository, git or GitHub write;
- no workflow run;
- the Stage 1 worktree was not touched;
- all new files are under `D/review-v5.3/`;
- scripts are mine, and import P's frozen `edits_check.py` only after verifying its blob hash.

I did not read or run `work-v53/`. Date 2026-11-23.

Goal link (sec. A.47): A1-EXIT (#1169). This review decides whether DESIGN-v5.3 closes review-v5.2's corrections V1-V8 and O1 under the owner's four blocking pass conditions. It adopts nothing and authorizes nothing.

Inputs (sha256, verified first; all match)

- DESIGN-v5.3.md 3b24ac8e5e651a5a5651ace69d36112d29e1afe9388696f056631f1c59e7773d
- CHANGES-v5.3.md 2f50b625333a99ada61795f6e3cdea9d184ca8ff96d2bc85375dc29732f85a0c
- DESIGN-v5.2.md 195d1e288b1d6750c333b4707332868d351926793ad2b2a555d64e3bd78f4aeb
- review-v5.2/review-v5.2.md 15260f0957ba81bb555c413a7e73db201a828f059a073a601fbe471da2c34fd0

Summary

V3, V4, V5, V6, V7, V8 and O1 are resolved and testable. V1 and V2 are much improved, but each still leaves a case that breaks a blocking pass condition:

- **V1 (pass condition 2).** The fail-closed correspondence rule models P's "two-step" edit as two sequential steps. In P's frozen checker, `old_step2`/`new_step2` is an alternative variant of the edit, and P applies exactly one variant. So for a P-faithful two-variant edit, v5.3 gives ERROR where P gives PASS. Its controls S11-57a and S11-57b also contradict its own correspondence rule. This misreading started in my own v5.2 review: my constructed cases (a) and (b) described sequential steps, and v5.3 adopted that framing.
- **V2 (pass condition 4).** The owner comment from the host is the right source of authority, but three inputs remain caller-choosable:
  - the repository whose owner is the identity;
  - the CI run's workflow code;
  - the designation form and thread, which the plan amendment inside `F` fixes.

The corrections are bounded text changes. They need the owner's confirmation on the points listed at the end.

***

1. V1: items 5 and 6 on P's unit (pass condition 2; not fully met)

Resolved:

- Items 5 and 6 are defined per edit and per variant pair, exactly as P's `static_new` defines them:
  - REG: set difference per pair;
  - CAPS: per pair, by the edit's `kind`;
  - INF less NEUTRAL: with P's splitter `re.split(r'(?<=[.;:?])\s+', t)`, P's rewrite and P's `inf_key` multiset.
- P's split regex is extracted by `python-ast-call-arg`, and the non-extractable parameters are linted against P's source.
- The per-splice unit is kept as an extra, and a FAIL from either unit is a FAIL.
- With a correspondence that matches P, the union equals P's result exactly. The per-splice evaluation then evaluates a pair that P also evaluates, so it can add no FAIL that P lacks, and the per-edit unit is P itself.
- On A1, P's `static_new` gives 0 / 0 / 0. All 399 splices are byte-identical to their edits. No edit carries `old_step2` or `new_step2` (`review-v5.2/rv52_parity.py`; and here, `rv53_step2.py`, which reads P's blob).

The remaining defect: what P's "second step" is. Measured with P's own code (`rv53_step2.py`):

- P's `variant(e, text)` takes the candidates `(old, new)` and then `(old_step2, new_step2)`, and returns the first whose `old` occurs exactly once in the text. `check` and `apply_edits` apply only that one pair.
- P's docstring says `--commit` checks that "every edit's old string ('old', or 'old_step2' where given) occurs exactly once".
- PREREG's edit table describes `old_step2` as "item (ii) on the projected integration".
- So `old_step2` is the old text in a later state of the file, an alternative, not a second edit applied after the first.
- v5.3 sec. 6.1 requires that "for an edit with a second step, the splice's replaced bytes equal `e.old` and its image equals the result of both steps".
  - For a toy two-variant edit, where H holds `old_step2`, P applies `(old_step2, new_step2)`. The P-faithful splice replaces `old_step2`, so v5.3 gives ERROR `SOURCE_CHANGED` while P applies the edit and its static scan gives 0 / 0 / 0.
  - Where H holds `old` and step 2's `old` happens to occur in step 1's result, v5.3 demands an image that P never produces.

  Either way the tool and P disagree. The failure is fail-closed, never a false PASS, but the owner's pass condition counts any different result as a defect.
- **Controls S11-57a and S11-57b.** They describe sequential steps ("step 1 removes 'now', step 2 re-adds it"). If such an edit's splice is built the way P applies the edit (one variant), the correspondence rule gives ERROR, not the stated FAIL `deny-match`. The expected outcome then does not follow from the rules. The per-edit unit itself is right: it scans both pairs, as P does, so the "now" variant is flagged.
- **Cases (a)-(c) as controls expecting FAIL.** Under v5.3 as written:
  - (c) holds (ERROR `SOURCE_CHANGED`, and FAIL per edit);
  - (a) and (b) hold only if the control's splice is the "both steps" image, which P never produces.

  After correction W1 they hold as restated there.
- **S11-57d** (the splitter) is a sound control.

I found no other case where P and the corrected rule could disagree:

- retained edits are evaluated as P does;
- the edit list is the one bound at `F` by `edits_sha256`;
- every pair P evaluates is evaluated.

2. V2: designation of `F` (pass condition 4; not fully met)

Resolved:

- The authority is the owner's host comment, read from the host API inside CI.
- A record inside `F`'s tree is never read for admission.
- Local runs never reach `"chain"` (TR13).
- Acceptance requires the consumer to read the host run that produced the result.
- The rule is not deferred; only the exact thread and form are left to the plan.

Checked against "independently verifiable, and cannot be self-declared or caller-chosen", three gaps remain:

- **(a) The repository is caller-choosable.**
  - The owner identity is "the owner of the repository in which the CI job runs, as the host's API reports it for the repository the job's own run record names". A caller who forks the repository and runs the workflow in the fork is the fork's owner. They can post the "designation" in the fork's thread with owner association `OWNER`, and points 2-3 hold.
  - The consumer's acceptance checks `head_sha`, workflow name and job name, but not the repository.
  - The canonical repository must be fixed outside the caller's control and checked by both the tool and the consumer, for example the repository id and full name pinned in the plan's text as the owner approves it, or in the consumer's own invocation context. Points 2-3 apply only to that repository.
- **(b) The CI run's code is caller-choosable.**
  - "The named workflow and job" are matched by name.
  - A branch can carry a modified workflow with the same name. That workflow can run a modified tool which writes a forged `result.json` claiming the pinned engine blob and `"chain"` admission. Those fields are self-reported by the result.
  - The consumer must bind the run to the workflow file actually executed. The host run record gives its path, and the consumer reads its blob at `head_sha` and compares it with the workflow blob pinned at `F` or on the canonical default branch. That workflow must invoke the pinned engine.
  - Without this binding, "a host CI artifact" proves only that some CI job produced the file.
- **(c) The designation form and thread are fixed inside `F`.**
  - Point 1 lets "the plan amendment" fix both, and the plan amendment is part of `F`'s tree. A caller-built `F` can therefore define a loose form and a thread of its choosing.
  - Combined with any owner comment that happens to quote that commit's full id for another purpose (for example "do not merge <id>"), the checks of point 3 can pass.
  - The form must be fixed outside `F`, as a generic, unambiguous engine rule that carries no project values. An example is a comment whose first line is exactly `Designate F <40-hex> for <round-id>`, with the round id and the withdrawal form defined the same way. Then no owner comment written for another purpose can satisfy it.

The writer's own additions:

- **"Unedited" (`updated_at` equals `created_at`).** Sound as a strengthening. It needs the owner's confirmation, because it makes any later typo fix void the designation (fail-closed).
- **"Not superseded by a later owner comment".** Sound in principle, but it depends on a "same round" and a "withdraw" form that are not yet defined. As written, TR12 is not testable until (c) fixes both. It needs owner confirmation.
- **The repository-owner identity source.** Workable for this repository, which is user-owned (its owner is a person who can author comments). It does not generalize to an organization-owned repository, where the owner is an organization and cannot author a comment. It needs owner confirmation together with the pinning in (a).

Refusal controls TR6-TR13 are sound but not complete. Missing:

- a designation in a fork or another repository by that repository's owner;
- a result from a CI run whose workflow blob is not the pinned one, with the same workflow and job names;
- an owner comment in a thread other than the round's thread;
- an owner comment that quotes `F` but not in the fixed form (for example "do not designate <F>");
- an explicit withdrawal comment;
- a deleted or hidden comment;
- a superseding comment beyond the first page of the API listing (reading the whole thread);
- the host API unavailable or erroring: never `"chain"`.

3. V3-V8 and O1

| Item | Status |
|---|---|
| V3: tool-landing class bound to exact blobs | resolved. A prefix only locates paths; listed paths with exact blobs; the class record pinned; R19 |
| V4: a control for every reconciliation condition | resolved: N12-N18, and the map in sec. 13.3 assigns one control to each of R1-R13 |
| V5: context hash, location, deterministic grant | resolved. `context_sha256` is defined (sentences in file order under splitter v2, crossing paragraphs, BOF and EOF, UTF-8, `sha256(prev 0x00 next)`), matching Stage 1's `sentence_context_sha`. "Location" means the neighbour pair. WB13 (a move with both neighbours: PASS) is explicit. The grant goes to the smallest byte offset (WB9, WB14). Small precision point (optional O2): define a sentence's byte offset as the file offset of its first byte |
| V6: SW2 reference | resolved: 14 sites named, and my 584/584 tuple-predicate run recorded |
| V7: native execution at `C` | resolved: a second clone at `C`; PASS only at both; G9 |
| V8: N10 pinned to the S6 probe | resolved. Inputs as I derived them (`M` 8e9b8334, `X` T1', `AGENTS.md` 6b1280fa at M, 9f4fc3e8 at X, composition 86d79863, D296 at 2332); N11 positive |
| O1: case-insensitive negatives for every allow rule (WB15) | resolved. `rv53_ci.py`: on all 7 W1 and 4 W2 sentences at T1', case-insensitive counts equal case-sensitive counts (W1-c: one `finit`), so no real-tree outcome changes. Applying the rule to every allow rule is a strengthening |

4. Other points

- **Acceptance and sec. A.42.** Acceptance now depends on a host CI artifact, while sec. A.42 item 2 says CI runs and artifacts are provenance and never the sole support of an enduring claim. A landing-time acceptance verdict may legitimately read the host, as sec. A.39's `check-run` attestations do. But the design should say how the accepted result is retained on `main`: committed with its run identity, re-derivable by re-running at the same commit. This is an owner point. It does not block the design.
- I found no regression in the unchanged parts. The deny rules, `resid`, the W1 allowance values and the item-7 check are byte-identical in intent; the diff touches none of them.

***

Required corrections

W1. V1 correspondence (pass condition 2). Restate P's second step as P defines it.

- An edit has one or two variants, `(old, new)` and optionally `(old_step2, new_step2)`.
- The splice must correspond to the variant that P's `variant()` selects at `H`: the first pair whose `old` occurs exactly once in `H`'s file. Its replaced bytes must equal that pair's `old` and its image that pair's `new`.
- Any other relation is ERROR `SOURCE_CHANGED`.
- The per-edit unit still evaluates both pairs, as `static_new` does.
- Restate S11-57a and S11-57b as two-variant edits whose unapplied variant adds "now" (or "no longer"): the per-edit unit gives FAIL and the per-splice unit alone would PASS.
- Add a control in which `H` holds `old_step2`. Expected: the correspondence holds, and the result equals P's.
- Note in the change record that the v5.2 review's sequential description of cases (a) and (b) was the source of the error.

W2. V2 repository binding (pass condition 4). Fix the canonical repository (id and full name) outside the caller's control, and require both the tool and the consumer to check that the run, the thread and the comment belong to it. Add a refusal control for a fork or another repository.

W3. V2 run binding (pass condition 4). The consumer verifies:

- the workflow file the host run executed, by path and blob at `head_sha`, against the pinned workflow blob;
- that this workflow runs the pinned engine.

Add a refusal control for a same-named, modified workflow.

W4. V2 designation form (pass condition 4). Fix the exact designation and withdrawal forms, and the meaning of "round", outside `F`, as generic rules of the tool. The plan may name the thread and the round id, but the form must be one that no comment written for another purpose can match. Add refusal controls for:

- the wrong form;
- the wrong thread;
- a withdrawal;
- a deleted or hidden comment;
- pagination;
- the host API unavailable.

Optional

- O2. Define a sentence's byte offset for WB14 as the offset of its first byte in the file.
- O3. State how an accepted result is retained on `main` (sec. A.42).

Points needing an owner decision

1. The owner identity source: the owner of the canonical repository as the host reports it, with owner association `OWNER`, assuming a user-owned repository. The alternative is another host source the caller cannot choose.
2. The "unedited since creation" rule: any edit voids a designation.
3. The "not superseded" rule, with its round and withdrawal forms (W4).
4. The canonical repository's identity and where it is pinned (W2), and the pinned workflow (W3).
5. Acceptance based on a host CI artifact, and its retention under sec. A.42 (O3).

Not verified

- No v5.3 implementation exists, and nothing was run on the Stage 1 engine for this review.
- The host API's exact semantics were not exercised, because no host call was made: whether `updated_at` changes only on edits, how hidden comments and owner associations are reported, and pagination.
- The owner decisions reached me through the coordinator, without comment ids.

Files (D/review-v5.3/; MANIFEST.sha256 covers them)

- `rv53_step2.py` and `out53-step2.txt`: P's variant semantics against v5.3's correspondence rule.
- `rv53_ci.py` and `out53-ci.txt`: case-insensitive negative counts on the W1 and W2 sentences.
- `rv5_rules.py`, `rv_git.py`: helpers copied unchanged from my earlier reviews.
- `data/`: P's `edits_check.py`, `edits.json` and `ledger.json`, as read from the object store.
- `diff-v52-v53.txt`.
