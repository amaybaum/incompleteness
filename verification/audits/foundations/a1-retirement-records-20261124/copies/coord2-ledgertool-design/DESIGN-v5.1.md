# Commit-independent ledger and terminology verification tool: design v5.1

## Status and authority

This is a paper-only design. Nothing is implemented, committed, pushed or published under it.

- It supersedes v5 where they differ. `DESIGN.md` (v1), `DESIGN-v2.md` to `DESIGN-v4.md` and
  `DESIGN-v5.md` stay as written. This document is complete in itself; it is not a diff. It differs
  from `DESIGN-v5.md` only by the corrections W1 and W2 and the clarification O8 of
  `review-v5/review-v5.md` (sha256
  dff73392fa0f255f58d0d658ac579a7bfe8bcbddec31cd88f34b2e32b5756af7, verdict ACCEPT WITH REQUIRED
  CORRECTIONS); `CHANGES-v5.1.md` lists every changed passage.
- Authority: owner decision #1169 c.7093128173 (amaybaum, 2026-11-23T06:13:50Z). It approves in
  principle the exception-free verification route. That route has four steps: the tool lands first
  through its own review and merge decision; `PREREG.md` is amended and frozen again so that every
  mandatory check of sec. 11 passes as written; the trials are rerun; the retirement is executed.
- That decision holds implementation, push, pull request, merge, the plan edit and execution.
- Review inputs: `review-v2.md` (sha256 1a86e3fb...eb9, addenda 1-4) and `review-v3.md` (sha256
  5041232c6c2c0fe3b7ec939564dd669dd4f3f4f82d8ce79d365c28e7a6d2e4ff), verdict REVISE, required
  corrections R1-R11. `DESIGN-v3.md` has sha256
  855e3da00341a0c3cb7234ba7473870115164d809adeb698dd80752bf3d29d9d.
- `review-v4/review-v4.md` (sha256 113d1c129ad761114a4b529c5ec90d6d79a224d468bffa0cbe7b3cfd922cca6f),
  the independent bounded delta review of `DESIGN-v4.md` (sha256
  3cde34d2209dbcd6c5f03f991fb27385c2e709b9bd1557b60d965f9aa219c625) and `CHANGES-v4.md` (sha256
  c3214f10ea57879e7771bcacd2ea9a446b3fcc27c7464ad0d41cf665c145fdca): verdict ACCEPT WITH REQUIRED
  CORRECTIONS, required corrections V1-V8, optional points O1-O7. All three hashes were verified
  before this revision.
- Owner decisions of 2026-11-23 on v3's open points 1-4 (D1-D4 below): adopt the v3 review's
  recommendations.
- Owner decisions of 2026-11-23 on the v4 review (called V5-D1 and V5-D2 here, to keep them apart
  from D1-D4): V5-D1, drop DR-1d and DR-2 from the active deny set with a recorded history, and
  keep DR-3 with its real witness in `AGENTS.md` at `H` (sec. 6.4, 6.4.1); V5-D2, widen `resid` as
  the v4 review's V8 proposes (sec. 6.6).
- All of these decisions reached this writer through the coordinating session
  (session_013T6pfKuv5mi3MXtKjH2tZb). This writer holds no comment id for them; the record that
  quotes them with author, time and comment id (sec. A.42 item 7) is still to be cited (sec. 15).
- Owner standing instructions that bind this revision: correct the design and its expected
  outcomes to match independently verifiable behaviour; never weaken a check to turn a real-tree
  failure green; no retrospective weakening; the generality conditions stay mandatory, within
  their scope.
- The v4 review recounted every v4 figure. The figures v5 introduces or changes carry the label
  WN (sec. 0.3) until an independent reviewer recounts them against this document.

Goal link (sec. A.47): A1-EXIT (#1169), the exception-free verification route. This design
decides how the tool verifies each mandatory check of the amended plan. It decides no scientific
question and no row disposition.

## Notation

| Symbol | Meaning |
|---|---|
| `E` | e837e3dbaa605efc867a213f3345cee14c36d8f5, the ledger pin. `E` has no other meaning in this document |
| `H` | 53c6601a10419b6b333cc992474272501ab542af, the scientific base |
| `T1'` | 14ac71b4b0a0c0aa2d7068d6799a73f474097060 |
| `P` | 4c79be642ca631573f06b444903be75ec4f5e2b6, the frozen plan |
| `W` | 413b0bb88f39cad901befcf4684355c7ee39480b, `main` at the time of v3 |
| `F` | the future freeze of the amended plan |
| `X` | the candidate (execution) commit |
| `C` | the certified execution head (sec. A.39 calls it `E`; renamed here, R9) |
| `M` | `main` at check time |
| `L` | the landing merge |

`R` is the frozen ledger record directory. It has tree b05efdca935a42b9c94ef1748c964696bf58fcd9 at
9882df8f, H, T1' and W.

Paths in this document: FULL is `book/The-Incompleteness-of-Observation-FULL.md`; chNN is the book
chapter file with that number.

***

## 0. Traceability

### 0.1 Owner acceptance conditions

| Condition | Answered in |
|---|---|
| 1. Distinct exit codes, including parser errors and `--help`; with a control | sec. 5; controls X1-X10 |
| 2. A frozen, reviewed `delegation.json` with exact-head evidence; missing evidence is never PASS | sec. 7 |
| 3. Deny-pattern coverage; adversarial FAILs, each traced to a named rule or sec. 9 condition | sec. 6.4-6.6, 9, 10.2 |
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

The v1 and v2 review items are answered as in v3 and keep their places below. `CHANGES-v4.md`
maps each v3 review correction and owner decision to the sections it changed; `CHANGES-v5.md` does
the same for the v4 review's corrections V1-V8, the decisions V5-D1 and V5-D2, and the optional
points O1-O7.

| Review item | Answered in |
|---|---|
| v1 Q1: HP class kept out of RET; attribution; tracking resumes after adjudication; unresolved sites touched later reported | sec. 3 |
| v1 Q2: new-pattern-in-replacement; per-hit classification records | sec. 8 |
| v1 Q3: preregistered context rule; BOF/EOF sentinel | sec. 4 |
| v1 Q4: placement | sec. 12 |
| v1 Q5: schema, fingerprints, output form, boundary cases | sec. 5, 10.1 |
| v2 addenda 1-4 | as mapped in v3 sec. 0.2; role model now H/M/X/C/L (sec. 13) |
| v3 R1: FAIL exit code; acceptance predicate; X7 | sec. 5; X7-X10 |
| v3 R2: DR-4 against V5 and the retired (A1) entries; a countercontrol at H for every DR; V7 precondition | sec. 6.4, 10.2, 10.3 |
| v3 R3: deny set strengthened; residual limit | sec. 6.4, 6.6, 1 |
| v3 R4: sec. 11 note 1; `item7-literal` | sec. 11, 6.1, 10.3 |
| v3 R5: sec. 8.2 profile sets and disjointness | sec. 8.2 |
| v3 R6: region mergers; both overlap counts; per-line classification; H7 | sec. 3.2, 3.3, 3.4; H7 |
| v3 R7: sec. 5 against `--final` | sec. 5, 11 note 2; X9 |
| v3 R8: adapters outside the purity scope; Z9 allowlist and synthetic controls; widening list | sec. 16.1-16.3; Z9a-Z9g |
| v3 R9: the two meanings of `E` | Notation; sec. 13 |
| v3 R10: S0 indicators | sec. 4.2-4.4; K5-K9 |
| v3 R11: ownership chain | sec. 6.3; O1-O9 |
| v4 V1: nine merger groups of 22 sites | sec. 3.2, 3.3; RT-T0 |
| v4 V2: `ptr` has 5 hits at T1' | sec. 6.5, 11 row 1 |
| v4 V3: the item-7 amendment check fails hard where the original does | sec. 5, 11 note 1, 16.2 (`checks`); V23-V26; RT-I7A |
| v4 V4: repo-scan split 96 / 31 / 14 / 35 | sec. 0.3, 8.2 |
| v4 V5: HP obligations and merges are widening | sec. 16.2; Z10 |
| v4 V6 and V5-D1: DR-1d and DR-2 dropped; DR-3's real witness | sec. 6.4, 6.4.1, 15; RT-DR, RT-DR3W |
| v4 V7: figure labels; source of v3's 86 | sec. 0.3, 8.2, 14 |
| v4 V8 and V5-D2: `resid` widened | sec. 1, 6.6, 8.2; V26 |
| v4 O2-O7 (adopted) | sec. 2.3 (O2), RT-DR (O3), 4.1 (O4), 6.3 (O5), 6.1 (O6), 11 note 1 (O7) |

### 0.3 Figures

Every figure below was measured read-only from git objects (sec. 14). The implementation reports
its own counts under the fixed definitions. The counts are references, never fitted. A difference
between an implementation's count and a reference here is a finding that blocks acceptance of the
implementation step until it is explained.

**Labels.** Each figure carries one label, used identically in this document and in
`CHANGES-v5.md`:

- **IR**: independently recounted by the v4 review with its own scripts (`review-v4/rv_*.py`). Most
  of these were also reproduced earlier by the v3 review or by the v4 writer.
- **IR+WR**: as IR, and recounted again by this writer for v5 with new scripts (`work-v5/`).
- **WN**: introduced or changed in v5 and measured by this writer only; pending an independent
  recount.

**Sites, regions and provenance.**

- 697 sites; s3 categories 346 / 136 / 109 / 106. IR.
- 113 E..H site changes, attributed #1475 48, #1474 23, #1470 15, #1473 15, #1472 12. IR+WR.
- Multi-step HP provenance: 3 sites (papers/Main.md:224, papers/Main.md:732,
  papers/Substratum.md:92), each changed by #1473 and then #1474. IR+WR.
- Region mergers (sec. 3.2): **9 groups covering 22 sites**, each formed at one E..H step. 8 groups
  at #1475 (7f28886f): FULL 4897/4899/4901/4903, FULL 4921/4923, FULL 4973/4975, ch18
  166/168/170/172, ch18 190/192, ch18 242/244, papers/Methodology.md 146/148 and 367/369; 1 group at
  #1474 (a1f38284): papers/Substratum.md 266/268. IR+WR.
- HP sites also overlapped by H..T1' splices: 19 sites and 31 distinct splices, region-attributed;
  18 sites and 31 splices, line-attributed (myers and histogram agree). The difference is
  papers/Substratum.md:266, whose region-attributed splice D029 (an empty image) lies in :268's line.
  Of the 9 merger groups, only Substratum.md 266/268 is overlapped by an H..T1' splice. IR.
- 383 unchanged, 197 replaced and 4 removed sites; 203 region lines. IR.

**Hit lines and review load at T1'.**

- Hit lines in the 197 site replacement regions: 84 under the profile set p0-core, p0-para,
  ledger-ext. Adding `count-grep` gives 86; the 2 extra lines are W1 lines (ch19:212, FULL:5284).
  IR.
- 200 unheld p0+ext lines; all 84 region hit lines among them; 116 outside them, of which 93 equal
  an unheld line at H; the other 23 split 16 (in splices over hit lines of HP site regions) and 7
  (new, on non-site lines: D237, D238, D241, D242, D246, D247, D388). IR.
- `resid` as in v4, on added text: 287 splice-image lines, 28 hits, 13 hit by no other review
  profile. IR+WR.
- `resid` as widened in v5 (sec. 6.6): 45 hits on the 287 lines, 17 hit by no other review profile;
  the 4 lines added by the widening are FULL:6265, appendix-c-objections.md:108,
  papers/Complexity.md:206 and papers/Structure.md:1010. WN. The v4 review's design target was the
  same 4 lines; this count agrees with it.
- Distinct corpus lines needing a classification record or rule under all review profiles: 226
  (200 p0+ext, 5 W1 lines that are not p0+ext hits, 4 W2 lines, 17 `resid`-only). WN (the v4 total
  of 222 was IR; the difference is the 4 `resid` lines).
- `ptr` at T1': 5 lines, the 4 W2 lines and papers/GR.md:58. IR+WR.
- The `repo` profile at T1', by the class P's `classify()` returns: 176 active lines explained by
  entries sec. 6.3 does not admit: 96 path-wide "unrelated label", 31 path-wide "guard pins", 14
  substring entries (9 unrelated label, 1 historical record label, 1 registry identifier, 3
  preserved historical evidence) and 35 "kernel identifier" (IDENT); 0 unexplained; 5486 lines in
  historical records, 2 in generated artifacts. IR+WR.
- Meaning-context failures under the adopted mapping: 12 (7 in E..H, 5 in H..T1'); for reference
  only, 8 if `per unit` were false. 52 unchanged sites with a context change (27 / 22 / 3). IR.
- S0 indicators under v4's definitions: ANAPH 23, LIST 49, TABLE 6, PARTIAL 521 of 697; among the 52
  changes 0, 3, 1, 39; indicator items 3 HP, 3 RET; no ANAPH failure. IR.

**Item 7 and the deny rules.**

- Literal item-7 greps over papers/*.md and book/*.md: at T1' "six structural" 7, "Fourteen" 0,
  "sixth of" 0, `\bA1\b` 4; at H 11, 1, 2 and 179. IR.
- The v5 deny set (DR-1a/b/c, DR-3, DR-4, DR-5; sec. 6.4) with the v5 splitter: at T1' 0 lines and
  0 sentences. At H: DR-1 61 lines (a 6, b 2, c 55), DR-3 0, DR-4 28, DR-5 1; 86 distinct lines.
  At E: 95 distinct lines. Per sentence (v5 splitter): at H DR-1a 6, DR-1b 2, DR-1c 65, DR-4 28,
  DR-5 1, as in v4; at E DR-1c 70, the others as per line. IR+WR for H and T1' (the splitter
  change of O6 changed no count there); WN for the per-sentence counts at E.
- DR-3 on `AGENTS.md`: one sentence at H (lines 37-39, blob sha256 d87acac5...e27), none at T1'
  (blob sha256 59b68984...ce2). IR+WR.
- DR-1d, DR-2 and DR-3 over history (sec. 6.4.1): no match of any of the three, at line or
  sentence level, in any of the 4677 distinct blobs that occur at a top-level `papers/*.md` or
  `book/*.md` path in some commit reachable from the 794 local refs; and no match of DR-1d or DR-2
  in any text file at H, W or T1'. Measured by the v5 review and by this writer. The 4677 is the
  union of two walks that each miss blobs:
  the path-limited walk (4657) and the unrestricted walk (4671), sec. 6.4.1.
- Retired lines at H that carry `\bA1\b` or a `count-grep` literal, are absent at T1', and match no
  deny rule: 95, all of them `ptr` or `count-grep` hits. IR+WR.
- The proposed item-7 amendment check (sec. 11 note 1) with no records: at H, 86 deny lines and
  123 `final-unclassified` lines, 209 FAIL lines in all, the 95 among the 123; at T1', 0 deny lines
  and 12 `final-unclassified` lines (the 7 W1 lines, the 4 W2 lines and papers/GR.md:58). WN.
  The 86 and 209 count line-level deny matches only (O8). If every line of a multi-line sentence
  that a deny rule matches is also counted as a deny line, H has 93 deny lines and 216 FAIL lines;
  the 123 does not change. These two figures were measured by the v5 review and by this writer.

**Withdrawn.**

- The v2 review's 24 sites / 24 splices and its 2 two-step sites.
- v3's figure of 86 hit lines in the 197 regions under the stated profiles. Under the stated
  profiles the figure is 84. v3's script (`work/measure10.py`) reached 86 by one deviation, a
  touching-overlap test (`start <= site_end and end >= site_start`): with only that test made
  strict, the same script gives 84. It skips empty replacement images. Counting the removed sites'
  offset lines under the strict test is an equivalent variant that also gives 86 with the same two
  extra lines (FULL:710, ch02:78), but it is not what v3's script did.
- v4's statement that there is one region merger (corrected to 9 groups, V1), v4's `ptr` count of 4
  (corrected to 5, V2), and v4's repo split 37 / 12 (corrected to 14 / 35, V4). v4's split counted
  each line by the first `EXPLAINED` entry for its path, not by the class `classify()` returns.
- The frozen tool's error counts (32 and 154): used by no expected outcome and recounted by no one.

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
- The context mapping and the S0 indicators are preregistered heuristics.
- A rule fingerprint recognizes only identical text. Any edited legitimate use returns to
  REVIEW_REQUIRED or FAIL.
- **Lexically unanchored paraphrases.** The deny rules close only forms with a fixed lexical anchor
  (a count or ordinal of posits, a label range, the (A1) label, a posit-ledger count, and in a
  sentence a posit noun with a connector and a finiteness word). A paraphrase without such an
  anchor cannot be closed by a regular expression. The guarantee of at least REVIEW_REQUIRED is
  implemented, on added text, only for the classes that `resid` (sec. 6.6) or another review profile
  matches:
  - a finiteness word together with a posit noun (posit, premise, axiom, assumption, hypothesis)
    within a 60-character window of one sentence;
  - a state-space noun (configuration, state or phase space) followed by "is finite" or a similar
    copula;
  - "finite set", with at most one word between;
  - "substratum", "universe" or "world" followed within 40 characters by "is", "be", "being" or
    "are", an optional article and at most one word, and "finite";
  - "finite number" or "finite count" of states, configurations, elements, points or sites.

  A paraphrase outside these classes stays outside the tool, and its detection rests on the plan's
  independent review of the exact head. Constructed examples outside them, which PASS when added:
  "the framework's sixth structural property, finiteness of the bijection" and "The framework's
  sixth structural property is finiteness of the substratum" (both no longer denied once DR-2 is
  dropped, V5-D1), "the six posits of the substratum", "six assumptions about the substratum",
  "The posit ledger lists fourteen.", "the fourteen-item posit ledger" and "$A_1$–$A_6$". The
  original literal item 7 misses each of these too.
- Delegated checks stay outside the tool's semantics, even when their evidence is bound to `X`.
- The tool checks that role fields differ and that a quoted authorization exists. It cannot check
  who wrote a record (sec. 6.3).

## 2. Pipeline and subject kinds

### 2.1 Pipeline stages

Every run executes the same stages in a fixed order. A stage that fails stops all later stages.

1. **Usage.** Arguments are parsed and the `--out` guard is applied.
2. **Integrity.** Objects, pins, record hashes, ledger hashes, the configuration and the adapter
   module blobs are checked.
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
| D | `terms` | one commit; with `--base B --ledger F:ledger.json`, also the added text of `B..commit` |

All four operations share the code paths of the pipeline stages.

**Where deny profiles run (O2).** Deny profiles (sec. 6.1) are evaluated on every tree a run
evaluates except `E` and `H`, the two trees named in the configuration as retired-form trees
(`roles.pin` and `roles.scientific_base`), where the retired forms are expected. In op D they are
evaluated on the named commit whatever it is, so that their countercontrols at `H` run through op D
(RT-DR). `result.json` lists the profiles evaluated on each tree.

**Added text.** Profiles with `applies_to: added-text` (`register`, `infinity`, `resid`) are
evaluated on the splice images of a ledgered segment. In op D they run only with `--base` and
`--ledger`.

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

**Region mergers (R6, V1).** Two sites whose walks produce the same post-region at the same step
share that region from then on. The tool reports each such site with `region_shared_with`: the
sorted list of the other site ids, the step at which the regions merged, and the shared region's
hash. A merger is never silent. On the chain E..H there are 9 merger groups covering 22 sites, each
formed at a single step:

| Step | Groups (sites at the pin) |
|---|---|
| #1475 (7f28886f) | FULL 4897/4899/4901/4903; FULL 4921/4923; FULL 4973/4975; ch18 166/168/170/172; ch18 190/192; ch18 242/244; papers/Methodology.md 146/148; papers/Methodology.md 367/369 |
| #1474 (a1f38284) | papers/Substratum.md 266/268 |

The sites of a group sit two lines apart, separated by blank lines. Blank lines are never unique,
so the anchors of the walks fall outside all sites of the group, and their pre-regions become one
block. Of the 9 groups, only Substratum.md 266/268 is overlapped by an H..T1' splice (D029).

### 3.3 HP adjudication record (schema `oi-hp-adjudication/1`)

The record is an immutable file in the audit directory, under the ownership chain of sec. 6.3. It
lists each `site_id` with the following:

- `steps`: each step's commit (full id), parent, position, `pre_sha256` and `post_sha256`;
- the carried `row`, `code` and `owner`, which must equal the frozen values; otherwise FAIL
  `adjudication-row-changed`;
- `own_lines`: for a site with `region_shared_with`, the lines of the shared final region at `H`
  that carry this site's text, by `line_sha256`. It is required for every one of the 22 merged
  sites of sec. 3.2, whether or not a splice overlaps the region. For an unshared site it is the
  whole final region;
- `semantic_classification`: which qualification is visible on the site's own lines, with the
  reason. For a shared region each site is classified on its own lines, never only on the block;
- `splice_attribution`: for each H..X splice that overlaps the final region, the site ids whose own
  lines it intersects;
- `hit_classifications` for every profile hit in the final region (sec. 8), bound by
  `line_sha256`;
- `context`: the pin and H context hashes plus a semantic statement, required when sec. 4 marks
  the site and its context changed in E..H;
- `author`.

The tool recomputes the walk of sec. 3.2 and compares it with the record. The result is:

- `provenance-adjudicated` only if every step matches exactly;
- FAIL `provenance-mismatch` if a commit or hash differs;
- FAIL `provenance-gap` if a step is missing or extra;
- FAIL `provenance-foreign` or `provenance-ambiguous` as in sec. 3.2;
- FAIL `hp-unadjudicated` if no record names the site;
- FAIL `record-invalid` if a site with `region_shared_with` has no `own_lines`, if the own lines of
  the sites sharing a region leave a non-blank region line unassigned, or if a splice overlapping
  the region is attributed to no site.

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
- **Two overlap counts (R6).** Each RET entry carries `region_splices` (splices overlapping the
  site's final region, the decision basis) and `line_splices` (a diagnostic: splices intersecting
  the site's own line, tracked through each step by `git diff -U0 --no-renames` with the myers
  algorithm, carrying the site's line range through the hunks). The FAIL class and the totals use
  `region_splices`. Once an adjudication exists, `line_splices` is replaced by the record's
  `splice_attribution`, which the tool checks as in sec. 3.3.
- At T1': 19 HP sites, overlapped by 31 distinct splices, region-attributed; 18 sites and 31
  splices line-attributed. The one difference is Substratum.md:266, whose region-attributed splice
  D029 lies in :268's line.

### 3.5 Context changes in E..H

Every item is assigned to the segment in which its change occurred. A context change on a
meaning-required site (sec. 4) that occurred in E..H is an `HP` item. It is resolved only by the
`context` field of that site's HP adjudication, or of a context adjudication for an unchanged site.
Indicator items of sec. 4.3 that arise in E..H are also `HP` items.

***

## 4. Preregistered context rule

Decided at S0, before any implementation output. The rule is stated per frozen s3 value and per
indicator. The mapping and the indicator definitions were adopted on their principle by the owner
decisions of 2026-11-23 (D2). Their counts at T1' are reported, not tuned.

**Context definition.** The ordered pair of the nearest non-blank line above and the nearest
non-blank line below, with sentinels `BOF` and `EOF`. Its hash is
`sha256(above + 0x00 + below)`, taken at the pin and at every tree.

**Identity.** Context is required for identity when `pin_count > 1`, or when the current text is
not unique (v1 sec. 4.4). A context change then makes the site FAIL `ambiguous`. All 697 pin lines
are unique at E.

**Meaning.** The principle: context is required exactly when the frozen record does not establish
that the qualification is visible on the site's own line. `per unit` stays on the required side: a
per-unit status means the qualification was established by a unit's correction, which may sit in
a neighbouring sentence.

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

The indicator ANAPH (sec. 4.2) also sets `meaning_context` to true. A reviewed context adjudication
may set it to true for a further site. Nothing can set it to false for a site the table or ANAPH
marks.

### 4.1 Decision

| Condition | Result |
|---|---|
| `meaning_context` true, context changed, no context adjudication matching both hashes | FAIL `context-meaning-unverified` |
| `meaning_context` true, context changed, matching adjudication | PASS |
| LIST or TABLE site, its structure context or its context changed, no adjudication matching both context hashes and both structure hashes (sec. 4.3) | REVIEW_REQUIRED `context-structure-changed` |
| `meaning_context` false, context changed, not covered by the row above | PASS with `context_changed: true`; requires verified identity and identical site bytes |

FAIL takes precedence: a LIST or TABLE site whose `meaning_context` is true and whose context
changed is FAIL `context-meaning-unverified`.

A context adjudication (schema `oi-context-adjudication/1`) records `site_id`, `segment`,
`from_context_sha256`, `to_context_sha256`, for LIST and TABLE sites also
`from_structure_sha256` and `to_structure_sha256`, and a semantic statement that the
qualification is still visible or still stated. It carries `author` and is under the ownership
chain of sec. 6.3.

### 4.2 S0 indicators: exact definitions (R10)

All four indicators are computed on the site's pin line at `E`. They are preregistered at S0 with
the definitions below, which are part of the A1 configuration (sec. 16.4). A change to any of them
is a configuration change and is widening (sec. 16.2).

- `strip(line)`: remove leading whitespace, then any run of blockquote markers `>` with their
  following whitespace, then one heading marker `#{1,6}` with its whitespace, then one list marker
  (`-`, `*`, `+`, or digits followed by `.` or `)`) with its whitespace, then any run of `*` and `_`.
- **ANAPH**: `strip(pin line)` matches, case-sensitively,
  `^(This|These|Such|Hence|Thus|It|Under this)\b`.
- **LIST**: the pin line matches either
  - `^\s*(>\s*)*([-*+]|\d+[.)])\s+` (a list item), or
  - `^\s*(>\s*)*(([-*+]|\d+[.)])\s+)?[*_]{0,2}\(\s*([A-Z]{1,3}\d{1,2}[a-z]?|[ivx]{1,4})\s*\)` (a
    labelled item, such as `*(A2) Determinism.*` or `(C1)`).
- **TABLE**: the pin line matches `^\s*\|`.
- **PARTIAL**: the site has a Phase-0 entry, and its `quote`, whitespace-normalized, differs from
  the whitespace-normalized pin line.

### 4.3 Indicator effects

| Indicator | Effect |
|---|---|
| ANAPH | sets `meaning_context` true. An anaphoric line takes its referent from the line above, so a changed context changes what the line asserts. FAIL `context-meaning-unverified` until adjudicated |
| LIST | REVIEW_REQUIRED `context-structure-changed` when the site's context (sec. 4) or its list context changed, unless adjudicated |
| TABLE | REVIEW_REQUIRED `context-structure-changed` when the site's context (sec. 4) or its table context changed, unless adjudicated |
| PARTIAL | informational only: the site carries `partial_quote: true`. No effect on any outcome |

**List context.** Walking up from the site over blank lines and list-item lines (as LIST defines
them), the first other non-blank line is the lead-in (`BOF` if none). Walking down the same way,
the first other non-blank line is the trailer (`EOF` if none). The siblings are the non-blank item
lines between them, other than the site. The list context is `(lead-in, siblings, trailer)`, and
its structure hash is the SHA-256 of its canonical JSON.

**Table context.** The table block is the maximal run of lines matching `^\s*\|` that contains the
site. The table context is `(header, caption above, caption below)`: the block's first line; the
nearest non-blank line above the block (`BOF` if none); and the first non-blank line after the
block if it starts with `Table:` or `: `, else the empty string. Its structure hash is defined as
for lists.

**Conservative reading.** The review recommended REVIEW when a list's lead-in or a sibling changed,
and the table context redefined as header plus caption. v4 keeps the neighbour-pair context of
sec. 4 for these sites as well, and adds the trailer to the list context. This is a strict
superset: it removes no v3 outcome, keeps the review's own TABLE true positive
(papers/Main.md:741, whose neighbour row changed) visible, and catches its LIST true positive
(papers/Substratum.md:127, whose following paragraph changed from "derived from E1-E3, A1-A2" to
"derived from E1-E3 and A2").

**Reference rates.** These are references for the preregistration. They are not tuned values.

| Indicator | v3 review's definitions: sites / of 52 changes | v4 definitions: sites / of 52 changes |
|---|---|---|
| ANAPH | 31 / 0 | 23 / 0 |
| LIST | 20 / 1, plus 2 false negatives (FULL:708, ch02:78) | 49 / 3 (FULL:708, ch02:78, Substratum.md:127) |
| TABLE | 6 / 1 (Main.md:741) | 6 / 1 (Main.md:741) |
| PARTIAL | 342 / 23 | 521 / 39 |

The review's definitions were its own and are not given exactly in its text; the v4 definitions
above are the preregistered ones. The differences in ANAPH, LIST and PARTIAL come from the
definitions (v4's LIST includes labelled items and ordered lists; v4's PARTIAL counts any
difference between quote and line). Only the v4 column is a reference for the implementation.

### 4.4 The real-tree cases at T1'

There are 52 unchanged sites whose context differs from the pin:

- 27 changed in E..H;
- 22 changed in H..T1';
- 3 changed in both segments.

Of these, the table of sec. 4 marks 12. ANAPH marks none of the 52.

| Origin | Cases | Result under the rule | Resolved by |
|---|---|---|---|
| E..H | 6 `not determined`, 1 `per unit` | HP FAIL `context-meaning-unverified` | the HP or context adjudication of sec. 3.5 |
| H..T1' | 2 `not determined`, 3 `per unit` | RET FAIL `context-meaning-unverified` | a context adjudication reviewed against the retirement's edits |

The 12 sites: E..H: FULL:4895, 4905, 4919; ch18:164, 174, 188; papers/Main.md:332. H..T1':
FULL:1340; ch05:25; papers/Computation.md:122; papers/GR.md:90; papers/Main.md:588.

Indicator items (none of these sites is marked by the s3 table):

| Origin | Sites | Result |
|---|---|---|
| E..H | LIST FULL:708, ch02:78 (a sibling item changed); TABLE papers/Main.md:741 (neighbour row changed) | 3 HP REVIEW_REQUIRED `context-structure-changed` |
| H..T1' | LIST FULL:708, ch02:78 (lead-in, sibling items and trailer changed); papers/Substratum.md:127 (the paragraph after the list changed) | 3 RET REVIEW_REQUIRED `context-structure-changed` |

The two contradictory cases named in v2 addendum 3 are the 2 `not determined` H..T1' cases. Under
this rule they are RET FAILs. RT-T (sec. 10.3) states this. It does not claim "no RET FAIL".

***

## 5. Outcomes, exit codes and output

| Outcome | Exit | Emitted when |
|---|---|---|
| PASS | 0 | every check holds and every control is green |
| REVIEW_REQUIRED | 10 | no FAIL item, at least one REVIEW item |
| FAIL | 20 | at least one FAIL item |
| USAGE | 64 | an argument error, `--help`, or a refused `--out` |
| ERROR | 65 | an integrity error (list below) |
| VOID | 70 | a preflight or self-test control failed |
| INTERNAL | 71 | any exception caught by the tool's wrapper |

**Why FAIL is 20 (R1).** CPython itself exits 1 on an uncaught exception, including one raised
before the tool's wrapper is installed (an import or syntax error in the tool's own package), and 2
when it cannot open the script; it exits 120 when flushing standard streams fails at shutdown. None
of the codes in the table is one of these. The parser overrides `ArgumentParser.error` and the
`-h`/`--help` action so that both exit 64; exit 2 is therefore excluded only for the parser's
paths, and the interpreter can still return it.

**The wrapper.** The entry point `tools/ledger_coverage.py` installs the wrapper before it imports
the tool's package. The wrapper catches `BaseException` (including `SystemExit` raised by frozen
code and `KeyboardInterrupt`) and maps it to INTERNAL, exit 71, with a `result.json`. A failure
before the wrapper is installed exits with the interpreter's own code.

**Acceptance predicate (sec. A.44).** A consumer (a workflow step, the plan's checker or a
reviewer) accepts a run only if all of the following hold:

- the exit status is 0;
- `result.json` exists in `--out` and validates against schema `oi-ledger-coverage/4`;
- its `outcome` is PASS, and the independent outcome checker (S7) recomputes PASS from its
  `preflight`, `record_checks` and `items`;
- its recorded engine blob and adapter module blobs equal the pinned ones (sec. 16.7), and its
  configuration `{path, blob_sha256}` equals the frozen one.

Any exit status not in the table (for example 1, 2, 120, 126, 127 or a signal) is non-acceptance,
whatever `result.json` says. An exit status in the table that disagrees with `result.json` is
non-acceptance.

**Integrity errors.** These produce ERROR:

- `PIN_MISMATCH`, `RECORD_TREE_MISMATCH`, `SCIENTIFIC_BASE_MISMATCH`, `MAIN_NOT_DESCENDANT`;
- `SOURCE_CHANGED`;
- a ledger hash, span, overlap or base mismatch;
- `edits_sha256` mismatch;
- an encoding error (not UTF-8, or CR present);
- an unresolvable object;
- the configuration classes of sec. 16.6.

Evaluation order fixes precedence: USAGE, INTERNAL (at any stage), ERROR, VOID, FAIL,
REVIEW_REQUIRED, PASS. Only exit 0 with the acceptance predicate is acceptance.

**Flags and REVIEW_REQUIRED (R7, V3).** No flag converts REVIEW_REQUIRED to PASS. A run of op D
names the plan check it implements with `--check ID`; the configuration's `checks` table (sec. 16.2)
gives each check its profiles and its `final_profiles`. `--final` converts the REVIEW items of the
selected check's `final_profiles` to FAIL `final-unclassified`, and changes nothing else. For A1,
item 7 lists `ptr` and `count-grep`, and item 11 lists `repo`. `--final` without `--check`, or with a
check that has no `final_profiles`, is USAGE. Controls X9 and V23-V25 show both directions.

**When no `result.json` is written.** In the USAGE case nothing is written to `--out`. One JSON
object with the same schema id, `outcome: "USAGE"` and the parser message goes to stderr. This is
the only case of the table without a `result.json`. A run that ends with an interpreter code
outside the table writes none either, and is non-acceptance.

**Frozen code.** Every call into frozen code in op A is wrapped. An exception becomes a structured
INTERNAL or ERROR with its class and message. The frozen `main()` is never called, so its line-523
`TypeError` cannot be reached.

**Output form.** Schema `oi-ledger-coverage/4`, which extends v3's `/3`:

- `site_counts`, `finding_counts` and `hit_counts` are separate;
- items carry `file` and `line` where applicable, and are sorted by
  `(obligation, class, subject, segment, fingerprint)`;
- the fingerprint is the SHA-256 of canonical JSON (sorted keys, no whitespace, UTF-8, null as
  `null`) over fields that do not depend on any diagnostic algorithm. For `unauthorized-edit` that
  is the expected and actual file hashes and the segment; difflib ranges are diagnostics only;
- every hit carries a `segment`, its profile and the tree it was scanned in. `pre_existing` is
  computed by the same scan at the prior endpoint;
- `repo_head` is removed;
- the output is written with sorted keys, indent 1, `ensure_ascii` true and a final LF;
- site fields: `pin_count`, `ordinal`, `pin_context_sha256`, `current_context_sha256`,
  `context_required`, `meaning_context`, `indicators` (`anaph`, `list`, `table`, `partial_quote`),
  `structure_context_sha256` (LIST and TABLE sites), `provenance` (record id or null),
  `region_shared_with`, `hp_overlap`, `region_splices` and `line_splices`;
- `profiles_evaluated`: per tree, the profiles run on it (sec. 2.3);
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
  interior offset also overlaps. A splice that only touches a site's boundary does not.
- A hit line is "in a splice image" if it contains the splice's offset in `X`. Empty images are
  included, for example D029 at Substratum.md:268.
- A removed site (empty image) has no replacement region; the line holding its offset is reported
  with the removal, not counted as a region line.
- A last line without LF is a line. Its span ends at end of file.

***

## 6. Profiles, rules and record lint

### 6.1 Scan profiles

Profiles are extracted from their source blobs by `ast` or JSON, never retyped, except the rule
patterns of sec. 6.4 and 6.6, which live in reviewed rule files. Each profile records its source
blob and the SHA-256 of its patterns.

**Review profiles.** A hit is REVIEW_REQUIRED unless held or classified.

| Profile | Source | Applies to |
|---|---|---|
| `p0-core`, `p0-para` | Phase-0 `sites.json` | tree |
| `ledger-ext` | `EXTENDED_PATTERNS` in `R/ledger_check.py` | tree |
| `ptr` | `PTR` in P's `edits_check.py` | tree |
| `repo` | `REPO_PAT` in P's `edits_check.py`; scope "active files", sec. 11 item 11 | tree |
| `count-grep` | the literal list of sec. 11 item 7: "Fourteen", "six structural", "sixth of" | tree |
| `resid` | sec. 6.6 (v4, widened in v5; rule file) | added text |

**Deny profiles.** Any match is FAIL. They are evaluated on every line and on every sentence of
every in-scope file of the trees named in sec. 2.3, not only on hits of other profiles.

| Profile | Source and scope |
|---|---|
| `DR-1`, `DR-3`, `DR-4`, `DR-5` | sec. 6.4 (DR-1d and DR-2 are retired, sec. 6.4.1) |
| `register` | `REG` and `CAPS`/`CAPS_OK` in P's `edits_check.py`; added text only |
| `infinity` | `INF` less the `NEUTRAL` disclaimer, in P's `edits_check.py`; added text only |

**Countercontrol profile `item7-literal` (R4).** The literal check of P's sec. 11 item 7 as
frozen: the case-sensitive literals "Fourteen", "six structural" and "sixth of" over
`papers/*.md` and `book/*.md`, each required to match zero lines, with `\bA1\b` reported. It is a
named countercontrol, run by `terms --profile item7-literal`. Any match is FAIL
`item7-literal-match`. It is not part of any amended check unless the amended plan names it; its
expected outcomes are fixed in RT-I7 (sec. 10.3).

**Sentence splitter, version 2 (versioned with the schema; O6).** A sentence ends at `.`, `?` or
`!`, optionally followed by a run of closing `*` or `_`, and then by whitespace and an uppercase
letter, a `*`, or end of paragraph. It does not end:

- inside `$...$` or a backtick span;
- after a word on the configuration's abbreviation list (A1: `sec.`, `Sec.`, `e.g.`, `i.e.`,
  `cf.`, `Fig.`, `Eq.`, `Eqs.`, `No.`, `vs.`, `et al.`, `Ch.`, `App.`, `Thm.`, `Prop.`, `Lem.`);
- after a single capital initial.

A paragraph is a maximal run of non-blank lines, broken also before every list-item line (a line
matching `^\s*(>\s*)*([-*+]|\d+[.)])\s+`). A sentence never crosses a paragraph boundary. Each
line of a paragraph is stripped of leading and trailing whitespace, and the lines are joined with
one space before splitting. Version 1 (v4) did neither: it let one "sentence" run across several
bullets, and did not end a sentence at "...no more.** Every". Measured, version 2 changes no deny
count at H or T1' at line or sentence level (sec. 14).

### 6.2 Rule schema `oi-term-rules/2`

A rule file is an immutable record under the ownership chain of sec. 6.3: a change is a new file,
which carries `supersedes: {path, blob_sha256}`.

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
- `author`.

**Deny rule.** Its fields:

- `id`;
- `pattern`: a reviewed regex, or a two-part sentence test as for DR-3;
- `scope`: `all-corpus` or exact paths;
- `positive_examples`, at least one, which the rule must match;
- `negative_examples`, at least one, which the rule must not match, for example the W1 and W2
  sentences;
- `countercontrol`: a real line or sentence at a named commit that the rule matches, in a scanned
  file or in a control-only input named by the controls file (sec. 6.4). No constructed text
  serves as a deny rule's countercontrol;
- `reason`;
- `author`.

Fingerprints and `max_instances` do not apply to deny rules.

**Applying an allow rule.** For a hit, the steps run in this order:

1. If no allow rule has the hit's file in scope, with a literal covering the trigger and a context
   matcher that holds, the hit stays REVIEW_REQUIRED `unclassified`.
2. If any deny profile matches the sentence, the result is FAIL `deny-match`.
3. If the rule's negative matcher matches the sentence, the result is FAIL `rule-negative-match`.
4. If the sentence or, when required, the context differs from every fingerprint, the result is
   REVIEW_REQUIRED `rule-fingerprint-mismatch`.
5. If the rule has already been applied `max_instances` times in the tree, the result is FAIL
   `rule-overreach`.
6. Otherwise the hit is classified by the rule.

No rule ever deletes text from the line before testing.

### 6.3 Records, review records, owner authorization and lint (R11, D4)

The chain below applies to every reviewed record kind: HP adjudications, context adjudications,
hit classifications, allow and deny rule files, scope records, side-change class records,
reconciliation records, PIN_OK entries outside `F`'s pin table, and the configuration itself. One
record is one immutable file in the audit directory of sec. 12.1, or in the amended plan's record
directory for records frozen with the plan.

**Writer (author).** Prepares the record and its evidence: the exact git object ids, the subject's
`line_sha256` or region hashes, the tool's REVIEW-mode explanation for that subject, and the
semantic statement (which qualification is visible, and why). The evidence may include tool
output, but the record states its classification in its own words. Its `author` field names the
writer. A writer may not review a record they wrote.

**Independent reviewer.** A non-author re-derives each record from the git object store, not from
the writer's output. For an HP record that means recomputing the walk, checking each step's commit
and hashes, and reading the pre and post text. For a classification or context record it means
reading the sentence and its context at the stated tree and judging the semantic statement. The
reviewer writes a separate immutable review record, schema `oi-review-record/1`, with:

- `reviewer`;
- `reviewed`: `{path, blob_sha256}` of exactly one record;
- `method`: how each item was re-derived, naming the object ids read;
- `verdicts`: one entry per item id of the reviewed record (`accept`, `reject` or `dissent`, with
  the reason);
- `dissent`, if any.

A review that cites only a passing tool run is invalid.

**Owner authorization.** The owner authorizes exact content. An authorization record, schema
`oi-owner-authorization/1`, quotes the owner's comment with `owner`, `time` and `comment_id` (sec.
A.42 item 7) and lists `authorizes: [{record: {path, blob_sha256}, review: {path, blob_sha256}}]`.
A batch may be authorized by one authorization record that lists every member. An authorization
that names a path without a hash authorizes nothing.

**Frozen configuration.** `retirement-config.json` at `F` references every record, review record
and authorization record by `{path, blob_sha256}` (sec. 16.2). A record added after `F` is
admissible only under sec. 13.3's reconciliation rule and never for a decision on `X`.

**What the tool checks.** A record fails, with FAIL `record-invalid`, on any of these:

- a referenced blob that does not exist at `F` at its path, or whose hash differs (this is ERROR
  `SOURCE_CHANGED` when the blob is the configuration's own reference);
- a schema or field error, or a missing field;
- no review record naming exactly this record's blob, or a review record naming another blob;
- `reviewer` equal to `author`;
- a review whose `verdicts` do not cover every item id of the record, or any item not `accept`;
- no authorization record listing both this record's blob and its review's blob;
- an authorization whose `owner` differs from the configuration's owner, or with no `comment_id`;
- a `reviewer`, `owner` or `comment_id` value that points to a tool run, a CI run, a check run or
  an Issue (a URL or run id rather than a person and a comment);
- a broken `supersedes` chain, or a reused id;
- a record not read from the git object store.

The tool never infers a role, a review or an authorization from a passing tool result.

**Root of trust (O5).** The configuration names the owner and references every authorization record,
so it cannot itself establish who the owner is. Its own root is `F`'s pin table, which the owner
designates with `F`: the configuration is admitted only if its sha256 is in that table, and the
configuration's `retirement.owner` must equal the owner who designated `F`, as quoted in the
designation record.

**Corrections.** A correction is a new record with `supersedes`, a new review and a new owner
authorization. Nothing is edited in place, and an id is never reused.

**Residual limit.** The tool can check that the role fields differ and that the quoted
authorization exists, not who actually wrote them. Identity rests on the reviewer's and the
owner's own recorded statements.

**Widening of an allow rule.** Any of the following, compared with the superseded version, is
widening:

- added files;
- a changed or shorter literal;
- fewer context or negative literals;
- **any change to the fingerprint set**, including a swap with the count unchanged (control A3r);
- a larger `max_instances`;
- `context_required` turned off;
- a new allow rule without `supersedes`.

**Widening of a deny rule.** A changed pattern, a narrower scope, removed examples, or a removed or
changed countercontrol.

Widening needs a `widening_review` record by a non-author reviewer other than the record's own
reviewer, under the same chain. Widening without it is FAIL `record-invalid`.

**Examples and fingerprints.** Each fingerprint must be reproduced by a sentence of its named file
at `recorded_at`. Each example and countercontrol must behave as stated. Otherwise the record fails
the lint.

**Kind-specific rules.**

- **PIN_OK.** An entry is valid only if listed in `F`'s pin table, or in a reviewed record that the
  configuration at `F` references. An entry dated after `F` is FAIL `pin-broken`.
- **Reconciliation.** A record written after `F` is valid only for a side change on `M`, and it
  never changes a decision of op C on `X` (sec. 13.3).

### 6.4 Deny rules DR-1, DR-3, DR-4, DR-5 (for independent review; measured in sec. 14)

These strengthen v3's seed rules as review-v3 required (R2, R3), less the two candidates the owner
dropped (V5-D1; sec. 6.4.1). They are a proposal for the independent review that the plan amendment
needs (sec. 11 note 1); they are not adopted. All are case-insensitive. Each must match none of the
W1 and W2 sentences at T1' and none of the replacement "Thirteen items" sentence
(papers/Main.md:738 at T1'); measured, none does. The identifiers DR-1d and DR-2 are retired and
are never reused.

Below, `N` is `(?:assumptions?|axioms?|posits?|premises?|conditions?)`, `CNT` is
`(?:six|seven|sixth|seventh)`, `LBL(k)` is `(?:\(\s*Ak\s*\)|\bAk\b)`, and `SEP` is
`(?:\s*(?:-{1,3}|–|—|\bthrough\b|\bto\b|\$?\\(?:text)?(?:endash|emdash)\$?)\s*|\s*,\s*(?:\.{3}|…|\$?\\l?dots\$?|\$?\\cdots\$?)\s*,?\s*)`.

- **DR-1** (a count or ordinal of the structural posits, or the A1-A6 range). One of:
  - a: `(?i)\bCNT\b[^.;]{0,40}\b(?:structural|substratum(?:'s|’s)?)\s+N`
  - b: `(?i)\bCNT\b[^.;]{0,40}\bstructural\s+propert(?:y|ies)\s+of\s+the\s+substratum\b`
  - c: `(?i)` followed by `LBL(1)`, `SEP` and `LBL(6)` in sequence (hyphen, double or triple hyphen,
    en dash, em dash, "through", "to", TeX dash macros, and the bare ellipsis list "A1, ..., A6",
    each with bare or parenthesized labels; a list with intermediate items, such as
    "A1, A2, \ldots, A6", is not matched)
- **DR-3.** A sentence (sec. 6.1) that matches both
  - the count part `(?i)structural\s+propert|structural\s+assumption|structural\s+axiom|structural\s+posit|\bposits?\b|\bpremises?\b|\baxioms?\b`, and
  - the tail `(?i)(?:one of which|one of its|one of the|among|includ\w*|the first being|first of which|namely)[^.;]{0,60}?(?:total[- ]finiteness|finite in total|totally finite|finiteness of (?:\$?\\?(?:mathcal\{)?S\}?\$?|the (?:configuration|state) space)|finiteness\b)`.
- **DR-4** (the retired posit entry; crosses the label's own period):
  `(?i)(?:\(\s*A1\s*\)|\bposit\s+A1\b|\bA1\b\s*(?:\(|:))[^.;]{0,60}(?:\.[^.;]{0,80})?\b(?:finit\w*|configuration\s+space|substratum)`
- **DR-5** (the posit-ledger count): `(?i)\b(?:fourteen|14)\b[^.;]{0,40}\b(?:items|posits|entries|premises|assumptions)\b`

DR-1, DR-4 and DR-5 are evaluated on each line and on each sentence; DR-3 on each sentence.

DR-1's ordinal alternatives also match current, legitimate references to A6 as "the sixth structural
assumption" in active files outside the corpus (for example `verification/README.md:2320` and
`A6Instantiation.lean:15` at T1'). In the corpus that usage was retired. The ordinal alternatives
therefore encode a corpus terminology decision, which the amendment states (sec. 11 note 1).

**Measured (sec. 14).** Each countercontrol asserts the target rule id on the named line or
sentence, not only the run's outcome (O3).

| Rule | T1' lines / sentences | H lines | Real-tree countercontrol at H |
|---|---|---|---|
| DR-1 | 0 / 0 | 61 (a 6, b 2, c 55) | a: FULL:6504 and book/glossary.md:13 ("The sixth of the framework's structural assumptions A1–A6"); b: ch09:104; c: FULL:718 |
| DR-3 | 0 / 0 | 0 in the corpus | `AGENTS.md` at H, the sentence of lines 37-39, by a control-only scan (below) |
| DR-4 | 0 / 0 | 28, including papers/Substratum.md:92 ("(A1) **Finiteness.** The configuration space $S$ is finite.") | papers/Substratum.md:92 |
| DR-5 | 0 / 0 | 1: papers/Main.md:736 ("Fourteen items, of unequal weight, and not fourteen independent physical assumptions") | papers/Main.md:736 |

**DR-3's witness (V5-D1).** No corpus blob in the repository's history matches DR-3. Its real
witness is the sentence of `AGENTS.md` at `H`, lines 37-39: "Every posit of the substratum model —
the posit ledger of `papers/Main.md`, including total finiteness (A1), linearity (A5), the lattice
and its coupling range, the form of the update and the measure selection — is a hypothesis that may
be false, not a fixed part of the framework." DR-3's count part matches "posit" and its tail matches
"including total finiteness". Ledger splice D296 (`AGENTS.md`, bytes 2332-2382 at `H`, lines 37-38)
rewrites it to "including linearity (A5)". `AGENTS.md` at T1' has no deny match at line or sentence
level.

- `AGENTS.md` is a ledgered file but lies outside the corpus that the deny profiles scan in
  production (`papers/*.md` and `book/*.md`). The production scan is not widened: other ledgered
  non-corpus files match deny rules at T1' with legitimate text (the A6 references above, Lean
  docstrings, guard pins), so a wider production scope would need its own allow rules and review.
- The control RT-DR3W exercises the witness by a **control-only scan**. The controls file names the
  input `{commit: H, path: AGENTS.md, blob: 12a9281fb88c14395b6715a3bf4b4f6b030f433c, sha256:
  d87acac54b5f6392af3323630236d98b14bb4d485d10c0ff56b20806b0883e27}`. The control reads that blob
  from the object store, splits it with the configured splitter (sec. 6.1), and applies DR-3 alone.
  It requires exactly one matching sentence, whose span starts on line 37 and includes lines 37-38.
  Its countercontrol reads `AGENTS.md` at T1' (sha256
  59b68984e659ef808819e02d4653d80388f8bd2f4c009796b162fc2453882ce2) the same way and requires 0
  matches.
- A control-only input is read only by the control that names it. It changes no profile's scope
  and no production result. Adding or changing a control-only input changes the controls file and
  is reviewed with it (sec. 16.2).
- No historical text is constructed for this purpose.

### 6.4.1 Rejected candidates DR-1d and DR-2 (history)

These two rules were proposed in v4 and dropped from the active set by owner decision V5-D1. They
are recorded here so that their purpose and patterns are not lost.

| Id | Purpose | Exact pattern (v4) | Forms it covered |
|---|---|---|---|
| DR-1d | a reversed ordinal: "structural" or "substratum" before "sixth/seventh" and a posit noun | `(?i)\b(?:structural\|substratum(?:'s\|’s)?)\s+(?:sixth\|seventh)\s+(?:assumption\|axiom\|posit\|premise\|condition\|property)\b` | "the substratum's sixth axiom, finiteness" (v4 V15) |
| DR-2 | an ordinal structural property, assumption or posit followed by finiteness | `(?i)\b(?:sixth\|seventh)\b[^.;]{0,40}\bstructural\s+(?:property\|assumption\|axiom\|posit\|premise\|condition)\b[^.;]{0,80}\bfinit` | "the framework's sixth structural property, finiteness of the bijection" (v4 V4) |

(The `\|` above is a table escape for `|`.)

**Why they were dropped.** Neither has a real-tree countercontrol. Neither pattern matches, at line
or sentence level, any blob of the history search below, nor any text file at `H`, `W` or T1'.
Their v4 countercontrols were single-line mutants of H lines, which are not evidence of a real
form. The absence of any match in history supports their removal. It does not prove that such a
form can never be written.

**The history search (W2).** The searched set is defined by commit trees, not by how a walk names
blobs: every blob that occurs at a top-level `papers/<name>.md` or `book/<name>.md` path in the tree
of any commit reachable from any local ref. With the 794 local refs (7857 commits) this set has
4677 distinct blobs. DR-1d, DR-2 and DR-3 match none of them, at line or sentence level. Two
cheaper walks each miss part of the set, which is why v5 and the v4 review reported different
counts; the difference is method, not refs:

- `git rev-list --all --objects -- papers book` (path-limited, 4657 blobs) omits 20 blobs. History
  simplification under a pathspec drops commits that make no corpus change relative to the parent
  it follows, so blobs that exist only in side-branch commits are never listed.
- `git rev-list --all --objects` (unrestricted, 4671 blobs, v5's figure) omits 6 blobs. It names
  each blob by the first path it meets, and these 6 are first met under a non-corpus path (for
  example `repo/papers/Main.md` or `README.md`), so a filter on the path name drops them.

The union of the two walks equals the tree-defined set exactly (4677 blobs).

**What removing them costs (measured).**

- Known retired material: there is no line or sentence in any tree or historical corpus blob that
  either rule matches, so no known retired A1 line loses a FAIL. At `E`, `H` and `W` the active
  deny set gives the same distinct line counts with or without them (95, 86, 86).
- Constructed forms: "the substratum's sixth axiom, finiteness" is REVIEW_REQUIRED through `resid`
  (a posit noun with a finiteness word). "the framework's sixth structural property, finiteness of
  the bijection" now PASSes when added: no deny rule, review profile or `resid` alternative matches
  it. The original literal item 7 does not catch it either ("sixth structural" contains neither
  "six structural" nor "sixth of"). It is listed as a residual in sec. 1 and kept as control V4
  with expected PASS, so that a change in its outcome is visible.
- The text of v4's DR-2 countercontrol (the former mutant M-DR2), "The framework's sixth
  structural property is finiteness of the substratum", now PASSes when added, alone or inside the
  glossary.md:13 line at H that the mutant edited: no deny rule, no review profile and no `resid`
  alternative matches it, and the original literal item 7 misses it too. It is listed as a residual
  in sec. 1 and kept as control V27 with expected PASS.
- The former mutant M-DR1d line (glossary.md:11 at H, edited to "The substratum's sixth axiom,")
  stays FAIL: DR-4 matches the same line.
- In sum, coverage was lost only for constructed strings: V4 and the M-DR2 text went from FAIL to
  PASS, and V15 from FAIL to REVIEW. No known retired real-tree material is affected.

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
`book/appendix-b-derivations.md:235` and `:246`, and at FULL lines 5914 and 5925. These four lines
are unchanged site lines (held for `p0-core`). The context matcher requires `SU(3)` or `anomaly`.
The negative matcher is: `Finiteness`, `finit`, `posit`, `substratum`, `configuration space`. These
rules replace the first two `RESIDUAL_ALLOW` entries, the corresponding `EXPLAINED` substring
entries and the blanket `(A1)` strip.

**The fifth `ptr` hit (V2).** `ptr` matches 5 lines at T1': the 4 W2 lines and papers/GR.md:58
("For a finite total system, restrict it to a conserved energy shell ..."), which matches PTR's
`finite total system`. P explains it by its third `RESIDUAL_ALLOW` entry ("finite-scope wording of
ledger X-70") and the strip `.replace('For a finite total system', '')`. W1 and W2 do not replace
that entry, and no allow rule does. GR.md:58 is one of the 84 replacement-region hit lines, so it
is resolved by its hit classification record (sec. 8), which names the `ptr` hit as well.

### 6.6 Residual review profile `resid` (widened in v5; for independent review)

`resid` is a review profile on added text. It exists so that a lexically unanchored paraphrase of
the retired posit, which no deny rule can close, is at least REVIEW_REQUIRED when it is added. v5
widens it as the v4 review's V8 proposed (owner decision V5-D2), and adds one alternative of its own.
Its pattern is the disjunction of three parts:

- **resid-a (v4)**:
  `(?i)\b(?:configuration|state|phase)\s+spaces?\b[^.;]{0,40}\b(?:is|be|being|are|remains?)\s+(?:\w+\s+)?finite\b|\b(?:posits?|premises?|axioms?|assumptions?|hypothes[ie]s)\b[^.;]{0,60}\bfinit\w*|\bfinit\w*[^.;]{0,60}\b(?:posits?|premises?|axioms?|assumptions?|hypothes[ie]s)\b`
- **resid-b (V8, as the v4 review proposed it)**:
  `(?i)\bfinite\s+(?:\w+\s+)?set\b|\b(?:substratum|universe|world)\b[^.;]{0,40}\b(?:is|be|being|are)\s+(?:a\s+)?(?:\w+\s+)?finite\b`
- **resid-c (v5)**: `(?i)\bfinite\s+(?:number|count)\s+of\s+(?:\w+\s+)?(?:states|configurations|elements|points|sites)\b`.
  The v4 review listed "The substratum is assumed to have a finite number of states." among the
  escapes its extension catches; measured, resid-b does not match it ("is assumed to have a" puts
  more than one word between "is" and "finite"). resid-c closes it.

**Forms it is meant to catch.** Measured, `resid` matches each of: "one of the posits is that the
configuration space is finite"; "a finite set with a deterministic bijection on it"; "uses a finite
set with a deterministic bijection"; "the substratum is a finite set with a bijection on it"; "We
take the substratum to be finite."; "the universe is assumed finite"; "The substratum is assumed to
have a finite number of states."; "the substratum's sixth axiom, finiteness". The first is the v3
review's example, which `p0-core` P4 and `ptr` do not match; the next three are real H sentences
with their "under A1" qualifier deleted (ch02:212, SM.md:30, ch02:136 at H).

**Every additional match, by tree.** `resid` is evaluated only on added text (sec. 2.3), so only
added-text lines receive an outcome from it. The whole-corpus counts below are given so that the
widening's reach is visible; outside added text they produce no item.

| Tree | Whole-corpus lines matched by resid-a | Lines matched by resid-b or resid-c only | Of those, hit by no other review profile | Outcome |
|---|---|---|---|---|
| E | 141 | 75 | 41 | none: `resid` is not evaluated on `E` |
| H | 138 | 79 | 42 | none: `resid` is not evaluated on `H` |
| T1' (whole corpus) | 98 | 88 | 46 | none outside added text |
| T1', added text (287 splice-image lines) | 28 | 17 | 4 | REVIEW_REQUIRED `unclassified` for the 4 lines below |

resid-c alone matches no line at E, H or T1', and none of the 287 added-text lines.

**The 4 newly matched lines at T1' (added text, no other review profile, no deny match).** Each
receives REVIEW_REQUIRED `unclassified` until a hit classification record or allow rule resolves
it. None receives FAIL, because no deny rule matches it, and none receives PASS without a record.

| Line | Text near the match | Reading (the writer's, for the reviewer) |
|---|---|---|
| FULL:6265 | "A referee who denies that the universe as a whole is finite does not thereby reject ..." | legitimate: the universe's finiteness is denied as a premise |
| book/appendix-c-objections.md:108 | the same sentence (mirror of FULL:6265) | legitimate |
| papers/Complexity.md:206 | "uniform relabelling of a finite set of hidden configurations ..." | legitimate scope wording |
| papers/Structure.md:1010 | "... takes the substratum to be a locally finite partially-ordered set ..." (causal-set literature) | legitimate: a description of another programme |

The 13 lines that resid-a alone already matched (sec. 0.3) keep REVIEW_REQUIRED as in v4. The
other 13 of the 17 added-text lines that resid-b matches are also hit by another review profile, so
the widening adds no item for them. `resid` therefore adds 17 REVIEW lines at T1' in all, 4 more
than v4. The v4 review's design target was 4 additional lines, and this count is the same 4 lines.

Adding or widening a review profile only adds REVIEW items, so it weakens nothing. resid-b and
resid-c need the same independent review as the deny set.

***

## 7. Delegation contract `delegation.json` (schema `oi-delegation/1`)

### 7.1 Location and pinning

- The contract is one structured record in the amended plan's record directory, beside
  `ledger.json` and `edits.json`. It is frozen with the plan at `F`, and its SHA-256 is listed in
  `F`'s PREREG pin table (the sec. 26.4 mechanism) and referenced by the configuration.
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

**preserve_check.py gaps (v2 addendum 4).** The amended plan must close gaps 1, 2, 5 and 7: record
the resolved candidate commit and tree and the checker blob, write a result on a usage error or
crash, and fail on a missing STALE id. Until it does, the contract's binding cannot hold, and the
affected classes are REVIEW_REQUIRED (missing) or FAIL (inconsistent). Gap 3 is met by the PDF
class below. Gap 4 is met by reading only the named checks' `status` and `discrepancies`
emptiness, never their text. Gap 8, the stale docstring, is corrected in the amendment.

### 7.3 Classes

| Class | Paths | How the tool verifies it |
|---|---|---|
| `tex` | the 9 TeX files of `tex_sources(ledger)`: Complexity, Computation, GR, Main, Methodology, SM, Structure, Substratum and FULL | delegated: `preserve_check.py --commit X --plan F --result-json OUT` in the clone, with the commit-mode checks "candidate against base, ledger, regenerated artifacts and plan record" and "scope assertions of amendment sec. 31" both `pass`. Native as well: each file's last line is `% source-sha256: <sha256 of X's .md>`, and the path set equals `tex_sources` |
| `pdf` | the 9 PDFs | delegated: `preserve_check.py --tree ... --pdf-compare BUILT --pdf-out OUT --plan F --result-json OUT` in the exact-head CI run on `X`. Required: `candidate_commit` and `candidate_tree` equal to `X`; a host run record (API) with `head_sha = X`, the named workflow and job, and conclusion success; the result hash equal to the uploaded artifact. Native as well: each PDF blob differs from `H`'s |
| `record-dir` | the plan's record directory | native: equals `F`'s blobs; additions only as enumerated under `execution/` |
| `sc42` | `verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json` | native re-execution in the clone at `X`: contains ca3a5bb2...; `--verbose` (plain and `-O`) exits 0 and is byte-identical to the file; `--self-test` (plain and `-O`) is byte-identical to the controls file, which equals `H`'s |
| `coverage-ledger` | `verification/coverage/LEDGER.json` (a ledgered file) | native: `H` plus its splices, except the fingerprint values of the seven STALE ids; each id exactly once; each value equals `tools/proof_census.py --json` (`X`'s blob, run in the clone, exit 0); any other byte FAIL |
| `ci` | the Lean kernel, Mathlib, R7 guard, `bohr_frequency_probe.py` and `guards_check.py --mutants` jobs | delegated: host run and job records (API) for the exact-head run on `X`, each named job concluding success |

Missing evidence is never PASS.

***

## 8. Classification of hits and the review load

### 8.1 Rules

| Hit | State until classified | Resolved by |
|---|---|---|
| any profile hit in an authorized replacement image, inside or outside a site region (`new-pattern-in-replacement` when the pattern is absent from the FROM region) | REVIEW_REQUIRED | a hit classification record or an allow rule |
| a hit on an unchanged site line | PASS | the frozen classification |
| a hit in an HP region | REVIEW_REQUIRED | the HP adjudication's `hit_classifications` |
| any other unheld hit | REVIEW_REQUIRED | a record or rule |
| a deny match on a tree where deny profiles run (sec. 2.3) | FAIL | not resolvable by a record |

A hit classification record (schema `oi-hit-classification/1`) binds:

- `file` and `line_sha256`, which must be unique in the tree;
- the segment;
- the splice id or HP step;
- the profiles and patterns;
- the semantic classification (which qualification is visible, with the reason);
- `author`, under the chain of sec. 6.3.

It states that it classifies meaning, and that the splice provenance is recorded separately. A line
hit by several profiles needs one classification that names every profile hit on it.

### 8.2 Review load before the amended plan can pass as written (R5)

Counted at T1'. Each row states its profile set and carries a label of sec. 0.3. The four rows
marked "p0+ext" are disjoint from each other; the rows under other profiles may share lines with
them, as stated.

| Set | Profile set | Lines | Label |
|---|---|---|---|
| Hit lines in the 197 site replacement regions | p0+ext | 84 | IR |
| Hit lines in splices over hit lines of HP site regions | p0+ext | 16 | IR |
| New hit lines on non-site lines (D237, D238, D241, D242, D246, D247, D388) | p0+ext | 7 | IR |
| Pre-existing unheld lines identical at H | p0+ext | 93 | IR |
| `resid` hits in added text, hit by no other review profile | resid (v5) | 17 (13 by resid-a, 4 added by resid-b) | 13 IR+WR; 4 WN |
| W1 allow rules | count-grep | 7 | IR. 2 lines (FULL:5270, ch19:198) are also p0+ext hits among the 93; 2 (ch19:212, FULL:5284) lie in replacement regions but are not p0+ext hits, so they are outside the 84; 3 are hit only by `count-grep` |
| W2 allow rules | ptr, repo | 4 | IR; unchanged site lines, held for p0-core |
| The fifth `ptr` hit, papers/GR.md:58 | ptr | 1 | IR+WR; one of the 84, resolved by its record |
| HP site adjudications, with `hit_classifications` for their regions and `own_lines` for the 22 merged sites | | 113 sites | IR |
| Meaning-context adjudications (sec. 4.4) | | 12 | IR; 7 HP, 5 RET |
| Indicator adjudications (sec. 4.4) | | 6 | IR; 3 HP, 3 RET |

**Totals.** Replacement-text hit lines under p0+ext: 84 + 16 + 7 = 107. Unheld or replacement p0+ext
lines in all: 107 + 93 = 200 (IR, also counted directly as 200). Distinct corpus lines that need a
classification record or rule under all review profiles: 200 + 5 (W1 lines that are not p0+ext
hits) + 4 (W2) + 17 (`resid`) = 226 (WN; the v4 total of 222, IR, had 13 `resid` lines).
Convention: 84 is used, with W1's 7 lines counted in their own row; v3's 86 came from a different
overlap test (sec. 0.3).

The `repo` profile (sec. 11 item 11) adds the following. Measured with P's own `classify()` at
T1', there are 0 unexplained lines, but 176 active lines are explained by entries that sec. 6.3
does not admit:

- 96 lines by path-wide "unrelated label" entries;
- 31 lines by path-wide "guard pins" entries;
- 14 lines by substring entries, without fingerprints (9 "unrelated label", 1 "historical record
  label", 1 "registry identifier (kept)", 3 "preserved historical evidence");
- 35 lines as "kernel identifier" (IDENT), without a rule.

The split is by the class `classify()` returns (IR+WR). v4's split (37 / 12) attributed each line by
the first `EXPLAINED` entry for its path, and so counted 23 IDENT lines in files that also carry
substring entries as substring lines.

Each needs an exact-path, fingerprinted rule or record. The 5486 lines in historical records and
the 2 lines in generated artifacts are outside the profile's scope. That scope is a reviewed scope
record (prefix lists are allowed only there), and any change to it is widening (sec. 16.2).

The HP regions' hits are among the 93 + 16. Records may therefore serve two rows of the table, but
each hit line needs exactly one classification.

Until all of the above exist, `coverage` and `terms` at T1' are REVIEW_REQUIRED at best, and FAIL
while any FAIL item of sec. 9 remains.

***

## 9. Complete list of FAIL and REVIEW conditions

### FAIL (exit 20)

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
- `item7-literal-match` (the countercontrol profile only);
- `rule-negative-match`, `rule-overreach`;
- `record-invalid`;
- `stale-adjudication`;
- `final-unclassified` (only under `--final`, sec. 5).

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
- `context-structure-changed`;
- `delegated-evidence-missing`;
- `side-change-unclassified` (a change on `M` outside every declared class).

ERROR, VOID, USAGE and INTERNAL are as in sec. 5.

***

## 10. Test matrix

Each control runs in both directions: the mutant gives the stated outcome, and the restored tree
returns to its control outcome. Each expected FAIL names the sec. 9 class that produces it, and
each expected deny FAIL names the rule alternative that produces it (measured on the control text,
sec. 14).

### 10.1 Unit and mutation controls (synthetic, in memory)

The v2 controls U1-U15 and M1-M11 stand, with v4 classes and exit codes. Added:

| Id | Case | Expected |
|---|---|---|
| K1 | the neighbour line of a meaning-context site is negated | FAIL `context-meaning-unverified` |
| K2 | the same next to a non-required site | PASS, `context_changed: true` |
| K3 | two site paragraphs swapped | per site, as K1 and K2 |
| K4 | a site line moved to a distant section of the same file | as K1 and K2 |
| K5 | an ANAPH site ("This bound ...") whose line above is changed, s3 `visible` | FAIL `context-meaning-unverified` |
| K6 | a labelled item `*(A2) Determinism.*` whose list lead-in is changed | REVIEW_REQUIRED `context-structure-changed` |
| K7 | a table row whose header row is changed; separately, whose neighbour row is changed | REVIEW_REQUIRED `context-structure-changed` in both |
| K8 | a list item whose trailer paragraph is changed (the Substratum.md:127 shape) | REVIEW_REQUIRED `context-structure-changed` |
| K9 | a PARTIAL site, nothing else changed | PASS; `partial_quote: true`; outcome unchanged when the flag is toggled |
| B1 | an empty-image splice on a site line | `authorized-removal`; a hit at its offset is "in image" |
| B2 | a multi-line splice (33 exist in P) | `authorized-replacement` with a line range |
| B3 | a zero-length insertion at a line boundary | the overlap rule of sec. 5 |
| B4 | a last line without LF | located and spanned to end of file |
| B5 | a splice making a replacement region non-unique in `X` | FAIL `duplicated` at the next search |
| B6 | a splice touching a site's end offset only | no overlap: site `unchanged` |
| H1 | HP adjudication naming #1473 where the walk gives #1474 | FAIL `provenance-mismatch` |
| H2 | one step listed where the walk gives two | FAIL `provenance-gap` |
| H3 | a change at an unpinned commit | FAIL `provenance-foreign` |
| H4 | an adjudicated site later rewritten outside every splice | FAIL `unauthorized-change` (RET) |
| H5 | an HP site overlapped by a splice, with no adjudication | FAIL `untracked-hp-overlap`, visible in HP and RET |
| H6 | an adjudication changing a site's row | FAIL `adjudication-row-changed` |
| H7 | two adjacent sites, separated by one blank line, both changed at one E..H step, and an H..X splice inside the second only | both sites reported as HP; each carries `region_shared_with` naming the other; `region_splices` lists the splice for both; `line_splices` lists it for the second only. With an adjudication whose `own_lines` leave a line unassigned, or attribute the splice to no site: FAIL `record-invalid` |

### 10.2 Adversarial controls (each tied to its rule)

The V controls are splices adding the stated text to the stated file (added text), unless stated
otherwise.

| Id | Case | Expected | By |
|---|---|---|---|
| L1 | the W1 sentence shifted by 40 lines | PASS | W1 rule |
| L2 | the W2 lines moved | PASS | W2 rule |
| L3 | a W1 sentence copied inside scope | FAIL `rule-overreach` | `max_instances` |
| L4 | a W1 sentence copied outside scope | REVIEW_REQUIRED `unclassified` | scope |
| V1 | "The six structural properties of the substratum are listed in Chapter 2." | FAIL `deny-match` | DR-1b |
| V2 | the W1 sentence of ch19:212 edited to "six structural properties, one of which is total finiteness," (a synthetic edit; DR-3's real witness is RT-DR3W) | FAIL `deny-match` | DR-3 |
| V3 | "(A1) the substratum is finite in total" in appendix B | FAIL `deny-match` | DR-4 |
| V4 | "the framework's sixth structural property, finiteness of the bijection" | PASS (no hit) | accepted residual after DR-2 was dropped (V5-D1, sec. 6.4.1); the original item 7 misses it too. Kept so that a change in its outcome is visible |
| V27 | "The framework's sixth structural property is finiteness of the substratum" (the text of v4's former DR-2 countercontrol), added alone and as the edited glossary.md:13 line | PASS (no hit) in both | accepted residual after DR-2 was dropped (V5-D1, sec. 6.4.1); the original item 7 misses it too. Kept so that a change in its outcome is visible |
| V5 | "**(A1) Finiteness.** The configuration space is finite." in appendix B | FAIL `deny-match` | DR-4 (case-insensitive; matched within the label) |
| V6 | "the six structural properties of the substratum, including finiteness" | FAIL `deny-match` | DR-1b and DR-3 |
| V7a | V2 with DR-3 removed from the profile set. Precondition: the text is an edit of a sentence fingerprinted by a W1 rule, inside that rule's scope | FAIL `rule-negative-match` | W1's negative matcher (`finit`): shows DR-3 is the operative deny rule |
| V7b | V2's text placed in a file outside every W1 rule's scope, DR-3 removed | REVIEW_REQUIRED `unclassified` | p0-core and `count-grep` hits with no rule |
| V7c | a W1 sentence edited with no negative literal (one word of the enumerated list changed) | REVIEW_REQUIRED `rule-fingerprint-mismatch` | sec. 6.2 step 4 |
| V9 | "Six structural assumptions define the substratum." | FAIL `deny-match` | DR-1a |
| V10 | "the six structural conditions on the substratum" | FAIL `deny-match` | DR-1a |
| V11 | "six structural premises of the framework" | FAIL `deny-match` | DR-1a |
| V12 | "the six substratum posits" | FAIL `deny-match` | DR-1a |
| V13 | "the structural assumptions A1 through A6" | FAIL `deny-match` | DR-1c |
| V14 | "A1--A6"; "A1—A6"; "(A1)–(A6)"; "A1, ..., A6" (four cases) | FAIL `deny-match` each | DR-1c |
| V15 | "the substratum's sixth axiom, finiteness" | REVIEW_REQUIRED `unclassified` | `resid` (resid-a), after DR-1d was dropped (V5-D1) |
| V16 | "posit A1 (finiteness) holds" | FAIL `deny-match` | DR-4 |
| V17 | "A1 (Finiteness): the configuration space is finite" | FAIL `deny-match` | DR-4 |
| V18 | "(A1) Finiteness. The configuration space S is finite." | FAIL `deny-match` | DR-4 |
| V19 | "The posit ledger has 14 items." | FAIL `deny-match` | DR-5 |
| V20 | "the six structural properties of the bijection, the first being finiteness of S" | FAIL `deny-match` | DR-3 |
| V21 | "one of the posits is that the configuration space is finite" | REVIEW_REQUIRED `unclassified` | `resid` only; residual limit (sec. 1): no deny rule |
| V22 | papers/Main.md:736's H sentence ("Fourteen items, ...") reinstated at a T1'-style `X` | FAIL `deny-match` | DR-5 (the original item 7 fails it too) |
| N-W | every W1 and W2 line at T1', and papers/Main.md:738 ("Thirteen items") | no deny match | negative examples |
| V23 | ch02-substratum.md:136 at H ("... the substratum is a set (finite under A1) with a bijection ...") reinstated at a T1'-style `X`; run as item 7 (`terms --check item7 --final`) | FAIL `final-unclassified` (`ptr` hit; no deny rule matches) | sec. 5, 11 note 1 (V3) |
| V24 | "six structural hypotheses" added; run as item 7 with `--final` | FAIL `final-unclassified` (`count-grep` hit; no deny rule matches) | V3 |
| V25 | the other direction: V23 and V24 without `--final` give REVIEW_REQUIRED `unclassified`; a W2 line with its rule under item 7 with `--final` gives PASS; a `resid`-only hit (V21) under item 7 with `--final` stays REVIEW_REQUIRED, since `resid` is not in item 7's `final_profiles` | as stated | sec. 5 |
| V26 | added, one at a time: "a finite set with a deterministic bijection on it"; "the substratum is a finite set with a bijection on it"; "We take the substratum to be finite."; "the universe is assumed finite"; "The substratum is assumed to have a finite number of states." | REVIEW_REQUIRED `unclassified` each | `resid` (resid-b, resid-b, resid-b, resid-b, resid-c) |
| A1r | rule scope widened to `book/` | FAIL `record-invalid` | sec. 6.3 |
| A2r | literal shortened to `(A1)` | FAIL `record-invalid` | widening |
| A3r | fingerprint swapped, count unchanged, no widening review | FAIL `record-invalid` | widening: any fingerprint change |
| A4r | widening review signed by the rule's author | FAIL `record-invalid` | reviewer is not the author |
| A5r | allow rule fingerprinting a sentence that a deny rule matches | FAIL `deny-match` | deny precedence (sec. 6.2 step 2) |
| A6r | literal not covering the trigger | FAIL `record-invalid` | trigger definition |
| A7r | reused rule id | FAIL `record-invalid` | id rule |
| A8r | allow rule with no negative example | FAIL `record-invalid` | examples |
| A9r | rule widened by one alternation | FAIL `record-invalid`, and caught by its own negative example | widening and examples |
| A10r | deny rule narrowed in scope | FAIL `record-invalid` | deny widening |
| A11r | deny rule whose countercontrol no longer matches | FAIL `record-invalid` | sec. 6.3 examples and countercontrols |
| S1r | a fingerprinted sentence edited | REVIEW_REQUIRED `rule-fingerprint-mismatch` | sec. 6.2 |
| S2r | a fingerprinted sentence deleted | REVIEW_REQUIRED `rule-stale` | |
| N1 | a PIN_OK entry dated after `F` | FAIL `pin-broken` | sec. 6.3 |
| N2 | a reconciliation record that changes a decision on `X` | FAIL `record-invalid` | sec. 13.3 |
| O1 | a record whose review record has `reviewer` equal to its `author` | FAIL `record-invalid` | sec. 6.3 |
| O2 | a review record naming another blob of the same path | FAIL `record-invalid` | binding to the reviewed blob |
| O3 | a review whose `verdicts` omit one item id | FAIL `record-invalid` | coverage of every item |
| O4 | an owner authorization naming the record's path without a hash | FAIL `record-invalid` | hash binding |
| O5 | a `reviewer` field holding a CI run URL; separately, an `owner` comment id pointing to an Issue | FAIL `record-invalid` | no role inferred from a tool result |
| O6 | a record edited in place after `F` (blob differs from the configuration's reference) | ERROR `SOURCE_CHANGED` | sec. 6.3, 16.2 |
| O7 | a superseding record with no new review or authorization | FAIL `record-invalid` | corrections |
| O8 | a record added after `F` and used for a decision on `X` | FAIL `record-invalid` | sec. 13.3 |
| O9 | a complete chain (record, review, authorization, configuration reference) | the record is admitted | positive control |
| G1 | delegated result whose `candidate` is an abbreviation | FAIL `delegated-evidence-invalid` | sec. 7.2 |
| G2 | no delegated result supplied | REVIEW_REQUIRED `delegated-evidence-missing` | sec. 7.2 |
| G3 | LEDGER.json with one STALE id removed | FAIL | sec. 7.3 |
| X1 | `record --pin H` | ERROR `PIN_MISMATCH`, exit 65 | sec. 5 |
| X2 | an exception injected in classification | INTERNAL, exit 71 | sec. 5 |
| X3 | an unknown flag | exit 64, stderr JSON, nothing written | sec. 5 |
| X4 | `--help` | exit 64 | sec. 5 |
| X5 | a missing required argument | exit 64, never 2 | sec. 5 |
| X6 | a run whose outcome is REVIEW_REQUIRED | exit 10, distinct from X3-X5 and from FAIL | sec. 5 |
| X7 | the tool run with a deliberately broken import in its package (a module raising `ImportError` at import time, before the wrapper's own imports complete) | a nonzero exit distinct from 20 (the interpreter's 1, or 71 if the wrapper caught it); no `result.json` with outcome PASS; the consumer's acceptance predicate reports non-acceptance | sec. 5 |
| X8 | the interpreter pointed at a missing script path | exit 2 from the interpreter; non-acceptance | sec. 5, unlisted codes |
| X9 | an unexplained `repo` hit run as item 11: without `--final`; with `--final`; a REVIEW item of a profile outside item 11's `final_profiles` with `--final`; and `--final` without `--check` | REVIEW exit 10; FAIL `final-unclassified` exit 20; that other item stays REVIEW; USAGE exit 64 | sec. 5 |
| X10 | exit 0 with a `result.json` whose outcome was edited to FAIL; exit 0 with an engine blob hash differing from the pin | non-acceptance in both | acceptance predicate |

### 10.3 Real-tree controls (CI)

The rules are preregistered. The counts are references (sec. 0.3).

| Id | Run | Rule | Reference |
|---|---|---|---|
| RT-A | `record --pin E --record H` | PASS | frozen replay: 0 errors; 697 anchors |
| RT-E | `coverage --commit E` | PASS (deny profiles not evaluated on `E`, sec. 2.3) | 697 unchanged |
| RT-H0 | `coverage --commit H`, no HP records | FAIL; every FAIL and indicator item has obligation HP | 113 `hp-unadjudicated`; 7 HP `context-meaning-unverified`; 3 HP `context-structure-changed` |
| RT-T0 | `coverage` at `X = T1'`, no records | FAIL. HP: 113 `hp-unadjudicated`, 7 context FAILs, 3 structure REVIEWs. RET: 19 `untracked-hp-overlap` (region-attributed; 18 line-attributed), 5 `context-meaning-unverified`, 3 `context-structure-changed`. Deny: 0. REVIEW: sec. 8.2 | 383 unchanged (168 moved), 197 replaced, 4 removed; 9 region-merger groups covering 22 sites, each site carrying `region_shared_with`; only Substratum.md 266/268 overlapped by a splice (D029) |
| RT-T | RT-T0 with all reviewed records of sec. 8.2 | PASS only when every record verifies under sec. 6.3; any missing record leaves REVIEW_REQUIRED or FAIL | |
| RT-C | `execution` at `X = T1'` with `F` = the amended freeze | candidate checks as sec. 11; PASS only with contract evidence | 399 splices verified at H; 23 corpus and 21 other ledgered files conform, except LEDGER.json under the `coverage-ledger` class |
| RT-D | `terms --commit T1' --base H --ledger F:ledger.json` | 0 deny matches; W1 and W2 PASS with their rules, else REVIEW; GR.md:58 PASS with its record, else REVIEW; `resid` 17 lines REVIEW until classified | |
| RT-DR | `terms --commit H --profile DR-1,DR-3,DR-4,DR-5` | FAIL `deny-match`; the item for each named countercontrol line of sec. 6.4 carries the target rule id (DR-1a on FULL:6504 and glossary.md:13, DR-1b on ch09:104, DR-1c on FULL:718, DR-4 on Substratum.md:92, DR-5 on Main.md:736), checked by id, not by the run's outcome (O3); the same profiles at T1' match 0 lines and 0 sentences | at H: DR-1 61 lines (a 6, b 2, c 55), DR-3 0, DR-4 28, DR-5 1, 86 distinct lines; at E: 95 |
| RT-DR3W | control-only scan of `AGENTS.md` at H (blob 12a9281f..., sha256 d87acac5...) with DR-3 alone (sec. 6.4); countercontrol: `AGENTS.md` at T1' (sha256 59b68984...) | exactly one DR-3 sentence at H, starting on line 37 and including lines 37-38 (the lines splice D296 rewrites); 0 at T1' | |
| RT-I7 | `terms --commit T1' --profile item7-literal`; the same at H | FAIL `item7-literal-match` at both | T1': exactly 7 "six structural" lines (SM.md:1394, ch09:137, ch19:198 and 212, FULL:2554, 5270 and 5284), 0 "Fourteen", 0 "sixth of"; `\bA1\b` 4 (the W2 lines). H: 11 / 1 / 2; `\bA1\b` 179 |
| RT-I7A | the proposed item-7 amendment check (sec. 11 note 1) at H and at T1', no records | FAIL at both. Every one of the 95 retired lines of sec. 0.3 is FAIL (`final-unclassified`), none only REVIEW | H: 86 `deny-match` lines and 123 `final-unclassified` lines (209 FAIL lines), counting line-level deny matches only; with every line of a matching multi-line sentence counted, 93 and 216, the 123 unchanged (O8). T1': 0 deny lines; 12 `final-unclassified` lines (the 7 W1 lines, the 4 W2 lines, GR.md:58), which become PASS once W1, W2 and GR.md:58's record exist |
| SW1 | per-site sweep at E: each of the 697 sites, one token deleted | exactly one FAIL naming that site | |
| SW2 | per-site sweep at H: each of the 584 sites | exactly one FAIL naming that site | |

***

## 11. Mapping of the mandatory sec. 11 checks (P's PREREG sec. 11) to the tool

Every command adds `--config F:<record dir>/retirement-config.json` and `--out DIR`, and reads
`F`'s records by object id. Profiles, rules, the delegation contract and the HP obligations come
from the configuration record. Paths given as `F:...` below are resolved through it. `X` is the
execution head. The "Countercontrol" column gives a mutant on which the original check fails; the
tool must also give a non-PASS result on it, and a FAIL wherever the original's failure was a hard
failure.

| # | Original check | Tool command | Expected at a T1'-style `X` | Countercontrol |
|---|---|---|---|---|
| 1 | `edits_check --commit X`: every `new` present; residual pointer scan zero unqualified | `execution --scientific-base H --candidate X --ledger F:ledger.json --edits F:edits.json` (splice postconditions) and `terms --commit X --profile ptr` | splices PASS; `ptr` has 5 hits: the 4 W2 lines PASS with their rules, papers/GR.md:58 with its hit classification record, else REVIEW | one splice reverted in `X`: FAIL `unauthorized-edit`. Original: the `new` string is absent |
| 2 | `ledger_check build` and `check`; CK1-CK8 PASS; extended scan 0 unqualified | `record --pin E --record F` and `coverage --commit X --segment E..H --segment H..X=F:ledger.json --hp F:hp.json --classify F:...` | FAIL or REVIEW (RT-T0) until the records of sec. 8.2 exist; PASS only with them | the frozen self-test's countercontrols at E: unclassified new site gives REVIEW_REQUIRED; dropped Phase-3 site gives FAIL `missing`; J row with S1 Yes gives FAIL (op A `record_checks`) |
| 3 | build; no dropped glyphs; page and median-character counts | `execution ... --delegation F:delegation.json` (classes `tex`, `pdf`, `ci`) | PASS only with bound exact-head evidence | evidence from another `head_sha`, or `build.rc` nonzero: FAIL `delegated-evidence-invalid` |
| 4 | `coverage_check.py`; STALE entries re-affirmed | `execution` class `coverage-ledger`, plus `ci` job `coverage_check` | PASS iff the seven values equal `proof_census` | one STALE value altered, or an id removed: FAIL |
| 5 | register scan of added lines: 0 | `execution` profile `register` on replacement text | PASS (P's `--static` recorded 0) | a splice adding "no longer": FAIL `deny-match` |
| 6 | infinity scan of added lines: 0 | `execution` profile `infinity` on replacement text | PASS (0 recorded) | a splice adding "is infinite": FAIL |
| 7 | corpus grep: only ledger false positives for `\bA1\b` and related terms; posit counts ("Fourteen", "six structural", "sixth of"): zero | as frozen: `terms --commit X --profile item7-literal` | **FAIL** at T1': 7 "six structural" lines (W1), 0 "Fourteen", 0 "sixth of"; `\bA1\b` 4 lines (W2). Item 7 as frozen does not pass at T1' (RT-I7) | the H-form "Fourteen items" reinstated (V22): FAIL in both the literal check and DR-5. See note 1 for the proposed amendment |
| 8 | mirrors byte-identical | `execution` subject `mirror` | PASS (P's `--static`: 0 findings) | FULL mirror text altered: FAIL `mirror-mismatch` |
| 9 | census registry notes updated in the same commit | `execution` conformance of `verification/lean-manuscript-census.json` (15 splices) | PASS | one registry splice dropped: FAIL `unauthorized-edit` |
| 10 | Lean docstring-only; kernel and Mathlib builds; CI | `execution` subject `lean` (equal outside comments) and class `ci` | PASS with evidence | a Lean definition changed: FAIL `lean-code-change` |
| 11 | `edits_check --repo-scan --final --commit X`: 0 unexplained | `terms --commit X --check item11 --scope F:repo-scope.json --rules F:repo-rules.json --final` | FAIL `final-unclassified` for each of the 176 lines of sec. 8.2 until it has an exact rule (REVIEW without `--final`); then PASS | a new unexplained `A1` line in a new active file: FAIL in the original, FAIL `final-unclassified` here. See note 2 |
| 12 | `edits_check --pins --commit <X's parent>`; guards mutants; R7 and bohr in CI | `execution` subject `pin` (counts at `H` and at `X`) and class `ci` | PASS (the original reported 0 unresolved at its base) | a guard-pin splice dropped: FAIL `pin-broken` |
| 13 | SC-42 regeneration and safeguards | `execution` class `sc42` (native) | PASS iff byte-identical | the result file hand-edited: FAIL |
| 14 | `preserve_check --commit X` (`--base main` when moved) | `execution --scientific-base H --main M --candidate X [--landing L]`, plus the `tex` contract | candidate PASS against `H`; landing per sec. 13 | an extra word in an unledgered file of `X`: FAIL `unauthorized-change`. `L` dropping W's workflow: FAIL `landing-drops-main-change`. Compare the original `--base W`, which failed on `X` only for that workflow file |

**Note 1 (item 7; owner decision D1).** Item 7 as frozen fails at T1': seven lines contain the
legitimate count of the bijection's properties (W1). The tool keeps that literal check as the named
countercontrol `item7-literal`, with the expected FAILs of RT-I7.

- Any restatement of item 7 is a **plan amendment**. It needs its own preregistered text, an
  independent review of the deny set (sec. 6.4), the `resid` profile (sec. 6.6) and the W1 rules,
  and the owner's authorization. It is not "passing as written", and it cannot be used in the
  current frozen trials. Under the exception-free route, the amendment must be adopted before any
  trial can claim item 7.
- The check this design proposes for that amendment: `terms --commit X --base H --ledger
  F:ledger.json --check item7 --final`, where the configuration's `checks.item7` (sec. 16.2) has
  profiles `ptr`, `count-grep`, `resid`, DR-1, DR-3, DR-4 and DR-5 and `final_profiles` `ptr` and
  `count-grep`. It requires zero deny matches; every `ptr` and `count-grep` hit not classified by a
  reviewed rule or record is FAIL `final-unclassified`; every unclassified `resid` hit is
  REVIEW_REQUIRED.
- **Failure behaviour is not weakened (V3).** The original item 7 fails hard on any `\bA1\b` line
  that is not a ledger false positive and on any posit-count literal. In the proposed check every
  such line is a `ptr` or `count-grep` hit, so it is FAIL unless a reviewed record classifies it,
  which is the counterpart of the original's "ledger false positive". At H, 95 retired lines carry
  `\bA1\b` or a `count-grep` literal and match no deny rule; under v4's check they were only
  REVIEW, and under this check all 95 are FAIL (RT-I7A). Counts with no records: at H, 86 deny lines
  (line-level matches; 93 if each line of a matching multi-line sentence is counted) and 123
  `final-unclassified` lines; at T1', 0 deny lines and 12 `final-unclassified` lines (the 7
  W1 lines, the 4 W2 lines and papers/GR.md:58), which pass once their rules and record exist.
  Countercontrols: V23 and V24 FAIL; V25 shows the other direction. `resid` hits stay REVIEW: the
  original check does not fail them at all, so keeping them REVIEW is stricter than the original,
  not weaker.
- **Scope (O7).** Item 7's scope is `papers/*.md` and `book/*.md`. Active files outside it still
  carry "the sixth structural assumption" for A6, whose count includes A1 (for example
  `verification/README.md:2320` and `A6Instantiation.lean:15` at T1'). The amendment's scope
  statement names this, and DR-1's ordinal alternatives are a corpus terminology decision
  (sec. 6.4).
- v3's claim that the restatement "changes the check's text, not its decision on any retired form"
  was false for v3's seed set: the H sentence "Fourteen items, of unequal weight, ..."
  (papers/Main.md:736) escaped DR-1..DR-4. With DR-5 it is a FAIL (RT-DR, V22). The claim is not
  repeated for the v5 set: whether that set preserves the original prohibition on every retired
  form is the independent review's question. The lexically unanchored paraphrases remain a stated
  residual limit (sec. 1), covered at least by REVIEW through `resid` for the classes sec. 1 names.
- The plan's own implementation never ran the literal grep. It checked the retired phrases of
  `identifier_sim()`, P lines 331-335.

**Note 2 (item 11).** The tool is stricter than item 11's original.

- The original passes a premise line in any path-wide-explained file, for example
  `tools/citation_roles_check.py`. The tool fails it.
- Without `--final`, the tool reports an unexplained line as REVIEW_REQUIRED, while the original
  reports it as a failure. The item names `--final`, and under it the REVIEW items of the `repo`
  profile become FAIL `final-unclassified` (sec. 5). No flag turns REVIEW_REQUIRED into PASS.

**Other wording the amendment must correct.** Item 4 says "four entries", but preserve_check's
STALE list has seven (sec. 31, nit 5). Item 12's "execution head's parent" becomes "the ledger base
H".

***

## 12. Placement and governance

### 12.1 Placement

- `tools/ledger_coverage.py` is the entry point. It installs the wrapper (sec. 5) and then imports
  the package.
- `tools/ledger_coverage/engine/` holds the engine (sec. 16.1), its JSON Schemas, the outcome
  checker and the in-memory self-test fixtures. This directory is the purity scope of Z9.
- `tools/ledger_coverage/adapters/` holds the adapter modules: the A1 adapters, the delegation class
  adapters and the synthetic configuration's adapters. It is outside the purity scope; each module
  is pinned by blob in the configuration that uses it (sec. 16.2).
- A new audit directory under `verification/audits/` (sec. A.36) holds the rule files, scope
  records, HP, context and hit classification records, review records, authorization records,
  reconciliation records, and the tool's landing record with its commands and counts.
- The plan's `delegation.json`, `hp.json`, `retirement-config.json` and rule files frozen with the
  plan live in the amended plan's record directory.
- The tool reads every record from git objects, which `export-ignore` does not affect.

### 12.2 Sec. 11 replacement text (v2 addendum 4, point 1)

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

The v2 sec. 13 rules stand, with the corrections below. The certified execution head is `C`
throughout (R9); `E` is only the ledger pin.

### 13.1 Roles and invariants

- **`H`** (`--scientific-base`) must equal `roles.scientific_base` in the frozen configuration
  record (sec. 16.2) and the ledger base. Every `base_sha256` must equal `H`'s blob. `R`'s tree at
  `H` is the pinned tree.
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
- **`C`**, the certified execution head, descends linearly from `X` when it differs from it. Each
  further commit is classified as `X` is.
- **`L`** has exactly two parents: the first equals the recorded `M` (FAIL
  `landing-first-parent-not-M` otherwise), and the second equals `C`. Each path is composed as in
  v2 sec. 13.2:
  - A ledgered conflict passes only if `L`'s bytes equal `M`'s bytes with `C`'s splices applied at
    `M`-translated offsets, each `old_sha256` re-verified against `M`.
  - A generated-artifact conflict is REVIEW_REQUIRED until it is regenerated from `L`'s sources
    under the contract.
  - Any other conflict is FAIL.

  The diff from `M` to `L` must equal the diff from `H` to `C`, path by path, after translation.

### 13.2 Controls

R1-R14, RT-X, RT-L and RT-L2 stand, read with `C` for the certified head. R15 is added: an `L`
whose first parent is a `main` other than the recorded `M` gives FAIL `landing-first-parent-not-M`.

### 13.3 Reconciliation records

- A record written after `F` is allowed only for side changes on `M` that the freeze could not
  foresee.
- It never changes any decision of op C on `X`, and never relabels a failing retirement check.
- It is under the ownership chain of sec. 6.3.

### 13.4 Re-resolving `M`

Immediately before landing, `M` is re-resolved from the remote `main` (`git ls-remote`, read-only)
and checked to equal `L`'s first parent. The landing record quotes the resolved id and the command.

**Sequencing safeguard (c.7093128173).** Before the tool lands, RT-L2 is run against a predicted
`M` that contains the tool's landing paths. It must show every side change classified and no
`base-drift`.

***

## 14. How the figures were measured

All figures were measured read-only, with throwaway scripts reading `git show`, `git ls-tree`,
`git rev-list` and `git cat-file --batch` from the local object store. Their outputs were written
outside the checkout, and the checkout stayed unmodified. Patterns are extracted from their blobs:
Phase-0 `sites.json` at `H`, `EXTENDED_PATTERNS` from `R/ledger_check.py` at `H` by `ast`, and P's
`edits_check.py` (blob sha256 2856e58c...d98c, verified against `P`'s tree). The v5 scripts are in
`work-v5/` beside this file; the v4 scripts in `work-v4/`; the earlier ones in `work/`; the v4
review's in `review-v4/`.

**v5 measurements (`work-v5/`).**

- **HP walk and mergers (`walk.py`).** A new implementation of sec. 3.2 from its text, over the
  first-parent chain E..H: 113 changed sites, 584 unchanged, 3 two-step sites, first-change
  attribution 48 / 23 / 15 / 15 / 12. Sites whose walks yield the same post-region at the same step
  are grouped: 9 groups, 22 sites (sec. 3.2).
- **Deny rules (`rules5.py`, `dr5.py`).** The v5 rule set and the v5 splitter (sec. 6.1, version 2).
  Line level over every top-level `papers/*.md` and `book/*.md` at E, H, W and T1': 95, 86, 86
  and 0 distinct lines. Per sentence (`sentcount.py`): at H DR-1a 6, DR-1b 2, DR-1c 65, DR-4 28,
  DR-5 1; at E DR-1c 70 and the others as per line; at T1' none. `AGENTS.md` at H
  and W: one DR-3 sentence (lines 37-39); at T1': none.
- **History search (`hist.py`, `hist2.py`).** The searched set is every blob at a top-level
  `papers/<name>.md` or `book/<name>.md` path in the tree of any commit reachable from the 794 local
  refs (7857 commits, `git rev-list --all` then `git ls-tree` per commit): 4677 blobs. It equals
  the union of the path-limited walk (`git rev-list --all --objects -- papers book`, 4657 blobs)
  and the unrestricted walk (`git rev-list --all --objects`, 4671 blobs), which miss 20 and 6 of
  them respectively (sec. 6.4.1). All 4677 were scanned for DR-1d, DR-2 and DR-3 at line and
  sentence level with the v5 splitter: 0 matches. (v5's first pass, `hist.py`, scanned the 4671
  of the unrestricted walk with a "sixth|seventh" prefilter, exact for DR-1d and DR-2: 0 matches.)
  Every
  text file at H (3543 files), W (3543) and T1' (3550): 0 matches of DR-1d or DR-2. DR-3 at H and W
  matches only `AGENTS.md`; at T1' it matches only the frozen record
  `verification/audits/foundations/a1exit-deletion-20261121/edits.json`, which quotes the old
  sentence as an edit's FROM text and is outside every deny scope.
- **Item 7 (`item7.py`).** PTR extracted from P's verified `edits_check.py`; the `count-grep`
  literals; deny lines at line level (`w1o8.py` adds the sentence-attributed variant of O8: 93
  deny lines, 123 unchanged, 216). At H: 198 `ptr` lines, 14 `count-grep` lines, 86 deny lines, 123
  lines that are `ptr` or `count-grep` hits and not deny lines. At T1': 5 `ptr` lines, 7 `count-grep`
  lines, 0 deny lines, 12 lines in all. Retired lines at H (carrying `\bA1\b` or a `count-grep`
  literal, the line text absent from the same file at T1', no deny match): 95, all among the 123.
- **Repo split (`repo.py`).** P's `edits_check.py` imported from its verified blob with `python -I`.
  Each `REPO_PAT` line of every tracked text file at T1' is classified by `classify()`; the
  mechanism (scope, path-wide entry, substring entry, IDENT) is read from the same `EXPLAINED`
  table: 96 / 31 / 14 / 35, with 5486 historical and 2 generated lines.
- **v3's 86 (`m10strict.py`).** `work/measure10.py` with only its overlap test changed from touching
  (`<=`, `>=`) to sec. 5's strict test gives 84. The script skips empty replacement images (`if seg
  and k >= 0`), so the touching test alone produced v3's 86.
- **`resid` (`resid5.py`, `resid5b.py`).** Added text is every T1' line holding a byte of a
  non-empty splice image in a `.md` file (287 lines). Each line is tested against resid-a, resid-b,
  resid-c, the other review profiles (p0-core, p0-para, ledger-ext, `ptr`, `repo`, `count-grep`)
  and the deny rules. Whole-corpus counts at E, H and T1' for the table of sec. 6.6.
- **Escape strings (`esc.py`).** The constructed strings of sec. 1 and 6.4.1 and of the v4 review,
  against the deny rules, `resid`, the other review profiles and the item-7 `final_profiles`.

**Figures carried from v4 and recounted by the v4 review** (`work-v4/` and `review-v4/rv_*.py`):

- **Context and the 12.** Unchanged sites are those whose pin line is unique in its file at E, H
  and T1'. A change is attributed to E..H if the context at H differs from the pin, and to H..T1'
  if the context at T1' differs from H's. 52 changes (27 / 22 / 3); 12 marked by the s3 table
  (7 / 5).
- **Overlap counts.** 19 sites and 31 splices by sec. 3.2's regions; 18 and 31 line-attributed
  (`git diff -U0 --no-renames`, myers and histogram agreeing). D029 (bytes 86149-86197 at H, empty
  image) lies inside :268's H line.
- **Hit lines in replacement regions (`b3.py`, `rv_b3.py`).** Non-HP sites are located at H by
  their unique pin line. A splice overlaps a site by sec. 5's rule. The region at T1' is the union
  of the site span and its overlapping splice spans at H, mapped to T1' offsets and expanded to
  whole lines; removed sites (empty image) have no region. 383 / 197 / 4 sites, 203 region lines,
  84 hit lines under p0+ext, 86 with `count-grep`. Variants: the touching test gives 381 / 199
  sites, 217 lines and 86 hit lines (extra: FULL:710, ch02:78); counting the removed sites' offset
  lines under the strict test gives 205 lines and 86, with the same two lines.
- **Unheld lines and the 16 / 7 split (`u116.py`, `rv_u116.py`, `rv_split23.py`).** 200; 84 in
  regions; 116 outside; 93 identical to an unheld H line; 16 in splices over hit lines of HP site
  regions; 7 new on non-site lines.
- **Literal greps (`lit.py`, `rv_lit.py`).** papers/*.md and book/*.md (top level),
  case-sensitive.
- **Indicators (`ind.py`, `ind2.py`, `rv_ctx.py`).** The definitions of sec. 4.2 and 4.3, applied to
  the pin line at E.
- **Merge ids.** `git rev-list --first-parent` over E..H, restricted to `papers` and `book` (v3).

***

## 15. Open points for the owner

1. **Decision records.** The owner decisions D1-D4, V5-D1 and V5-D2 of 2026-11-23 reached this
   writer only through the coordinating session. The design should cite them with author, time and
   comment id once the record exists (sec. A.42 item 7).
2. **Accepted residuals after V5-D1.** With DR-1d and DR-2 dropped, "the framework's sixth
   structural property, finiteness of the bijection" PASSes when added (control V4), and "the
   substratum's sixth axiom, finiteness" is REVIEW only (V15). The text of v4's former DR-2
   countercontrol, "The framework's sixth structural property is finiteness of the substratum",
   also PASSes (V27). None of these forms occurs in any tree or historical corpus blob.
3. **Residual classes of `resid` (V8).** After widening, the REVIEW guarantee covers the classes of
   sec. 1. Constructed forms outside them PASS: "the six posits of the substratum", "six assumptions
   about the substratum", "The posit ledger lists fourteen.", "the fourteen-item posit ledger" and
   "$A_1$–$A_6$" (the original item 7 misses them too). The owner may accept them as residual or ask
   for further rules. Optional point O1 of the v4 review proposed deny rules for them; v5 does not
   add them, because none has a real-tree match (0 at E, H and T1'), the same ground on which V5-D1
   dropped DR-1d and DR-2.
4. **LIST and TABLE reading.** v4 and v5 keep the neighbour context for list and table sites in
   addition to the review's structure contexts (sec. 4.3). This is stricter than D2's wording; the
   v4 review found it correct.
5. **Independent recount.** The figures labelled WN in sec. 0.3 need an independent recount before
   they are used as references.
6. **Item 7.** The amendment text itself is outside this design (sec. 11 note 1).

***

## 16. Generality: a core independent of any retirement, with frozen per-retirement configuration (condition 9)

### Scope

This section covers design only. It does not include:

- a second real retirement;
- a generic verifier of scientific proofs or semantic correctness;
- any reduction of A1 coverage or preservation obligations;
- any postponement of a review defect.

Only the A1 adapters and one minimal synthetic adapter set are specified. The acceptance gate
remains A1 correctness and fail-closed verification. Generalization is accepted only if every A1
control of sec. 10 and sec. 11 has the same outcome under the configured engine as specified above
(S13).

### 16.1 The engine (`tools/ledger_coverage/engine/`)

The engine is retirement-independent. It contains:

- the pipeline of sec. 2;
- the outcome, exit codes, acceptance checker and output of sec. 5;
- the algorithms: anchors (v1 sec. 4.2-4.4), the overlap and image rules (sec. 5), the region walk
  and merger reporting (sec. 3.2), the context hash, the indicator machinery and structure
  contexts with definitions supplied by the configuration (sec. 4), sentence splitting with the
  abbreviation list supplied by the configuration, rule application and record lint (sec. 6);
- the four role checks (sec. 13);
- the adapter interface definitions (sec. 16.3) and the loader that admits adapter modules by
  pinned blob;
- the configuration loader and validator (sec. 16.6);
- the purity lint Z9.

It contains no commit or tree id, path of a retirement record, terminology, regex pattern, site or
hit count, PR number, delegation class, s3 value, adapter name or checker schema. The adapters,
which must contain their retirement's schema strings (for example "a1exit deletion exact-edit
ledger v2"), are outside the engine, in `tools/ledger_coverage/adapters/` (R8).

**Z9, the purity lint.** It runs over the source blobs of `tools/ledger_coverage/engine/` and the
entry point, parsed by `ast`, and fails on any of the following:

- a hexadecimal literal of 7 or more hex digits standing alone (in a string or as a number),
  including any 40-hex literal;
- a string literal equal to any string value occurring in the A1 configuration, in a record it
  references, or in the synthetic configuration, unless the value is on the allowlist;
- a string literal or identifier matched by any review or deny profile of the A1 configuration.

**The allowlist** is fixed in the engine and is itself linted to contain only:

- the interface field names of sec. 16.3 and of the engine's record schemas (for example `id`,
  `file`, `start`, `end`, `new`, `old_sha256`, `new_sha256`, `splices`, `sites`, `base`, `files`,
  `retained`, `mirrors`, `site_id`, `pin_line`, `carried`, `row`, `code`, `owner`, `author`,
  `reviewer`, `reviewed`, `verdicts`, `supersedes`, `path`, `blob_sha256`, `segment`);
- the engine's own schema ids: `oi-ledger-coverage/4`, `oi-retirement-config/1`,
  `oi-term-rules/2`, `oi-delegation/1`, `oi-hp-adjudication/1`, `oi-context-adjudication/1`,
  `oi-hit-classification/1`, `oi-scope/1`, `oi-side-change-classes/1`, `oi-reconciliation/1`,
  `oi-review-record/1`, `oi-owner-authorization/1`;
- the engine's own enumerations: outcome names, sec. 9 class names, ERROR and configuration class
  names, extractor kinds, `review`, `deny`, `tree`, `added-text`, `accept`, `reject`, `dissent`.

Z9's controls are synthetic: they run the lint on an in-memory engine tree (Z9a-Z9f) and on the
real engine tree (Z9g). Z9 runs in CI and in `self-test`; a failure in `self-test` is VOID.

| Id | Case | Expected |
|---|---|---|
| Z9a | a 40-hex commit id planted as a string literal in an engine module | lint FAIL |
| Z9b | a 7-hex abbreviation planted | lint FAIL |
| Z9c | the A1 regex `\bA1\b` planted as a string literal | lint FAIL |
| Z9d | the s3 value "per unit Q2" planted | lint FAIL |
| Z9e | the allowlisted field name `splices` used in an engine module | lint PASS |
| Z9f | an adapter module under `adapters/` containing "a1exit deletion exact-edit ledger v2" | lint PASS (outside the purity scope); the same string moved into the engine: FAIL |
| Z9g | the real engine tree | lint PASS |

### 16.2 Configuration record `oi-retirement-config/1`

**Location and pinning.**

- One reviewed, versioned JSON record, `retirement-config.json`, in the retirement plan's record
  directory, frozen with the plan at `F`, under the ownership chain of sec. 6.3.
- Its SHA-256 is listed in `F`'s PREREG pin table, the sec. 26.4 mechanism.
- The tool reads it only as `--config F:path` from the object store. A hash that differs from the
  pin is ERROR `SOURCE_CHANGED`.
- A change after `F` requires a new configuration version and a new freeze.

**Fields.** All fields are required unless marked optional.

| Field | Content |
|---|---|
| `schema` | `oi-retirement-config/1` |
| `config_id`, `version`, `supersedes` | identity; `supersedes` is `{path, blob_sha256}` or null |
| `retirement` | name, accountable Issue and owner login |
| `roles` | `scientific_base` (full id); `pin` and `record_commit` (optional, for replay); `side_change_classes` (`{path, blob_sha256}`) |
| `corpus` | an exact path list, or declared path sets with stated patterns, in a scope record (sec. 6.3) |
| `adapters.ledger` | `{adapter, adapter_version, module: {path, blob_sha256}, path, blob_sha256, companion: [{role, path, blob_sha256}]}` |
| `adapters.sitemap` | as `adapters.ledger`, or null when the retirement has no frozen site map |
| `adapters.replay` | `{adapter, adapter_version, module: {path, blob_sha256}, module_path, record_tree, functions}`, or null (optional) |
| `profiles` | `[{name, kind: review or deny, scope, applies_to: tree or added-text, source: {commit, path, blob_sha256, extractor: {kind, selector}}, pattern_sha256}]` |
| `checks` | one entry per plan check that op D implements: `{id, profiles, final_profiles}`. `final_profiles` lists the review profiles whose REVIEW items `--final` converts for that check (sec. 5). A1: `item7` with `final_profiles` `ptr` and `count-grep`; `item11` with `final_profiles` `repo` |
| `rules` | `[{path, blob_sha256}]`, rule files `oi-term-rules/2` |
| `context_mapping` | `{source_field, values: {value: bool}, default: "invalid"}`. A value outside the table is a configuration error |
| `indicators` | the exact definitions of sec. 4.2 and the effects of sec. 4.3, as data (patterns, word lists, effect per indicator) |
| `sentence` | `{splitter_version, abbreviations}` |
| `hp_obligations` | `[{segment: [from, to], merges: [{pr, commit, first_parent}]}]` |
| `delegation` | `{path, blob_sha256}` (`oi-delegation/1`) with `class_adapters: [{adapter, adapter_version, module: {path, blob_sha256}}]`, or null |
| `records` | every record, review record and authorization record the run may use: `[{kind, path, blob_sha256}]` |
| `operations` | the supported subset of `record`, `coverage`, `execution` and `terms` |
| `controls` | `{path, blob_sha256}`: the retirement's preregistered control set (sec. 10, 11) with expected outcome rules |
| `author` | the configuration's writer; its review and authorization are records under sec. 6.3 |

Supported extractor kinds: `json-pointer`, `python-ast-assign` (a module-level name bound to a
string, a tuple of strings, a dict of strings, or a compiled regex call with a literal pattern), and
`literal-list`. The extractor's output must hash to `pattern_sha256`.

**Lint.** The configuration takes the lint of sec. 6.3, with these additions:

- every referenced blob exists at its stated commit (or at `F`) with its stated hash, adapter
  modules included;
- `roles.scientific_base` equals the ledger adapter's reported base;
- the `hp_obligations` segments end at `scientific_base`, and every merge is on its first-parent
  chain with its stated first parent;
- every delegation class has a class adapter;
- no profile name is duplicated, and every `final_profiles` entry of a check is a review profile listed in that check's `profiles`;
- every deny profile has examples in a rule file and a countercontrol named there, the countercontrol being a real line of a scanned file or a control-only input of the controls file;
- the controls file names at least one positive and one adversarial control per configured
  operation.

**Widening (R8, V5).** Every change compared with the superseded configuration is widening, and
needs a `widening_review` under sec. 6.3, unless it is on this non-widening list:

- adding a deny profile, a review profile or a control;
- adding a scope path to a deny profile;
- a context-mapping value changed from false to true;
- adding an entry to a check's `final_profiles`;
- removing an allow rule file.

For definiteness, each of the following is widening (the list is illustrative; the rule above
decides):

- a scope removed or narrowed, and any change to a scope record;
- a deny profile removed or changed; any profile changed;
- a context-mapping value changed from true to false; any change to `indicators`;
- an HP obligation removed;
- an HP obligation added, or a merge added to one (V5). A new merge turns a step that would be FAIL
  `provenance-foreign` into an adjudicable step, and a new obligation for a further segment turns
  changes that would be RET `unauthorized-change` into adjudicable HP sites; both can increase
  acceptance;
- a delegation class added;
- an allow-rule file added, or a new allow rule without `supersedes`;
- a side-change class added or changed;
- an adapter added, or an adapter's module blob or `adapter_version` changed;
- an extractor kind or selector changed;
- a sentence abbreviation added, or `splitter_version` changed (merged sentences change what the
  sentence-level DR-3 sees);
- any change to `operations`;
- an entry removed from a check's `final_profiles`, or a check removed from `checks`;
- a control-only input (sec. 6.4) added, removed or changed;
- a control removed or its expected outcome relaxed.

### 16.3 Adapter interfaces (versioned)

Each adapter is a module under `tools/ledger_coverage/adapters/` that declares an interface name,
an adapter name and an integer version. The engine admits an adapter only if the configuration
names it, its module blob hash equals the configured pin, and its declared interface, name and
version equal the configured ones. Anything else is ERROR `CONFIG_INVALID`. The engine holds no
adapter names.

| Interface | Must return |
|---|---|
| ledger | `base`; `splices [{id, file, start, end, old_sha256, new_sha256, new}]` (byte spans at `base`); `files {path: {base_sha256, expected_sha256}}`; `retained [{id, site_ref}]`; `mirrors [{id, mirror_of}]`; `ignored_fields`; plus validation errors (overlap, hash, schema) |
| sitemap | `pin`; `sites [{site_id, file, pin_line, carried: {row, code, owner}, context_field_value, quote}]`; `override_anchors`; `read_entries` |
| replay | `{equalities: [{name, equal}], errors: [str], self_test: bool}`, computed by calling the named functions of a frozen module in a materialization (v1 sec. 3.2), wrapped (sec. 5) |
| delegation | the classes of sec. 7. A class adapter has `verify(evidence, roles) -> PASS, REVIEW or FAIL` and a structured reason |

**The A1 adapters** (all under `adapters/`, each pinned by blob in the A1 configuration):

- `a1exit-exact-edit/2` reads `ledger.json` ("a1exit deletion exact-edit ledger v2") and
  `edits.json` ("a1exit deletion edit list v1").
- `a1exit-sitemap/2` reads the frozen `sitemap.json` ("a1exit site map v2"), `rows.json` and the
  Phase-0 quotes.
- `python-frozen-replay/1` replays `ledger_check.py`'s `manuscript_digest`, `build`, `render`,
  `splice_block`, `check`, `extended_unmapped` and `self_test`.
- The delegation class adapters are `preserve-check-v1` (tex, pdf), `record-dir/1`, `rerun-equal/1`
  (sc42), `fingerprint-regen/1` (coverage-ledger) and `host-run/1` (ci).

### 16.4 A1 as the first configuration: where each A1 constant goes

Every constant of v1-v3 and of this document's sec. 3-13 moves into the A1 configuration
`a1exit-retirement-config`, version 1, into a record it pins, or into an A1 adapter module it pins.
No check changes.

| Constant | Destination |
|---|---|
| `E`, record commit, `R` tree b05efdca | `roles.pin`, `roles.record_commit`, `adapters.replay.record_tree` |
| `H` | `roles.scientific_base` |
| `R` paths and the Phase-0/2 record paths | `adapters.sitemap`, `adapters.replay.module_path` |
| ledger and edits schema ids, `retained_unchanged`, `mirror_of` | the `a1exit-exact-edit/2` module, `adapters.ledger.companion` |
| frozen function names, line-523 handling | the `python-frozen-replay/1` module, `adapters.replay.functions` |
| corpus `papers/*.md`, `book/*.md` | `corpus` |
| profiles p0-core, p0-para, ledger-ext, ptr, repo, count-grep, item7-literal, register, infinity | `profiles` (sources: Phase-0 `sites.json`; `R/ledger_check.py` `EXTENDED_PATTERNS`; `P` `edits_check.py` `PTR`, `REPO_PAT`, `REG`, `CAPS`, `CAPS_OK`, `INF`, `NEUTRAL`; sec. 11 item 7 literals) |
| `resid` (resid-a, resid-b, resid-c), DR-1, DR-3, DR-4, DR-5, W1, W2, the converted `EXPLAINED` entries | rule files under `rules`, profiles naming them |
| item 7 and item 11 profile sets and `final_profiles` (`item7`: `ptr`, `count-grep`; `item11`: `repo`) | `checks` |
| DR-3's control-only witness input (`AGENTS.md` at H) | `controls` |
| repo scope (historical prefixes and files, generated artifacts) | a scope record under `records` |
| s3 mapping (sec. 4) | `context_mapping` (`source_field: s3`) |
| ANAPH, LIST, TABLE, PARTIAL definitions and effects | `indicators` |
| sentence abbreviations | `sentence.abbreviations` |
| the six pinned merges and PR numbers (sec. 3.1) | `hp_obligations[0]` (segment `[E, H]`) |
| tex/pdf/record-dir/sc42/coverage-ledger/ci classes, STALE ids, SC42_BASE ca3a5bb2, `tex_sources` rule, `a1exit-checker-result-v1` | `delegation.json` and the class adapters' parameters in it |
| W's workflow, the tool's landing paths | `roles.side_change_classes` |
| every HP, context, hit classification, review and authorization record | `records` |
| controls RT-*, SW*, the sec. 11 mapping and countercontrols | `controls` |

Counts such as 697, 113 and 19 are not configuration. They are references in the controls file and
in the landing record.

Acceptance criterion S13: the configured engine reproduces every A1 control outcome of sec. 10 and
11 as corrected in this document (control V5 matched by DR-4, V4 and V27 PASS, V15 REVIEW, V7a-V7c,
V23-V26, RT-I7, RT-I7A, RT-DR, RT-DR3W among them), compared item by item with these expectations.

### 16.5 Synthetic second configuration (test only)

`synthetic-retirement-config` is held as in-memory fixture data under `tools/` and is never
committed as a record. Its adapters (`line-patch/1`, `artifact-hash/1`) are modules under
`adapters/`, pinned by blob in the fixture. It is structurally different from A1:

| Aspect | A1 | Synthetic |
|---|---|---|
| Ledger adapter | `a1exit-exact-edit/2` (byte spans, hashes) | `line-patch/1`: edits `{id, file, old_line_sha256, new_lines}`, located by unique whole-line hash |
| Site map | frozen sitemap | none: sites are declared in the configuration as `{site_id, file, line_sha256, carried}` |
| Replay | yes | none; op `record` unsupported |
| Profiles | Phase-0 and the plan's regexes | one review profile `axiom-Z` (`\bAxiom Z\b`), one deny profile `Z-premise` (`\bAxiom Z\b[^.]{0,40}\b(holds|assumed)\b`) |
| HP | one obligation, six merges | one obligation, one synthetic merge |
| Delegation | six classes | one class `artifact-hash/1`: a declared file must hash to a value computed by a declared deterministic recipe |
| Context field | `s3` | `kind`, with values `{definition: true, remark: false}` |
| Indicators | ANAPH, LIST, TABLE, PARTIAL | one: LIST |

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
| Y9 | a list-item site whose lead-in changed | REVIEW_REQUIRED `context-structure-changed` |
| Y10 | the `line-patch/1` module edited by one byte, configuration unchanged | ERROR `SOURCE_CHANGED` |

### 16.6 Fail-closed configuration validation

Validation runs in the integrity stage (sec. 2.1), before any subject is evaluated. No
configuration defect can lead to PASS.

| Defect | Outcome | Exit | Class |
|---|---|---|---|
| unknown `schema`, or unknown or mismatched adapter interface, name or version | ERROR | 65 | `CONFIG_INVALID` |
| missing required field, or unknown field | ERROR | 65 | `CONFIG_INVALID` |
| operation not in `operations` | ERROR | 65 | `CONFIG_UNSUPPORTED` |
| missing or failing review chain (sec. 6.3); reviewer equal to author; widening without review | ERROR | 65 | `CONFIG_UNREVIEWED` |
| hash or pin mismatch of the configuration, an adapter module or any referenced blob | ERROR | 65 | `SOURCE_CHANGED` |
| inconsistency: base differs from the ledger, merge off the chain, context value missing, extractor hash mismatch, duplicate profile, a `final_profiles` entry that is not a review profile | ERROR | 65 | `CONFIG_INCONSISTENT` |
| configuration controls file absent or empty for an operation | VOID | 70 | `CONFIG_NO_CONTROLS` |

Controls Z1-Z8 each give one of these defects in the synthetic configuration and expect the stated
class. Z9 is the purity lint of sec. 16.1, with its controls Z9a-Z9g.

Z10 (V5): the synthetic configuration superseded by a version that adds a merge to its HP
obligation, with no `widening_review`, so that a step now FAIL `provenance-foreign` would become
adjudicable: ERROR `CONFIG_UNREVIEWED`, exit 65, and the step is not admitted. With a valid
widening review and a matching adjudication, the same step is `provenance-adjudicated`.

### 16.7 Reproducibility

Every `result.json` records:

- `config`: `{config_id, version, path, commit, blob_sha256}`;
- each adapter's interface, name, version, module blob hash and input blob hashes;
- each profile's name, source commit, path, blob and `pattern_sha256`;
- every rule file's path and blob, and the id of every rule applied (in each explanation);
- every record, review record and authorization record used, by path and blob;
- the delegation record hash and each class adapter version;
- the HP obligation's pinned merges;
- the engine blob hash (the entry point and every engine module).

Two runs with equal inputs produce byte-identical output (sec. 5). That is checked in CI by running
twice and comparing.

### 16.8 Implementation step

| Step | Work | Acceptance |
|---|---|---|
| S13 | Configuration loader and validator, adapter admission by blob, the A1 configuration, the synthetic configuration | Z1-Z8, Z9a-Z9g, Z10 and Y1-Y10 behave; every A1 control has the same outcome as specified in sec. 10-11 of this document; no engine source contains an A1 constant (Z9) |
