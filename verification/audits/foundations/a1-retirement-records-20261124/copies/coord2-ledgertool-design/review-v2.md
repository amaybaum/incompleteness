Independent read-only review: commit-independent A1-EXIT ledger coverage tool, design (sha256 447d23f362bbe265af61aaf19dc02928ecb06bc0e3393ac188087a670bc83e04)

Verdict: REVISE.

The design is sound in its core. The figures it relies on reproduce from git objects. It fails closed, it never resolves a site by proximity or similarity, and it keeps the frozen tool unmodified. It does not yet reflect the owner's Q1, Q3 and Q4 decisions, and reflects Q2 only in part. Reproduction also found a coverage hole that the RT-T figures hide: 24 of the 113 sites changed between E and H are rewritten again by H..T1' splices, and the design does not track them. The changes below are needed before S0 (preregistration).

Scope and method. I read the frozen ledger_check.py (blob 223a1d71d9cf77262a4e50c6c93bf2df15c0abbf, 561 lines) and the frozen rows.json and sitemap.json. I worked only in a disposable scratch directory outside the checkout, using git show and git cat-file, and reproduced every figure below with my own scripts. The checkout was left unmodified (git status --porcelain empty). I made no fetch with depth and created no ref, commit, push, dispatch or GitHub post. The two branches named in the brief were fetched by name.

Objects checked. E, H, P and T1' resolve. E is an ancestor of H. T1' is a single-parent child of H. The record directory R has tree b05efdca935a42b9c94ef1748c964696bf58fcd9 at 9882df8f, H, T1' and the current main 413b0bb88f39cad901befcf4684355c7ee39480b. R is not present in E itself: E is only the pin that rows.json and sitemap.json record, so the design must never read R at E (it does not).

Findings by review question

Question 1. Site identity at the pin. Confirmed.

- The frozen map has 697 sites: 435 exact, 83 anchor, 32 splice, 16 fuzzy, 109 extra, 11 new, 11 p2-census. None has a null line, no two share a (file, line) key, and no site line is blank.
- All 697 site lines are unique as whole lines in their file at E. All 135 override anchors are substrings of their pin lines, and all 135 override keys are map sites.
- Two anchors occur twice in their file: FULL:4927 (copy at 4827) and ch18-beyond:196 (copy at 96), as the design states.
- Every new_site_rules read entry (11 in all) has a unique pin line, still matches its rule, and is itself a map site. The converted read set is therefore redundant with site coverage at the pin. It is not harmful.
- No corpus file at E contains CR.
- Residual limitation: byte-exact anchors identify the line the frozen map chose. They do not identify the Phase-0 quote. For the 16 fuzzy and 83 anchor relocations, whether that line was the right one rests on the ledger's own review, not on this tool. Op A shows only that the map is what the frozen build() produces.
- One site lacks a non-blank neighbour on one side. The context hash needs a defined sentinel for a missing neighbour, and the design does not give one.

Question 2. Adjudicating the 113 E..H changes without weakening coverage. Possible, but not as designed.

- 113 site lines do not survive as whole lines from E to H. 584 do (536 at the same line, 48 moved).
- I walked the first-parent chain E..H; six commits change the corpus. Each of the 113 breaks at exactly one first-parent merge:
- 0cd5d5b (#1470): 15
- a1f3828 (#1473): 15
- 0ba358c (#1474): 23
- 4de2eab (#1472): 12
- 7f28886 (#1475): 48
- #1494 (53c6601) breaks none of them. The design's attribution list, which includes #1494, is imprecise.
- Every break is a replace hunk and none is whitespace-only.
- Two sites (Main.md:224 and Main.md:732) have two-step provenance: changed by #1473, then again by #1474.
- Provenance can therefore be reconstructed against git history at per-site, per-commit granularity.
- Coverage gap. Under sec. 4.4 these 113 sites stay unresolved and are carried forward. The H..T1' segment then does not track them at all. Of the 113, 24 have an H image, unique in its file, that H..T1' splices overlap (24 distinct splices).
- So RT-T's "0 unauthorized site changes in H..T1'" is vacuous for these sites. The retirement's rewrites of 24 historical sites appear nowhere in the site accounting.
- Sec. 4.6 resolves a site to a to_region_sha256 but does not say that the site then resumes tracking. Unless it does, adjudication would close the finding and lose coverage of later segments.

Question 3. The T1' figures reconcile with P's ledger.json. Confirmed.

- ledger.json: schema "a1exit deletion exact-edit ledger v2", base H, edits_sha256 528f146d... (matches edits.json at P).
- 399 splices with unique ids. Every old_sha256 matches H's bytes and every new_sha256 matches its new text, and no two splices overlap.
- 44 ledgered files, 23 of them corpus files. All 23 corpus files of T1' equal H plus their splices byte for byte. No unledgered corpus file changes between H and T1', and no corpus file is added or removed.
- Of the 584 sites resolved at H: 383 unchanged (215 at the same line, 168 moved; every moved one agrees by offset translation and by unique whole-line search), 197 authorized replacements and 4 authorized removals. That is 584 in total.
- The 4 removals are FULL:706, FULL:6502, ch02-substratum:76 and glossary:11, keyed at E.
- Each of the 197 replacement regions occurs exactly once in T1'. In none of them does the pin line survive. No region grew when extended to whole lines, and no splice touches two sites.
- 299 splices are in corpus files: 243 touch a site and 56 touch none.
- Hit lines: 595 at E (all held), 602 at H (110 unheld), 496 at T1' (116 unheld).
- The 116 break down as 93 identical to an unheld line at H, 16 inside splices on lines already unheld at H, and 7 new.
- The 7 new hits sit on non-site lines in the images of D237, D238, D241, D242, D246, D247 and D388, as the design states.
- One of the 16 (Substratum.md:268) lies at D029, a pure deletion with an empty image. The attribution "inside a splice image" is undefined for empty images and must be defined.
- Outside B's scope but worth recording: one non-corpus ledgered file, verification/coverage/LEDGER.json, differs at T1' from its expected_sha256 in ledger.json (T1' 8cc2b50b..., expected 8b19841b...). The design's conformance claim is correctly limited to corpus files. Its output must say that a HOLDS covers nothing outside the corpus.
- The ledger field retained_unchanged (D032, D039, ids in edits.json with no splice) is not mentioned in the design. The parser must state how it treats that field.

Frozen tool, reproduced with my own replay harness:

- At E: digest, rebuild and render equal; 0 CK errors; extended scan 0; self_test true.
- At H: 32 errors (14 CKa, 11 CK3, 7 CK4); extended 8; rebuild has 707 sites.
- At T1': 154 errors (55 CKa, 52 CK3, 43 CK4, 3 CK7, 1 CK5); extended 30; rebuild has 739 sites.
- main('check') raises TypeError at line 523 on both trees. At H the message is NoneType vs int; at T1' it is int vs NoneType. The cause is a None in the line or the row position, not only in the row.
- The frozen self_test also returns true at H and T1', which confirms that it does not discriminate away from the pin.

Question 4. Can the mutation tests tell a harmless shift from an unauthorized semantic change? Only for changes to the site's own bytes.

- U2, U3 and RT-T's 168 moved sites show that a pure shift passes. U4, U9 and the "finite" deletion mutant show that a byte change fails.
- The matrix has no case where meaning changes while the site bytes stay identical: context edits, reordering, moving a paragraph into a different section, or negating a neighbouring line. All of these pass as moved or unchanged. Under the owner's Q3 decision, some of them must fail.
- At T1', 52 of the 383 unchanged sites have context that differs from the pin. The design would report them and fail none.
- The meaning mutant is a single site. One site does not show that every site is wired. Systematic per-site mutation is cheap and belongs in CI.

Question 5. Schema, exit codes and failure conditions. Not complete or deterministic as written.

- Exit 2 with --out refused cannot write result.json, which contradicts "exit status and result.json always agree".
- The precedence between exit codes is unspecified when several conditions hold.
- counts mixes site statuses and finding classes under one key space, and some names collide (for example unauthorized-change).
- findings are said to be sorted by (file, line, site_id), but findings have no file or line field.
- The fingerprint serialization (field order, separator, encoding of null) is unspecified. For unauthorized-edit, the subject is a difflib range, so the fingerprint depends on a diagnostic algorithm.
- hits carries no segment index, although 4.7 scans "TO".
- repo_head varies with the checkout and is not an input of the verdict.
- JSON output form (key order, separators, ASCII escaping, final LF) is unspecified, so byte determinism is not guaranteed.
- No status or field records pin_count, ordinal, the pin and current context hashes, a context-required flag, or adjudication provenance.
- Two boundary cases are undefined: the overlap rule at a zero-length splice on a line boundary, and the last line of a file with no terminating LF.
- What makes an adjudication stale is undefined when an adjudication file names segments outside the chain.

Required changes

Q1 (historical provenance):

- Delete the reconstructed-ledger alternative from sec. 13 and wherever else it is implied. Sec. 13 Q1 becomes a stated requirement, not a question.
- Define a distinct finding class, historical-provenance, for site changes in unledgered segments that precede the retirement base. Report it, count it and list it separately from every finding of the retirement segment H..T1'. RT-H and RT-T must state their rules per segment, so that no E..H change is counted or described as part of the A1 retirement.
- Correct the RT-H attribution: the 113 come from #1470, #1472, #1473, #1474 and #1475, not #1494.
- Extend the site adjudication schema with git provenance, and have the tool verify it from objects.
- Fields to add: for each step, the introducing first-parent commit and its parent; the bytes hash of the site's region before and after that step; and the step's position in the chain.
- Checks the tool performs: the before-region occurs exactly once at the parent; the after-region occurs exactly once at the commit; the region is byte-identical across every other corpus-changing commit in the segment; and the chain of steps composes from the pin line to to_region_sha256 at TO.
- Multi-step provenance (Main.md:224 and Main.md:732) must be expressible.
- If any check fails, or a step cannot be attributed to a single commit, the site stays unresolved: fail closed.
- The adjudication carries the frozen row, code and owner, and the tool checks that they equal the carried values. An adjudication can never change them (sec. 1 non-goal).
- An adjudicated site resumes tracking from its verified to_region in every later segment. Its later rewrites by authorized splices are then reported as authorized-replacement or authorized-removal, and are reported as unauthorized otherwise.
- Until adjudication exists, B must report for each carried unresolved site whether later-segment splices or changes touch its diagnostic image. This is a diagnostic, not a pass. RT-T must state the count (24 at T1' by my reproduction).

Q2 (semantic classification of new hits):

- A hit in replacement text is never held by provenance alone.
- Add a status or class new-pattern-in-replacement. It applies to every pattern name present in an authorized replacement image and absent from the FROM region, whether or not the line lies inside a site region.
- By my reproduction this covers the 7 non-site hits plus 46 lines inside site replacement regions that gain a pattern name absent at the site's H line: core:P8 38, ext:X5 5, core:P3 3, para:P8 2, para:P9 2, para:P3 1. The design currently marks those 46 held, with no classification.
- Each such hit fails until an individual classification record binds it. The record binds file, line_sha256 (required to be unique in TO), splice id, patterns and a semantic classification field (which qualification is visible, with reason, reviewer and owner record).
- The record states that it classifies meaning, and that splice provenance is recorded separately. Whether the 46 in-site cases need the same treatment as the 7 should be confirmed with the owner. The principle of the Q2 decision covers them, and the design must not silently hold them.

Q3 (context):

- Replace sec. 4.5 and delete sec. 13 Q3.
- Preregister at S0 a rule that marks a site context_required at the pin, decided before any outcome is seen. Context is required in either of two cases:
- for identity, when pin_count is above 1 or the site's current text is not unique in a later tree;
- for meaning, by stated criteria (for example a table row or list item, a line beginning with an anaphoric reference, a site whose Phase-0 quote is only part of its line, or one marked by a reviewed record).
- A context change on a context_required site is a finding. On any other site it is reported with the before and after hashes and permitted only when identity is verified and the site bytes are identical.
- Context is computed at the pin and at TO with a defined sentinel for a missing neighbour.
- RT-T must state how many of the 52 context changes fail under the rule.

Q4 (placement):

- Place the executable tool, its JSON Schema and its self-test fixtures under tools/.
- Place adjudication and classification records, and the landing record with commands and counts, in a separate audit directory under verification/audits/ (sec. A.36). The design must not propose verification/audits/foundations/ for the code.
- State that the tool reads those records from git objects, which export-ignore does not affect.
- Delete the placement half of sec. 13 Q4. The question of whether B should ever cover non-manuscript files may stay open.

Mutation tests:

- Add context-only mutants: negate or replace the neighbouring line of a context_required site, which must fail; do the same next to a non-required site, which must hold with context_changed true.
- Add a swap of two site paragraphs, and a move of a site line to a distant section of the same file. Both must behave per the Q3 rule.
- Add one test each for an empty-image splice on a site line, a multi-line splice (33 exist in P), a zero-length insertion at a line boundary, and a last line without LF.
- Add an authorized splice that makes a replacement region non-unique in TO; it must fail at the next search.
- Add a historical-provenance adjudication whose named commit is wrong; it must fail closed.
- Add an adjudicated site later rewritten by an unauthorized change; it must fail.
- In CI, add a per-site sweep: for each of the 697 sites at E, and for each of the 584 at H, a one-token deletion yields exactly one finding, naming that site_id. Run each mutant in both directions.

Schema, exit codes and failure conditions:

- Fix exit precedence as 2, 3, 4, 1, 0 in evaluation order (usage, then integrity, then controls, then findings).
- When --out is refused, write nothing, exit 2, and emit one JSON object with the same schema id on stderr; state that this is the only case without result.json.
- Wrap every call into the frozen code in op A so that any exception becomes a structured error, with its class and message recorded, never a traceback. State that the frozen main() is never called, so the line-523 TypeError cannot be reached. RT-A' already shows the pin-mismatch path is a structured exit 3.
- Split counts into site_counts, finding_counts and hit_counts.
- Give findings explicit file and line where applicable, and sort them by (class, subject, segment, fingerprint).
- Define the fingerprint as the SHA-256 of canonical JSON (sorted keys, no whitespace, UTF-8) over fields that do not depend on difflib. For unauthorized-edit, use the expected and actual file hashes and the segment, and keep difflib ranges as diagnostics only.
- Add a segment index to hits, or state that hits are scanned at the candidate only, and say how pre_existing is computed at the prior endpoint.
- Remove repo_head, or exclude it from the determinism claim.
- Fix the output form: sorted keys, indent 1, ensure_ascii true, final LF.
- Add the missing site fields: pin_count, ordinal, pin_context_sha256, current_context_sha256, context_required, provenance (adjudication id or null).
- Define overlap as a splice with start below the site's end and end above its start, with a zero-length splice at an interior offset counted as overlapping; a hit line is "in a splice image" when it contains the splice's TO offset, including empty images.
- State how retained_unchanged and the other unread ledger fields are treated.
- State in result.json the files the run covers, so that a HOLDS cannot be read as tree-wide conformance.
- An adjudication naming a segment outside the chain is reported as out-of-scope, not stale, and does not count as a finding.

Residual limitations (after the changes above)

- A HOLDS establishes coverage only. It does not establish that a replacement keeps the finite-only, conditional or open qualification. It also does not establish that the fuzzy and anchor relocations of the frozen map chose the right line at the pin. Both stay with the ledger's and the retirement plan's reviews.
- Coverage is defined by sites plus the frozen pattern sets. An edit in an unledgered segment that removes a qualifying sentence matching no pattern and adjacent to no context_required site is not detected.
- The context_required criterion is a preregistered heuristic. It can miss meaning dependencies outside it, which is why per-site review of context_changed reports remains necessary.
- Python regex behaviour is assumed stable across the versions used. The patterns are read from the record, and S3's two-version check should be kept.

Whether the design reflects the owner's decisions

- Q1: no. It offers a retrospective ledger, has no git-provenance verification, has no distinct class kept out of the retirement accounting, misattributes #1494, and does not resume tracking after adjudication.
- Q2: in part. The 7 hits fail closed, but the classification records are not semantic or splice-bound, and 46 new in-site hits are held by provenance alone.
- Q3: no. Context changes are report-only.
- Q4: no. Placement is left open, with the audit directory proposed for the code.
- Pin mismatch as a structured error: yes for op A (RT-A' exit 3); it should also state the exception wrapping above.
- Not an A1-retirement gate, landing only after the retirement by a separate review and merge decision: yes (sec. 12).

Goal link (sec. A.47): supporting verification tooling for the A1-EXIT ledger record. This review decides whether the design is ready for preregistration, and no scientific question.

Addendum: scope extension

After the review above was written, a message from the coordinating session (session_013T6pfKuv5mi3MXtKjH2tZb) relayed an extension of scope from the owner. I did not verify it against an owner record. It asks that false-positive discrimination be built into the same tool, and that the current text and a forthcoming revision be judged against eight further requirements. No revised text had arrived when this addendum was written, so only the current text is assessed. The verdict, REVISE, covers both. A revision needs its own read before it can be accepted.

How the current text measures against the extended requirements:

- Content-based anchoring that tolerates line movement: met for manuscript sites (sec. 4.2 to 4.4; 168 moved sites at T1' resolve). For hits it is not met. Hit adjudications are keyed by line_sha256 with no uniqueness requirement and no provenance.
- Provenance-aware separation of authorized from unauthorized edits: met for ledgered segments. It is not met for unledgered history (see the Q1 required changes and the 24-site gap).
- Context-aware classification of legitimate terminology: absent. The text has only held, unmapped-hit and exact-fingerprint adjudication. Both of the owner's examples are present at T1'. "the six structural properties developed in Chapter 5 (isotropy, sublattice structure, ...)" is at ch09-universality:137, with a parallel at SM.md:1394. The appendix B anomaly condition "(A1)" is at appendix-b-derivations:235 and 246.
- The retirement plan's edits_check.py at P handles these with special-case string exceptions. One is a RESIDUAL_ALLOW list keyed by (file, substring). Another is a blanket line.replace('(A1)', '') before the residual scan. A third is an exact-phrase list for "six". Under the blanket strip, any line in an allow-listed file that contains the allow substring and "(A1)" is accepted whatever the "(A1)" refers to. That is the masking hazard a generalized rule mechanism must remove.
- Three-state result (PASS, REVIEW REQUIRED, FAIL), where an unresolved review blocks acceptance: absent. Sec. 5 has HOLDS, FAILS, ERROR and VOID.
- Reviewed classification rules that recognize a verified false positive automatically: absent. Adjudications match single fingerprints only, so the same legitimate text at a new location, or in a mirror, is a fresh finding.
- Adversarial tests showing that legitimate changes pass and genuine violations fail: partial (sec. 8). The false-positive dimension has none.
- Auditable, machine-readable explanation for every classification: partial. held_by and attribution exist, but there is no per-item record of the rule, the evidence and the reasoning chain.
- One framework covering the ledger, replacement verification, terminology scans and pin verification: not met. Sec. 1 excludes non-manuscript files, and the edits_check --commit and --pins modes are not modelled.

Further required changes:

- Define one evaluation pipeline: integrity, then identity, then provenance, then classification, then verdict. The ledger sites, splice replacements, terminology scans (frozen pattern sets plus the retirement's residual-pointer and count patterns) and pin targets (the PINS literals of guards_check.py and edits_check.py) are each a "subject kind" in it, not a separate tool.
- Each subject kind states its own anchor and context rule. A pin target is anchored by file and exact literal with a required occurrence count at a named commit. It is not a tool mode that assumes an unexecuted tree.
- Results are three-state.
- FAIL: an integrity error, an unauthorized change, a rule match whose explicit negative condition also matches, or a refuted classification.
- REVIEW REQUIRED: any subject that no reviewed rule or record resolves, including every new pattern hit in replacement text (Q2) and every context change on a context_required site (Q3).
- PASS: only when no subject is in either other state.
- REVIEW REQUIRED takes its own exit code. It blocks acceptance exactly as FAIL does, and no flag or warning converts it.
- Classification rules are reviewed records under the audit directory (Q4), never code constants.
- Each rule binds four things: a subject kind; a positive matcher; a mandatory context matcher (for example, for "(A1)" in appendix B: the line matches the anomaly-condition form, with the SU(3) or anomaly vocabulary within the same line or its neighbours); and a mandatory negative matcher that must not match (for example the posit's own wording: "Finiteness", "configuration space", "finite S").
- Each rule also records a scope (files, or mirrors named explicitly), its reviewer and owner record, and at least one recorded positive and one recorded negative example.
- A rule may never match by deleting text from the line before testing.
- A rule matching a subject its negative matcher also matches yields FAIL, not PASS.
- A rule with no recorded negative example is invalid (exit 3).
- Rule adoption follows sec. A.29's hard-to-vary test in miniature. The rule is written before the run that uses it. Its examples become controls. A rule that would accept its own negative examples, or that a later edit to the rule text could widen without review, is rejected.
- Every subject carries an explanation object: the subject id and kind; the anchor and its hashes; the provenance chain (segment, splice ids, or adjudication and commit steps); the rule id and rule blob hash that classified it, or null; which matchers matched; the resulting state; and, for REVIEW REQUIRED, the decision a reviewer must record to resolve it. The explanation is part of result.json and its JSON Schema.
- Adversarial tests for false positives:
- the two owner examples pass under their rules;
- the same tokens used as a genuine posit reference fail. For example, insert "**(A1) Finiteness.** The configuration space is finite." into appendix B; or write "the six structural properties of the substratum, including finiteness".
- a legitimate example copied into a file outside the rule's scope is REVIEW REQUIRED;
- a rule widened by one alternation is caught by its own negative examples;
- each case runs in both directions.
- Model the edits_check --commit and --pins checks as subject kinds evaluated against an executed tree at a named commit, with the expected literal counts stated per commit. The plan's assumption that the checks run on a pre-execution tree is then a declared input, not a mode.

Residual limitation of the extension: rules generalize from reviewed examples and can still miss uses that their matchers do not anticipate. The negative-example requirement and the REVIEW REQUIRED default bound this risk but do not remove it, and a PASS on terminology remains a coverage statement, not a semantic one.

Addendum 2: integration roles and landing order

A second message from the same coordinating session relayed a further owner requirement, which I also did not verify against an owner record. The tool would now land on main before the A1 retirement, and the retirement plan would be amended so that every check passes as written with this tool. The design must distinguish and verify four trees: the scientific base H, the current integration base on main, the candidate retirement tree, and the landing merge tree. No revised text had arrived when this addendum was written.

Conflict with the earlier decision. This reverses an owner decision given in the original brief: the tool "is not an A1-retirement gate and lands only after the retirement lands". Both decisions cannot govern at once. The change needs a recorded owner decision, quoted with author and time (sec. A.42 item 7, sec. A.45 rule 3), before a design built on it is accepted. Sec. 12 of the design must then be rewritten, because a tool the retirement's checks depend on is a retirement gate.

Hazard in "every check passes as written with this tool": amending the retirement plan so that its checks pass with a new tool must not weaken any check's decision rule (sec. A.29: preregister the rule, not the outcome). Required:

- every amended check maps to the tool subject kind and rule that replaces it;
- for each, a countercontrol shows the tool fails on a mutant that the original check failed on;
- no check is turned green by reclassifying a finding the original check reported.

Measured state (read-only, from git objects):

- Current main is 413b0bb88f39cad901befcf4684355c7ee39480b. H is on its first-parent chain. The one first-parent commit after H is the merge of #1543, which changes only .github/workflows/a1exit-trial-verify.yml. R is unchanged at main (tree b05efdca).
- The local origin/main ref in this checkout (df6da1c6) is stale and is an ancestor of H; the current main was read with ls-remote.
- T1' differs from H in 70 paths. The ledger covers 44 of them, and every one of the 44 changes. The other 26 are not ledgered:
- 18 generated artifacts: the .tex and .pdf of FULL, Complexity, Computation, GR, Main, Methodology, SM, Structure and Substratum;
- 7 files in the deletion record directory a1exit-deletion-20261121/;
- 1 file in an unrelated audit: verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json.
- As noted above, one ledgered file, verification/coverage/LEDGER.json, does not equal its expected_sha256 at T1'.
- A check that "passes as written" over T1' must account for both cases: the unrelated sc42 file and the LEDGER.json mismatch. The current design, limited to corpus files, sees neither.

How the current design measures. It models one linear segment chain from the pin, in which consecutive endpoints must be equal. It has no notion of roles. It cannot express a two-parent landing merge. It cannot tell an authorized change on main from a retirement edit: a segment from H to the landing tree would attribute main's changes to the retirement, and a ledgered segment would report them as unledgered-file-change. Not met.

Required changes (roles and invariants):

- Replace the segment chain with named roles, each resolved once to a full id and recorded in result.json with the invariants it passed: H, M (current main), C (candidate), E (certified execution head, where it differs from C) and L (landing merge).
- H, the scientific base. A constant commit id in the tool's configuration. The ledger's base equals H. Every ledgered file's base_sha256 equals H's blob. R's tree at H equals the pinned tree. Every retirement edit is checked against H's bytes and never against M's. H never moves.
- M, the integration base. Resolved at run time from main and recorded.
- Invariants for M: H lies on M's first-parent chain; R's tree at M equals the pinned tree; every path changed between H and M is listed as an integration change, with the first-parent commit that changed it.
- Integration changes are classified by declared, reviewed classes (for example the trial workflow file, or this tool's own landing paths). A change outside every class is REVIEW REQUIRED. An integration change to a ledgered file, or to any corpus file, is FAIL unless the landing check below reproduces the merge.
- Integration changes are never counted as retirement edits, and retirement edits are never checked against M.
- C, the candidate. Invariants:
- C has exactly one parent, H.
- Every path in the diff from H to C falls in exactly one declared class: ledgered (the blob equals expected_sha256, and the bytes equal H plus the file's splices), generated (in a declared set, with a declared recipe, verified by rebuild or by an exact-head attestation recorded as provenance under sec. A.42), or round record (under the round's own directory).
- Any other path is FAIL. At T1' that includes sc42-integration-result.json, unless a class covers it, and verification/coverage/LEDGER.json unless its expected_sha256 is corrected.
- Paths outside the diff are byte-identical to H by construction, and the tool asserts this.
- E, if distinct from C, descends linearly from C. Each further commit is classified the same way.
- L, the landing merge. Invariants:
- L has exactly two parents: the first equals M as recorded at landing, the second equals E.
- For each path, three cases apply. If E[p] equals H[p], then L[p] must equal M[p]. If M[p] equals H[p], then L[p] must equal E[p]. If both differ from H, the path is a conflict.
- A conflict on a ledgered file passes only if L[p] equals M's bytes with E's splices applied at M-translated offsets, each old_sha256 re-verified against M's bytes. A conflict on a generated artifact requires regeneration from L's sources and is REVIEW REQUIRED until verified. Any other conflict is FAIL.
- Equivalently, the diff from M to L equals, path by path, the diff from H to E after translation. The tool reports any difference.
- The verdict of each role check is separate in result.json. A landing check never re-derives the retirement edits from M, and a candidate check never reads M.
- Tests for the roles:
- an authorized workflow change on M passes the landing check and is not reported as a retirement edit;
- an unclassified change on M is REVIEW REQUIRED;
- a change on M to a ledgered byte range produces a conflict that fails unless reproduced;
- a landing merge with parents swapped fails;
- a landing merge whose first parent is not the recorded M fails;
- a candidate with two parents, or with a parent other than H, fails;
- an unclassified path in C fails;
- each case runs in both directions.

Verdict after addendum 2: REVISE, unchanged. The role model above is required in addition to the earlier changes. Acceptance also needs the recorded owner decision that resolves the conflict with the original landing-order requirement.

Addendum 3: DESIGN-v2 (sha256 7bd794645d50a1e81d093e334b9278b95cfbee6cf628a0fb742501e346014096 as stated by the sender)

The coordinating session sent the revised design as message text; I did not receive the file and cannot confirm the hash. I checked the landing-order change against the owner record by a read-only read of #1169. Owner decision c.7093128173 (amaybaum, 2026-11-23T06:13:50Z) supersedes the execution-exception route of c.7092885251. It approves in principle that the tool lands first, that PREREG.md is amended and re-frozen so that every mandatory check of sec. 11 passes as written, and that the four trees are distinguished. It holds implementation, push, pull request, merge and the plan edit. The conflict noted in addendum 2 is therefore resolved by a recorded owner decision.

Verdict on v2: REVISE. v2 meets most of the earlier requirements, and its four-tree model (sec. 13) meets the requirement as stated. The required changes below are fewer and narrower than for v1, but several are blocking: as written, v2's own rules contradict its stated real-tree outcomes.

What v2 resolves (checked against git objects where a figure is given):

- Q1. There is no retrospective ledger, HP is a separate obligation, and insufficient provenance fails closed. The first-parent chain from E to H has 14 commits, as stated. The attribution 48, 23, 15, 15, 12, with 0 for #1494, matches my walk.
- Q2. Hits in authorized replacement text are REVIEW_REQUIRED until classified individually. Sec. 3.2 row 2 also stops a changed site region from holding its hits, which closes the 46 in-site cases of my earlier review.
- Q3. Context changes are reported, and fail where context is needed for identity or meaning (but see required change 7).
- Q4. The executable goes under tools/ and the records in a separate audit directory.
- A pin mismatch is a structured ERROR before any frozen code runs, and uncaught exceptions are INTERNAL.
- Three-state outcome; one engine with four operations; per-item explanations; adversarial controls including rule abuse.
- Op C moves the precondition test to the ledger's base, which corrects the wrong-tree defects of edits_check --commit and --pins as described.
- W1 and W2 lines confirmed at T1'. "six structural properties" occurs at SM.md:1394, ch09-universality:137, ch19-open-problems:198 and 212, and FULL 2554, 5270 and 5284. The anomaly-condition "(A1)" lines are appendix-b-derivations:235 and 246 and FULL 5914 and 5925.
- Sec. 13 gives each tree its own invariants, never substitutes one for another, and composes the landing per path. This meets the four-tree requirement. It is consistent with the independent review at c.7092883720: there, the landing merge of W and the execution commit passed against W with the same 73 paths and blobs, and --base W failed on the execution commit only for the workflow file.

Required changes to v2:

- Change 1: (Coordinator-flagged; confirmed against c.7093128173.) Sec. 11's sentence "It does not substitute for the pending sec. 11 item 2 exception, which the owner decides on its own record" is out of date and must be replaced. The exception route of c.7092885251 is superseded. The tool is part of the replacement route. The plan amendment, new freeze, repeated trials, execution and merge each keep their own gate. Landing the tool decides nothing about the retirement.
- Change 2: Exit-code collision. REVIEW_REQUIRED is exit 2, which is also the default exit status of Python argparse on a usage error. A bad flag would read as REVIEW_REQUIRED. The parser's error path must exit 64, with a control that proves it. USAGE must also be placed in the precedence list.
- Change 3: LEDGER.json contradiction. Op C (3) requires every ledgered file to conform to base plus splices. RT-C nevertheless counts verification/coverage/LEDGER.json, a ledgered file that does not conform at T1', as delegated. That turns a failing check green by reclassification. Either declare it in a reviewed record as a ledgered-regenerated file, with its regeneration recipe and its rebuild verified at exact C, or it fails. A blanket delegation must not absorb a ledgered file.
- Change 4: Delegated results must be bound to the tree. A supplied --delegated-result is an unauthenticated local file. The tool must either run the named delegated checker itself, from the plan's blob at exact C and in a materialization of the object store, as op A does for the frozen tool, or verify that the result records C's full commit id and the checker's blob hash. Otherwise the item is REVIEW_REQUIRED. The delegation list must come from a reviewed structured record, not prose; this closes open point 1 of sec. 12.
- Change 5: HP regions and tracking.
- The post-step region must have an algorithm-independent definition: for example, the bytes strictly between the nearest unchanged neighbouring lines that are unique at both the parent and the merge. The pass decision must not depend on a diff algorithm.
- An adjudicated site must resume tracking from its last step's region through every later segment. v2 does not say so.
- By my reproduction, at least 24 of the 113 have H regions overlapped by H..T1' splices. RT-T must report the 113 under H..X explicitly, as authorized-replacement, unchanged or failure. They must not stay invisible to RET.
- Change 6: Context changes in the E..H segment. A context change of an unchanged site whose context is needed for meaning has no obligation class in v2. HP covers changed site text only. At T1', 6 such context changes originate in E..H. Assign every item to the segment where the change occurred, and let HP adjudications cover context changes.
- Change 7: The meaning-context rule is not operational, and RT-T contradicts it.
- "a site whose frozen S3 column cites a qualification outside its own line" cannot be derived from the frozen s3 values. Those values are categories: visible 346, n/a 136, not determined 109, per unit 106. Replace the clause with an explicit preregistered mapping from each s3 value to meaning_context.
- Under v2's own text, "not determined" means context is required. Of the 52 unchanged sites at T1' whose context differs from the pin, 8 are "not determined". Of those 8, 6 changed in E..H and 2 in H..T1'.
- The 2 are therefore RET FAIL items under v2's rules, which contradicts RT-T's rule "no RET FAIL item". Define the reviewed record that resolves a context FAIL. Restate RT-T so that its rule follows from the design's own decision table; do not fit the outcome.
- Change 8: Reference counts in RT-T and RT-C understate the review load. Under sec. 3.2, every hit line in replacement text without a rule is REVIEW_REQUIRED, not only the 7 non-site lines. By my reproduction that is 107 lines: 84 in replaced site regions, 16 in splices on lines unheld at H and 7 new on non-site lines. This agrees with the 107 changed pattern-matching lines of c.7092883720. A further 93 pre-existing unheld lines identical at H are REVIEW_REQUIRED as unclassified. The plan can pass as written only once all of these are classified by reviewed rules or records, and the design should say so.
- Change 9: Rule schema gaps.
- Add an author field; the lint (reviewer equal to author) and control A4r both need it.
- Deny rules need reviewed pattern matchers, and a lint specific to their kind: fingerprints and max_instances do not apply to them, and corpus-wide scope must be allowed. V2 and V4 cannot be met by the literal-only matcher.
- Define the sentence splitter without "at a line boundary", which is ambiguous, and give its handling of abbreviations such as "sec." and "e.g.".
- Change 10: Plan mapping. For the amended PREREG to pass "as written", the design must give a table mapping every mandatory check of the amended sec. 11 to a tool operation, its exact flags and its expected outcome. Each entry needs a countercontrol showing that the tool fails where the original check failed, so that no check is weakened (addendum 2).
- Change 11: PIN_OK reasons and reconciliation records must be reviewed, fingerprinted records in the audit directory, with the same lint as rules: non-author reviewer, owner record and immutability.
- Change 12: (Minor.) Identify the HP merges by full commit ids pinned in the tool's configuration and cross-checked against the PR numbers. They should not be resolved by parsing subject text. The landing record must state how M was re-resolved immediately before the landing, as c.7092883720 requires.

Residual limitations specific to v2:

- Exact sentence fingerprints recognize a verified false positive only where its text is identical. Any edited or new legitimate use returns to REVIEW_REQUIRED, by design.
- Delegated checks remain outside this tool's semantics even when bound to C.
- S4b's claim that op C reproduces edits_check.check() with 0 failures at H was not run in this review.

Verdict after addendum 3: REVISE. With changes 1 to 12, I expect v2 to be acceptable for preregistration; the revised text needs its own review.

Addendum 4: the owner's three review points on DESIGN-v2

The coordinating session relayed three further owner points and asked that the verdict resolve each one, with corrections precise enough to apply. Sources read for this addendum: preserve_check.py and edits_check.py at P (blobs read with git show), the phase-0 patterns, and the corpus at H and T1'. Verdict on DESIGN-v2: REVISE, unchanged. Points 1 to 3 below add precise corrections to addendum 3's changes 1, 4 and 9. No point raises a blocker beyond them, but point 3 finds that two of v2's adversarial controls would not be detected at all as written.

Point 1. Sec. 11 and the no-exceptions objective

- Replace the sentence of sec. 11 "It does not substitute for the pending sec. 11 item 2 exception, which the owner decides on its own record." with this text:
- "The tool is part of the verification route adopted by owner decision c.7093128173 (amaybaum, 2026-11-23T06:13:50Z), which supersedes the execution exception of c.7092885251. Under that route the retirement plan is amended and frozen again so that each of its mandatory checks names an operation of this tool and its exact command, and passes as written. No check is waived, replaced after the freeze, or recorded as a deviation. Landing the tool decides nothing about the retirement: the plan amendment and its freeze, the repeated trials, the execution and the merge each keep their own owner gate."
- Consistency with the objective across the rest of v2. Four further edits are needed.
- Sec. 12, open point 1. Delete it and replace it with the frozen delegation contract of point 2. The question it asks is answered there.
- Sec. 2 op C (3) and sec. 8. "delegated" may never be satisfied by evidence supplied after the freeze that the frozen contract does not name. Add to sec. 8 under FAIL: "delegated-evidence-invalid". Add under REVIEW_REQUIRED: "delegated-evidence-missing".
- Sec. 2 op C (4), the PIN_OK "recorded reason". A reason recorded after the freeze would be an exception. Require that every PIN_OK entry is listed in the frozen plan's pin table, or in a reviewed record pinned by the freeze. Otherwise the result is FAIL pin-broken.
- Sec. 13.3, reconciliation records. A record written after the freeze is permitted only for side changes on main that the freeze could not foresee. It is a reviewed record and never relabels a failing retirement check. State that a reconciliation never changes any decision of op C on X.
- Sec. 0 and sec. 9.3 are otherwise consistent with the objective. RT-C reads "REVIEW_REQUIRED, or PASS once the delegated results are supplied". Amend it to read "PASS only with the contract evidence of point 2".

Point 2. The delegation contract

Where it lives and how it is pinned:

- One structured record, delegation.json, with schema oi-delegation/1. It lives in the amended plan's own record directory, beside ledger.json and edits.json. It is frozen with the plan at F.
- Its SHA-256 is listed in the amended PREREG's pin table, the mechanism of PREREG sec. 26.4 that preserve_check.py --verify-pins already checks.
- The tool reads it only from F's objects (--delegation F:path). It refuses the file, with ERROR SOURCE_CHANGED, unless its hash equals the pin in F's PREREG.
- It enumerates exact paths, with no globs or prefixes.
- The tool checks that the path set equals what the ledger implies. For TeX, that is preserve_check's tex_sources(ledger). For the other classes, it is the class's fixed paths. Any changed path at C that is outside the ledger and outside this record is FAIL unauthorized-change.

Is preserve_check.py --result-json at P enough? It is usable, but not enough on its own. Measured from P's blob:

- What it emits. write_result emits schema a1exit-checker-result-v1 with these fields: checker, mode, plan, ledger_sha256, ledger_base, candidate, base, checks (each with name, status and discrepancies) and verdict. It exits 0 on pass and 1 on fail. It writes the file on failure too.
- Gap 1: candidate is not a resolved commit. It is the --commit argument as given, which may be a ref name or an abbreviation. In --tree mode it is a directory path, with no commit or tree id at all.
- Gap 2: the checker's own blob is not recorded. Its integrity rests on the self-check, which compares the script's bytes with the plan's copy only when --plan is passed. plan may be null.
- Gap 3: PDFs are not verified in --commit mode. They are only listed as left to the CI build. They are verified only by --tree with --pdf-compare BUILT, against the CI build's outputs (build.rc, pdf-pages.tsv and the built PDFs).
- Gap 4: the evidence is aggregate. TeX, SC-42, the coverage fingerprints and the record directory share the single check "candidate against base, ledger, regenerated artifacts and plan record". Its discrepancies are free text, and reading them would be log-text parsing (sec. A.44).
- Gap 5: no file on a crash. An argparse error (exit 2) or an uncaught exception writes no result file.
- Gap 6: --commit mode modifies the repository. It runs git worktree add in the repository it is started from, which the new tool's no-write rule forbids.
- Gap 7: set_fingerprints skips silently when a coverage id is not found.
- Gap 8: a stale docstring. It says "four coverage entries", but STALE lists seven: MAIN:L-3, STRUCTURE:P-9.5, SUBSTRATUM:C-effective-finiteness-gauge-class-transfer, SUBSTRATUM:T-23, SM:L-1c-canonical-projection-resummed-kernel, SM:P-4b-symmetric-point-custodial-scalarity-component and SM:T-19.

Rules common to every class:

- Delegated checkers run only from F's objects, in a disposable full clone at exact C created under --out. They never run in the user's repository or a worktree of it.
- The tool records each checker's blob SHA-256, the command line, the exit status and the SHA-256 of the result file in its own result.json.
- Evidence absent: REVIEW_REQUIRED, delegated-evidence-missing. This covers a run that was not made, or a result file not produced.
- Evidence present but defective in any of these ways: FAIL, delegated-evidence-invalid.
- a schema other than a1exit-checker-result-v1;
- checker other than preserve_check.py;
- plan other than F's full id;
- ledger_base other than H;
- ledger_sha256 other than the hash of F's ledger.json;
- candidate other than C's full 40-hex id, where the mode records a commit;
- base other than H;
- a nonzero exit;
- verdict other than pass;
- a required check that is missing, not pass, or has non-empty discrepancies;
- a checker blob that differs from F's copy.
- No combination of evidence produces PASS for a class unless every required item holds.

Per class:

- Rebuilt TeX. Nine paths at T1': papers/Complexity, Computation, GR, Main, Methodology, SM, Structure and Substratum .tex, and book/The-Incompleteness-of-Observation-FULL.tex.
- Checker: preserve_check.py from F, run as --commit C(full) --plan F(full) --result-json OUT in the clone.
- Required: exit 0; mode commit; the bindings above; the check "candidate against base, ledger, regenerated artifacts and plan record" with status pass and discrepancies empty (which also requires its base-rebuild control to hold); the check "scope assertions of amendment sec. 31 in the candidate" with status pass.
- Native checks by the tool as well: the last line of each TeX file at C is "% source-sha256: X", where X is the SHA-256 of C's source .md; and the TeX path set equals tex_sources(ledger). A failure of either is FAIL.
- Rebuilt PDF. Nine paths, the PDFs of the same sources.
- Checker: preserve_check.py from F, run as --tree CHECKOUT --pdf-compare BUILT --pdf-out OUT --plan F --result-json OUT, inside the exact-head CI workflow run on C.
- Required: exit 0; the check "committed PDFs against the CI build (pages, pdftotext)" with status pass and discrepancies empty.
- Binding: because --tree records only a path, the amended preserve_check must add two fields, candidate_commit (git rev-parse HEAD of the tree) and candidate_tree. The contract requires them equal to C and C's tree id.
- The host run record (read from its API, sec. A.44) must show head_sha equal to C, the workflow and job named in the contract, and a job conclusion of success. The result file's SHA-256 must match the run's uploaded artifact.
- Native check by the tool: each PDF blob at C differs from H's, as the contract requires a rebuild.
- If any of these is absent, the class is REVIEW_REQUIRED. If any is inconsistent, it is FAIL.
- The plan's record directory. Not delegated; the tool checks it natively.
- Every path under the record directory at C equals F's blob.
- Additions are allowed only under its execution/ subdirectory, and only for the files the contract enumerates (for this round: execution/RESULT.md and the two result.json files).
- Anything else is FAIL. This is the rule preserve_check already applies, so delegating it adds nothing.
- The regenerated SC-42 result, verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json. Prefer native re-execution in the clone at C, using C's own blob of check_sc42_integration.py. Requirements:
- the clone contains ca3a5bb25ec6fdff3d3ccffcacd2d7bac3bb4caf (preserve_check's SC42_BASE);
- python3 -I -B check_sc42_integration.py --verbose exits 0, and its stdout equals C's result file byte for byte;
- the same holds with -O;
- --self-test and -O --self-test each exit 0, and their stdout equals sc42-integration-controls.json at C, which must equal H's copy.
- The delegated alternative is the preserve_check commit-mode evidence above, which covers it only in aggregate.
- The regenerated coverage LEDGER.json, verification/coverage/LEDGER.json. It is a ledgered file with seven regenerated fields; the tool checks it natively.
- C's bytes equal H plus the file's splices, except the fingerprint values of the seven STALE ids above.
- Each STALE id occurs exactly once in the file. A missing or duplicated id is FAIL, unlike set_fingerprints.
- Each replaced value equals the fingerprint that tools/proof_census.py --json (C's blob, run in the clone, exit 0) reports for that id.
- Any other byte difference is FAIL.
- This replaces v2's "regenerated: delegated" for this file.

Point 3. Do the expected FAILs of sec. 9.2 follow from the specification?

Measured with the profiles extracted from H and P:

- V1 ("The six structural properties of the substratum ...") and V4 ("the framework's sixth structural property, finiteness of the bijection") match no existing profile: p0-core, p0-para, ledger-ext, ptr and repo all miss them.
- Sec. 3.2 decides only hits. As written, V1 and V4 are therefore never examined, and pass silently.
- V2 and V3 are hits (core:P2, ptr and repo; core:P1, ptr and repo respectively), but v2 specifies no deny rule that matches them. A fingerprint mismatch, a failed residual test, or a forbids literal voiding the allow rule each leads only to REVIEW_REQUIRED.
- So the claimed protection against a disguised reintroduction is not enforced for V1 to V4.
- Required correction 3a. Deny rules are scan profiles. A deny rule is evaluated on every sentence of every corpus file, not only on hits of other profiles. Add this to sec. 3.2 and sec. 6.1. Deny matchers are reviewed regular expressions, with scope "all corpus files"; addendum 3, change 9 covers the schema.
- Required correction 3b: seed deny rules, to be reviewed. I measured each against the four controls, the W1 sentence and both trees. Each catches its control. None matches W1 or any line at T1'. DR-1 matches 59 lines at H, the pre-retirement retired forms, which makes it its own countercontrol.
- DR-1, the retired count of structural assumptions: `\b(six|seven|sixth|seventh)\b[^.;]{0,40}\bstructural (assumptions?|axioms?|posits?)\b`, or `\bA1\s*[en-dash or hyphen]\s*A6\b`, or `\b(six|seven|sixth|seventh)\b[^.;]{0,40}\bstructural propert(y|ies) of the substratum\b`. Catches V1.
- DR-2, an ordinal structural item with finiteness: `\b(sixth|seventh)\b[^.;]{0,40}\bstructural (property|assumption|axiom|posit)\b[^.;]{0,80}\bfinit`. Catches V4.
- DR-3, total finiteness as a member of a premise list: a sentence containing "structural propert", "structural assumption", "structural axiom", "structural posit", "posit", "premise" or "axiom", in which "one of which", "one of its", "one of the", "among" or "includ..." is followed within 60 characters by "total finiteness", "total-finiteness", "finite in total" or "totally finite". Catches V2.
- DR-4, "(A1)" as a finiteness label: `\(A1\)[^.;]{0,60}\b(finit\w*|substratum|configuration space)`. Catches V3, and does not match appendix-b-derivations:235 or 246.
- Required correction 3c: corrected expectations in sec. 9.2.
- V1: FAIL by DR-1.
- V2: FAIL by DR-3. Without DR-3, REVIEW_REQUIRED (rule-fingerprint-mismatch).
- V3: FAIL by DR-4. Without it, REVIEW_REQUIRED, because the forbids literal voids the W2 rule.
- V4: FAIL by DR-2. Without it, PASS, because there is no hit.
- Add a control that runs DR-1 to DR-4 at T1' with 0 matches required, and DR-1 at H with matches required.
- The other expected FAILs of sec. 9.2:
- L3: FAIL rule-overreach, by sec. 3.3. Consistent.
- A1r, A2r, A4r and A7r: FAIL rule-invalid, by sec. 6.3. Consistent once the author field of addendum 3, change 9 exists; A4r needs it.
- A3r (a fingerprint swapped, with the count unchanged) is not widening under sec. 6.3's list, which counts only added fingerprints. As written it would PASS. Correct the lint so that any change to the fingerprint set is widening, and so that each fingerprint must be reproduced by a sentence of the named file at recorded_at; otherwise FAIL rule-invalid.
- A5r: FAIL by deny precedence (sec. 3.2 row 1, sec. 6.2 check 6). Consistent once the deny rule exists.
- A6r: sec. 6.3 must define the trigger as the profile match span of the fingerprinted sentence at recorded_at, so that the lint can evaluate it.
- P1 (the wrong merge named): no FAIL class covers it. Sec. 4 check 2 has no class. Add "provenance-mismatch" to sec. 4 and to the FAIL list of sec. 8.
- P2 and P3: FAIL provenance-gap and provenance-foreign. Consistent.
- C3: FAIL pin-broken. Consistent.
- R3 to R14: the classes candidate-parent, landing-parents, landing-drops-main-change, landing-conflict-unresolved, landing-extra-change and base-drift appear only in sec. 13. Sec. 8 calls itself complete, so add them there. Add SCIENTIFIC_BASE_MISMATCH and MAIN_NOT_DESCENDANT to the ERROR list of sec. 5.
- U4, U5, U7, U8 and U9: FAIL by sec. 3.1. Consistent.

Verdict after addendum 4: REVISE. Addendum 3's changes 1 to 12 stand. Points 1 to 3 above give the exact text and rules for changes 1, 4 and 9, and add corrections 3a to 3c, the A3r lint fix, provenance-mismatch and the completeness of sec. 8. With these applied, I would expect v2 to be acceptable for preregistration; the corrected text needs its own review.
