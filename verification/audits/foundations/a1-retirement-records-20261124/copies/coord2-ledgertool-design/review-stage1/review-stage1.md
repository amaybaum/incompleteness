# Independent review: Stage 1 of the ledger and terminology verification tool

Reviewer: an independent non-author reviewer (no part in the design or the implementation). Date
2026-11-23. Read-only review of a local commit under the owner decision of 2026-11-23: no push, no
pull request, no GitHub write, no workflow run, no git write in any repository. All runs were made in
an independent copy of the object store under `review-stage1/repo` (a `cp -a` of the `.git`
directory, checked out detached at the reviewed head). The implementation worktree W was only read.

Goal link (sec. A.47): A1-EXIT (#1169), the exception-free verification route. This review decides
whether the Stage 1 implementation may proceed toward landing, and what must change first. It
decides no scientific question, adopts no rule or record, and authorizes nothing.

## 1. Inputs, verified

| Input | Identity | Check |
|---|---|---|
| W HEAD | 8c1e628a08272ad9414929fa8e003020e1cc2234, branch `tools/ledger-coverage-20261123` | verified; parents 8c1e628a -> aff3cf08 -> 6f1ff70f -> 9595265b -> 944fc9d1 -> 4fb2c1ee, linear, 5 commits |
| Base | 4fb2c1eed350edf95da2b316abcca93717246589 | `git diff --name-status`: 46 entries, all `A`; 11660 insertions, 0 deletions; no existing file changed |
| W working tree | | clean (`git status --short` empty) |
| DESIGN-v5.1.md (governs) | sha256 0c4ff0e60331d0e9604ece0c997dec472b3f977bf24384676d74f850bff4a3fe | verified |
| CHANGES-v5.1.md, review-v4/, review-v5/, review-v5.1/ | | read for context |
| impl-stage1/REPORT.md | sha256 9093f93a002fcc2dfa5574468ed15bf37044a6434c59b2f2d81d3eecde7cad9f | verified; `MANIFEST.sha256` of impl-stage1 verifies (all OK) |
| E, H, P, T1', W(main at v3) | e837e3db..., 53c6601a..., 4c79be64..., 14ac71b4..., 413b0bb8... | all resolve to commits in the copy |
| Current remote `main` | 4fb2c1eed350edf95da2b316abcca93717246589 | `git ls-remote origin main` (read-only), 2026-11-23 |

## 2. Verdict

**REVISE.**

The engine core is sound where I could test it: the counts it reports reproduce, its output is
deterministic across processes, its exit codes and fail-closed configuration refusal behave, and
the unreviewed drafts are refused under the review chain. Each of the writer's three count
differences is explained below, and in each the implementation is right and a design figure or
expectation is wrong. But the Stage 1 commit cannot go to landing review as it stands:

- the acceptance predicate accepts a control-harness result as a real run (B1);
- three delegation classes that the design makes native re-executions accept self-reported JSON
  instead, and no clone-at-X execution path exists (B2);
- the trust root of the configuration is the caller's `--config-sha256`, plus any review and
  authorization file found beside the configuration, and nothing ties it to the owner's
  designation of `F` (B3);
- C's further commits are not classified (B4);
- A1 edit-list semantics are hard-coded in the engine, and Z9 misses them because its value set
  leaves out the records the configuration references through its adapters (B5);
- the control report overstates its own results. RT-T is recorded as met without being run, and
  RT-D is recorded as met while two W1 lines FAIL (B6).

The design also needs a v5.2 correction for W1, SW2, the structure-REVIEW count, the region-line
figure, RT-D's `resid` figure and the register and infinity semantics (D1-D6). RT-L2 fails at
current main for a real reason, which is not a tool defect but does block landing under the
sequencing safeguard (sec. 13.4) until the owner resolves it.

## 3. Findings by owner priority

### 3.1 Priority 1: W1 self-match (ch19:198, FULL:5270)

**Reproduced.** With the engine's splitter (version 2, the configured abbreviations), the sentence
that W1-c fingerprints at T1' (ch19:198 = FULL:5270) is "On a finite periodic quotient of
$\mathbb{Z}^3$, a qualified case of A4 (Chapter 2), the notion of ... (one of the framework's six
structural properties of the bijection), isotropy is built in ...". It is one sentence, and the
design's W1 negative list (`A1`, `A1-A6`, `finit`, `assumption`, `axiom`, `of the substratum`)
matches it through `finit`. Sec. 6.2 step 3 applies the negative matcher to the whole sentence, so
both lines are FAIL `rule-negative-match`. The tool implements sec. 6.2 faithfully. The other 5 W1
lines (SM.md:1394, ch09:137, FULL:2554, ch19:212, FULL:5284) match no negative literal and PASS
(`scripts/rs_w1.py`, `out/w1.json`).

**This is a design defect, not an implementation defect.** The design states W1's negative list,
and it also states that every W1 line PASSes with its rule: RT-D ("W1 and W2 PASS with their
rules"), RT-I7A ("which become PASS once W1, W2 and GR.md:58's record exist"), sec. 8.2 and sec. 11
note 1. For these two lines the two statements contradict each other. No design figure ever
measured W1 application, because the W1 rules were "for review; not adopted". The lint has a gap
too. Sec. 6.3 asks that each fingerprint be reproduced at `recorded_at`, but it never asks that the
fingerprinted sentence be accepted by its own rule through steps 1-6. The implementation's
`lint_rule` therefore passes W1-c. Its positive example is a fragment that leaves out "finite
periodic quotient".

**What the negative is for, read from the design.** W1's negative literals pick out text that ties
the property count to the retired posit: finiteness ascribed to the substratum or configuration
space, `A1`, or "assumption", "axiom" and "of the substratum". Control V7a records the intended use:
a W1 sentence edited to include "one of which is total finiteness" must FAIL through the negative
matcher. "finite periodic quotient of Z^3" describes the lattice (the qualified A4 case), not a
finiteness posit. Under the design's intent the sentence should PASS.

**The correct rule.** The check must not be weakened to make it pass, so I separate two options.
They differ only in how a *mutant* of the W1-c sentence is classified. Neither changes any outcome
on a real tree other than the two lines.

- **Option A (no engine change; recommended).** For W1-c only, replace the bare stem `finit` with
  the design's own retired-finiteness vocabulary, fixed in advance from reviewed design text rather
  than chosen to fit:
  - DR-3's finiteness tail (`total[- ]finiteness | finite in total | totally finite | finiteness`);
  - resid-a, resid-b and resid-c's finiteness alternatives (configuration, state or phase space ...
    finite; finite ... set; substratum, universe or world ... is finite; finite number or count of;
    posit-noun ... finit and finit ... posit-noun);
  - "configuration space" and "state space", the terms W2's own negative list and DR-4's tail
    already use;
  - the other five negative literals, unchanged.

  Measured: both W1-c lines match nothing, so they PASS. Every V7a-style mutant still matches:
  "namely total finiteness", "the first being finiteness of S", "since the substratum is finite",
  "on a finite configuration space", "on a finite set". One kind of mutant moves from FAIL to
  REVIEW `rule-fingerprint-mismatch`: one that adds finiteness wording outside that vocabulary, such
  as "of finite capacity". Fingerprints still hold every edit of the sentence at REVIEW at least. W1-a,
  W1-b and W1-d keep `finit` unchanged.
- **Option B (no narrowing; a schema and engine change).** Keep `finit` and give the negative
  matcher an occurrence bound equal to the literal's count in the fingerprinted sentence. Any added
  `finit` then FAILs. This needs a new rule-schema field and an engine change, so it is a design
  change.

Either option is a rule decision that needs the independent review and owner authorization of
sec. 6.3, like the rest of W1. The design should also add a lint clause: every fingerprinted
sentence, at `recorded_at`, must be classified PASS by its own rule through steps 1-6. That clause
is a strengthening, and it would have caught this defect.

**Expected outcomes.**

- Under the design as written, RT-D at T1' is FAIL: two `rule-negative-match` items, and 5 of the 7
  W1 lines PASS.
- RT-I7A at T1' with the rules in place has 10 lines PASS and 2 FAIL `rule-negative-match`. The
  "12 become PASS" does not hold.
- Item 7 cannot pass at a T1'-style `X` without a corrected W1-c.
- After either correction, the design's stated outcomes hold.

### 3.2 Priority 2: the seven failed SW2 sites

Sites: FULL:4895, 4905, 4919; ch18:164, 174, 188; papers/Main.md:332.

**Reproduced** with the writer's mutation (last token deleted at H, segments E..H `hp` and H..X
unledgered), for these 7 sites only (`scripts/rs_sw2.py`, `out/sw2probe.json`). At the unmutated H
each site already carries exactly one FAIL: obligation HP, `context-meaning-unverified`, segment
e837e3db..53c6601a. The mutant adds exactly one FAIL: obligation RET, `unauthorized-change`,
segment 53c6601a..X. No item disappears.

**Classification: a design defect in SW2's expected outcome, over an existing evidence condition.
It is not an implementation defect.** These 7 sites are exactly the design's 7 E..H meaning-context
sites (sec. 4.4), which carry HP FAILs at H by the design's own rule until their context
adjudications exist. SW2's wording, "exactly one FAIL naming that site", ignores the HP items that
the design itself expects at H.

**Correct expectation for SW2:** each of the 584 sites gains exactly one new FAIL item naming it, of
obligation RET in segment H..X. The items naming it at the unmutated H, all of obligation HP in
segment E..H, are unchanged. The writer's delta predicate checks this for 584 of 584 sites. Once the
7 context adjudications exist, the strict reading holds as well. One improvement to that predicate
is recommended: compare items by `(obligation, class, segment, fingerprint)` rather than by class
name (O3).

### 3.3 Priority 3: count differences

| Difference | Reproduced | Correct per the design | Cause |
|---|---|---|---|
| 7 HP structure REVIEWs at H (design 3) | yes, `scripts/rs_struct.py`: from the design text, 6 LIST and 1 TABLE among the 584 E..H-unchanged sites have a context or structure change in E..H. They are FULL:706, FULL:708, ch02:76, ch02:78, Substratum.md:94, Substratum.md:253 and Main.md:741. Only 3 of the 7 are still unique at T1' | **7** | The rule (sec. 4.1, 4.3, 3.5) has no T1' condition. The reference population of sec. 14 ("unique at E, H and T1'") was built for the T1' context table and cannot apply to an E..H count at H. RT-H0 and RT-T0 should read 7 HP `context-structure-changed` |
| 215 region lines (design 203) | yes, `scripts/rs_regions.py`: with the site span excluding its LF, 203 lines; including it, 215. Site counts 383/197/4 are the same either way. The 12 extra lines come from 3 sites (Main.md:44 at E with D259; ch01:28 with D310; FULL:361 with D311), whose second splice starts at the site line's LF and inserts a paragraph | **215** | v1 sec. 4.3 defines the span as "line bytes plus its LF", and v5.1 carries v1 sec. 4.3 forward (sec. 3.4). The measurement scripts used a span without the LF. The LF-inclusive span is also the conservative one, because it catches a splice that removes the line break |
| RT-D `resid` 45 (design 17) | yes, `scripts/rs_rtd.py`: under item 7's profile set (which is also the tool's default for `terms` with `--base`), 45 lines carry a `resid` REVIEW, and on 45 of them `resid` is the only review hit evaluated. Under all review profiles (p0-core, p0-para, ledger-ext, ptr, count-grep, resid), 45 carry a `resid` hit and **17** carry no other review hit | both, under their definitions; RT-D should state **45** | The design's 17 is the sec. 8.2 review-load count (lines needing a record *only* because of `resid`). RT-D's command evaluates no p0 profile, so every one of the 45 is a `resid` REVIEW item in that run. RT-D should read: "45 `resid` lines REVIEW (17 of them hit by no other review profile)". Sec. 0.3 already has 45 / 17 correctly |
| W2-b context literal `\mathrm{SU}(3)` | yes: the source line is "(A1) is automatically satisfied: $\mathrm{SU}(3)$ is vector-like ...". The literal "SU(3)" does not occur | the implementation's | The design wrote the rendered form. A literal matcher must use the source bytes. Not a weakening |
| W1-b context "isotropy, sublattice structure, link content" (not the full list) | yes | acceptable; the design should state it | With the full six-item list as one context literal, V7c (one list word changed) gives REVIEW `unclassified` at step 1, not the specified `rule-fingerprint-mismatch`. Both are REVIEW, so no outcome is weakened. Only the REVIEW class differs. The design should say which literal is meant |
| register and infinity parameters (`splice_kinds`, `replaced_text_rewrite`, `match_keys`; image net of replaced text) | traced to P's frozen `edits_check.py`: lines 348-349 ("finiteness fails" key), 370 (old text read with A1 as finiteness), 377 (REG tokens new minus old), 379 (CAPS only for kinds ptr/consistency/handoff) | faithful to the original items 5 and 6; **a design gap** | Sec. 6.1 says a deny profile's "any match is FAIL" on added text, while sec. 11 rows 5 and 6 expect "PASS (P's `--static` recorded 0)". Only P's net-of-old semantics give both. The design must state those semantics (D6). The two regexes in `match_keys` and `replaced_text_rewrite` are retyped, not extracted. Sec. 6.1 allows retyped patterns only in reviewed rule files, so they move to a rule file or get an extractor (B-F2). The 30 line-level matches the writer reports should be listed in the landing record so that a reviewer can confirm each one is already in the replaced text |

### 3.4 Priority 4: simplified trust and review mechanics

Classification key:

- **B-L** blocks landing. The safeguard lives in the engine, and the amended plan pins the engine
  blob at `F` (sec. 16.7), so a safeguard added after landing needs a second landing before `F`.
- **B-F** blocks the freeze `F` or any acceptance use. It is records or configuration work and does
  not change the engine.
- **NB** does not block.

| # | Design safeguard | Implementation | Class |
|---|---|---|---|
| T1 | Root of trust: the configuration is admitted only if its sha256 is in `F`'s PREREG pin table (sec. 6.3 O5, 16.2) | `--config-sha256` from the command line. The caller chooses the root | **B-L** (B3) |
| T2 | `retirement.owner` equals the owner who designated `F`, as quoted in the designation record | not implemented | **B-L** (B3) |
| T3 | The configuration's own review and authorization | any JSON in the configuration's directory at the given revision with the review or authorization schema naming the configuration's blob is admitted. Together with T1-T2, a configuration plus two files beside it decide their own admission | **B-L** (B3) |
| T4 | `--freeze`/`F` absent | the `plan` field of delegated evidence is compared with `F` = None, so evidence with `plan: null` passes that check. Fail-open when no `F` is given | **B-L** (part of B2): with no `F`, delegated classes must be REVIEW or ERROR, never PASS |
| T5 | Widening reviews as records | separate review records of kind `widening`, admitted by the configuration. This matches "a `widening_review` record" in sec. 6.3. But `widening_review_ok` checks no owner authorization of the widening review and no verdict coverage of every item (only "every verdict accept", with at least one present) | **B-L** (small; part of B4's fix set): require item coverage and an authorization, as for ordinary reviews |
| T6 | Explanation object for every subject (sec. 5), part of the JSON Schema | REVIEW items carry class, rule, detail and `resolution_needed`. Sites and PASS hits have no explanation object. The schema check is a subset validator | **NB** for landing. Required before any record writing begins (sec. 6.3 writer evidence uses the REVIEW-mode explanation) and before `F` (acceptance requires validation against the full schema). Engine work, so fold it into the landing if possible |
| T7 | C's further commits "classified as X is" (sec. 13.1) | linear parentage only | **B-L** (B4): an unledgered change in a commit after `X` is otherwise never checked |
| T8 | Landing: diff M..L equals diff H..C after translation | enforced per path (only-C, only-M, neither, both). Equivalent path by path. A dropped execution change is labelled `landing-extra-change` | **NB**; a precise class name is recommended (O4) |
| T9 | Context adjudications | implemented; exercised only through the FAIL and REVIEW paths. No control shows a matching adjudication giving PASS (sec. 4.1 row 2) | **NB**; add the positive control (O5) |
| T10 | N1 (PIN_OK after `F`) | "`recorded_at` not an ancestor of `F`". With no `F` every PIN_OK is `pin-broken` (fail-closed) | **NB** |
| T11 | N2 (a reconciliation that changes a decision on `X`) | `record-invalid`, the candidate's items unchanged | **NB**; meets sec. 13.3 |
| T12 | `rule-stale` on older trees | not evaluated on ancestors of `recorded_at`. A candidate `X` (parent `H`) is never an ancestor of T1', so only E..H trees are exempt | **NB**; the design should state the scoping (D7) |
| T13 | Y8 | the runner was given a placeholder. Rerun here with the real synthetic engine hash: holds (section 6). Still to run in one CI job | **NB** |
| T14 | Delegated native classes (sec. 7.3: `sc42` native re-execution; `coverage-ledger` running `proof_census.py --json` in the clone; `tex` running `preserve_check.py` in a disposable clone at `X` that the tool creates, recording checker blob, command line, exit and result hash, sec. 7.2) | no clone or execution path exists. `rerun-equal/1` accepts a supplied JSON with `verbose_equal: true`, `fingerprint-regen/1` accepts a supplied census JSON, and `preserve-check-v1` accepts a supplied result file. Any supplier can write a PASS | **B-L** (B2) |
| T15 | `pdf` class: `candidate_commit`/`candidate_tree` equal `X`, and the result hash equals the uploaded artifact | not checked. `pdf-host-run.json` is parsed by the checker-result verifier | **B-L** (part of B2) |
| T16 | Rule-id reuse "never reused" | checked within the rule files of one run, not across superseded history | **NB** (O6) |

### 3.5 Priority 5: verified locally vs CI

**Verified locally here** (own copy; cost noted):

- Engine self-test: 83/83, twice, byte-identical result; identical to the writer's
  `engine-self-test-result.json`. Under 1 s.
- Synthetic controls: 36/36, twice; output identical to the writer's. About 0.5 s.
- A1 controls without the sweeps (88 controls; about 6.5 min per run): rerun at the final commit
  8c1e628a. Per control, the outcomes and actual values are identical to the writer's log, except
  RT-L2's predicted-main side-change list. The writer's log was produced at 6f1ff70f, and the
  predicted `M` now also carries `evidence/stage1-controls.json` and the later `synthetic_fixture.py`
  blob. The committed evidence file states the 6f1ff70f provenance correctly. REPORT.md presents
  the results as those of the final commit without that qualifier.
- Full A1 run with the sweeps and `--syn-engine` (Y8), about 26 min: section 6.
- Determinism: coverage at T1' (both segments), 1,257,733 bytes, sha256
  8dccb30e55e715ab1e1e38dd8fa64bfca2144e2366beecc591a6da459fe790a0. Identical in 4 runs across 3
  processes, with `-I` (random hash seed) and with `PYTHONHASHSEED=12345`. The size equals the
  writer's. The hash differs from the writer's because the result records the configuration's
  commit.
- CLI exit codes through the real interpreter: `--help` 64; unknown or missing argument 64 with
  stderr JSON and nothing written; non-empty `--out` 64; chain run 65 `CONFIG_UNREVIEWED`; wrong
  `--config-sha256` 65 `SOURCE_CHANGED`; missing script 2 (interpreter); `purity-lint` 0.
- Independent recounts: W1 sentences and negatives; SW2's 7 sites; structure REVIEWs; region lines;
  RT-D `resid` counts; indicators (ANAPH 23, LIST 49, TABLE 6, PARTIAL 521); site counts
  (197 / 4 / 215 + 168 moved / 113 HP); finding counts (HP 113 / 7 / 7, RET 19 / 5 / 3,
  replacement-text REVIEW 57 + 50 = 107 = 84 + 16 + 7).
- Placement: `tools/artifact_placement_check.py` OK. All new files are under `tools/` and
  `verification/audits/foundations/ledger-coverage-tool-20261123/`, consistent with sec. A.36 and
  design sec. 12.1. `py_compile` of every new module OK.

**Sampled or not run locally:** the release gate was not rerun. The writer reports the same 5
environmental failures on unchanged main as on the branch. I did not reproduce that.

**Only CI can verify** (proposed CI plan, one workflow on the exact head, dispatched only with owner
authorization):

1. Job `ledger-tool-controls`: `self-test`, `purity-lint --config`, the synthetic runner, and
   `a1_controls.py` including the sweeps (about 20 min; shard SW1 and SW2 by file with a matrix).
   Run twice and compare `result.json` bytes (sec. 16.7). Upload the structured results. The verdict
   reads exit statuses and the result files (sec. A.44).
2. Job `ledger-tool-delegation` (after B2): a full clone at `X` (no `--depth`, no alternates) under
   `--out`. Run `preserve_check.py --commit X --plan F --result-json` from `F`'s blob, the SC-42
   checker (plain and `-O`, `--verbose` and `--self-test`) and `proof_census.py --json`, all
   executed by the tool's own delegation path. Then `execution ... ` on the produced evidence, and
   RT-C to PASS.
3. Host-run evidence: the exact-head run and job records read from the API inside the job (classes
   `pdf` and `ci`) and written as structured files, with the PDF artifact hash.
4. Lean-dependent gate steps (`lean-axioms`, Mathlib) and the full release gate, including the
   steps that are undecidable in a shallow clone (`citation-roles`, `legacy-records`,
   `v3-receipts`, `v3-corpus`). Run on main and on the head, and compare step conclusions.
5. RT-L2 against a predicted `M` re-resolved at dispatch time.

### 3.6 Priority 6: configuration records and the harness

- **Unreviewed records are refused.** Confirmed through the real interpreter: ERROR
  `CONFIG_UNREVIEWED`, exit 65. Records named on the command line but not referenced by the
  configuration give `record-invalid` (code read; exercised by the engine O-controls and Z10).
- **The harness can be mistaken for a real run. This is a defect (B1).** The harness is reachable
  only in-process (`cli.run(harness=True)`); there is no CLI flag, which is good. But a
  harness-produced `result.json` is a normal result whose only mark is
  `config.admission = "control-harness: ..."`. The independent acceptance predicate
  `checker.accept()` does not read that field. Applied to the harness PASS result of RT-E with the
  pinned engine and configuration hashes, `accept()` returns **True**. Fix:
  - `accept()` requires `config.admission == "chain"`;
  - the schema makes `admission` required;
  - the harness writes a distinct top-level marker, or no `result.json` named as an acceptable
    result.
- **Drift is not silently ignored.** Confirmed at current main 4fb2c1ee (= `origin/main`):
  - H..M changes `.claude/settings.json` (added at 4fb2c1ee), `AGENTS.md` (sec. A.49, hunks at lines
    715 and 1524, away from D296's lines 37-38) and the trial workflow;
  - the tool reports `base-drift` FAIL for `AGENTS.md` and `side-change-unclassified` REVIEW for
    `.claude/settings.json`;
  - RT-L2 does not meet. Reproduced.

  This is an existing evidence condition, not a tool defect. Under sec. 13.4 it blocks the tool's
  landing until the owner decides: a reviewed reconciliation record for AGENTS.md, or a new base;
  and a reviewed side-change class for `.claude/settings.json`.

### 3.7 Other points

- **Engine purity (Z9).** The writer's Z9g (0 findings) holds for the value set the writer chose. I
  repeated it independently by `ast` and found no 7+-hex literal, no PR number, no count, and no A1
  path or pattern. However, `engine/execution.py:252` hard-codes the A1 edit-list semantics of P's
  `edits_check.py` (lines 718-735): edit kind `'guard-pin'`, `pin_note` values `'message'` and
  `'comment'`, and the piece filter (length >= 12, prefixes `'ok'`, `'in '`, `'#'`). It also reads
  `ledger['edits']`, which is not in the ledger interface of sec. 16.3. Z9 misses this because its
  value set leaves out the records the configuration references through its adapters (`ledger.json`,
  `edits.json`, `sitemap.json`, `rows.json`, `sites.json`). With them added, the engine's own lint
  reports `'guard-pin'`, `'comment'` and `'message'` at that line (`scripts/rs_z9companions.py`; the
  other 43 hits are control ids such as K1 and M1 that collide with row codes, which is allowlist
  noise). This is a defect against condition 9.1 (B5). The class name `item7-literal-match` in the
  engine is allowed by the design (sec. 9 class names). That one A1-specific item name reaches the
  engine's enumerations is a design point for the record (O7).
- **Control predicates weaker than their stated expectations (B6).**
  - RT-T is recorded "meets" with `passed = (exit != 0)` on RT-T0's run, while REPORT sec. 7 item 17
    says RT-T was not run.
  - RT-D is recorded "meets" on "no deny-match" alone, while 2 W1 lines FAIL and the expectation
    says W1 PASS.
  - The A1r-A11r controls test the lint and widening functions for truthiness, not an emitted FAIL
    `record-invalid`.
  - Several sec. 11 countercontrols check only the mutant direction. S11-3's evidence also lacks
    jobs, so it does not isolate `head_sha`.

  So the "88 of 91" overstates. By the stated expectations, at least RT-D, RT-T, RT-L2 and SW2
  do not meet. Y8 meets once the placeholder is replaced (section 6).
- **Fail-closed and exit codes:** as specified, apart from B1 and T4.
- **Committed evidence** `evidence/stage1-controls.json`: correctly labelled UNREVIEWED and states
  its tested commits. It inherits the overstatements of B6. Regenerate it at the final head after
  the corrections, or replace it with the landing record of sec. 12.1 (sec. A.28).

## 4. Blocking defects (numbered)

- **B1.** Fix the acceptance predicate so it cannot accept a control-harness result: require
  `config.admission == "chain"`, make the field required in the schema, and add a control (an
  X10-style case with a harness PASS result: non-acceptance).
- **B2.** Implement the delegation execution path of sec. 7.2:
  - a disposable full clone at exact `X` under `--out`;
  - checkers run from `F`'s blobs, recording checker blob, command line, exit and result hash;
  - `sc42` and `coverage-ledger` re-executed natively;
  - `tex` and `pdf` bound to `X` and the artifact hash.

  Self-reported evidence for a native class must never be accepted. With no `F`, delegated classes
  are never PASS (T4). The clone may run only in CI (sec. A.40), but the code path and its controls
  must exist and be tested there.
- **B3.** Implement the root of trust:
  - read `F`'s PREREG pin table, and admit the configuration only if its sha256 is listed;
  - check `retirement.owner` against the designation record of `F`;
  - read the configuration's own review and authorization only as `F` pins them, not from "any JSON
    beside it".

  `--config-sha256` may remain as an additional equality check.
- **B4.** Classify each commit after `X` in `C` path by path, as `X` is (sec. 13.1). Bring
  `widening_review_ok` to the full chain: item coverage and owner authorization (T5).
- **B5.** Move the guard-pin semantics (kind name, `pin_note` values, piece filter) into the A1
  ledger adapter or its `pin_rules`, through a declared interface field. Extend Z9's value set to
  every record the configuration references, adapter companions included, with the needed
  enumerations allowlisted.
- **B6.** Make every control predicate check its stated expectation:
  - RT-T reported as not run, not met;
  - RT-D checks the W1, W2 and GR.md:58 states and the `resid` count;
  - A1r-A11r run through the pipeline to `record-invalid`;
  - both directions where the design requires them.

  Regenerate REPORT and the evidence file at the final head.
- **B7 (owner decision, not a tool defect).** RT-L2 at current main: `AGENTS.md` base-drift and
  `.claude/settings.json` unclassified. The sequencing safeguard (sec. 13.4) must hold before
  landing.

**Design corrections required (v5.2), each with its expected-outcome change:**

- **D1.** W1-c negative (Option A or B, sec. 3.1), plus the lint clause that every fingerprinted
  sentence PASSes its own rule. Until then RT-D and RT-I7A at T1' have 2 FAIL `rule-negative-match`.
- **D2.** SW2 expectation as stated in sec. 3.2.
- **D3.** RT-H0 and RT-T0: 7 HP `context-structure-changed` (named sites); sec. 4.4's indicator
  table extended by FULL:706, ch02:76, Substratum.md:94 and :253.
- **D4.** Region lines 215 under the LF-inclusive span (sec. 0.3, 14); the measurement definition
  aligned with v1 sec. 4.3.
- **D5.** RT-D: 45 `resid` REVIEW lines (17 hit by no other review profile).
- **D6.** Register and infinity semantics: matches in a splice image net of the replaced text, with
  P's three parameters, stated and reviewed.
- **D7.** State the `rule-stale` scoping (T12).
- **D8.** State the W1-b and W2-b context literals as source-byte literals.

**Before `F` (B-F), not blocking landing:**

- B-F1: reviewed records for everything sec. 8.2 lists;
- B-F2: move the two retyped infinity regexes into a reviewed rule file or an extractor;
- B-F3: the full explanation object and schema (T6), if not folded into the landing;
- B-F4: the delegation contract frozen with the plan.

## 5. Optional improvements

- O1. Positive and negative example of W1-c should be the full fingerprinted sentence, not a
  fragment.
- O2. REPORT should state that the A1 logs were produced at 6f1ff70f.
- O3. SW predicates should compare items by `(obligation, class, segment, fingerprint)`.
- O4. A specific class for a landing that drops an execution change.
- O5. A context-adjudication PASS control (sec. 4.1 row 2).
- O6. Rule-id reuse checked across the supersedes history.
- O7. Record in the design that `item7-literal-match` is an engine enumeration.
- O8. The `near_splice` pin prefilter (20-character windows within 100 bytes of a splice) skips
  literals shorter than 20 characters. With `min_len` 20 from P this is lossless. State it as an
  invariant and add a control, so that a smaller `min_len` cannot silently skip pins.

## 6. Full A1 run (sweeps and Y8)

The full A1 run was made once at 8c1e628a with `--syn-engine 204a2d8b...d681`, the engine hash the
synthetic run records (about 26 min; sweeps 792 s). Result: 89 of 91 controls pass their predicates.
Two fail: RT-L2 (sec. 3.6) and SW2 (sec. 3.2). Every control's actual value equals the writer's
log, apart from RT-L2's predicted-main path list (provenance, sec. 3.5) and Y8.

- **SW1:** 697 of 697 sites give exactly one FAIL naming the site, and exactly one new FAIL against
  the unmutated tree (420 s).
- **SW2:** the strict predicate fails on exactly the 7 sites of sec. 3.2. The delta predicate holds
  for 584 of 584 sites.
- **Y8:** run with the synthetic engine hash instead of the placeholder. The A1 and synthetic
  results record the same engine blob, 204a2d8b09ca63983e42f4eec8db82d266a3dc56f0b8cf054770ddf4f7bed81e,
  so Y8 holds. The writer's "does not meet" was an artefact of the placeholder. The two results
  were recorded by separate processes on one host, not in one CI job as the design states, so the
  CI plan should still run both in one job.

By stated expectation rather than by predicate, the controls that do not meet at this head are
RT-D and RT-I7A's "becomes PASS" (W1-c, D1), RT-T (not run), RT-L2 (B7) and SW2 under its current
wording (D2).

## 7. Scripts and outputs

`scripts/`: `rs_git.py`, `rs_regions.py`, `rs_struct.py`, `rs_sw2.py`, `rs_w1.py`, `rs_rtd.py`,
`rs_purity.py`, `rs_z9companions.py`, `rs_determinism.py`, `rs_cmp.py`. They read git objects only,
use the engine read-only from the reviewer's copy, and write only under `review-stage1/out/`. Their
outputs are under `out/`. The copy of the object store (`repo/`) is not part of the manifest.
`MANIFEST.sha256` lists this file, the scripts and the small outputs.
