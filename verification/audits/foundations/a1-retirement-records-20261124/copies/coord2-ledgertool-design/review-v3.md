Independent read-only review of DESIGN-v3 (commit-independent ledger and terminology verification tool), rule O6

Verdict: REVISE

Reviewer: a fresh Claude Code session, read-only, authorized by the owner through the coordinating session session_013T6pfKuv5mi3MXtKjH2tZb. No branch, ref, commit, push, dispatch, GitHub post or tracked-file change was made. Objects P and T1' were fetched by branch name with `--refmap= --no-write-fetch-head`, so no ref was written. All scripts and outputs are in a session workspace outside the checkout. Date 2026-11-23.

Goal link (sec. A.47): A1-EXIT (#1169), the exception-free verification route. This review decides whether DESIGN-v3 is fit to implement as the verifier of the amended plan's mandatory checks. It decides no scientific question and no row disposition.

Summary of the verdict. The architecture is sound and most of the v2 review is answered. The four disputed figures were reproduced: v3 is right on three of them, and on the fourth (84 against 86) its figure follows from a profile set its own sec. 14 does not state. The verdict is REVISE, not ACCEPT WITH REQUIRED CORRECTIONS, for three reasons. First, the deny-rule set that v3 offers as the replacement for sec. 11 item 7 does not preserve the original prohibition: it misses the retired posit-count form that the literal grep catches at H (Main.md:736, "Fourteen items"). Second, two expected outcomes of the test matrix do not follow from the rules as specified (V5 against DR-4; sec. 5 against note 2 of sec. 11). Third, the corrected deny set needs its own independent review before it can be preregistered. A bounded delta review of the corrections listed below is enough; the rest of the design need not be re-reviewed.

Input integrity. The design arrived as two cross-session messages (PART 1, lines 1-661, and PART 2, lines 662-1263). I did not reproduce sha256 855e3da00341a0c3cb7234ba7473870115164d809adeb698dd80752bf3d29d9d (69817 bytes). The text arrived only as message content, with the characters less-than and greater-than replaced by the entities amp-lt and amp-gt. A byte-exact file could not be recovered without retyping 70 kB by hand, and a retyped file would test my transcription, not the transfer. The review is of the text as received. I found no sign of truncation: both parts end with their stated end markers, and the section numbering runs 0 to 16 without a gap.

Objects verified. E e837e3db, H 53c6601a, P 4c79be64, T1' 14ac71b4 and W 413b0bb8 all resolve. E is an ancestor of H. T1' has the single parent H. P is not an ancestor of T1'. The record tree R is b05efdca935a42b9c94ef1748c964696bf58fcd9 at 9882df8f, H, T1' and W. The first-parent chain E..H has 14 commits, as v3 states. Applying the 399 byte-span splices of P's `ledger.json` to H reproduces T1' blob-for-blob in 43 of 44 files. The exception is `verification/coverage/LEDGER.json`, which v3's `coverage-ledger` class covers. The splice spans are byte offsets.

Question B: the four numerical discrepancies

I fixed the definitions below in a scratch file before computing any count. Where a definition admits a sensible variant, I report every variant. No method was chosen for its result.

B definitions. Sites are the 697 entries of the frozen `sitemap.json`. A site's pin line is line `line` of `file` at E. A site is an HP site if it changed at any first-parent step of E..H. I computed this three independent ways:

- DEF-V: v3 sec. 3.2 as written, implemented from the text alone.
- DEF-G myers: `git diff -U0 --no-renames` per step, carrying the site's line range through the hunks.
- DEF-G histogram: the same with the histogram algorithm, as a sensitivity control.

Overlap uses v3 sec. 5's byte rule against the site's final region at H. Hit lines use the Phase-0 core and paraphrase patterns plus the frozen `EXTENDED_PATTERNS`, extracted from their blobs. Context uses the nearest non-blank line above and below, with sentinels.

B1, HP sites also edited by H..T1' splices.

- DEF-V gives 19 sites and 31 distinct splices.
- DEF-G gives 18 sites and 31 splices, under both myers and histogram.
- A line-level `git diff H T1'` against the DEF-V regions gives 19; against the DEF-G regions it gives 18.
- The one-site difference is papers/Substratum.md:266. Under sec. 3.2 it shares a merged three-line region (266-268) with the site at :268. Blank lines are never unique, so the walk's anchors fall outside both sites, and the two pre-regions become one block. The only splice touching the merged region is D029, an empty-image splice inside line 268. Line-precise tracking does not attribute D029 to :266.
- v3's 19/31 is therefore correct under its own rule, and its 18 by line diff is also correct.
- The review's 24 sites with 24 splices is not reproduced under any line-precise definition. Widening each region by two lines on each side gives 24 sites but 43 splices (44 site-splice pairs), so 24/24 matches no definition I could find.
- Paragraph-level and one-line widening both give 18 sites and 31 splices.

B2, two-step HP sites. There are 3 under all three methods: papers/Main.md:224, papers/Main.md:732 and papers/Substratum.md:92. I checked Substratum.md:92 by hand: `git diff -U0` shows line 92 rewritten by #1473 (f1c8c6b1 to a1f38284) and again by #1474 (a1f38284 to 0ba358cc). v3's 3 is correct and the review's 2 is wrong. The first-change attribution reproduces exactly: #1475 48, #1474 23, #1470 15, #1473 15, #1472 12, for 113 in total.

B3, hit lines in the 197 site replacement regions at T1'.

Definition: non-HP sites are located at H by their unique pin line. A splice overlaps a site if it intersects the site line's content span (with the zero-length rule). The region at T1' is the union of the site span and its overlapping splice spans at H, mapped through every splice of the file and expanded to whole T1' lines.

- This gives 383 unchanged, 197 replaced and 4 removed sites, as both reports say, and 203 region lines.
- With the Phase-0 and extended profiles (the profile set v3 sec. 14 states), the count is 84 hit lines, the review's figure. Including the LF in the span changes the region to 215 lines but not the count.
- Adding the `count-grep` literal list gives 86, v3's figure. The two extra lines are book/ch19-open-problems.md:212 and book/The-Incompleteness-of-Observation-FULL.md:5284. Both are W1 sentences ("six structural properties of the bijection").
- Adding `PTR` or `REPO_PAT` alone leaves 84.
- v3's 86 therefore follows from a profile set its own sec. 14 does not state. It also breaks the disjointness that sec. 8.2 claims, because those 2 lines are among the 7 lines of the W1 row. The disjoint figures are 84 + 16 + 7 = 107, with the W1 row's 7 lines counted separately.
- I did not independently reproduce the 16, 7 and 93 sets. They depend on the v1 sec. 4.7 held-set definition, which was not in the review input.

B4, meaning-context failures at T1'.

Definition: an unchanged site is one whose pin line is unique in its file at E, H and T1'. A context change is attributed to E..H if ctx(E) differs from ctx(H), and to H..T1' if ctx(H) differs from ctx(T1').

- This gives 52 unchanged sites with a context change: 27 in E..H only, 22 in H..T1' only and 3 in both.
- Counting the s3 values that begin "not determined" gives 8: 6 in E..H and 2 in H..T1'.
- Also counting the values that begin "per unit" gives 12: 7 in E..H and 5 in H..T1'.
- None of the marked cases changed in both segments.
- Both reports' figures are reproduced; the difference is purely which s3 values are marked. Under the owner's direction to keep "per unit" context-sensitive, 12 is the applicable figure.
- The 12 sites:
- E..H: FULL:4895, 4905, 4919; ch18:164, 174, 188; Main.md:332.
- H..T1': FULL:1340; ch05:25; Computation.md:122; GR.md:90; Main.md:588.

Further figures confirmed: the s3 categories (346 / 136 / 109 / 106); DR-1 matches 59 lines at H and 0 at T1'; DR-1..DR-4 match 0 at T1'. Literal greps over papers/*.md and book/*.md:

- at T1': "six structural" 7, `\bA1\b` 4, "sixth of" 0, "Fourteen" 0;
- at H: "six structural" 11, "Fourteen" 1, "sixth of" 2, `\bA1\b` 179.

Question A: conditions, decision logic and generality

Owner condition 1 (exit codes): not met as written.

- FAIL is exit 1. That is also the exit status CPython returns for an uncaught exception raised before the wrapper is installed, for example an import error in the tool's own package or a syntax error.
- Exit 2 also remains reachable outside argparse: the interpreter returns it when it cannot open the script.
- So "exit 2 is never emitted" holds only for the parser, and exit 1 is ambiguous between FAIL and a crash.
- Required: give FAIL a code no interpreter emits (for example 20). A consumer that accepts exit 0 must also require a `result.json` whose `outcome` is PASS, whose schema validates, and whose recorded engine blob equals the pinned one (sec. A.44). Any exit status outside the table is non-acceptance.
- Control X7: run the tool with a deliberately broken import, and expect a non-zero exit that is distinct from FAIL, with no PASS result.

Owner condition 2 (delegation): met in design. Missing evidence is REVIEW_REQUIRED, defective evidence is FAIL, the contract is pinned at F, and evidence is bound to the full 40-hex id of X. The preserve_check gaps 1, 2, 5 and 7 are correctly made preconditions of the amended plan.

Owner condition 3 (adversarial FAILs traced to rules): not met. Two cases:

- V5 does not follow from DR-4. DR-4 as specified is `\(A1\)[^.;]{0,60}\b(finit\w*|substratum|configuration space)`. It is case-sensitive, and its class stops at the first period. I ran it on V5's text, "**(A1) Finiteness.** The configuration space is finite.", and it does not match: "Finiteness" is capitalized, and the period after it ends the window. V5's expected FAIL `deny-match` therefore has no rule that produces it.
- The same holds on the real tree: DR-4 matches 0 lines at H. It does not catch the retired (A1) entries themselves, for example Substratum.md:92 at H ("(A1) **Finiteness.** The configuration space $S$ is finite."). So DR-4 has no real-tree countercontrol, and neither do DR-2 and DR-3 (0 lines at H each). Only DR-1 has one (D2).
- V7 expects REVIEW `rule-fingerprint-mismatch`. That holds only if the V2 sentence is an edited copy of a fingerprinted W1 sentence; otherwise the "total finiteness" hit is REVIEW `unclassified`. The control must state its precondition.

Owner condition 4 (preregistered s3 mapping): met. The principle is stated before the counts, "per unit" is kept true, and an adjudication may only add `meaning_context`, never remove it. See decision 2 below for the indicators.

Owner condition 5 (classification and review load): met in structure, but the sec. 8.2 table is not disjoint as claimed (B3). Required: state the profile set behind each row, and either use 84 with W1's 7 lines counted separately, or keep 86 and remove the 2 shared lines from the W1 row. State the total for whichever convention is chosen.

Owner condition 6 (deterministic HP regions): the rule is deterministic and reproducible; my independent implementation gives exactly v3's 113 / 3 / 19 / 31. Three corrections are required:

- When two sites' walks produce the same region, report the merger as a structured link (for example `region_shared_with`), and give the overlap count both as region-attributed (19) and as line-attributed (18). Otherwise an adjudicator reads D029 as a retirement rewrite of Substratum.md:266.
- An HP adjudication must classify each site's own line, not only the shared block.
- Add control H7: two adjacent changed sites separated by a blank line, with a splice on one of them. Expected: both sites are reported, the merger is linked, and the line-attributed overlap names only the spliced site.

Owner condition 7 (sec. 11 mapping): mostly met. Item 7 is treated under decision 1. There is also an internal contradiction:

- Sec. 5 says "No flag converts REVIEW_REQUIRED".
- Note 2 of sec. 11 has `--final` turn REVIEW items of the `repo` profile into FAIL `unclassified`.
- The conversion is in the strict direction, so it weakens nothing, but the two statements conflict. Required: sec. 5 should read "No flag converts REVIEW_REQUIRED to PASS; `--final` converts the REVIEW items of the profiles it names to FAIL", and the countercontrol should show it.

Owner condition 8 (record lint): met in design. Ownership is treated under decision 4.

Owner condition 9 (generality): sound in principle, with the following required corrections. No A1 check is weakened by the relocation itself.

- Z9 is over-broad and also under-specified. A lint that fails on "any string value occurring in the A1 configuration or its records" will fire on the generic field names the engine's adapter interfaces must use: `id`, `file`, `start`, `end`, `new`, `splices`, `sites`.
- It also conflicts with sec. 16.3: the A1 adapters (`a1exit-exact-edit/2` and the others) sit in the engine's registry and must contain the A1 schema strings, such as "a1exit deletion exact-edit ledger v2".
- Required: put the adapters in modules outside the purity scope, pinned by blob in the configuration. Give Z9 an explicit allowlist of interface field names and the engine's own schema ids, and make its pass and fail cases synthetic controls (a planted 40-hex literal, a planted A1 regex, a planted s3 value).
- The configuration widening list in sec. 16.2 is incomplete. Each of the following can lead to more acceptance and must be widening:
- adding an allow-rule file, or a new allow rule without `supersedes`;
- adding a side-change class;
- any change to a scope record;
- an adapter or adapter-version change;
- an extractor selector change;
- adding sentence abbreviations, which merge sentences and so change what the sentence-level DR-3 sees;
- a change to `operations`.
- Notation collision. The notation table defines `E` as the ledger pin e837e3db. Sec. 13.1 uses `E` for the certified execution head (sec. A.39 vocabulary). Required: rename one of them, for example `C` for the certified head, everywhere, including RT-L and the role model.
- The synthetic configuration Y1-Y8 and the fail-closed classes Z1-Z8 are adequate. Y8 (same engine blob for both configurations) is the right reproducibility control.
- S13 (every A1 control has the same outcome under the configured engine) is the correct acceptance gate. Its expectations must be the corrected ones, V5 in particular.

Decision logic against sec. 10 and 11. Apart from the defects above, every expected FAIL of sec. 10.2 names a sec. 9 class, and the counts in RT-T0 are consistent with my reproduction:

- 113 `hp-unadjudicated`;
- 7 HP context items;
- 19 `untracked-hp-overlap` under the region rule;
- 5 RET `context-meaning-unverified`;
- 383 unchanged, 197 replaced and 4 removed sites.

Open decision 1: sec. 11 item 7

Original check: "Corpus grep for `\bA1\b`, ... only the ledger's false positives remain; grep of posit counts ("Fourteen", "six structural", "sixth of"): zero."

Result: as proposed, DR-1..DR-4 plus classification of the `count-grep` hits does not preserve the original prohibition, so it cannot be adopted as written.

- The retired posit-count form escapes the deny set. At H, "Fourteen items, of unequal weight, and not fourteen independent physical assumptions" (papers/Main.md:736) is caught by the literal grep and matched by none of DR-1..DR-4.
- Under the proposal, reinstating that sentence at a candidate gives only a `count-grep` hit, which an allow rule could classify as legitimate. The original check fails it outright.
- v3 note 1's claim that the restatement "changes the check's text, not its decision on any retired form" is therefore false for this form.
- T1' carries the successor "Thirteen items" at Main.md:738, so the old count is a real stale-count hazard (sec. A.30: a removed claim can hide in a count).
- The "sixth of" form at H (glossary.md:13, FULL:6504) is caught, but only by DR-1's A1-A6 alternative, not by any rule about the ordinal.

Adversarial paraphrases within the scope of item 7. I tested 22 strings against the seed DR-1..DR-4. These are missed:

- "Six structural assumptions define the substratum." (DR-1 is case-sensitive);
- "the six structural conditions on the substratum";
- "six structural premises of the framework";
- "the six substratum posits";
- "the structural assumptions A1 through A6";
- "A1--A6" and "A1" em-dash "A6";
- "(A1)" en-dash "(A6)";
- "A1, ..., A6";
- "the substratum's sixth axiom, finiteness";
- "posit A1 (finiteness) holds";
- "A1 (Finiteness): the configuration space is finite";
- "(A1) Finiteness. The configuration space S is finite.";
- "The posit ledger has 14 items.";
- "one of the posits is that the configuration space is finite";
- "the six structural properties of the bijection, the first being finiteness of S".

Several of these also escape every review profile (for example "the six substratum posits"), so they would PASS.

Required strengthening before the amendment can be reviewed:

- make DR-1, DR-2 and DR-4 case-insensitive;
- extend DR-1's nouns to premises and conditions;
- extend DR-1's range alternative to double hyphen, en dash, em dash, "through", "to", an ellipsis list and parenthesized labels;
- let DR-4 cross the label's own period, and add "posit A1";
- add a DR-5 for the posit-ledger count, for example `(?i)\b(fourteen|14)\b[^.;]{0,40}\b(items|posits|entries|premises)\b`;
- give every DR a real-tree countercontrol at H.

I measured strengthened variants of this kind on the real trees: 0 matches at T1', and at H 61 (DR-1), 22 (DR-4) and 1 (DR-5) lines. The extra coverage costs no false positive at T1'. These variants are illustrations for the deny-rule reviewer, not a proposal I have reviewed. Paraphrases with no fixed lexical anchor ("one of the posits is that the configuration space is finite") cannot be fully closed by regex. That limit must be stated as residual, and those forms must be guaranteed at least REVIEW through a review profile (P4 and ptr already cover "finite configuration space" and "posit").

Procedure, as the owner directed:

- The restated item 7 is a plan amendment. It needs its own preregistered text, an independent review of the deny set and the W1 rules, and the owner's authorization. It cannot be used in the current frozen trials.
- The literal check must stay in the tool as a named countercontrol, `item7-literal`, with its expected outcome documented:
- at T1': FAIL, with exactly 7 "six structural" lines (SM.md:1394, ch09:137, ch19:198 and 212, FULL:2554, 5270 and 5284), 0 "Fourteen" and 0 "sixth of";
- at H: FAIL, with 11 / 1 / 2.
- Item 7 as currently frozen therefore does not pass as written at T1'. Under the exception-free route, the amendment must be adopted before any trial can claim item 7.

Open decision 2: context mapping and syntactic indicators

On the merits, the s3 principle is right: context is required exactly where the frozen record does not establish that the qualification is visible on the site's own line. "per unit" belongs on the required side. A per-unit status means the qualification was established by a unit's correction, which may sit in a neighbouring sentence. None of the 12 marked cases is spurious on reading. GR.md:90's above-context, for example, changed from "including A1" to "including finiteness of the total system". "per unit" should stay true; narrowing it to reduce the H..T1' count from 5 to 2 would be choosing a rule by its count.

I tested the four indicators, with definitions fixed before measuring, on all 697 sites and on the 52 real context changes.

- PARTIAL (the Phase-0 quote does not cover the line): fires on 342 of 697 sites and on 23 of the 52 changes. It measures how Phase-0 excerpts were truncated, not whether meaning depends on context. Recommendation: informational only, with no effect on the outcome. As FAIL or REVIEW it would add about 20 review items at T1' with no meaning signal in the cases I read (for example FULL:452 and ch01:119, where a corollary's statement was edited).
- LIST (the site line is a list item): fires on 20 sites and 1 of the 52. That one is a true positive the s3 mapping misses: papers/Substratum.md:127 (s3 "visible", so it PASSes with `context_changed`) is the item "The triple satisfies C1 ... C4". The paragraph below it changed from "derived from E1-E3, A1-A2" to "derived from E1-E3 and A2", which changes the premises the item's claim rests on.
- I found one false negative of my LIST definition. FULL:708 and ch02:78, "*(A2) Determinism.*", are a labelled item of the posit list whose heading changed to "five properties". The indicator must include labelled-item forms (a line starting with an emphasized or parenthesized label such as (A2) or (C1)).
- Recommendation for LIST: REVIEW_REQUIRED when the list's lead-in or a sibling item changed.
- TABLE (the site line is a table row): fires on 6 sites and 1 of the 52 (Main.md:741, where a neighbouring row's status cell changed). For a table row, the nearest non-blank line is a sibling row, not the qualifier. The qualifiers are the header row and the caption or preceding paragraph. Recommendation: REVIEW_REQUIRED, with the context for table rows redefined as header row plus caption.
- ANAPH (the site line opens with an anaphor such as This, These, Such, Hence, Thus, It or Under this): fires on 31 sites and 0 of the 52. An anaphoric line takes its referent from the line above, so a changed above-context changes what the line asserts. Recommendation: FAIL `context-meaning-unverified` unless adjudicated, that is, the indicator sets `meaning_context` true. It costs no real-tree failure at T1' and closes the clearest semantic dependence.
- These indicators must be preregistered at S0 with their exact definitions and these measured rates as references, not tuned afterwards.

Open decision 3: overlap and counts. See question B. My findings for the record:

- 19 HP sites / 31 splices under sec. 3.2 (18 line-attributed, with the Substratum.md:266 merger explained);
- 3 two-step sites;
- 84 hit lines under the stated profiles (86 with `count-grep`);
- 12 meaning-context failures under the adopted mapping (8 if "per unit" were false).

The review's 24/24 and its 2 two-step sites should be withdrawn. v3's 86 must be restated with its profile set.

Open decision 4: who owns the review records

The chain below applies to HP provenance adjudications, terminology and hit classifications, context resolutions, allow and deny rules, and scope and side-change records. One record is one immutable file in the audit directory of sec. 12.1.

- Writer (author): prepares the record and its evidence: the exact git object ids, the subject's `line_sha256` or region hashes, the tool's REVIEW-mode explanation for that subject, and the semantic statement (which qualification is visible, and why).
- The writer's evidence may include tool output, but the record states its classification in its own words. Its `author` field names the writer. A writer may not be the reviewer of the same record.
- Independent reviewer: a non-author re-derives each record from the git object store, not from the writer's output. For HP records that means recomputing the walk, checking each step's commit and hashes, and reading the pre and post text. For classification and context records it means reading the sentence and its context at the stated tree and judging the semantic statement.
- The reviewer writes a separate immutable review record that names the reviewed record's path and blob sha256, the method, the verdict per item and any dissent. A review that cites only a passing tool run is invalid.
- Owner: authorizes the exact content. The authorization names each record's path and blob sha256 and its review record's blob sha256, and is quoted in the repository with author, time and comment id (sec. A.42 item 7).
- A batch may be authorized by a manifest record listing every member's blob sha256. An authorization that names a path without a hash authorizes nothing.
- Frozen configuration: `retirement-config.json` at F references every record, review record and authorization quote by `{path, blob_sha256}`. A record added after F is admissible only under sec. 13.3's reconciliation rule and never for a decision on X.
- Verifier: the tool checks:
- each referenced blob exists at its pinned commit with its hash;
- the record's schema and lint;
- `author` differs from `reviewer`, and the owner record exists;
- the review record names exactly this record's blob;
- the review's verdict covers every item.
- The tool never infers a role, a review or an authorization from a passing tool result. A record whose `reviewer` or `owner_record` field points to a tool run, a CI run or an Issue is FAIL `record-invalid`.
- Changes: a correction is a new record with `supersedes`, a new review and a new owner authorization. Nothing is edited in place, and an id is never reused.
- Residual limit: the tool can check that the role fields differ and that the quoted authorization exists, but not who actually wrote them. Identity rests on the reviewer's and the owner's own recorded statements.

Required corrections, consolidated (for the bounded delta review)

- R1: replace FAIL exit 1 with a code no interpreter emits; require a consistent `result.json` for acceptance; add control X7 (broken import). State that exit 2 is excluded only for parser paths and that any unlisted code is non-acceptance.
- R2: fix DR-4 so that V5 and the retired (A1) entries at H match it, or change V5's expectation. Give every DR a real-tree countercontrol at H. State V7's precondition.
- R3: strengthen the deny set as described under decision 1 (case-insensitivity, nouns, range forms, DR-5 for the posit count), with independent review of the set and its examples. State the lexically unanchored paraphrases as a residual limit covered at least by REVIEW profiles.
- R4: rewrite note 1 of sec. 11. The restatement is a plan amendment that needs its own review and authorization, and it does not preserve the "Fourteen" prohibition as proposed. Keep `item7-literal` as a countercontrol with the documented expected FAILs at T1' (7/0/0) and at H (11/1/2).
- R5: sec. 8.2: state each row's profile set, correct the disjointness (84 plus W1's 7, or 86 with W1 reduced to 5), and restate the total.
- R6: sec. 3: report region mergers (Substratum.md:266/268) as structured links, give both the region-attributed and the line-attributed overlap counts (19 and 18), require per-line classification in shared regions, and add control H7.
- R7: reconcile sec. 5 ("no flag converts REVIEW_REQUIRED") with sec. 11 note 2 (`--final` converts to FAIL).
- R8: sec. 16: move the A1 adapters out of the engine's purity scope, or give Z9 an explicit allowlist; make Z9's controls synthetic; complete the configuration widening list as above.
- R9: rename one of the two meanings of `E`.
- R10: add the indicator rules of decision 2 at S0: ANAPH sets `meaning_context` (FAIL until adjudicated); LIST, including labelled items, and TABLE give REVIEW_REQUIRED, with table context redefined as header plus caption; PARTIAL is informational only. Record the measured rates as references.
- R11: adopt the ownership chain of decision 4 in sec. 6.3, with the review record as a separate immutable file bound to the reviewed blob.

Residual limitations of this review

- The design text's sha256 was not reproduced (see Input integrity).
- The 16, 7 and 93 sets, the 176 repo-scan lines and the frozen tool's error counts (32 and 154) were not independently recounted.
- No implementation exists, so the controls were checked against the specified rules, not run. V1 to V6 and the DR measurements were run with my own transcription of the seed regexes.
- My indicator definitions (ANAPH word list, LIST and PARTIAL thresholds) are mine. Their rates are references for the preregistration, not tuned values.
- The semantic readings in decision 2 are a reviewer's reading of a sample, not an adjudication.
- This review establishes nothing about scientific correctness and adopts no rule, record or count.
