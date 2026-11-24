Independent read-only review of DESIGN-v4 (commit-independent ledger and terminology verification tool): the bounded delta review

Verdict: ACCEPT WITH REQUIRED CORRECTIONS

Reviewer: an independent, non-author Claude Code subagent session. It did not write v1 to v4 or the v3 review. The work was read-only, as the owner decision set. No file in the checkout was changed, moved or deleted. No branch, ref, commit, push, pull request, GitHub write or workflow run was made, and no fetch was needed. All four commits were already present. The checkout stayed clean at 556cfb08. Everything this review wrote is under `D/review-v4/`, where D = <records>/coord2-ledgertool-design. Date 2026-11-23.

Goal link (sec. A.47): A1-EXIT (#1169), the exception-free verification route. This review decides whether DESIGN-v4 answers the v3 review and the owner decisions D1-D4 closely enough that the tool can be implemented. It decides no scientific question, no row disposition, no deny or allow rule, and no count. It is not an adoption.

Input integrity (sha256, checked before any other work; all match)

- DESIGN-v4.md 3cde34d2209dbcd6c5f03f991fb27385c2e709b9bd1557b60d965f9aa219c625
- CHANGES-v4.md c3214f10ea57879e7771bcacd2ea9a446b3fcc27c7464ad0d41cf665c145fdca
- DESIGN-v3.md 855e3da00341a0c3cb7234ba7473870115164d809adeb698dd80752bf3d29d9d
- review-v3.md 5041232c6c2c0fe3b7ec939564dd669dd4f3f4f82d8ce79d365c28e7a6d2e4ff
- Commits E e837e3db, H 53c6601a, P 4c79be64 and T1' 14ac71b4 resolve in the local object store.
- Blobs read from them: P's `edits_check.py` has sha256 2856e58c...1d98c, which matches v4 sec. 14. P's `ledger.json` is 2055e68f...32b5. The frozen `sitemap.json` at H is 586c526b...2cb9, and Phase-0 `sites.json` at H is 00165404...4a5f. The data copies are in `review-v4/data/`.

Method. Every recount was made with my own scripts (`review-v4/rv_*.py`). I wrote them from the design text and read only git objects. I did not import or run the writer's `work-v4/` scripts. I read two of the writer's scripts afterwards, only to diagnose a disagreement, and say so where it applies: `work/measure9.py` (task 2, the repo split) and `work/measure10.py` (task 5, the source of v3's 86). Profiles were extracted from their blobs by `ast` or JSON, never retyped. The deny rules and `resid` were transcribed from v4 sec. 6.4 and 6.6 (`rv_rules.py`). The sentence splitter was implemented from sec. 6.1.

Summary of the verdict. v4 answers R1-R11 and D1-D4 in substance. Every figure that v4 labels as a writer measurement reproduces exactly, with two exceptions:

- the repo-scan split, where the sum 176 holds but 37/12 should read 14/35;
- the number of region mergers, which is 9 groups of 22 sites, not 1.

The remaining required corrections are bounded:

- three text corrections: the mergers, the `ptr` count for item 1, and the figure labels;
- one misclassification in the widening list;
- one substantive defect in the proposed item-7 amendment check: unclassified `ptr` and `count-grep` hits stay REVIEW where the original check fails hard, contrary to v4's own sec. 11 rule;
- the D1 countercontrol status.

On that status, my search of the whole repository history finds no corpus text matched by DR-1d or DR-2. It does find one real line at H that DR-3 matches, in AGENTS.md, which lies outside the corpus scope. Neither redesign nor a full re-review is needed. The open owner points are listed at the end.

***

Task 1. Status of R1-R11 and D1-D4

| Item | Status | Where in v4 | Notes |
|---|---|---|---|
| R1 exit codes, acceptance, X7 | resolved | sec. 5; X6-X10 | FAIL is 20. No code in the table is 1, 2 or 120. The wrapper is installed before the package import. The acceptance predicate requires a consistent `result.json`. X7 (broken import), X8 (interpreter exit 2) and X10 (tampered result) are added. |
| R2 DR-4 against V5 and the (A1) entries; countercontrols; V7 | partly resolved | 6.4; 10.2 V5, V7a-c; 10.3 RT-DR | DR-4 now matches V5 and Substratum.md:92 (recounted). V7 is split correctly: I checked V7a's precondition, and ch19:212 carries "of the bijection". The countercontrols of DR-1d, DR-2 and DR-3 are open under D1 (task 4, V6). |
| R3 deny set strengthened; residual | resolved for the listed forms | 6.4, 6.6, 1 | All 15 deny-closable strings of the v3 review's list fail by the named rule. The 16th (V21) is REVIEW via `resid`. The residual statement exists, but its class is narrower than D1's wording (V8). New anchored gaps are listed in task 4 (optional O1). |
| R4 note 1; `item7-literal` | resolved, with a new defect in the proposed amendment check | 6.1, 9, 10.3 RT-I7, 11 row 7 and note 1 | 7/0/0 and 11/1/2 with the named lines are recounted. The proposed amendment check yields REVIEW where the original fails hard (V3). |
| R5 profile sets and disjointness in sec. 8.2 | resolved | 0.3, 8.2 | The figures 84, 16, 7, 93, 107, 200 and 222 are recounted. The 16/7 split is now independently reproduced. The repo split is wrong (V4). |
| R6 mergers, two counts, own lines, H7 | partly resolved | 3.2, 3.3, 3.4, H7, RT-T0 | The mechanism is right. 19/31 and 18/31 are recounted. The claim "at T1' there is one" merger is false: there are 9 merger groups of 22 sites (V1). |
| R7 sec. 5 against `--final` | resolved | 5; 9 `final-unclassified`; 11 note 2; X9 | |
| R8 adapters, Z9, widening list | partly resolved | 12.1, 16.1-16.3, Z9a-g | Adapters sit outside the purity scope. The Z9 allowlist and its synthetic controls are present. All seven omitted widening items are now widening. However, "adding an HP obligation or a merge to one" is listed as non-widening, and it can increase acceptance (V5). |
| R9 two meanings of `E` | resolved | Notation; 13 | A grep finds every remaining `E` denoting the pin. |
| R10 S0 indicators | resolved | 4.2-4.4; K5-K9 | The definitions are exact. Rates and items are recounted (task 2). |
| R11 ownership chain | resolved | 6.3; O1-O9 | |
| D1 item 7 | partly resolved | 6.4, 6.6, 11 note 1, 15 | Done: the amendment procedure, `item7-literal` 7/0/0 and 11/1/2, the R3 strengthening, and the stated residual. Open: real-tree countercontrols for DR-1d and DR-2 (none exists in history), and for DR-3 (one exists, out of scope); see V6. Also open: the REVIEW guarantee is narrower than D1's wording (V8), and the amendment check does not fail hard (V3). |
| D2 context | resolved | 4, 4.1-4.4 | `per unit` stays true. ANAPH sets `meaning_context`. LIST, including labelled items, and TABLE give REVIEW, with the header-plus-caption context. PARTIAL is informational. Both rate sets are recorded as references. v4's stricter neighbour-context reading is correct (task 5). |
| D3 counts | partly resolved | 0.3, 3.4, 8.2, 14 | The adopted figures are reproduced. The merger count is wrong (V1), the repo split is wrong (V4), and some figure labels are inconsistent (V7). |
| D4 ownership | resolved | 6.3, 12.1, 16.2 | Writer, independent reviewer with a separate record bound to the blob sha256, owner authorization naming the blobs with author, time and comment id, configuration referenced by `{path, blob_sha256}`, the verifier's checks, and no role inferred from a tool result are all present. Optional O5 adds a root-of-trust note. |

Accuracy of CHANGES-v4.md. It is accurate apart from these points:

- (a) The R6 row says 19/18/31 were "not recomputed by v4". DESIGN-v4 sec. 0.3 lists them under "Reproduced by the independent v3 review and recounted for v4". The two documents disagree (V7). I have now recounted the figures, and they hold.
- (b) The R6 row and v4 sec. 3.2 say there is one merger. There are nine (V1).
- (c) Section 2, "Source of v3's 86": the touching test is evident in `work/measure10.py` (`x['start'] <= b and x['end'] >= a`). The second claimed deviation, the removed sites' empty-image lines, is not evident there: the script skips an empty replacement segment (`if seg and k >= 0`). The touching test alone reproduces 86, with the same two lines. The withdrawal of 86 stands, but its stated cause should name the touching test only (V7).
- (d) Section 3, the 176 row: the 96/31/37/12 breakdown is wrong in its last two parts (V4).
- (e) Section 3, the 16/7 row: it is now independently recounted (task 2).

***

Task 2. Independent recounts

Every figure below was recomputed with my own scripts at the stated trees, from the design's definitions.

| Figure (v4 location) | v4 | Mine | Script | Result |
|---|---|---|---|---|
| DR-1 at H, lines (a / b / c / d) | 61 (6 / 2 / 55 / 0) | 61 (6 / 2 / 55 / 0) | rv_dr.py | agree |
| DR-1c at H, sentences | 65 | 65 | rv_dr.py | agree |
| DR-2 / DR-3 at H | 0 / 0 | 0 / 0 (also 0 at E) | rv_dr.py | agree |
| DR-4 at H | 28, incl. Substratum.md:92 | 28, incl. Substratum.md:92 | rv_dr.py | agree |
| DR-5 at H | 1 (Main.md:736) | 1 (Main.md:736) | rv_dr.py | agree |
| distinct deny lines at H | 86 | 86 | rv_dr.py | agree |
| deny set at T1', lines / sentences | 0 / 0 | 0 / 0 | rv_dr.py | agree |
| mutants M-DR1d, M-DR2, M-DR3 | each original fails to match, each mutant matches | same; each edited substring occurs once in its line | rv_mut.py | agree (see the note on M-DR1d below) |
| item7-literal at T1' | 7 / 0 / 0, `\bA1\b` 4 | 7 / 0 / 0 (SM.md:1394, ch09:137, ch19:198 and 212, FULL:2554, 5270, 5284), `\bA1\b` 4 (W2 lines) | rv_lit.py | agree |
| item7-literal at H | 11 / 1 / 2, `\bA1\b` 179 | 11 / 1 (Main.md:736) / 2 (FULL:6504, glossary.md:13), 179 | rv_lit.py | agree |
| HP sites, two-step, attribution | 113; 3 (Main.md:224, Main.md:732, Substratum.md:92); #1475 48, #1474 23, #1470 15, #1473 15, #1472 12 | same | rv_hp.py | agree |
| HP/RET overlap, region-attributed | 19 sites / 31 splices | 19 / 31 | rv_hp.py | agree |
| HP/RET overlap, line-attributed | 18 / 31; the difference is Substratum.md:266 | 18 / 31 under both myers and histogram; the difference is Substratum.md:266 | rv_lineattr.py | agree |
| region mergers at T1' | "one: Substratum.md:266 and :268" | 9 groups, 22 sites (below) | rv_merge.py | disagree (V1) |
| replacement regions | 383 / 197 / 4; 203 region lines | 383 / 197 / 4; 203 | rv_b3.py | agree; T1' equals H plus the splices in every ledger file except `verification/coverage/LEDGER.json` |
| hit lines in regions (p0+ext) | 84; 86 with `count-grep` (ch19:212, FULL:5284) | 84; 86 with the same two lines | rv_b3.py | agree |
| variants | touching test: 381/199, 217 lines, 86 (FULL:710, ch02:78); removed-site lines: 205 lines, 86 | same | rv_b3.py | agree |
| unheld p0+ext lines at T1' | 200; 84 subset; 116 outside; 93 identical to an unheld H line | 200; 84 subset; 116; 93 (same under per-file or global held sets) | rv_u116.py | agree |
| 16 / 7 split of the 23 | 16 / 7 (D237, D238, D241, D242, D246, D247, D388) | 16 / 7: the 7 are exactly those splices, on H lines that are neither site lines nor hit lines; the 16 lie in splices over H lines that are hit lines in HP site regions | rv_split23.py | agree; this closes v4 sec. 15 item 5 for the split |
| sec. 8.2 total | 222 | 222 (200 unheld p0+ext, 9 W1/W2 lines held or not p0+ext, 13 `resid`-only) | rv_222.py | agree |
| meaning-context failures | 12 (7 / 5), the named sites; 8 if `per unit` were false | 12 (7 / 5), the same 12 sites; 8 (6 / 2) | rv_ctx.py | agree |
| context changes | 52 (27 / 22 / 3) | 52 (27 / 22 / 3) | rv_ctx.py | agree |
| s3 categories | 346 / 136 / 109 / 106 | 346 / 136 / 109 / 106 | rv_ctx.py | agree |
| indicator rates of 697 | ANAPH 23, LIST 49, TABLE 6, PARTIAL 521 | 23, 49, 6, 521 | rv_ctx.py | agree |
| indicators among the 52 | 0, 3, 1, 39 | 0, 3, 1, 39 | rv_ctx.py | agree |
| indicator items | HP: LIST FULL:708, ch02:78, TABLE Main.md:741; RET: LIST FULL:708, ch02:78, Substratum.md:127; no ANAPH failure | identical | rv_ctx.py | agree |
| `resid` on added text at T1' | 287 lines, 28 hits, 13 hit by no other profile | 287, 28, 13 | rv_resid.py | agree |
| repo profile at T1', P's `classify()` | 176 = 96 path-wide unrelated + 31 path-wide guard pins + 37 substring + 12 IDENT; 5486 historical; 2 generated | 176 = 96 + 31 + 14 substring (9 unrelated label, 1 historical record label, 1 registry identifier, 3 preserved historical evidence) + 35 kernel identifier (IDENT); 5486; 2; 0 unexplained | rv_repo.py | the sum agrees, the split disagrees (V4) |
| `ptr` hits at T1' (sec. 11 row 1) | 4 (W2) | 5: the 4 W2 lines plus papers/GR.md:58 | rv_w.py | disagree (V2) |

Causes of the disagreements.

- Mergers. All nine groups arise in the E..H walk at a single step, by sec. 3.2's own definition (same post-region at the same step):
  - FULL 4897/4899/4901/4903, 4921/4923 and 4973/4975;
  - ch18 166/168/170/172, 190/192 and 242/244;
  - Methodology.md 146/148 and 367/369;
  - all eight of these at #1475 (7f28886f);
  - Substratum.md 266/268, at #1474 (a1f38284).

  Only Substratum.md 266/268 is overlapped by an H..T1' splice (D029). v4 appears to have counted only the merger that affects the overlap counts.
- Repo split. I read the writer's `work/measure9.py` only to diagnose this. It labels each line with the kind of the first `EXPLAINED` entry for its path, whatever class `classify()` returns. So 23 lines in files that also carry substring entries (verification/README.md, the census JSON, A6Instantiation.lean, HexLatticeGas.lean and others) are counted as "substring", although `classify()` returns `kernel identifier` for them. Under the class `classify()` returns, the split is 14 substring and 35 IDENT. None of the 176 is in the `pending R-1` class at T1'.
- `ptr`. GR.md:58 at T1' ("For a finite total system, restrict it ...") matches PTR's `finite total system`. In P it is explained by the third `RESIDUAL_ALLOW` entry ("finite-scope wording of ledger X-70") and by the strip `.replace('For a finite total system', '')`. v4's W1 and W2 rules do not convert that entry. The line is in the 84, so it already needs a hit classification record, and the total of 222 is unaffected.

Note on M-DR1d. The original glossary.md:11 line at H already matches DR-4, and M-DR2's original line matches DR-1a and DR-1c. A mutant run at H fails whatever DR-1d does. RT-DR must therefore assert the target rule id on the named line, not the run's outcome. The RT-DR wording ("each DR family matches at least one line") implies this; making it explicit is optional (O3).

***

Task 3. The `resid` profile

Coverage of the forms the v3 review listed as escaping:

- "one of the posits is that the configuration space is finite" (V21): `resid` matches, no deny rule matches, so REVIEW, as v4 states.
- "the six substratum posits": DR-1a matches, so FAIL. `resid` does not match (there is no finiteness word); the deny rule covers it.
- Every other string on the v3 list that carries a finiteness word and a posit noun also matches `resid` (V5, V15-V18).
- Reviewer-constructed forms, `resid` hit (REVIEW at least):
  - "the first structural assumption, finiteness of the configuration space";
  - "the finiteness assumption";
  - "The configuration space is finite by assumption.";
  - "S is finite, as the first posit requires";
  - "among the posits is the finiteness of the total configuration space" (also DR-3).

The 13 T1' lines hit by `resid` and by no other review profile. They are 5 mirror pairs and 3 single lines:

| Line | Text near the match | Judgment |
|---|---|---|
| FULL:1116 / ch04-methodology:10 | "The second is a separate posit. The finite-capacity definition and the explicit hypotheses ..." | legitimate successor wording; a fit review subject (finite capacity beside "posit" and "hypotheses"); not a retired form |
| FULL:1132 / ch04:26 | "(... linearity, background independence), with its finite-substratum scope, are not derivable from the foundational premise" | legitimate; this is the replacement of the posit list; worth review |
| FULL:1336 / ch05-gauge-structure:19 | "provides the finite-substratum scope, the structural assumptions A2–A6 and ..." | legitimate (A2–A6); worth review |
| FULL:2607 / ch09-universality:190 | "The finite scope and five structural axioms must be checked for compatibility ..." | legitimate (the count is corrected to five); a high-value review subject, because its H predecessor matched DR-1a and DR-4 |
| FULL:6273 / appendix-c-objections:116 | "Finiteness is therefore the stated scope of specific results, not a premise about the universe" | legitimate; worth review |
| papers/Substratum.md:133 | "not a consequence of finiteness, of A2–A6 or of the nearest-neighbor wave equation" | legitimate |
| papers/Substratum.md:205 | "The finite-substratum scope and the structural assumptions A2–A6 exclude several broad classes" | legitimate |
| papers/Substratum.md:233 | "Finite substratum, structural assumptions (A2–A6)" | legitimate |

None of the 13 is a retired form. None is noise either: each states the finite scope next to an assumption noun, which is exactly where a reinstated posit would sit. A record per line (or per mirror pair, with exact paths) is a proportionate cost.

False negatives built from real-tree text. I took real H lines and deleted the "under A1" qualifier, so that each sentence asserts finiteness outright (`rv_fn.py`):

- ch02-substratum.md:212 at H, edited to "a finite set with a deterministic bijection on it";
- SM.md:30, edited to "uses a finite set with a deterministic bijection";
- ch02:136, edited to "the substratum is a finite set with a bijection on it".

All three match no deny rule, no review profile and not `resid`. Added in a splice, they would PASS. Other escapes: "We take the substratum to be finite.", "The substratum is assumed to have a finite number of states." and "the universe is assumed finite".

These forms fall inside v4's stated residual, which has neither a posit noun nor a state-space noun. But they are the commonest retired construction ("a set (finite under A1)" occurs about 15 times at H) with its qualifier removed. An illustrative extension, which no one has reviewed, catches all six and adds only 4 REVIEW lines at T1' (`rv_resid_ext.py`):

```
(?i)\bfinite\s+(?:\w+\s+)?set\b|\b(?:substratum|universe|world)\b[^.;]{0,40}\b(?:is|be|being|are)\s+(?:a\s+)?(?:\w+\s+)?finite\b
```

The 4 lines are FULL:6265, appendix-c:108, Complexity.md:206 and Structure.md:1010, each legitimate. See V8.

***

Task 4. The deny rules

Correctness of each regex against its intent. I transcribed and ran every rule.

- DR-1a/b catch counts and ordinals before "structural/substratum + noun" and "structural properties of the substratum".
- DR-1c catches A1..A6 ranges with hyphen, double or triple hyphen, en dash, em dash, "through", "to", TeX dash macros, the bare ellipsis list "A1, ..., A6", and parenthesized labels.
- DR-1d catches "substratum's sixth axiom".
- DR-2 catches "sixth structural property ... finit".
- DR-3 is a sentence-level test: a posit-like noun plus a connector followed by finiteness.
- DR-4 catches "(A1)", "posit A1", "A1 (" and "A1:" followed by finiteness, the configuration space or the substratum, across the label's own period.
- DR-5 catches "fourteen/14 ... items/posits/entries/premises/assumptions".
- All of them behave as v4 sec. 10.2 states on V1-V22 (`rv_ex.py`): every expected rule fires, V7 and V8 behave as stated, and no W1 or W2 line, nor Main.md:738 ("Thirteen items"), matches.

Absence of matches at T1'. There are 0 lines and 0 sentences across papers/*.md and book/*.md, for every rule.

Forms that still escape every deny rule (constructed; optional O1). Each is listed with what it gets otherwise:

- Count without "structural" next to the noun: "the six posits of the substratum" and "six assumptions about the substratum". These PASS: no rule or profile hits them.
- Posit count without a following noun: "The posit ledger lists fourteen." and "the fourteen-item posit ledger". These PASS.
- TeX subscript labels: "$A_1$–$A_6$". This PASSes.
- Ranges with intermediate items or other dashes:
  - "A1, A2, \ldots, A6"; v4 sec. 6.4 calls this an "ellipsis list", but only "A1, ..., A6" with no intermediate item matches;
  - "A1−A6" with U+2212.
  These are REVIEW through p0-core and `ptr`.
- Label after the name: "Finiteness (A1)". This is REVIEW.
- "six structural hypotheses": `count-grep` REVIEW only. N lacks hypothesis or hypotheses.

The original literal item 7 also misses all of these except "A1, A2, \ldots, A6", "A1−A6" and "Finiteness (A1)", which carry `\bA1\b`. The pure PASS cases are therefore residual gaps of the original as well, not regressions. I measured illustrative fixes ("CNT N of/on/about/for the substratum", `fourteen[- ]item`, subscript range): 0 matches at E, H and T1' (`rv_dr6.py`). That means they would have no real-tree countercontrol either.

The most common retired forms are REVIEW only. 95 lines at H that carry `\bA1\b` and were rewritten by the ledger are matched by no deny rule, for example "a set (finite under A1)", "the open hypothesis A1" and "Posit A1 plays different roles" (`rv_gap.py`). At an X that reinstates one, the amendment check gives REVIEW (via `ptr` and p0-core), while the original item 7 fails it hard. This is the basis of V3.

An illustrative deny form, "`A1` other than the literal label `(A1)`", matches 170 lines at H and 0 at T1' (`rv_dr6.py`). It would give a deny rule with a real-tree countercontrol. It is an illustration for the deny-rule reviewer, not a reviewed proposal.

Search for real-tree countercontrols for DR-1d, DR-2 and DR-3, as D1 requires (`rv_hist.py`, `rv_tree_all.py`):

- Corpus, whole history. I scanned every distinct blob of papers/*.md and book/*.md reachable from any ref: 4657 blobs. The scan was line-level for DR-1d and DR-2, and sentence-level for DR-1d, DR-2 and DR-3. It found zero matches. The prefilters are exact: every DR-1d or DR-2 match contains "sixth" or "seventh", and every DR-3 match contains "finit". A sanity run with DR-1a added finds the expected glossary and FULL lines. No pinned or historical corpus tree contains a qualifying countercontrol for any of the three rules.
- Whole trees at H and W (every text file). There is one match: DR-3 on AGENTS.md at H, lines 37-38, "Every posit of the substratum model — the posit ledger of `papers/Main.md`, including total finiteness (A1), linearity (A5), ...". This is a genuine retired form, rewritten by ledger splice D296 ("including linearity (A5)"). AGENTS.md at T1' has 0 deny matches at line and sentence level (`rv_ledgered.py`). So DR-3 has a qualifying real-tree line at H, but it lies outside the corpus scope v4 gives the deny rules.
- v4 sec. 6.4 states that "no real-tree line exists that they could match". That is false for DR-3.
- Extending the deny scope to every ledgered file is not viable. Several ledgered non-corpus files match deny rules at T1' with legitimate text, for example:
  - verification/README.md:2320, "the sixth structural assumption" (A6-cov);
  - A6Instantiation.lean:15;
  - Lean docstrings, "the finiteness predicate `A1` ... the configuration space is finite";
  - guard pins in edge_rigidity_probe.py.

  AGENTS.md alone could be added.
- Observation for the deny-rule reviewer: DR-1a's ordinal alternative also hits current, legitimate references to A6 as "the sixth structural assumption" in active non-corpus files at T1'. In the corpus that usage was retired (glossary.md:13 at T1' reads "The structural assumption A6 of the reconstruction theorem (A2–A6)"). The ordinal alternatives therefore encode a corpus terminology decision, and the amendment should say so.

Status under D1: DR-1d and DR-2 have no real-tree countercontrol anywhere in history. They stay open unless the owner approves the mutant countercontrols, or the rules are dropped; dropping them loses V4 and V15, and only DR-2 covers V4. DR-3 can be given a real-tree countercontrol by adding AGENTS.md to the deny scope. Otherwise it also stays open (V6).

Countercontrols of the other rules are real lines at H, and I confirmed each: DR-1a glossary.md:13 and FULL:6504; DR-1b ch09:104; DR-1c FULL:718 (among the 55); DR-4 Substratum.md:92; DR-5 Main.md:736.

***

Task 5. The writer's other deviations

- Source of v3's 86. The conclusion is right: 84 under sec. 5's strict rule, and the touching test alone gives 86 with FULL:710 and ch02:78. The detail is wrong: v3's script does not show the second deviation (V7).
- Deny profiles only on trees that must be free of retired forms (sec. 2.3). This is right and necessary. Measured, the v4 rules match 95 lines at E and 86 at H. If they ran there, RT-E could not PASS, and RT-H0 would carry non-HP FAILs. Nothing is weakened, because the decision tree X is still scanned.
  - The rule names the endpoint of a ledgered segment. A run whose only segment ending at X is unledgered would then not evaluate the deny profiles. Such a run fails anyway (`unauthorized-change`), but the cleaner rule is "every tree except E and H, which are named as retired-form trees" (O2).
- LIST and TABLE keep the neighbour context (sec. 4.3). This is right. Under the v3 review's literal recommendation (header plus caption only), its own TABLE true positive, Main.md:741, whose neighbour row changed, would no longer be caught. v4's reading is a strict superset and removes no outcome. It is a deviation in the strict direction from D2's wording, and it is listed for the owner in sec. 15 item 4.
  - Minor: the sec. 4.1 row should require the adjudication to match both context hashes as well as both structure hashes, for a site whose neighbour context changed while its structure hash did not (O4).
- The 16/7 split was not recounted by the writer. It is now independently reproduced (task 2). The label "in splices on lines unheld at H" is accurate: the 16 lie in splices over hit lines of HP site regions, which no content-held set covers.

***

Task 6. Other blocking points

- The item-7 amendment check is weaker than the original on hard failures (V3). v4 sec. 11 states: "the tool must also give a non-PASS result on it, and a FAIL wherever the original's failure was a hard failure". The proposed amendment check (sec. 11 note 1) requires zero deny matches and "every `ptr`, `count-grep` and `resid` hit classified". So a reinstated retired line that no deny rule covers is only REVIEW_REQUIRED, while the original item 7 fails it outright. Examples:
  - a real H form such as "the substratum is a set (finite under A1)";
  - a constructed one, such as "six structural hypotheses".

  The outcome is still non-acceptance, so no PASS leaks. But the stated rule is violated, and nothing in the check stops the REVIEW item from being resolved by a record before `F`.
- The widening list misclassifies HP additions (V5). Adding a merge to an HP obligation turns a step that is now FAIL `provenance-foreign` into an adjudicable step. Adding an HP obligation for a further segment turns changes that would otherwise be RET `unauthorized-change` into adjudicable HP sites. Both can increase acceptance, so both are widening.
- The sentence splitter (sec. 6.1) never breaks a joined paragraph at a list item that has no blank line before it. It also does not break at a terminator followed by closing emphasis ("... no more.** Every ..."). In AGENTS.md at H, one "sentence" spans three bullets. This is deterministic, so it is not a correctness defect. But it widens what DR-3 and the allow-rule fingerprints see, which raises the false-positive risk (O6).
- I found no other contradictions, no untestable expected outcome apart from those named in V1-V3 and O3, and no generality violation. The purity scope, allowlist, adapter admission by blob, Y1-Y10, Z1-Z9g and S13 are consistent with sec. 16. The owner's standing instruction is respected throughout: no check is weakened to turn a real-tree failure green, and v4 corrects its own expected outcomes in the strict direction (V7a-c, RT-E, RT-H0).

***

Required corrections

V1. Sec. 3.2, the "Region mergers" paragraph, and RT-T0 (sec. 10.3): replace "At T1' there is one" and "one region merger" with "9 merger groups (22 sites), all formed at a single E..H step: 8 at #1475 (FULL 4897-4903, 4921/4923, 4973/4975; ch18 166-172, 190/192, 242/244; Methodology.md 146/148, 367/369) and Substratum.md 266/268 at #1474. Only 266/268 is overlapped by an H..T1' splice (D029)". State that `own_lines` is required for all 22 sites. Correct the R6 row of CHANGES-v4 to match.

V2. Sec. 11 row 1 and sec. 6.5: `ptr` has 5 hits at T1', not 4. The fifth is papers/GR.md:58 ("For a finite total system"), which P explains by its third `RESIDUAL_ALLOW` entry and a strip. State that W1 and W2 do not replace that entry, and that GR.md:58 is resolved by its hit classification record, since it is one of the 84. Correct the expected outcome to "5 hits: 4 W2 lines PASS with their rules, GR.md:58 with its record, else REVIEW".

V3. Sec. 11 note 1: change the proposed amendment check so that an unclassified `ptr` or `count-grep` hit at X is FAIL, as the original item 7 is. For example, give `--final` a per-check profile list that includes `ptr` and `count-grep` for item 7, or give item 7 its own conversion class. Alternatively, add a reviewed deny rule for bare `A1` outside the literal label `(A1)`; illustrated, it matches 170 lines at H and 0 at T1'. Add countercontrols with expected FAIL:
- a reinstated H line such as ch02-substratum.md:136 at H ("the substratum is a set (finite under A1)");
- "six structural hypotheses".

V4. Sec. 0.3, sec. 8.2 and CHANGES-v4 section 3: the repo-scan split is 96 path-wide "unrelated label", 31 path-wide "guard pins", 14 substring entries (9 unrelated label, 1 historical record label, 1 registry identifier, 3 preserved historical evidence) and 35 IDENT, under the class P's `classify()` returns. It is not 37/12. The sum of 176, the 5486 and the 2 are right. State that the earlier split attributed lines by path, not by returned class.

V5. Sec. 16.2: move "adding an HP obligation or a merge to one" from the non-widening list to the widening list, with the reason. Add a control in which a merge added without a widening review turns `provenance-foreign` into an admissible step, with expected outcome ERROR `CONFIG_UNREVIEWED`.

V6. Sec. 6.4, sec. 15 item 2 and RT-DR: correct "no real-tree line exists" as follows.
- DR-1d and DR-2 match no line or sentence in any historical corpus blob (4657 blobs), nor in any text file at H or W.
- DR-3 matches a real retired sentence at H in AGENTS.md:37-38 ("Every posit ... including total finiteness (A1) ..."), which ledger splice D296 rewrites, and AGENTS.md at T1' has no deny match.

Then either add AGENTS.md to the deny-rule scope and make that sentence DR-3's real countercontrol, or keep DR-3 with DR-1d and DR-2 as open under D1. Put the mutant-countercontrol question for DR-1d and DR-2 (and DR-3 if it stays open) to the owner as a decision; it is not settled by the design.

V7. Figure provenance:
- Sec. 0.3 lists 19/31 and 18 as "recounted for v4", while sec. 14 and CHANGES-v4 (R6) say they were not recomputed. Make the labels agree. All of these figures are now independently recounted by this review.
- Sec. 0.3, sec. 14 and CHANGES-v4 section 2 say v3's script "used both deviations". Its code shows the touching test and skips empty images. Attribute the 86 to the touching test, and keep the removed-site-lines route only as an equivalent variant.

V8. Sec. 1 (the residual limit) and sec. 15: state explicitly that the D1 guarantee of "at least REVIEW" is implemented only for paraphrases with a finiteness word and a posit or state-space noun. The constructed escapes are examples outside that class, for the owner to accept or close: "a finite set with a deterministic bijection on it", "the substratum is a finite set ...", "We take the substratum to be finite.", "the universe is assumed finite". Either widen `resid` (the illustrative extension in task 3 catches all of them at a cost of 4 REVIEW lines at T1'), or record the owner's acceptance of the narrower class.

Optional points

- O1. Close the anchored deny gaps of task 4:
  - "six posits of the substratum";
  - "fourteen-item", and "lists fourteen" with no noun;
  - `$A_1$–$A_6$`;
  - ranges with intermediate items;
  - U+2212 and U+2010/U+2011 separators;
  - "Finiteness (A1)";
  - "hypotheses" in N.

  Note that none of them has a real-tree countercontrol (0 at E and H), so they fall under the same D1 decision as V6.
- O2. Sec. 2.3: say "deny profiles run on every tree the run evaluates except `E` and `H`", rather than tying them to the endpoint of a ledgered segment.
- O3. RT-DR: assert the target rule id on each named countercontrol line, since the M-DR1d and M-DR2 lines already match DR-4 and DR-1a/c, so the run's outcome alone proves nothing about the target rule.
- O4. Sec. 4.1: a LIST or TABLE adjudication should match both context hashes and both structure hashes.
- O5. Sec. 6.3: state that the root of trust for the configuration's own owner field and authorization is `F`'s owner-designated pin table.
- O6. Sec. 6.1: end a paragraph (or a sentence) at a list-item line, and accept a terminator followed by closing `*` or `_` and then whitespace as a sentence end. Re-measure DR-3 and fingerprints afterwards.
- O7. The `item7-literal` scope and the repo profile do not cover active non-corpus uses of "the sixth structural assumption" at T1' (verification/README.md:2320, A6Instantiation.lean:15). These are A6 references whose count includes A1. They are outside item 7's corpus scope, but they are worth one line in the amendment's scope statement.

What I could not verify

- The semantic correctness of any classification, rule or adjudication. My judgments in task 3 are a reviewer's reading, not records.
- The behaviour of an implementation: none exists. The controls were checked against the specified rules, not run.
- The source of the owner decisions D1-D4. Like the writer, I received them only through the coordinating session, and I hold no comment id.
- The frozen tool's error counts (32 and 154), which v4 withdraws. Not recounted.
- The exact definitions behind the v3 review's indicator rates. Only v4's definitions were recounted.
- My sentence splitter implements sec. 6.1 as written. The writer called theirs an approximation. For every deny count the two agree.
- My history search covers objects reachable from the refs in the local repository, not refs that exist only on the remote.

Files (all under D/review-v4/; MANIFEST.sha256 covers every file)

- `rv_git.py`, `rv_rules.py` and `rv_prof.py` are the helpers: git access, my transcription of the rules, and profile extraction.
- `rv_lit.py`, `rv_dr.py`, `rv_mut.py`, `rv_ex.py`, `rv_hp.py`, `rv_merge.py`, `rv_lineattr.py`, `rv_b3.py`, `rv_u116.py`, `rv_split23.py`, `rv_w.py`, `rv_222.py`, `rv_ctx.py`, `rv_resid.py`, `rv_resid_ext.py`, `rv_fn.py`, `rv_gap.py`, `rv_dr6.py`, `rv_hist.py`, `rv_hist_sanity.py`, `rv_tree_all.py`, `rv_ledgered.py` and `rv_repo.py` are the recount and search scripts.
- `out-*.json` and `out-*.txt` are their outputs.
- `data/` holds the blobs read from E, H and P.
