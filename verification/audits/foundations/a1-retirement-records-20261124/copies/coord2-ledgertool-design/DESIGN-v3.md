# Commit-independent ledger and terminology verification tool: design v3

## Status and authority

This is a paper-only design. Nothing is implemented, committed, pushed or published under it.

- It supersedes v2 where they differ. `DESIGN.md` (v1) and `DESIGN-v2.md` stay as written.
- Authority: owner decision #1169 c.7093128173 (amaybaum, 2026-11-23T06:13:50Z). It approves in
  principle the exception-free verification route. That route has four steps: the tool lands first
  through its own review and merge decision; `PREREG.md` is amended and frozen again so that every
  mandatory check of sec. 11 passes as written; the trials are rerun; the retirement is executed.
- That decision holds implementation, push, pull request, merge, the plan edit and execution.
- Authoritative review input: `review-v2.md` (sha256 1a86e3fb...eb9). It contains addenda 1-4.

Goal link (sec. A.47): A1-EXIT (#1169), the exception-free verification route. This design
decides how the tool verifies each mandatory check of the amended plan. It decides no scientific
question and no row disposition.

## Notation

| Symbol | Commit |
|---|---|
| `E` | e837e3dbaa605efc867a213f3345cee14c36d8f5, the ledger pin |
| `H` | 53c6601a10419b6b333cc992474272501ab542af, the scientific base |
| `T1'` | 14ac71b4b0a0c0aa2d7068d6799a73f474097060 |
| `P` | 4c79be642ca631573f06b444903be75ec4f5e2b6, the frozen plan |
| `W` | 413b0bb88f39cad901befcf4684355c7ee39480b, `main` at the time of writing |
| `F` | the future freeze of the amended plan |
| `X` | the candidate (execution) commit |
| `M` | `main` at check time |
| `L` | the landing merge |

`R` is the frozen ledger record directory. It has tree b05efdca935a42b9c94ef1748c964696bf58fcd9 at
9882df8f, H, T1' and W.

***

## 0. Traceability

### 0.1 Owner acceptance conditions

| Condition | Answered in |
|---|---|
| 1. Distinct exit codes, including parser errors and `--help`; with a control | sec. 5, controls X3-X6 |
| 2. A frozen, reviewed `delegation.json` with exact-head evidence; missing evidence is never PASS | sec. 7 |
| 3. Deny-pattern coverage; adversarial FAILs, each traced to a named rule or sec. 9 condition | sec. 6.4, 6.5, 9, 10.2 |
| 4. A preregistered s3-to-context mapping; the T1' cases resolved transparently | sec. 4 |
| 5. Every replacement-text and unclassified hit classified, with the review load stated | sec. 8 |
| 6. Deterministic HP regions; full merge ids; HP/RET overlap visible in both | sec. 3 |
| 7. Each mandatory sec. 11 check mapped to an operation, flags, expected outcome and countercontrol | sec. 11 |
| 8. Review and authorization lint for rules, PIN_OK reasons, reconciliation records and other records | sec. 6.3 |
| 9. Generality with strict scope limits | sec. 16 |
| 9.1. A core that does not depend on any retirement | sec. 16.1; control Z9 |
| 9.2. A frozen per-retirement configuration `oi-retirement-config/1`: schema, adapters, location, pinning and lint | sec. 16.2, 16.3 |
| 9.3. A1 as the first configuration, with every A1-specific constant relocated and no check weakened | sec. 16.4 |
| 9.4. A structurally different synthetic configuration with positive and adversarial controls | sec. 16.5 |
| 9.5. Fail-closed configuration validation, with exit codes and classes | sec. 16.6 |
| 9.6. Reproducibility record | sec. 16.7 |

### 0.2 Review changes

The review's v1 Q1-Q5 findings are carried over from v2 and corrected here.

| Review item | Answered in |
|---|---|
| v1 Q1: HP class kept out of RET; attribution corrected; tracking resumes after adjudication; unresolved sites touched later reported | sec. 3 |
| v1 Q2: new-pattern-in-replacement; per-hit classification records | sec. 8 |
| v1 Q3: preregistered context rule; BOF/EOF sentinel | sec. 4 |
| v1 Q4: placement | sec. 12 |
| v1 Q5: schema, fingerprints, output form, boundary cases | sec. 5, 10.1 |
| v1 mutation list | sec. 10.1 |
| Addendum 1 (extension): one pipeline, subject kinds, rules with negative matchers and examples, explanations | sec. 2, 6, 10 |
| Addendum 2: role model H/M/X/E/L | sec. 13 |
| Addendum 3, change 1: sec. 11 sentence replaced | sec. 12 |
| Addendum 3, change 2: exit-code collision | sec. 5 |
| Addendum 3, change 3: LEDGER.json | sec. 7.3 |
| Addendum 3, change 4: delegated results bound to the tree | sec. 7 |
| Addendum 3, change 5: HP regions and tracking | sec. 3 |
| Addendum 3, change 6: E..H context changes | sec. 3.5, 4 |
| Addendum 3, change 7: meaning-context mapping | sec. 4 |
| Addendum 3, change 8: review load | sec. 8 |
| Addendum 3, change 9: rule schema; deny kind; sentence splitter | sec. 6 |
| Addendum 3, change 10: plan mapping | sec. 11 |
| Addendum 3, change 11: PIN_OK and reconciliation lint | sec. 6.3, 13.3 |
| Addendum 3, change 12: pinned merge ids; M re-resolution | sec. 3.1, 13.4 |
| Addendum 4, point 1: sec. 11 text; delegated evidence after `F`; PIN_OK at `F`; reconciliation scope | sec. 12, 7, 13.3 |
| Addendum 4, point 2: delegation contract; preserve_check gaps | sec. 7 |
| Addendum 4, point 3: deny as profiles, DR-1..DR-4, V1-V4, A3r, provenance-mismatch, sec. 9 completeness | sec. 6.4, 6.3, 3.3, 9 |

### 0.3 Figures that differ from the review

Each figure was reproduced read-only from git objects (method in sec. 14). The implementation
reports its own counts under the fixed definitions. The counts are never fitted.

- **HP sites also touched by RET splices: 19 sites and 31 splices**, under the region definition
  of sec. 3.2. A whole-file line diff from E to H gives 18. The review states 24 sites and 24
  splices; I could not reproduce that figure. Condition 6 is met regardless of the count: every
  overlapping site stays visible in both accountings (sec. 3.4).
- **Multi-step HP provenance: 3 sites**: Main.md:224, Main.md:732 and Substratum.md:92, each
  changed by #1473 and then #1474. The review gives 2. Substratum.md:92 is corroborated by the
  plan's own re-pin table (P, PREREG sec. 31: "S2-B and S2-C edited the (A1) entry").
- **Hit lines inside the 197 site replacement regions at T1': 86.** The review gives 84. Total hit
  lines in replacement text: 86 + 16 + 7 = 109, against the review's 107.
- **Meaning-context failures at T1': 12.** The mapping of sec. 4 marks both `not determined` and
  `per unit` sites. It yields 12 meaning-required context changes, 7 originating in E..H and 5 in
  H..T1'. The review counted `not determined` only: 8, of which 6 are in E..H and 2 in H..T1'.

The following agree with the review:

- the 697 sites and their s3 categories (346 / 136 / 109 / 106);
- the 113 E..H site changes, attributed 48 / 23 / 15 / 15 / 12 to five merges;
- 52 context changes among unchanged sites;
- the 116 unheld hit lines at T1' (93 + 16 + 7);
- DR-1 matching 59 lines at H and 0 at T1', with DR-1..DR-4 matching 0 lines at T1';
- the frozen tool's error counts (32 and 154).

***

## 1. Purpose, non-goals and residual limits

**Purpose.** One evaluation pipeline verifies, for named commits:

- that the frozen record `R` is correct at its pin;
- that every ledger site and every terminology subject at a candidate is accounted for;
- that a candidate is exactly `H` plus the ledger;
- that a landing merge composes `main` with the candidate exactly.

Each mandatory check of the amended plan is one configuration of this pipeline (sec. 11).

**Non-goals.**

- **Scientific correctness.** A PASS establishes coverage and provenance only. It does not show
  that a replacement keeps its finite-only, conditional or open qualification. It does not show
  that a classification rule's reading is right. It does not show that the frozen map's 16 fuzzy
  and 83 anchor relocations chose the right line at the pin. Those questions stay with:
  - the classification records' reviewers;
  - the plan's independent non-author review of the exact head;
  - the owner's decisions.
- **Row dispositions.** The tool reclassifies no row. Row, code and owner are carried from the
  frozen map, and no record may change them.

**Residual limits.**

- Coverage is defined by the sites, the profiles and the rules. A removed qualifying sentence is
  not detected if it matches no profile and sits next to no context-required site.
- The context mapping is a preregistered heuristic.
- A rule fingerprint recognizes only identical text. Any edited legitimate use returns to
  REVIEW_REQUIRED.
- Delegated checks stay outside the tool's semantics, even when their evidence is bound to `X`.

## 2. Pipeline and subject kinds

### 2.1 Pipeline stages

Every run executes the same stages in a fixed order. A stage that fails stops all later stages.

1. **Usage.** Arguments are parsed and the `--out` guard is applied.
2. **Integrity.** Objects, pins, record hashes and ledger hashes are checked.
3. **Controls.** The in-memory preflight controls run.
4. **Identity.** Every subject is located.
5. **Provenance.** Ledger splices, HP adjudications and reconciliations are applied.
6. **Classification.** Profiles, rules and records are applied.
7. **Outcome.** The overall result is computed.

### 2.2 Subject kinds

Each subject kind has its own anchor and context rule.

| Kind | Anchor | Context | Source |
|---|---|---|---|
| `site` | exact pin line bytes, `pin_count`, `ordinal` | sec. 4 | frozen `sitemap.json` |
| `splice` | id, span, `old_sha256`, `new_sha256` at `H` | the image's offset in `X` | `ledger.json` at `F` |
| `hit` | file, segment, `line_sha256` (unique in its tree) | the sentence and its neighbours | profiles (sec. 6.1) |
| `pin` | check file, exact literal, target file, occurrence counts at `H` and at `X` | none | Python literals of tracked checks, by `ast` |
| `mirror` | edit id pair (`mirror_of`) | none | `edits.json` at `F` |
| `path` | path and blob id in each role | none | the role trees (sec. 13) |
| `delegated` | delegation entry id | none | `delegation.json` at `F` (sec. 7) |

### 2.3 Operations

| Op | Subcommand | Roles used |
|---|---|---|
| A | `record` | `E`, plus the record commit |
| B | `coverage` | `E`, `H`, `X` (and `L`) |
| C | `execution` | `H`, `X`, `M`, `L` |
| D | `terms` | any one commit |

All four operations share the code paths of the pipeline stages.

### 2.4 Ledger fields

The ledger adapter (sec. 16.3) reads the ledger. The rules below are the A1 adapter's.

- `retained_unchanged` (D032, D039): each id must exist in `edits.json`, must have no splice, and
  must have its site text byte-identical at `H` and at `X`. Otherwise the result is FAIL
  `retained-changed`.
- Every other unread ledger field is reported under `ignored_fields`. An unknown schema id is
  ERROR `SOURCE_CHANGED`.

***

## 3. Historical provenance obligation `HP` (segment E..H)

### 3.1 Pinned merges

The A1 configuration record (sec. 16.4) pins the merges by full commit id. The engine contains
no merge ids. The tool cross-checks each pinned merge against the PR number in its subject, and
never resolves a merge from subject text.

| PR | Merge commit | First parent | Sites first changed |
|---|---|---|---|
| #1470 | 0cd5d5bfb4f6641c8b08706c4eb636ee730ebbf0 | 1c7eedc402eafd2bac654484fa790874a33f444d | 15 |
| #1473 | a1f38284d21338b66119c870a551a670c73e3fa7 | f1c8c6b18b245c2faaa68abb464d70ab332b7bec | 15 (plus 3 second steps of #1474) |
| #1474 | 0ba358ccf05eb461c3a5bd686062f65115c293fc | a1f38284d21338b66119c870a551a670c73e3fa7 | 23 |
| #1472 | 4de2eabd6c7c88dc214db70a813ec44b8641b630 | 0adc410c4ad8c3ff51fc77ebb2e055506d758fc8 | 12 |
| #1475 | 7f28886f4cc96fbfa7407af1fdc37de2f0e562e5 | 4de2eabd6c7c88dc214db70a813ec44b8641b630 | 48 |
| #1494 | 53c6601a10419b6b333cc992474272501ab542af (= `H`) | fd9f99cc8866bd4f4244298f819fa99d5c707fba | 0 |

The first-parent chain from E to H has 14 commits. Six of them change the corpus.

### 3.2 Region definition (independent of any diff algorithm)

For a site, the region is a block of whole lines. For each first-parent commit `c` with parent `p`
in E..H, in order, the region is updated as follows.

1. **Carried.** If the region occurs exactly once as a whole-line block in both `p` and `c`, it is
   carried unchanged.
2. **Not unique at the parent.** If it does not occur exactly once in `p`, the site is FAIL
   `provenance-ambiguous`.
3. **Changed at this commit.** Otherwise the site is changed at `c`:
   - The upper anchor is the nearest line above the block in `p` that occurs exactly once in `p`
     and exactly once in `c`. If there is none, the sentinel `BOF` is used. The lower anchor is
     chosen the same way below the block, with the sentinel `EOF`.
   - The anchors must keep their order in `c`. If they do not, the site is FAIL
     `provenance-ambiguous`.
   - The pre-region is the lines of `p` strictly between the anchors. The post-region is the lines
     of `c` strictly between the anchors. Both are trimmed of leading and trailing blank lines.
   - The step `{commit c, parent p, position k, pre_sha256, post_sha256}` is recorded. The
     post-region becomes the region.

These rules depend only on the two texts. An empty post-region means the site was removed in that
step. A step at a commit that is not in sec. 3.1 is FAIL `provenance-foreign`.

### 3.3 HP adjudication record

The record is reviewed, immutable and stored in the audit directory, with the lint of sec. 6.3. It
lists each `site_id` with the following:

- `steps`: each step's commit (full id), parent, position, `pre_sha256` and `post_sha256`;
- the carried `row`, `code` and `owner`, which must equal the frozen values; otherwise FAIL
  `adjudication-row-changed`;
- `semantic_classification`: which qualification is visible, with the reason;
- `hit_classifications` for every profile hit in the final region (sec. 8), bound by
  `line_sha256`;
- `context`: the pin and H context hashes plus a semantic statement, required when sec. 4 marks
  the site and its context changed in E..H;
- `author`, `reviewer`, `review_record` and `owner_record`.

The tool recomputes the walk of sec. 3.2 and compares it with the record. The result is:

- `provenance-adjudicated` only if every step matches exactly;
- FAIL `provenance-mismatch` if a commit or hash differs;
- FAIL `provenance-gap` if a step is missing or extra;
- FAIL `provenance-foreign` or `provenance-ambiguous` as in sec. 3.2;
- FAIL `hp-unadjudicated` if no record names the site.

### 3.4 Resumed tracking and HP/RET overlap

- An adjudicated site resumes tracking in H..X from its final region at H, under the ledgered
  rules of v1 sec. 4.3. It then becomes `authorized-replacement`, `authorized-removal`,
  `unchanged`, `moved` or a RET FAIL.
- An HP site whose H region is touched by any H..X splice keeps two independent entries:
  - in `HP`: its provenance status;
  - in `RET`: its H..X status, with `hp_overlap: true` and the splice ids.

  Neither entry is counted in the other obligation's totals. An E..H edit is never reported as a
  retirement edit, and a retirement splice is never reported as historical.
- Without an adjudication, an HP site stays unresolved. Its RET entry is then
  `untracked-hp-overlap`, a FAIL listing the overlapping splices. This makes the retirement's
  rewrites of historical sites visible before any adjudication exists.
- At T1' (sec. 0.3): 19 HP sites, overlapped by 31 distinct splices.

### 3.5 Context changes in E..H

Every item is assigned to the segment in which its change occurred. A context change on a
meaning-required site (sec. 4) that occurred in E..H is an `HP` item. It is resolved only by the
`context` field of that site's HP adjudication, or of a context adjudication for an unchanged site.

***

## 4. Preregistered context rule

Decided at S0, before any implementation output. The rule is stated per frozen s3 value. The
mapping below is the proposal for owner adoption. Its counts at T1' were measured after the
mapping was chosen on its principle and are reported, not tuned.

**Context definition.** The ordered pair of the nearest non-blank line above and the nearest
non-blank line below, with sentinels `BOF` and `EOF`. Its hash is
`sha256(above + 0x00 + below)`, taken at the pin and at every tree.

**Identity.** Context is required for identity when `pin_count > 1`, or when the current text is
not unique (v1 sec. 4.4). A context change then makes the site FAIL `ambiguous`. All 697 pin lines
are unique at E.

**Meaning.** The principle: context is required exactly when the frozen record does not establish
that the qualification is visible on the site's own line.

| Frozen s3 value | Sites | `meaning_context` |
|---|---|---|
| visible (names the hypothesis); rewritten at deletion | 194 | false |
| visible (P0/P1/P2 disposition) | 144 | false |
| visible (applied splice) | 5 | false |
| visible (none: the (NR) corollary ...) | 3 | false |
| n/a | 136 | false |
| not determined: Q3 census | 81 | true |
| not determined | 28 | true |
| per unit regression audit (#1468) | 45 | true |
| per unit Q1 corrections (Step 2) | 28 | true |
| per unit Step-2 phase | 15 | true |
| per unit R6 corrections (Step 2) | 9 | true |
| per unit R1/R2 scoping | 8 | true |
| per unit Q2 | 1 | true |

A reviewed context adjudication may also set `meaning_context` to true for a further site. It can
never set it to false for a site the table marks.

### 4.1 Decision

| Condition | Result |
|---|---|
| `meaning_context` true, context changed, no context adjudication matching both hashes | FAIL `context-meaning-unverified` |
| `meaning_context` true, context changed, matching adjudication | PASS |
| `meaning_context` false, context changed | PASS with `context_changed: true`; requires verified identity and identical site bytes |

A context adjudication records `site_id`, `segment`, `from_context_sha256`, `to_context_sha256`
and a semantic statement that the qualification is still visible or still stated. It also carries
the lint fields of sec. 6.3.

### 4.2 The real-tree cases at T1'

There are 52 unchanged sites whose context differs from the pin:

- 27 changed in E..H;
- 22 changed in H..T1';
- 3 changed in both segments.

Of these, the table marks 12:

| Origin | Cases | Result under the rule | Resolved by |
|---|---|---|---|
| E..H | 6 `not determined`, 1 `per unit` | HP FAIL `context-meaning-unverified` | the HP or context adjudication of sec. 3.5 |
| H..T1' | 2 `not determined`, 3 `per unit` | RET FAIL `context-meaning-unverified` | a context adjudication reviewed against the retirement's edits |

The two contradictory cases named in addendum 3 are the 2 `not determined` H..T1' cases. Under
this rule they are RET FAILs. RT-T (sec. 10.3) states this. It does not claim "no RET FAIL".

***

## 5. Outcomes, exit codes and output

| Outcome | Exit | Emitted when |
|---|---|---|
| PASS | 0 | every check holds and every control is green |
| FAIL | 1 | at least one FAIL item |
| REVIEW_REQUIRED | 10 | no FAIL item, at least one REVIEW item |
| USAGE | 64 | an argument error, `--help`, or a refused `--out` |
| ERROR | 65 | an integrity error (list below) |
| VOID | 70 | a preflight or self-test control failed |
| INTERNAL | 71 | any uncaught exception, wrapped |

**Integrity errors.** These produce ERROR:

- `PIN_MISMATCH`, `RECORD_TREE_MISMATCH`, `SCIENTIFIC_BASE_MISMATCH`, `MAIN_NOT_DESCENDANT`;
- `SOURCE_CHANGED`;
- a ledger hash, span, overlap or base mismatch;
- `edits_sha256` mismatch;
- an encoding error (not UTF-8, or CR present);
- an unresolvable object.

**Exit 2 is never emitted.** The parser overrides `ArgumentParser.error` and the `-h`/`--help`
action so that both exit 64, because Python's argparse default of 2 would otherwise collide with a
review result.

Evaluation order fixes precedence: USAGE, INTERNAL (at any stage), ERROR, VOID, FAIL,
REVIEW_REQUIRED, PASS. Only exit 0 is acceptance. No flag converts REVIEW_REQUIRED.

**When no `result.json` is written.** In the USAGE case nothing is written to `--out`. One JSON
object with the same schema id, `outcome: "USAGE"` and the parser message goes to stderr. This is
the only case without a `result.json`.

**Frozen code.** Every call into frozen code in op A is wrapped. An exception becomes a structured
INTERNAL or ERROR with its class and message. The frozen `main()` is never called, so its line-523
`TypeError` cannot be reached.

**Output form.** Schema `oi-ledger-coverage/3`, which extends v2 sec. 7 with the review's v1 Q5
fixes:

- `site_counts`, `finding_counts` and `hit_counts` are separate;
- items carry `file` and `line` where applicable, and are sorted by
  `(obligation, class, subject, segment, fingerprint)`;
- the fingerprint is the SHA-256 of canonical JSON (sorted keys, no whitespace, UTF-8, null as
  `null`) over fields that do not depend on any diagnostic algorithm. For `unauthorized-edit` that
  is the expected and actual file hashes and the segment; difflib ranges are diagnostics only;
- every hit carries a `segment` and the tree it was scanned in. `pre_existing` is computed by the
  same scan at the prior endpoint;
- `repo_head` is removed;
- the output is written with sorted keys, indent 1, `ensure_ascii` true and a final LF;
- site fields: `pin_count`, `ordinal`, `pin_context_sha256`, `current_context_sha256`,
  `context_required`, `meaning_context`, `provenance` (record id or null) and `hp_overlap`;
- `covered_paths` lists exactly the paths the run's verdict covers. A PASS states nothing about
  any other path;
- an adjudication naming a segment outside the chain is `out-of-scope`, which is reported but is
  not a finding.

**Explanation.** Every subject carries an explanation with:

- the subject id and kind;
- the anchor and its hashes;
- the provenance chain (segment, splice ids, HP steps, reconciliation id);
- the rule id and rule blob hash, or null;
- each matcher's result;
- the resulting state;
- for REVIEW_REQUIRED, `resolution_needed`: the record kind and the fields a reviewer must supply.

The explanation is part of the JSON Schema. The outcome is a pure function of `preflight`,
`record_checks` and `items`. An independent checker of about 30 lines recomputes it (S7).

**Boundary cases.**

- A splice overlaps a site if `start < site_end` and `end > site_start`. A zero-length splice at an
  interior offset also overlaps.
- A hit line is "in a splice image" if it contains the splice's offset in `X`. Empty images are
  included, for example D029 at Substratum.md:268.
- A last line without LF is a line. Its span ends at end of file.

***

## 6. Profiles, rules and record lint

### 6.1 Scan profiles

Profiles are extracted from their source blobs by `ast` or JSON, never retyped. Each records its
source blob and the SHA-256 of its patterns.

**Review profiles.** A hit is REVIEW_REQUIRED unless held or classified.

| Profile | Source |
|---|---|
| `p0-core`, `p0-para` | Phase-0 `sites.json` |
| `ledger-ext` | `EXTENDED_PATTERNS` in `R/ledger_check.py` |
| `ptr` | `PTR` in P's `edits_check.py` |
| `repo` | `REPO_PAT` in P's `edits_check.py`; scope "active files", sec. 11 item 11 |
| `count-grep` | the literal list of sec. 11 item 7: "Fourteen", "six structural", "sixth of" |

**Deny profiles.** Any match is FAIL. They are evaluated on every sentence of every in-scope file,
not only on hits of other profiles (addendum 4, correction 3a).

| Profile | Source and scope |
|---|---|
| `DR-1`..`DR-4` | sec. 6.4 |
| `register` | `REG` and `CAPS`/`CAPS_OK` in P's `edits_check.py`; added text only |
| `infinity` | `INF` less the `NEUTRAL` disclaimer, in P's `edits_check.py`; added text only |

**Sentence splitter (versioned with the schema).** A sentence ends at `.`, `?` or `!` followed by
whitespace and then an uppercase letter, a `*`, or end of paragraph. It does not end:

- inside `$...$` or a backtick span;
- after a word on a fixed abbreviation list: `sec.`, `Sec.`, `e.g.`, `i.e.`, `cf.`, `Fig.`,
  `Eq.`, `Eqs.`, `No.`, `vs.`, `et al.`, `Ch.`, `App.`, `Thm.`, `Prop.`, `Lem.`;
- after a single capital initial.

A paragraph is a maximal run of non-blank lines. A sentence never crosses a paragraph boundary.

### 6.2 Rule schema `oi-term-rules/2`

A rule file is an immutable record: a change is a new file, which carries `supersedes: {path,
blob_sha256}`.

**Allow rule.** Its fields:

- `id` (never reused);
- `profiles` it addresses;
- `scope.files`: exact paths; mirrors are named explicitly;
- `matcher.literal`, which must contain the trigger, defined as the profile match span of each
  fingerprinted sentence at `recorded_at`;
- `matcher.context`: required co-occurring literals in the sentence or its neighbouring
  sentences, for example the enumerated list;
- `matcher.negative`: literals or regexes that must not match;
- `context_required`;
- `max_instances`, equal to the number of fingerprints;
- `fingerprints`: `{file, sentence_sha256, context_sha256}`;
- `recorded_at`;
- `positive_examples` and `negative_examples`, at least one of each. These become controls;
- `reason`;
- `author`, `reviewer`, `review_record` and `owner_record`.

**Deny rule.** Its fields:

- `id`;
- `pattern`: a reviewed regex, or a two-part sentence test as for DR-3;
- `scope`: `all-corpus` or exact paths;
- `positive_examples`, at least one, which the rule must match;
- `negative_examples`, at least one, which the rule must not match, for example the W1 and W2
  sentences;
- `reason`;
- `author`, `reviewer`, `review_record` and `owner_record`.

Fingerprints and `max_instances` do not apply to deny rules.

**Applying an allow rule.** The rule applies only if all of the following hold:

- the hit's file is in scope;
- the literal covers the trigger;
- the context matcher holds;
- the negative matcher fails;
- the sentence and, if required, the context equal a fingerprint;
- no deny profile matches.

No rule ever deletes text from the line before testing. A rule whose negative matcher also matches
the subject yields FAIL `rule-negative-match`, not PASS.

### 6.3 Record lint (rules, PIN_OK, reconciliation, HP, context, hit classification, delegation)

Every reviewed record kind carries `author`, `reviewer`, `review_record` and `owner_record`. The
owner record is quoted with its author and time (sec. A.42 item 7). A record fails the lint, with
FAIL `record-invalid`, on any of these:

- a missing field;
- `reviewer` equal to `author`;
- a record not read from the git object store at its pinned commit;
- a blob hash that differs from its pin. The pin is in `F`'s PREREG pin table for records frozen
  with the plan, and in the record's own landing commit otherwise;
- a broken `supersedes` chain;
- a reused id.

**Widening of an allow rule.** Any of the following, compared with the superseded version, is
widening:

- added files;
- a changed or shorter literal;
- fewer context or negative literals;
- **any change to the fingerprint set**, including a swap with the count unchanged (control A3r);
- a larger `max_instances`;
- `context_required` turned off.

**Widening of a deny rule.** A changed pattern, a narrower scope, or removed examples.

Widening without a `widening_review` record by a different non-author reviewer is FAIL
`record-invalid`.

**Examples and fingerprints.** Each fingerprint must be reproduced by a sentence of its named file
at `recorded_at`. Each example must behave as stated. Otherwise the record fails the lint.

**Kind-specific rules.**

- **PIN_OK.** An entry is valid only if listed in `F`'s pin table, or in a reviewed record pinned
  by the freeze. An entry dated after `F` is FAIL `pin-broken`.
- **Reconciliation.** A record written after `F` is valid only for a side change on `M`, and it
  never changes a decision of op C on `X` (sec. 13.3).

### 6.4 Seed deny rules (for review; measured in sec. 14)

These are the review's addendum 4 forms. Each must catch its control and must match neither the W1
nor the W2 sentences. Measured: DR-1 matches 59 lines at H and none at T1', and DR-1..DR-4 match
0 lines at T1'.

- **DR-1.** One of three alternatives:
  - `\b(six|seven|sixth|seventh)\b[^.;]{0,40}\bstructural (assumptions?|axioms?|posits?)\b`
  - `\bA1\s*[-\u2013]\s*A6\b`
  - `\b(six|seven|sixth|seventh)\b[^.;]{0,40}\bstructural propert(y|ies) of the substratum\b`
- **DR-2.** `\b(sixth|seventh)\b[^.;]{0,40}\bstructural (property|assumption|axiom|posit)\b[^.;]{0,80}\bfinit`
- **DR-3.** A sentence that contains "structural propert", "structural assumption", "structural
  axiom", "structural posit", "posit", "premise" or "axiom", and in which "one of which", "one of
  its", "one of the", "among" or "includ..." is followed within 60 characters by "total
  finiteness", "total-finiteness", "finite in total" or "totally finite".
- **DR-4.** `\(A1\)[^.;]{0,60}\b(finit\w*|substratum|configuration space)`

### 6.5 Seed allow rules W1 and W2 (for review; not adopted)

**W1: "six structural properties" counting the bijection's properties.** At T1' the profile
`count-grep` matches 7 lines:

- `papers/SM.md:1394`
- `book/ch09-universality.md:137`
- `book/ch19-open-problems.md:198` and `:212`
- FULL lines 2554, 5270 and 5284

There is one rule per distinct sentence. The context matcher requires the enumerated list
(isotropy, sublattice structure, link content, anomaly cancellation, taste content, generation
count) or "of the bijection". SM.md:1394's sentence carries neither, so its rule sets
`context_required: true` and cites SM's own definition of the six properties. The negative matcher
is: `A1`, `A1-A6`, `finit`, `assumption`, `axiom`, `of the substratum`.

**W2: the anomaly condition "(A1)".** The profiles `ptr` and `repo` match it at
`book/appendix-b-derivations.md:235` and `:246`, and at FULL lines 5914 and 5925. The context
matcher requires `SU(3)` or `anomaly`. The negative matcher is: `Finiteness`, `finit`, `posit`,
`substratum`, `configuration space`. These rules replace the `EXPLAINED`/`RESIDUAL_ALLOW`
substring entries and the blanket `(A1)` strip.

***

## 7. Delegation contract `delegation.json` (schema `oi-delegation/1`)

### 7.1 Location and pinning

- The contract is one structured record in the amended plan's record directory, beside
  `ledger.json` and `edits.json`. It is frozen with the plan at `F`, and its SHA-256 is listed in
  `F`'s PREREG pin table (the sec. 26.4 mechanism).
- The tool reads it only as `--delegation F:path`. A hash that differs from the pin is ERROR
  `SOURCE_CHANGED`.
- It enumerates exact paths, with no globs.
- The path set must equal what the ledger implies: `tex_sources(ledger)` for TeX, and the fixed
  paths of the other classes. A changed path at `X` outside the ledger and the contract is FAIL
  `unauthorized-change`.
- Evidence not named by the frozen contract is never accepted, however and whenever it is
  supplied.

### 7.2 Rules common to every class

- Delegated checkers run only from `F`'s blobs, in a disposable full clone at exact `X` created
  under `--out`. They never run in the user's repository or a worktree of it. This contains
  preserve_check's `git worktree add` (gap 6).
- The tool records each checker's blob SHA-256, its command line, its exit status and the SHA-256
  of its result file.
- **Evidence absent** (a run not made, or no result file): REVIEW_REQUIRED
  `delegated-evidence-missing`.
- **Evidence defective**: FAIL `delegated-evidence-invalid`. That is any of:
  - a schema other than `a1exit-checker-result-v1`;
  - `checker` other than `preserve_check.py`;
  - `plan` other than `F`;
  - `ledger_base` or `base` other than `H`;
  - `ledger_sha256` other than `F`'s ledger;
  - `candidate` other than `X`'s full 40-hex id;
  - a nonzero exit;
  - `verdict` other than `pass`;
  - a required check missing, not `pass`, or with non-empty discrepancies;
  - a checker blob that differs from `F`'s copy.
- A class PASSes only if every required item holds.

**preserve_check.py gaps (addendum 4).** The amended plan must close gaps 1, 2, 5 and 7: record the
resolved candidate commit and tree and the checker blob, write a result on a usage error or crash,
and fail on a missing STALE id. Until it does, the contract's binding cannot hold, and the affected
classes are REVIEW_REQUIRED (missing) or FAIL (inconsistent). Gap 3 is met by the PDF class below.
Gap 4 is met by reading only the named checks' `status` and `discrepancies` emptiness, never their
text. Gap 8, the stale docstring, is corrected in the amendment.

### 7.3 Classes

| Class | Paths | How the tool verifies it |
|---|---|---|
| `tex` | the 9 TeX files of `tex_sources(ledger)`: Complexity, Computation, GR, Main, Methodology, SM, Structure, Substratum and FULL | delegated: `preserve_check.py --commit X --plan F --result-json OUT` in the clone, with the commit-mode checks "candidate against base, ledger, regenerated artifacts and plan record" and "scope assertions of amendment sec. 31" both `pass`. Native as well: each file's last line is `% source-sha256: <sha256 of X's .md>`, and the path set equals `tex_sources` |
| `pdf` | the 9 PDFs | delegated: `preserve_check.py --tree ... --pdf-compare BUILT --pdf-out OUT --plan F --result-json OUT` in the exact-head CI run on `X`. Required: `candidate_commit` and `candidate_tree` equal to `X`; a host run record (API) with `head_sha = X`, the named workflow and job, and conclusion success; the result hash equal to the uploaded artifact. Native as well: each PDF blob differs from `H`'s |
| `record-dir` | the plan's record directory | native: equals `F`'s blobs; additions only as enumerated under `execution/` |
| `sc42` | `verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json` | native re-execution in the clone at `X`: contains ca3a5bb2...; `--verbose` (plain and `-O`) exits 0 and is byte-identical to the file; `--self-test` (plain and `-O`) is byte-identical to the controls file, which equals `H`'s |
| `coverage-ledger` | `verification/coverage/LEDGER.json` (a ledgered file) | native: `H` plus its splices, except the fingerprint values of the seven STALE ids; each id exactly once; each value equals `tools/proof_census.py --json` (`X`'s blob, run in the clone, exit 0); any other byte FAIL. This replaces v2's "delegated" |
| `ci` | the Lean kernel, Mathlib, R7 guard, `bohr_frequency_probe.py` and `guards_check.py --mutants` jobs | delegated: host run and job records (API) for the exact-head run on `X`, each named job concluding success |

Missing evidence is never PASS.

***

## 8. Classification of hits and the review load

### 8.1 Rules (addendum 3 change 8; owner Q2)

| Hit | State until classified | Resolved by |
|---|---|---|
| any profile hit in an authorized replacement image, inside or outside a site region (`new-pattern-in-replacement` when the pattern is absent from the FROM region) | REVIEW_REQUIRED | a hit classification record or an allow rule |
| a hit on an unchanged site line | PASS | the frozen classification |
| a hit in an HP region | REVIEW_REQUIRED | the HP adjudication's `hit_classifications` |
| any other unheld hit | REVIEW_REQUIRED | a record or rule |
| a deny match anywhere | FAIL | not resolvable by a record |

A hit classification record binds:

- `file` and `line_sha256`, which must be unique in the tree;
- the segment;
- the splice id or HP step;
- the patterns;
- the semantic classification (which qualification is visible, with the reason);
- the lint fields.

It states that it classifies meaning, and that the splice provenance is recorded separately.

### 8.2 Review load before the amended plan can pass as written

Counted at T1', with these sets disjoint:

| Set | Lines | Source |
|---|---|---|
| Hit lines in the 197 site replacement regions | 86 | mine; the review gives 84 |
| Hit lines in splices on lines unheld at H | 16 | review figure, reproduced |
| New hit lines on non-site lines (D237, D238, D241, D242, D246, D247, D388) | 7 | review figure, reproduced |
| Pre-existing unheld lines identical at H | 93 | review figure, reproduced |
| HP site adjudications, with `hit_classifications` for their regions | 113 sites | |
| Meaning-context adjudications (sec. 4.2) | 12 | 7 HP, 5 RET |
| W1 and W2 allow rules | 7 + 4 lines | the `count-grep`, `ptr` and `repo` hits |

The `repo` profile (sec. 11 item 11) adds the following. Measured with P's own `classify()` at
T1', there are 0 unexplained lines, but 176 active lines are explained by entries that sec. 6.3
does not admit:

- 96 lines by path-wide "unrelated label" entries;
- 31 lines by path-wide "guard pins" entries;
- 37 lines by substring entries, without fingerprints;
- 12 lines as "kernel identifier" (IDENT), without a rule.

Each needs an exact-path, fingerprinted rule or record. The 5486 lines in historical records and
the 2 lines in generated artifacts are outside the profile's scope. That scope is a reviewed scope
record (prefix lists are allowed only there), and widening it is linted as in sec. 6.3.

The sets overlap: the HP regions' hits are among the 93 + 16. Records may therefore serve two
lines of the table, but each hit line needs exactly one classification.

Until all of the above exist, `coverage` and `terms` at T1' are REVIEW_REQUIRED at best, and FAIL
while any FAIL item of sec. 9 remains.

***

## 9. Complete list of FAIL and REVIEW conditions

### FAIL (exit 1)

Sites:

- `unauthorized-change`, `missing`, `duplicated`, `ambiguous`;
- `context-meaning-unverified`;
- `retained-changed`.

Ledgered files:

- `unauthorized-edit`;
- `unledgered-file-change`.

Historical provenance:

- `hp-unadjudicated`, `untracked-hp-overlap`;
- `provenance-mismatch`, `provenance-gap`, `provenance-foreign`, `provenance-ambiguous`;
- `adjudication-row-changed`.

Hits and rules:

- `deny-match`;
- `rule-negative-match`, `rule-overreach`;
- `record-invalid`;
- `stale-adjudication`.

Pins and mirrors:

- `pin-broken`, `pin-target-missing`;
- `mirror-mismatch`.

Lean:

- `lean-code-change`.

Delegation:

- `delegated-evidence-invalid`;
- an `unauthorized-change` path outside the ledger and the contract.

Tree roles:

- `candidate-parent`;
- `landing-parents`, `landing-first-parent-not-M`;
- `landing-drops-main-change`, `landing-conflict-unresolved`, `landing-extra-change`;
- `base-drift`.

Record checks:

- op A record checks not all holding.

### REVIEW_REQUIRED (exit 10)

- `unclassified`;
- `new-pattern-in-replacement`;
- `unclassified-in-replacement`;
- `rule-fingerprint-mismatch`;
- `rule-stale`;
- `delegated-evidence-missing`;
- `side-change-unclassified` (a change on `M` outside every declared class).

ERROR, VOID, USAGE and INTERNAL are as in sec. 5.

***

## 10. Test matrix

Each control runs in both directions: the mutant gives the stated outcome, and the restored tree
returns to its control outcome. Each expected FAIL names the sec. 9 class that produces it.

### 10.1 Unit and mutation controls (synthetic, in memory)

The v2 controls U1-U15 and M1-M11 stand, with v3 classes and exit codes. The review's controls are
added:

| Id | Case | Expected |
|---|---|---|
| K1 | the neighbour line of a meaning-context site is negated | FAIL `context-meaning-unverified` |
| K2 | the same next to a non-required site | PASS, `context_changed: true` |
| K3 | two site paragraphs swapped | per site, as K1 and K2 |
| K4 | a site line moved to a distant section of the same file | as K1 and K2 |
| B1 | an empty-image splice on a site line | `authorized-removal`; a hit at its offset is "in image" |
| B2 | a multi-line splice (33 exist in P) | `authorized-replacement` with a line range |
| B3 | a zero-length insertion at a line boundary | the overlap rule of sec. 5 |
| B4 | a last line without LF | located and spanned to end of file |
| B5 | a splice making a replacement region non-unique in `X` | FAIL `duplicated` at the next search |
| H1 | HP adjudication naming #1473 where the walk gives #1474 | FAIL `provenance-mismatch` |
| H2 | one step listed where the walk gives two | FAIL `provenance-gap` |
| H3 | a change at an unpinned commit | FAIL `provenance-foreign` |
| H4 | an adjudicated site later rewritten outside every splice | FAIL `unauthorized-change` (RET) |
| H5 | an HP site overlapped by a splice, with no adjudication | FAIL `untracked-hp-overlap`, visible in HP and RET |
| H6 | an adjudication changing a site's row | FAIL `adjudication-row-changed` |

### 10.2 Adversarial controls (each tied to its rule)

| Id | Case | Expected | By |
|---|---|---|---|
| L1 | the W1 sentence shifted by 40 lines | PASS | W1 rule |
| L2 | the W2 lines moved | PASS | W2 rule |
| L3 | a W1 sentence copied inside scope | FAIL `rule-overreach` | `max_instances` |
| L4 | a W1 sentence copied outside scope | REVIEW_REQUIRED `unclassified` | scope |
| V1 | "The six structural properties of the substratum ..." | FAIL `deny-match` | DR-1 |
| V2 | "... of the bijection (isotropy, ...), one of which is total finiteness" | FAIL `deny-match` | DR-3 |
| V3 | "(A1) the substratum is finite in total" in appendix B | FAIL `deny-match` | DR-4 |
| V4 | "the framework's sixth structural property, finiteness of the bijection" | FAIL `deny-match` | DR-2 |
| V5 | "**(A1) Finiteness.** The configuration space is finite." in appendix B | FAIL `deny-match` | DR-4 |
| V6 | "the six structural properties of the substratum, including finiteness" | FAIL `deny-match` | DR-1 |
| V7 | V2 with DR-3 removed from the profile set | REVIEW_REQUIRED `rule-fingerprint-mismatch` | shows DR-3 is the operative rule |
| V8 | V4 with DR-2 removed | PASS (no hit) | shows why deny rules are profiles |
| D1 | DR-1..DR-4 run at T1' | 0 matches required | seed control |
| D2 | DR-1 run at H | matches required (59 measured) | countercontrol |
| A1r | rule scope widened to `book/` | FAIL `record-invalid` | sec. 6.3 |
| A2r | literal shortened to `(A1)` | FAIL `record-invalid` | widening |
| A3r | fingerprint swapped, count unchanged, no widening review | FAIL `record-invalid` | widening: any fingerprint change |
| A4r | widening review signed by the rule's author | FAIL `record-invalid` | reviewer is not the author |
| A5r | allow rule fingerprinting a sentence that a deny rule matches | FAIL `deny-match` | deny precedence |
| A6r | literal not covering the trigger | FAIL `record-invalid` | trigger definition |
| A7r | reused rule id | FAIL `record-invalid` | id rule |
| A8r | allow rule with no negative example | FAIL `record-invalid` | examples |
| A9r | rule widened by one alternation | FAIL `record-invalid`, and caught by its own negative example | widening and examples |
| A10r | deny rule narrowed in scope | FAIL `record-invalid` | deny widening |
| S1r | a fingerprinted sentence edited | REVIEW_REQUIRED `rule-fingerprint-mismatch` | sec. 6.2 |
| S2r | a fingerprinted sentence deleted | REVIEW_REQUIRED `rule-stale` | |
| N1 | a PIN_OK entry dated after `F` | FAIL `pin-broken` | sec. 6.3 |
| N2 | a reconciliation record that changes a decision on `X` | FAIL `record-invalid` | sec. 13.3 |
| G1 | delegated result whose `candidate` is an abbreviation | FAIL `delegated-evidence-invalid` | sec. 7.2 |
| G2 | no delegated result supplied | REVIEW_REQUIRED `delegated-evidence-missing` | sec. 7.2 |
| G3 | LEDGER.json with one STALE id removed | FAIL | sec. 7.3 |
| X1 | `record --pin H` | ERROR `PIN_MISMATCH`, exit 65 | sec. 5 |
| X2 | an exception injected in classification | INTERNAL, exit 71 | sec. 5 |
| X3 | an unknown flag | exit 64, stderr JSON, nothing written | sec. 5 |
| X4 | `--help` | exit 64 | sec. 5 |
| X5 | a missing required argument | exit 64, never 2 | sec. 5 |
| X6 | a run whose outcome is REVIEW_REQUIRED | exit 10, distinct from X3-X5 | sec. 5 |

### 10.3 Real-tree controls (CI)

The rules are preregistered. The counts are references.

| Id | Run | Rule | Reference |
|---|---|---|---|
| RT-A | `record --pin E --record H` | PASS | frozen replay: 0 errors; 697 anchors |
| RT-E | `coverage --commit E` | PASS | 697 unchanged |
| RT-H0 | `coverage --commit H`, no HP records | FAIL; every FAIL item has obligation HP | 113 `hp-unadjudicated`; 7 HP context items |
| RT-T0 | `coverage` at `X = T1'`, no records | FAIL. HP: 113. RET: 19 `untracked-hp-overlap`, 5 `context-meaning-unverified`. REVIEW: sec. 8.2 | 383 unchanged (168 moved), 197 replaced, 4 removed |
| RT-T | RT-T0 with all reviewed records of sec. 8.2 | PASS only when every record verifies; any missing record leaves REVIEW_REQUIRED or FAIL | |
| RT-C | `execution` at `X = T1'` with `F` = the amended freeze | candidate checks as sec. 11; PASS only with contract evidence | 399 splices verified at H; 23 corpus and 21 other ledgered files conform, except LEDGER.json under the `coverage-ledger` class |
| RT-D | `terms --commit T1'` | 0 deny matches; W1 and W2 PASS with their rules | |
| SW1 | per-site sweep at E: each of the 697 sites, one token deleted | exactly one FAIL naming that site | |
| SW2 | per-site sweep at H: each of the 584 sites | exactly one FAIL naming that site | |

***

## 11. Mapping of the mandatory sec. 11 checks (P's PREREG sec. 11) to the tool

Every command adds `--config F:<record dir>/retirement-config.json` and `--out DIR`, and reads
`F`'s records by object id. Profiles, rules, the delegation contract and the HP obligations come
from the configuration record. Paths given as `F:...` below are resolved through it. `X` is the execution head.
The "Countercontrol" column gives a mutant on which the original check fails; the tool must also
give a non-PASS result on it, and a FAIL wherever the original's failure was a hard failure.

| # | Original check | Tool command | Expected at a T1'-style `X` | Countercontrol |
|---|---|---|---|---|
| 1 | `edits_check --commit X`: every `new` present; residual pointer scan zero unqualified | `execution --scientific-base H --candidate X --ledger F:ledger.json --edits F:edits.json` (splice postconditions) and `terms --commit X --profile ptr` | splices PASS; `ptr` has 4 hits (W2), PASS with the W2 rules, else REVIEW | one splice reverted in `X`: FAIL `unauthorized-edit`. Original: the `new` string is absent |
| 2 | `ledger_check build` and `check`; CK1-CK8 PASS; extended scan 0 unqualified | `record --pin E --record F` and `coverage --commit X --segment E..H --segment H..X=F:ledger.json --hp F:hp.json --classify F:...` | FAIL or REVIEW (RT-T0) until the records of sec. 8.2 exist; PASS only with them | the frozen self-test's countercontrols at E: unclassified new site gives REVIEW_REQUIRED; dropped Phase-3 site gives FAIL `missing`; J row with S1 Yes gives FAIL (op A `record_checks`) |
| 3 | build; no dropped glyphs; page and median-character counts | `execution ... --delegation F:delegation.json` (classes `tex`, `pdf`, `ci`) | PASS only with bound exact-head evidence | evidence from another `head_sha`, or `build.rc` nonzero: FAIL `delegated-evidence-invalid` |
| 4 | `coverage_check.py`; STALE entries re-affirmed | `execution` class `coverage-ledger`, plus `ci` job `coverage_check` | PASS iff the seven values equal `proof_census` | one STALE value altered, or an id removed: FAIL |
| 5 | register scan of added lines: 0 | `execution` profile `register` on replacement text | PASS (P's `--static` recorded 0) | a splice adding "no longer": FAIL `deny-match` |
| 6 | infinity scan of added lines: 0 | `execution` profile `infinity` on replacement text | PASS (0 recorded) | a splice adding "is infinite": FAIL |
| 7 | corpus grep: only ledger false positives for `\bA1\b` and related terms; posit counts zero | `terms --commit X --profile ptr,count-grep,DR-1..DR-4` | `\bA1\b` 4 lines (W2); `count-grep` 7 lines (W1); DR 0. PASS with W1 and W2, else REVIEW | the H-form "six structural assumptions" reinstated: FAIL `deny-match` (DR-1). See note 1 |
| 8 | mirrors byte-identical | `execution` subject `mirror` | PASS (P's `--static`: 0 findings) | FULL mirror text altered: FAIL `mirror-mismatch` |
| 9 | census registry notes updated in the same commit | `execution` conformance of `verification/lean-manuscript-census.json` (15 splices) | PASS | one registry splice dropped: FAIL `unauthorized-edit` |
| 10 | Lean docstring-only; kernel and Mathlib builds; CI | `execution` subject `lean` (equal outside comments) and class `ci` | PASS with evidence | a Lean definition changed: FAIL `lean-code-change` |
| 11 | `edits_check --repo-scan --final --commit X`: 0 unexplained | `terms --commit X --profile repo --scope F:repo-scope.json --rules F:repo-rules.json` | REVIEW until the 176 lines of sec. 8.2 have exact rules; then PASS | a new unexplained `A1` line in a new active file: FAIL in the original, REVIEW here, with `--final` mapping it to FAIL. See note 2 |
| 12 | `edits_check --pins --commit <X's parent>`; guards mutants; R7 and bohr in CI | `execution` subject `pin` (counts at `H` and at `X`) and class `ci` | PASS (the original reported 0 unresolved at its base) | a guard-pin splice dropped: FAIL `pin-broken` |
| 13 | SC-42 regeneration and safeguards | `execution` class `sc42` (native) | PASS iff byte-identical | the result file hand-edited: FAIL |
| 14 | `preserve_check --commit X` (`--base main` when moved) | `execution --scientific-base H --main M --candidate X [--landing L]`, plus the `tex` contract | candidate PASS against `H`; landing per sec. 13 | an extra word in an unledgered file of `X`: FAIL `unauthorized-change`. `L` dropping W's workflow: FAIL `landing-drops-main-change`. Compare the original `--base W`, which failed on `X` only for that workflow file |

**Note 1 (owner decision needed).** Item 7 as literally written ("grep of posit counts ... 'six
structural' ...: zero") fails at T1'. Seven lines contain the legitimate count of the bijection's
properties (W1).

- The plan's own implementation never ran that literal grep. It checked the retired phrases of
  `identifier_sim()`, P lines 331-335.
- The amended item 7 must therefore state the check it means: zero DR-1..DR-4 matches, and every
  `count-grep` hit classified by a reviewed rule.
- This changes the check's text, not its decision on any retired form. D2 shows DR-1 catches all
  59 retired-form lines at H.
- Whether this restatement is acceptable as "passes as written" is for the owner.

**Note 2.** The tool is stricter than item 11's original.

- The original passes a premise line in any path-wide-explained file, for example
  `tools/citation_roles_check.py`. The tool fails it.
- The tool reports an unexplained line as REVIEW_REQUIRED, while the original reports it as a
  failure. With `--final` (the item's own flag), REVIEW items of the `repo` profile become FAIL
  `unclassified`, so the countercontrol is a FAIL in both.

**Other wording the amendment must correct.** Item 4 says "four entries", but preserve_check's
STALE list has seven (sec. 31, nit 5). Item 12's "execution head's parent" becomes "the ledger base
H".

***

## 12. Placement and governance

### 12.1 Placement

- `tools/ledger_coverage.py` holds the executable. Its JSON Schemas and self-test fixtures, held as
  in-memory data, are also under `tools/`.
- A new audit directory under `verification/audits/` (sec. A.36) holds the rule files, scope
  records, HP, context and hit classification records, reconciliation records, and the tool's
  landing record with its commands and counts.
- The plan's `delegation.json`, `hp.json` and rule files frozen with the plan live in the amended
  plan's record directory.
- The tool reads every record from git objects, which `export-ignore` does not affect.

### 12.2 Sec. 11 replacement text (addendum 4, point 1; replaces v2's sentence)

"The tool is part of the verification route adopted by owner decision c.7093128173 (amaybaum,
2026-11-23T06:13:50Z), which supersedes the execution exception of c.7092885251. Under that route
the retirement plan is amended and frozen again so that each of its mandatory checks names an
operation of this tool and its exact command, and passes as written. No check is waived, replaced
after the freeze, or recorded as a deviation. Landing the tool decides nothing about the
retirement: the plan amendment and its freeze, the repeated trials, the execution and the merge
each keep their own owner gate."

### 12.3 Governance

- The tool's landing may add paths only under `tools/` and its audit directory. It touches no
  ledgered path (control R14).
- Records strengthen no claim (sec. A.22, A.46 item 1).

***

## 13. Four trees

The v2 sec. 13 rules stand, with the corrections below.

### 13.1 Roles and invariants

- **`H`** (`--scientific-base`) must equal `roles.scientific_base` in the frozen configuration
  record (sec. 16.2) and the ledger base. Every `base_sha256` must equal `H`'s blob. `R`'s tree at `H` is the pinned tree.
- **`M`** (`--main`) is resolved once and recorded. Its invariants:
  - `H` is on `M`'s first-parent chain;
  - `R`'s tree at `M` is pinned;
  - every path changed between `H` and `M` is a side change, listed with its first-parent commit.

  Side changes are classified by a reviewed side-change class record (for example, the trial
  workflow file, or the tool's landing paths). An unclassified side change is REVIEW_REQUIRED
  `side-change-unclassified`. A side change to a ledgered or corpus path is `base-drift`, a FAIL for
  the landing unless it is reconciled. Side changes are never retirement edits.
- **`X`** has exactly one parent, `H`. Every path in the diff from `H` to `X` is in exactly one
  class: ledgered, delegated or record. Every other path is byte-identical to `H`. No check of `X`
  reads `M`.
- **`E`**, the certified head, descends linearly from `X` when it differs from it. Each further
  commit is classified as `X` is.
- **`L`** has exactly two parents: the first equals the recorded `M` (FAIL
  `landing-first-parent-not-M` otherwise), and the second equals `E`. Each path is composed as in
  v2 sec. 13.2:
  - A ledgered conflict passes only if `L`'s bytes equal `M`'s bytes with `E`'s splices applied at
    `M`-translated offsets, each `old_sha256` re-verified against `M`.
  - A generated-artifact conflict is REVIEW_REQUIRED until it is regenerated from `L`'s sources
    under the contract.
  - Any other conflict is FAIL.

  The diff from `M` to `L` must equal the diff from `H` to `E`, path by path, after translation.

### 13.2 Controls

R1-R14, RT-X, RT-L and RT-L2 stand. R15 is added: an `L` whose first parent is a `main` other than
the recorded `M` gives FAIL `landing-first-parent-not-M`.

### 13.3 Reconciliation records

- A record written after `F` is allowed only for side changes on `M` that the freeze could not
  foresee.
- It never changes any decision of op C on `X`, and never relabels a failing retirement check.
- It carries the lint of sec. 6.3.

### 13.4 Re-resolving `M`

Immediately before landing, `M` is re-resolved from the remote `main` (`git ls-remote`, read-only)
and checked to equal `L`'s first parent. The landing record quotes the resolved id and the command.

**Sequencing safeguard (c.7093128173).** Before the tool lands, RT-L2 is run against a predicted
`M` that contains the tool's landing paths. It must show every side change classified and no
`base-drift`.

***

## 14. How the figures were measured

All figures were measured read-only, with throwaway scripts reading `git show` and
`git cat-file --batch`. Their outputs were written outside the checkout, and the checkout stayed
unmodified.

- **Context.** 52 changes, split by the origin of each change. A change is attributed to E..H if
  the context at H differs from the pin, and to H..T1' if the context at T1' differs from H's.
- **HP walk.** As in sec. 3.2. It gives 113 sites with a unique region at H, 3 two-step sites, and
  19 sites overlapped by 31 distinct splices. For comparison, a whole-file `difflib` hunk image
  gives 18.
- **Hit counts.** Phase-0 and extended profiles, with held sets as in v1 sec. 4.7. That gives 116
  unheld lines (93 / 16 / 7), and 86 hit lines in site replacement regions.
- **DR-1..DR-4.** Applied line by line to every `papers/*.md` and `book/*.md` at H and at T1'.
  Literal greps at T1': `six structural` 7, `\bA1\b` 4, `sixth of` 0, `Fourteen` 0.
- **Repo scan.** P's `edits_check.py` was imported from its blob, and its `classify()` applied to
  every tracked file at T1'.
- **Merge ids.** `git rev-list --first-parent` over E..H, restricted to `papers` and `book`.

***

## 15. Open points for the owner

1. **Item 7.** Is the restatement of note 1 (sec. 11) acceptable, or must the literal grep stand?
   If the literal grep stands, the plan cannot pass at any tree that keeps W1's legitimate
   sentences.
2. **The context mapping of sec. 4.** Adopt it as proposed, or narrow `per unit` to false? Narrowing
   reduces the H..T1' FAILs from 5 to 2 and must be decided on principle, not by this count. The
   review's syntactic criteria (table row, list item, anaphoric start, partial Phase-0 quote) are
   not included. Should any be added at S0?
3. **The HP/RET overlap count.** 19 here against the review's 24. The definition of sec. 3.2
   decides; an independent recount under it is requested.
4. **Review load.** The records of sec. 8.2 are reviewing work the amended plan needs before it can
   pass as written. Who writes and reviews them, and under which authorization (sec. A.45 rule 3)?

***

## 16. Generality: a core independent of any retirement, with frozen per-retirement configuration (condition 9)

### Scope

This section covers design only. It does not include:

- a second real retirement;
- a generic verifier of scientific proofs or semantic correctness;
- any reduction of A1 coverage or preservation obligations;
- any postponement of a v2 review defect.

Only the A1 adapters and one minimal synthetic adapter are specified. The acceptance gate remains
A1 correctness and fail-closed verification. Generalization is accepted only if every A1 control of
sec. 10 and sec. 11 has the same outcome under the configured engine as specified above.

### 16.1 The engine (`tools/ledger_coverage.py` and its package)

The engine is retirement-independent. It contains:

- the pipeline of sec. 2;
- the outcome, exit codes and output of sec. 5;
- the algorithms: anchors (v1 sec. 4.2-4.4), the overlap and image rules (sec. 5), the region walk
  (sec. 3.2), the context hash (sec. 4), sentence splitting (with the abbreviation list supplied by
  the configuration), and rule application and record lint (sec. 6);
- the four role checks (sec. 13);
- the adapter interfaces (sec. 16.3).

It contains no commit or tree id, path of a retirement record, terminology, regex pattern, site or
hit count, PR number, delegation class, s3 value or checker schema.

Control Z9 enforces this. A lint over the engine's source blobs fails on any of the following:

- a 40-hex or 7-hex-or-longer hexadecimal literal;
- any string value occurring in the A1 configuration or its records, other than schema ids the
  engine itself defines;
- any identifier matching the A1 terminology profiles.

Z9 runs in CI and in `self-test`.

### 16.2 Configuration record `oi-retirement-config/1`

**Location and pinning.**

- One reviewed, versioned JSON record, `retirement-config.json`, in the retirement plan's record
  directory, frozen with the plan at `F`.
- Its SHA-256 is listed in `F`'s PREREG pin table, the sec. 26.4 mechanism.
- The tool reads it only as `--config F:path` from the object store. A hash that differs from the
  pin is ERROR `SOURCE_CHANGED`.
- A change after `F` requires a new configuration version and a new freeze.

**Fields.** All fields are required unless marked optional.

| Field | Content |
|---|---|
| `schema` | `oi-retirement-config/1` |
| `config_id`, `version`, `supersedes` | identity; `supersedes` is `{path, blob_sha256}` or null |
| `retirement` | name and accountable Issue |
| `roles` | `scientific_base` (full id); `pin` and `record_commit` (optional, for replay); `side_change_classes` (path or record reference) |
| `corpus` | an exact path list, or declared path sets with stated patterns, linted as scope records (sec. 6.3) |
| `adapters.ledger` | `{adapter, adapter_version, path, blob_sha256, companion: [{role, path, blob_sha256}]}` |
| `adapters.sitemap` | as `adapters.ledger`, or null when the retirement has no frozen site map |
| `adapters.replay` | `{adapter, adapter_version, module_path, record_tree, functions}`, or null (optional) |
| `profiles` | `[{name, kind: review or deny, scope, applies_to: tree or added-text, source: {commit, path, blob_sha256, extractor: {kind, selector}}, pattern_sha256}]` |
| `rules` | `[{path, blob_sha256}]`, rule files `oi-term-rules/2` |
| `context_mapping` | `{source_field, values: {value: bool}, default: "invalid"}`. A value outside the table is a configuration error |
| `sentence` | `{splitter_version, abbreviations}` |
| `hp_obligations` | `[{segment: [from, to], merges: [{pr, commit, first_parent}]}]` |
| `delegation` | `{path, blob_sha256}` (`oi-delegation/1`), or null |
| `operations` | the supported subset of `record`, `coverage`, `execution` and `terms` |
| `controls` | `{path, blob_sha256}`: the retirement's preregistered control set (sec. 10, 11) with expected outcome rules |
| `author`, `reviewer`, `review_record`, `owner_record` | lint fields (sec. 6.3) |

Supported extractor kinds: `json-pointer`, `python-ast-assign` (a module-level name bound to a
string, a tuple of strings, or a compiled regex call with a literal pattern), and `literal-list`.
The extractor's output must hash to `pattern_sha256`.

**Lint.** The configuration takes the record lint of sec. 6.3, with these additions:

- every referenced blob exists at its stated commit with its stated hash;
- `roles.scientific_base` equals the ledger adapter's reported base;
- the `hp_obligations` segments end at `scientific_base`, and every merge is on its first-parent
  chain with its stated first parent;
- every delegation class is known to the adapter set;
- no profile name is duplicated;
- every deny profile has examples in a rule file;
- the controls file names at least one positive and one adversarial control per configured
  operation.

**Widening.** Any of the following, compared with the superseded configuration, is widening and
needs a `widening_review`:

- a scope removed, or a deny profile removed;
- a profile changed;
- a context-mapping value changed from true to false;
- an HP obligation removed;
- a delegation class added.

### 16.3 Adapter interfaces (versioned)

Each adapter has a name and an integer version. The engine accepts only adapter names and versions
in its registry, and anything else is a configuration error.

| Interface | Must return |
|---|---|
| ledger | `base`; `splices [{id, file, start, end, old_sha256, new_sha256, new}]` (byte spans at `base`); `files {path: {base_sha256, expected_sha256}}`; `retained [{id, site_ref}]`; `mirrors [{id, mirror_of}]`; `ignored_fields`; plus validation errors (overlap, hash, schema) |
| sitemap | `pin`; `sites [{site_id, file, pin_line, carried: {row, code, owner}, context_field_value}]`; `override_anchors`; `read_entries` |
| replay | `{equalities: [{name, equal}], errors: [str], self_test: bool}`, computed by calling the named functions of a frozen module in a materialization (v1 sec. 3.2), wrapped (sec. 5) |
| delegation | the classes of sec. 7. A class is an adapter of its own with `verify(evidence, roles) -> PASS, REVIEW or FAIL` and a structured reason |

**The A1 adapters:**

- `a1exit-exact-edit/2` reads `ledger.json` ("a1exit deletion exact-edit ledger v2") and
  `edits.json` ("a1exit deletion edit list v1").
- `a1exit-sitemap/2` reads the frozen `sitemap.json` ("a1exit site map v2") and `rows.json`.
- `python-frozen-replay/1` replays `ledger_check.py`'s `manuscript_digest`, `build`, `render`,
  `splice_block`, `check`, `extended_unmapped` and `self_test`.
- The delegation classes are `preserve-check-v1` (tex, pdf), `record-dir/1`, `rerun-equal/1`
  (sc42), `fingerprint-regen/1` (coverage-ledger) and `host-run/1` (ci).

### 16.4 A1 as the first configuration: where each A1 constant goes

Every constant of v1, v2 and this document's sec. 3-13 moves into the A1 configuration
`a1exit-retirement-config`, version 1, or into a record it pins. No check changes.

| Constant | Destination |
|---|---|
| `E`, record commit, `R` tree b05efdca | `roles.pin`, `roles.record_commit`, `adapters.replay.record_tree` |
| `H` | `roles.scientific_base` |
| `R` paths and the Phase-0/2 record paths | `adapters.sitemap`, `adapters.replay.module_path` |
| ledger and edits schema ids, `retained_unchanged`, `mirror_of` | `a1exit-exact-edit/2` (adapter), `adapters.ledger.companion` |
| frozen function names, line-523 handling | `python-frozen-replay/1`, `adapters.replay.functions` |
| corpus `papers/*.md`, `book/*.md` | `corpus` |
| profiles p0-core, p0-para, ledger-ext, ptr, repo, count-grep, register, infinity | `profiles` (sources: Phase-0 `sites.json`; `R/ledger_check.py` `EXTENDED_PATTERNS`; `P` `edits_check.py` `PTR`, `REPO_PAT`, `REG`, `CAPS`, `CAPS_OK`, `INF`, `NEUTRAL`; sec. 11 item 7 literals) |
| repo scope (historical prefixes and files, generated artifacts) | a scope record under `rules` |
| DR-1..DR-4, W1, W2, the converted `EXPLAINED` entries | rule files under `rules` |
| s3 mapping (sec. 4) | `context_mapping` (`source_field: s3`) |
| sentence abbreviations | `sentence.abbreviations` |
| the six pinned merges and PR numbers (sec. 3.1) | `hp_obligations[0]` (segment `[E, H]`) |
| tex/pdf/record-dir/sc42/coverage-ledger/ci classes, STALE ids, SC42_BASE ca3a5bb2, `tex_sources` rule, `a1exit-checker-result-v1` | `delegation.json` and the class adapters' parameters in it |
| W's workflow, the tool's landing paths | `roles.side_change_classes` |
| controls RT-*, SW*, the sec. 11 mapping and countercontrols | `controls` |

Counts such as 697, 113 and 19 are not configuration. They are references in the controls file and
in the landing record.

Acceptance criterion S13: the configured engine reproduces every A1 control outcome of sec. 10 and
11, compared item by item with this document's expectations.

### 16.5 Synthetic second configuration (test only)

`synthetic-retirement-config` is held as in-memory fixture data under `tools/` and is never
committed as a record. It is structurally different from A1:

| Aspect | A1 | Synthetic |
|---|---|---|
| Ledger adapter | `a1exit-exact-edit/2` (byte spans, hashes) | `line-patch/1`: edits `{id, file, old_line_sha256, new_lines}`, located by unique whole-line hash |
| Site map | frozen sitemap | none: sites are declared in the configuration as `{site_id, file, line_sha256, carried}` |
| Replay | yes | none; op `record` unsupported |
| Profiles | Phase-0 and the plan's regexes | one review profile `axiom-Z` (`\bAxiom Z\b`), one deny profile `Z-premise` (`\bAxiom Z\b[^.]{0,40}\b(holds|assumed)\b`) |
| HP | one obligation, six merges | one obligation, one synthetic merge |
| Delegation | six classes | one class `artifact-hash/1`: a declared file must hash to a value computed by a declared deterministic recipe |
| Context field | `s3` | `kind`, with values `{definition: true, remark: false}` |

**Controls**, run by the same executable with no code change:

| Id | Case | Expected |
|---|---|---|
| Y1 | edits applied exactly; sites moved | PASS |
| Y2 | one edit's new lines changed | FAIL `unauthorized-edit` |
| Y3 | "Axiom Z is assumed" added | FAIL `deny-match` |
| Y4 | a legitimate "Axiom Z" hit with its allow rule | PASS; the same hit with the rule widened without review gives FAIL `record-invalid` |
| Y5 | a site with `kind: definition` and its neighbour changed | FAIL `context-meaning-unverified` |
| Y6 | the artifact hash wrong | FAIL `delegated-evidence-invalid`; evidence absent gives REVIEW_REQUIRED |
| Y7 | `record` requested | ERROR `CONFIG_UNSUPPORTED` |
| Y8 | the A1 configuration and the synthetic one run in one CI job by the same engine blob | identical engine hash recorded in both results |

### 16.6 Fail-closed configuration validation

Validation runs in the integrity stage (sec. 2.1), before any subject is evaluated. No
configuration defect can lead to PASS.

| Defect | Outcome | Exit | Class |
|---|---|---|---|
| unknown `schema`, or unknown adapter name or version | ERROR | 65 | `CONFIG_INVALID` |
| missing required field, or unknown field | ERROR | 65 | `CONFIG_INVALID` |
| operation not in `operations` | ERROR | 65 | `CONFIG_UNSUPPORTED` |
| missing or failing review fields; reviewer equal to author; widening without review | ERROR | 65 | `CONFIG_UNREVIEWED` |
| hash or pin mismatch of the configuration or any referenced blob | ERROR | 65 | `SOURCE_CHANGED` |
| inconsistency: base differs from the ledger, merge off the chain, context value missing, extractor hash mismatch, duplicate profile | ERROR | 65 | `CONFIG_INCONSISTENT` |
| configuration controls file absent or empty for an operation | VOID | 70 | `CONFIG_NO_CONTROLS` |

Controls Z1-Z8 each give one of these defects in the synthetic configuration and expect the stated
class. Z9 is the core-purity lint of sec. 16.1.

### 16.7 Reproducibility

Every `result.json` records:

- `config`: `{config_id, version, path, commit, blob_sha256}`;
- each adapter's name, version and input blob hashes;
- each profile's name, source commit, path, blob and `pattern_sha256`;
- every rule file's path and blob, and the id of every rule applied (in each explanation);
- the delegation record hash and each class adapter version;
- the HP obligation's pinned merges;
- the engine blob hash.

Two runs with equal inputs produce byte-identical output (sec. 5). That is checked in CI by running
twice and comparing.

### 16.8 Implementation step

| Step | Work | Acceptance |
|---|---|---|
| S13 | Configuration loader and validator, adapter registry, the A1 configuration, the synthetic configuration | Z1-Z9 and Y1-Y8 behave; every A1 control has the same outcome as specified in sec. 10-11; no engine source contains an A1 constant (Z9) |
