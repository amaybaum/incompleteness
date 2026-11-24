Independent review of DESIGN-v5.2 (ledger and terminology verification tool)

Verdict: REVISE

Reviewer: an independent, non-author session. It wrote none of the DESIGN-v1 to v5.2 text and none of the Stage 1 implementation. It earlier wrote review-v4, review-v5 and review-v5.1.

Limits kept:
- no repository, git or GitHub write;
- no workflow run;
- the Stage 1 worktree `coord2-impl-wt` was only read (HEAD 8c1e628a08272ad9414929fa8e003020e1cc2234, status clean).

To run the Stage 1 engine, I extracted a copy with `git archive 8c1e628a tools/ledger_coverage tools/ledger_coverage.py` into `review-v5.2/toolcopy/`. It is byte-identical to the worktree's files. All new files are under `D/review-v5.2/`. The scripts are mine, except where I quote the frozen P code (`edits_check.py`, verified blob) or drive the Stage 1 engine copy. I did not read or run `work-v52/`. Date 2026-11-23.

Goal link (sec. A.47): A1-EXIT (#1169). This review decides whether DESIGN-v5.2 meets the owner's decisions and pass conditions for the Stage 1 corrections. It adopts no rule, record or count, and authorizes nothing.

Inputs (sha256, verified first; all match)

- DESIGN-v5.2.md 195d1e288b1d6750c333b4707332868d351926793ad2b2a555d64e3bd78f4aeb
- CHANGES-v5.2.md eecb878295bfe43372800a658faf26236083850673bbafe096383c41aac8b6cb
- DESIGN-v5.1.md 0c4ff0e60331d0e9604ece0c997dec472b3f977bf24384676d74f850bff4a3fe
- review-stage1/review-stage1.md 007d4ada8c19cb3103073d80f75c9721d57c908f7cd8813a7b52c568449d4b6a
- coord2-records/DRIFT-FINAL-NOTES.md ca07a51456e3799fe3542c49ea80f0a728b883a5957aa3c6fb3a9b4d89869c81

Why REVISE

Most items are resolved and testable, and every figure I re-derived reproduces. Two of the owner's four blocking pass conditions are not met:

- Pass condition 2, register/infinity parity. Per-splice checking is not equivalent to P's per-edit checking in general. I constructed three cases (two two-step edits and one merged splice) in which P's per-edit check fails and the per-splice check passes. On the frozen A1 data the two units give identical results, but only because every splice equals one edit byte for byte and no two-step edit exists. The design neither states nor enforces that condition. The owner classed any such difference as a blocking design defect.
- Pass condition 4, freeze designation. The authority for `F`'s designation is a record inside `F`'s own tree. Whoever creates `F` writes that record, and a commit cannot contain an owner's designation of itself. Nothing makes the designation independently verifiable, so it is self-declared.

The other required corrections are bounded.

***

Pass condition 1: the W1 allowance (option B)

Resolved in substance. Sec. 6.2 step 3 grants the allowance only when all of the following hold:

- same file;
- same sentence sha256;
- same context sha256;
- one grant per fingerprint per tree.

Re-derived (`rv52_w1.py`, splitter v2 as I transcribed it):

- The W1-c sentence (ch19:198 and FULL:5270 at T1') is one sentence of 404 characters with exactly one `finit` match, case-sensitively and case-insensitively alike. No other negative literal matches.
- The other five W1 sentences match no negative literal.
- Each W1 sentence occurs once in its file. The two W1-c fingerprints share a sentence sha256 but differ in file.

Abuse attempts, on paper and against the real text:

| Attempt | Outcome under v5.2 | Holds? |
|---|---|---|
| Add a second finiteness word inside the sentence | sentence sha changes, so allowance 0 and FAIL; even with the same sha, the count rule gives FAIL (WB2) | yes |
| Replace "finite" with another finit word ("finitely"), keeping the count at 1 | sha changes, allowance 0, FAIL | yes |
| Copy the sentence to another paragraph in scope | context differs, FAIL (WB3) | yes |
| Copy the sentence to another file, mirror or chapter | the file check gives no allowance, FAIL; out of scope, REVIEW (WB4) | yes |
| Copy the sentence together with both neighbours (same text, same context) within the file | one fingerprint grants once, so the second copy FAILs; `max_instances` also gives `rule-overreach` | yes, but which copy FAILs is not defined (V5c) |
| Move the sentence together with both neighbours to another section of the same file | context sha unchanged, so the allowance still applies and the sentence PASSes | not covered by WB5, which moves the sentence alone. Whether "location" means the neighbours or the position must be stated (V5a, V5b) |
| Add a finiteness claim to a neighbouring sentence | W1-c's context changes, so W1-c FAILs; the new sentence is a `resid` or p0 hit | yes (stricter) |
| Lookalike characters ("fіnite" with a Cyrillic і) | sha changes; `finit` does not match, so step 4 gives REVIEW `rule-fingerprint-mismatch`; under item 7 with `--final` it is FAIL `final-unclassified` (`count-grep`) | yes, never PASS |
| Capitalized "Finiteness" added to the sentence | sha changes; the case-sensitive `finit` misses it, so REVIEW, and FAIL under item 7 `--final` | never PASS. The same gap exists for V7a-type mutants: W1 has no `Finit` literal while W2 does (optional O1) |
| Raise or move an allowance | widening (sec. 6.3) plus the lint rule that the allowance equals the exact count (WB10) | yes |

The allowance therefore cannot be transferred to other text or files, duplicated, or exploited through near-matches, because every near-match changes the sentence sha. The design does not define the fingerprint's `context_sha256`; it says only "the same neighbouring sentences". The location binding depends on that definition. Stage 1 computes sha256(previous sentence 0x00 next sentence) over the file's sentence list, with BOF and EOF as sentinels (`engine/rules.py:15`). The design must state the definition (V5a).

Pass condition 2: register and infinity parity (blocking, not met)

Measured (`rv52_parity.py`, which imports P's frozen `edits_check.py` with `-I` after verifying its blob hash):

- On the frozen data:
  - P's own `static_new` over P's `edits.json` gives infinity 0, register 0 and caps 0.
  - The per-splice computation of DESIGN-v5.2 sec. 6.1 (image against the H bytes it replaces) also gives 0 / 0 / 0, with P's `sentences()` splitter and with splitter v2 alike.
  - The reason is structural. All 399 splices have replaced bytes equal to their edit's `old` and an image equal to its `new`. The ledger has no splice that is not an edit. The only edits without a splice are D032 and D039, which are retained. No edit has `new_step2`.
- In general the two units can differ. These are constructed cases, run through P's own `static_new` against the per-splice rule:

| Case | Per-edit (P) | Per-splice (v5.2) |
|---|---|---|
| (a) a two-step edit: step 1 removes "now", step 2 re-adds it | register 1 (FAIL) | 0 (PASS) |
| (b) a two-step edit: step 1 adds "no longer", step 2 removes it | register 1 (FAIL) | 0 (PASS) |
| (c) one splice covering two edits: one deletes "now", the other adds it elsewhere | register 1 (FAIL) | 0 (PASS) |

The same non-compositionality affects the infinity multiset and `register-caps`. In addition, v5.2 does not say which sentence splitter `infinity` uses. P uses `sentences()`, which splits after `.`, `;`, `:` or `?` followed by whitespace. Splitter v2 does not split at `;` or `:`, and that changes which NEUTRAL spans exempt an INF match. Under the owner's pass condition this is a blocking design defect (V1).

Pass condition 3: S6 (met)

- Sec. 13.1 evaluates the composition for every ledgered conflict on every landing check. Sec. 13.3 makes a record's `l` only a prediction, checked against the composition. The landing passes for a path only if `L` equals the composition and, where a record exists, the composition equals `l`.
- With "the diff from `M` to `L` equals the diff from `H` to `C`", a landing that loses either the retirement's change or main's change is rejected.
- **The drift writer's probe, reproduced independently (`rv52_s6.py`, from git objects).**
  - Composing `M` = 8e9b8334's AGENTS.md with D296 at the translated offset (2332, an identity translation, with the old bytes unique at H and at M) gives blob 86d79863, which equals the drift records' `l`.
  - The probe's landing AGENTS.md is `X`'s blob 9f4fc3e8. It keeps D296 but loses M's inserted section, bytes 46677-47031.
  - Under v5.2: L ≠ composition gives FAIL `landing-conflict-unresolved`; the record's `l` ≠ composition makes the record `record-invalid` and inapplicable (R7). So the previously accepted landing is rejected.
- **Regression control.** N10 specifies the probe's shape. The owner requires a control that reproduces the probe itself, so N10 should be pinned to the probe's exact inputs (V8).

Pass condition 4: freeze designation (blocking, not met)

Sec. 6.3 admission step 2 reads "the owner's designation record of `F`" from `F`'s own tree, at a path the plan will fix. The record "names `F`'s parent, the pin table's path and the owner". This does not meet the condition, for three reasons:

- A commit cannot contain a record of its own designation, because its id is unknown when it is written. The record can only be a claim made by whoever created `F`, and the designation itself comes later, from the owner (sec. A.39 item 1).
- `--freeze F` is chosen by the caller. A caller can create a commit whose tree holds a designation record naming any owner, a pin table listing its own configuration, and a matching configuration. Steps 2-4 then hold.
- The quoted `comment_id` is never checked against its source.

So the source of authority is self-declared and not independently verifiable. Deferring the exact path to the plan is acceptable. Deferring the authority is not (V2).

The `pdf` and `ci` classes already show the pattern a fix can follow: authority read from the host inside the job, never from a caller-supplied file.

***

D1-D8 (Stage 1 review)

| Item | Status | Re-derived |
|---|---|---|
| D1 W1-c | resolved (option B), subject to V5 | W1-c finit count 1, 404 characters; the other W1 sentences have no negative matches |
| D2 SW2 | resolved in rule; the reference figure is wrong (V6) | **Rerun:** SW2 under v5.2's predicate, comparing items by `(obligation, class, segment, fingerprint)`, with the Stage 1 engine copy (`rv52_sw2.py`, 360 s). For each of the 584 sites, exactly one new item appears: RET `unauthorized-change`, segment H..X; no item present at the unmutated H is lost. The result is 584 of 584. A first evaluation of my script reported 584 violations: my test compared the segment with the full 40-hex id of H, but the engine prints the segment abbreviated as `53c6601a..<x>`. I corrected that test and re-evaluated the stored per-site results without re-running; the stored results show the expected single item for every site (`out52-sw2-eval.txt`). **Finding:** 14 sites, not 7, carry items at the unmutated H: the 7 meaning-context FAIL sites and the 7 structure-REVIEW sites (FULL:706, 708; ch02:76, 78; Main.md:741; Substratum.md:94, 253) |
| D3 7 HP structure REVIEWs | resolved | `rv52_struct.py`: E..H gives 7, the named sites (4 of them not unique at T1'); H..T1' gives 3 (FULL:708, ch02:78, Substratum.md:127) |
| D4 215 region lines | resolved | 215 with the LF-inclusive span; 203 without it; 383/197/4; 84 hit lines, 86 with `count-grep` |
| D5 RT-D 45 / 17 | resolved | 45 added-text lines with a `resid` hit, none of them a `ptr` or `count-grep` hit; 17 hit by no other review profile |
| D6 register and infinity | **not resolved** | see pass condition 2 (V1) |
| D7 `rule-stale` scoping | resolved | |
| D8 source-byte literals | resolved | |

B1-B6 (Stage 1 review)

| Item | Status |
|---|---|
| B1: acceptance reads admission and never accepts a harness result | resolved: the sec. 5 predicate, the required schema field, `control-result.json`, X11. Its trust still depends on pass condition 4 |
| B2: delegated checks run natively, with independently verified results | resolved for `X` (sec. 7.2). The tree being evaluated also includes `C` when `C` ≠ `X` (sec. 13.1 says a delegated path "is checked by its class at `C`"), but 7.2 names only a clone at `X` (V7) |
| B3: trust root tied to `F` and its pin table | partly resolved: tied to `F`'s pin table, but `F`'s designation is self-declared (V2) |
| B4: later commits classified file by file; reviewed, owner-authorized widening | resolved (sec. 13.1 `C`; sec. 6.3 widening review; R16, R17, A12r) |
| B5: engine free of project-specific values | resolved (Z9 over the adapter companions; `guard_pins` in the ledger interface; Z9h) |
| B6: summaries distinguish PASS, FAIL, SKIP and NOT RUN; predicates equal expectations | resolved (sec. 10.4) |

S2-S7 (as the owner restated them)

| Item | Status |
|---|---|
| S2: reconciling a file the retirement also modifies is permitted when every required check passes | resolved (sec. 13.3; N2 runs op C with and without the records; N3) |
| S3: classes bound to exact file hashes | **partly resolved.** Pinned paths must match blob and path (R18), but "a declared prefix class for paths the tool itself lands" is exempt from hash binding. Any later change under those prefixes on `M` stays classified (V3) |
| S4: supersedes chains for every applicable record type | resolved (sec. 6.3 lint, all kinds; S4a) |
| S5: every required reconciliation check actually executed | **partly resolved.** Sec. 13.3 makes the tool evaluate R1-R13 itself, but only R13, R1, R9, R2, R4 and R7 have controls (N4-N9). The text "Each condition has its own control (N4-N9)" is not accurate (V4) |
| S6: landing composition always checked | resolved (pass condition 3) |
| S7: duplicate class detected, meaning unchanged | resolved for the design (Z11: a duplicate id is ERROR). Removing the duplicate from the Stage 1 draft record is a records change outside the design |

Deferred optional points (O2, O4, O6, O7, O8)

I found no safety dependency that requires adopting any of them now:

- O6 (id reuse across history): records are admitted by blob hash at `F`, so a reused id cannot change what is accepted.
- O8 (the pin prefilter's `min_len`): it is lossless at A1's `min_len` of 20, and changing it is a configuration change that counts as widening.

Both remain recommended.

***

Required corrections

V1. Register/infinity parity (blocking).
- Define items 5 and 6 on P's unit. For every `edits.json` entry frozen at `F`, evaluate its `(old, new)` pair and, if present, its `(old_step2, new_step2)` pair, exactly as P's `static_new` does: P's `sentences()` splitter for `infinity`; CAPS restricted by the edit's own `kind`; the rewrite and key rule as in P.
- Optionally also evaluate per splice, and FAIL if either unit flags.
- Alternatively, keep the per-splice unit only behind a fail-closed precondition checked in the integrity stage, with ERROR otherwise: every splice maps to exactly one edit, its replaced bytes equal the edit's `old`, its image equals the edit's `new`, and no edit has a step 2.
- Add the constructed cases (a)-(c) as controls, each with expected FAIL.
- State the measured A1 result: 0 / 0 / 0 under both units, and 399 of 399 splices byte-identical to their edits.

V2. Freeze designation (blocking). Define the authority for `F` outside the caller's control and outside `F`'s own tree, and make it independently verifiable. For example:
- `F`'s designation is the owner's host comment that quotes `F`'s full 40-hex id;
- the tool reads it from the host API inside the CI job (sec. A.44) and checks author login, comment id and quoted id;
- the owner login comes from a source the caller cannot choose (for example the repository's own records on `main`, or host permission data), not from the configuration or from `F`'s tree;
- local runs cannot reach `"chain"` admission.

Add controls:
- a designation record in `F`'s tree with no matching host comment: refused;
- a comment by another account: refused;
- a comment quoting another commit: refused;
- a caller-built `F` whose pin table lists its own configuration: refused.

The plan may still fix the record's path.

V3. S3: bind the tool-landing prefix class to exact hashes. For example, pin the landing commit's tree entries (each path with its blob) or the subtree ids, so that any later blob under the prefix on `M` gives `side-change-unclassified`. Add a control.

V4. S5: add one control per reconciliation condition that lacks one: R3, R5, R6, R8, R10, R11, R12. Correct the sentence "Each condition has its own control (N4-N9)".

V5. W1 allowance precision:
- (a) Define the fingerprint `context_sha256` exactly: which neighbours, whether they cross a paragraph boundary, the sentinels and the byte encoding.
- (b) State what "location" means. Either it is defined by the neighbours, so that a move of the sentence together with both neighbours keeps the allowance, with a control showing this; or it is bound to position, with a control showing the move FAILs.
- (c) Make the one-grant rule deterministic (for example, the first matching sentence in file order receives the grant), so that the FAIL always falls on the same copy.

V6. SW2's reference: 14 sites carry HP items at the unmutated H, the 7 meaning-context FAILs and the 7 structure REVIEWs. Replace "the 7 sites with an HP item at H" with that. Record the measured 584/584 under the tuple predicate, noting that this review ran it with the Stage 1 engine.

V7. B2: state that delegated and native classes are executed on every tree whose delegated paths are evaluated: a clone at `C` as well when `C` ≠ `X`, with the same recording and independent re-derivation.

V8. S6 regression control: pin N10 to the probe's exact inputs. Those are:
- `M` = 8e9b83341cf5bc7fd9fb260892d0385fc9bfab4d;
- `X` = T1' (14ac71b4);
- a landing whose AGENTS.md is `X`'s blob 9f4fc3e8;
- a record whose `l` names that blob;
- the composed blob 86d79863 as the reference.

Expect FAIL `landing-conflict-unresolved` and `record-invalid`. N11 is the positive direction at the same inputs.

Optional

- O1. Add `Finit` (or a case-insensitive form) to W1's negatives, or state literal case semantics explicitly, so that a capitalized finiteness edit is a `rule-negative-match` FAIL rather than REVIEW.
- O2. Keep O6 and O8 on the deferred list. Neither is a safety dependency today.

Not verified

- No implementation of v5.2 exists. All controls were checked against the specified rules, not run, except SW2, which I ran with the Stage 1 engine.
- The owner decisions S1-D1 to S1-D3 and the pass conditions reached me through the coordinator, without comment ids.
- The `register-caps` and `infinity` parity was measured with P's own functions and my transcription of v5.2's per-splice rule, not with the Stage 1 implementation of it.
- The 30 line-level matches the implementation reports were not recounted.

Files (D/review-v5.2/; MANIFEST.sha256 covers them, except `toolcopy/` and `sw2out/`)

- Scripts: `rv52_w1.py`, `rv52_struct.py`, `rv52_parity.py`, `rv52_s6.py` and `rv52_sw2.py`.
- Helpers copied unchanged from my earlier reviews: `rv5_rules.py`, `rv_git.py`, `rv_prof.py`, `rv_hp.py`, `rv_ctx_v4.py`, `rv_b3_v4.py`, `rv5_resid_copy.py`.
- `data/`: the blobs read from E, H and P.
- Outputs: `out52-w1.txt`, `out52-struct.txt`, `out52-parity.txt`, `out52-s6.txt`, `out52-b3.txt`, `out52-sw2.json`, `out52-sw2.log`, `out52-sw2-eval.txt`.
- `diff-v51-v52.txt`.
- `toolcopy/` and `sw2out/` are not listed in the manifest. `toolcopy/` is a `git archive` of 8c1e628a (`tools/ledger_coverage`, `tools/ledger_coverage.py`), byte-identical to the worktree, and can be recreated with that command. `sw2out/` is the engine's own scratch output.
