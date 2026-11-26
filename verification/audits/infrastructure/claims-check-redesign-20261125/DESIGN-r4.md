# Withdrawn-claim checker: redesign, revision r4 (Issue #1565)

Paper-only. This note is a delta to `DESIGN-r3.md`, which stays in force except where this note
changes it. Nothing here modifies `tools/claims_check.py` or any other repository file. The r3
files, and every earlier file in this directory, are unchanged. `CHANGES-r4.md` maps each change to
the r3 review (PR #1567 comment 7170477503) and to the owner's decision.

**Goal link.** Verification integrity (Issue #1565). This revision decides whether the four
corrections that the r3 review required close the record holes it found, without adding detection
vocabulary, and what they cost in review load. It decides no manuscript claim and licenses no
hypothesis.

**Authority.** Owner decision (`amaybaum`, 2026-11-25T18:50:53Z; #1169 comment 7171541574),
verbatim: "Authorize all four proposed corrections and the documentation changes." "Do not expand
the vocabulary beyond the stated corrections. Explicitly acknowledge that independent scientific
review remains responsible for detecting reworded claims outside the checker's defined patterns."
"Complete one focused independent review before presenting the design for adoption."

***

## 0. What the checker does, and what it does not

**The checker flags defined patterns and enforces the structure of review records. Independent
scientific review is responsible for detecting reworded claims outside those patterns.**

- *Flags defined patterns.* A sentence is flagged only when the terms of a rule's frozen argument
  and cue sets co-occur in it (or in its anaphora window), when a strong cue or literal formula
  occurs, or when a bare canonical template matches (`DESIGN-r3.md` §3.3–3.4).
- *Enforces record structure.* A flagged sentence is cleared only by a review record that is bound
  to the exact sentence, rule, code and a commit on the main ref, and that stays within the
  mechanical bounds of `DESIGN-r3.md` §3.6 as amended in §1 below.
- *Does not detect rewording.* A claim restated in words outside the frozen sets is not flagged.
  On the r3 reviewer's batch W, 16 of 30 must-not-pass items still pass under r4 (§3). No lexical
  scanner closes this class, and r4 does not try to: the owner's decision rules out expanding the
  vocabulary beyond the stated corrections. Ordinary independent scientific review of manuscript
  changes carries it.
- *Does not judge records.* The bounds limit what a record can claim; they do not make its claim
  true. A reviewer who misreads a sentence can still write a record within the bounds (§5).

***

## 1. Changes

Each change is one of the four authorized corrections, the `--main` default (review nit 7), or
documentation. Nothing else changed in `work/proto.r4.py` (`diff work/proto.r3.py work/proto.r4.py`).

1. **Hypothesis token refuses `unrelated` (review finding 2).** An `unrelated` record is refused
   (exit 3) when the sentence contains a hypothesis token, `H-` followed by a letter or digit
   (H-slope, H-Hawking, H-χ, …). Such a sentence is cleared only by a `governed` record citing an
   owner-adopted licence (`DESIGN-r3.md` §3.6 R4; the deployed list is empty), or by rewording. The
   check reads the flagged sentence, as the correction states. It does not read a code-A finding's
   anaphora window (§5).
2. **The record's evidence carries the rule's own match (review finding 2).** For the `mention`,
   `supposition` and `question` bases, the quoted evidence, supposition clause or question must
   contain the match that raised the finding, in addition to the r3 checks:
   - code C: every argument set and every cue set of the rule;
   - code A: every cue set, the argument sets present in the sentence, and the anaphor that stands
     for the missing argument (the missing argument is in the window, by definition of code A);
   - code P: the strong-cue match.
   The `negated` and `other-subject` checks are unchanged.
3. **Unique rule identifiers (review finding 3).** The second rule that r3 also called `W-KDEG`
   (subject "the framework's answer", object `K =`, `2d`, `six`) is renamed **`W-KDEG-ANSWER`**.
   `W-KDEG` keeps its meaning: coupling-degree minimization fixing `K`. The new rule carries
   `family: W-KDEG`, so the controls, which name `W-KDEG`, test both rules as before; it shares
   r3's W-KDEG bare templates, so no verdict changes. Record checks now look up the rule that raised
   the finding. A record for a `W-KDEG-ANSWER` finding must name `W-KDEG-ANSWER`. The prototype
   asserts that rule identifiers are unique. No identifier is reused (§A.30).
4. **Word lists brought into line with `DESIGN-r3.md` §3.2 (review finding 4).** No new term was
   added. Two kinds of edit:
   - *inflections:* `coupling` → `couplings?`; `horizon` → `horizons?` (in "temperature of the
     horizon"); `thermal ratio/spectrum/character` → plural forms; `quantum formalism, structure,
     rule, description, behaviour` → plural forms; `quadratic symbol`, `propagation geometry`,
     `projected memory` → plural forms; `single value` → `single values?`; `condition for` →
     `conditions? for`; `lead… to` → also `led to`;
   - *bare generic heads:* `symmetr…` and `substratum` removed from the `W-BM-EUCLID` argument set
     and replaced by the multi-word phrase that already occurs in the rule's own bare template,
     `substratum symmetry` ("cubic symmetry" is covered by `cubic`); bare `horizon` removed from the
     `W-GR-THERM-KIN` argument set, whose horizon temperatures and thermality terms remain.
   The bare-head sweep covered only these three terms, the ones the r3 review named. `cubic`,
   `hidden`, `minim…` and `ignorance` remain single-word terms; keeping them costs review load,
   not silent passes.
5. **`--main` defaults to `origin/main`, not `HEAD` (review nit 7).** The gate passes the main ref
   explicitly after fetching it with full history. If the ref is absent, every record is refused
   (exit 3).

The argument-only widening that the review offered under finding 1, and the `isotropic`, `quadratic`
and `metric` additions to `W-BM-EUCLID`, are not adopted: both add vocabulary. The LaTeX
normalization of `W-GR-EPSKAPPA` (nit 9) is not adopted either, because it is not among the
authorized corrections.

***

## 2. Acceptance rule, as amended

`DESIGN-r3.md` §5 stands, with these amendments.

- **Criterion 2, M1: dropped.** M1 kept only the deletion mutants that still satisfy the detection
  condition C1 and then checked that they were flagged. That holds by construction, so the control
  cannot fail and proves nothing (review finding 5). **M2 is restated as a segmentation check.**
  Inserting a marker cannot remove a co-occurrence from a unit, so M2 can fail only if an insertion
  changes sentence segmentation. It is reported, not counted as independent evidence.
- **Criterion 3, injection: restated.** An appended sentence normally forms its own unit, so the
  injection result mostly re-tests the sentence-local controls. Its zero for the earlier controls
  follows almost entirely from their standalone verdicts. It is reported as a check on segmentation
  and on the anaphora window, not as independent evidence.
- **Criterion 5** now includes the review's record-loophole probes, each of which must give exit 3.
- **Criterion 6.** Batch W was written by the r3 reviewer against r3. Its results were known before
  r4 was written, so it is not held out for r4. The owner's decision requires one focused
  independent review before the design is presented for adoption.

The lexicon criterion of `DESIGN-r3.md` §3.2 was fixed after r3's first measurement, as r3 states;
the 1,427 → 248 narrowing was a dial chosen after measurement (review nit 6). The r4 edits of §1
item 4 were made by applying that criterion before the first r4 run, but r4 is a single local
revision and that order cannot be checked from the files.

***

## 3. Measurements (`work/proto.r4.py`, harness `work/run_r4.py`; outputs in `results-r4/`)

Silent PASS of must-not-pass items, r3 → r4. It does not increase on any batch.

| Batch | r3 | r4 | Other outcomes, r4 |
|---|---|---|---|
| All 195 preserved controls (7 files) | 0 MISS, 0 FPFAIL | 0 MISS, 0 FPFAIL | identical to r3: 67 exact, 54 blocked, 74 load |
| r1 and Y-review probes (48) | 0 | 0 | identical to r3 |
| Batch W (SHA-256 `6317946b…76d6b9a9`, verified), per-rule | 17 / 30 | **16 / 30** | 0 FPFAIL; W-P-09 ("couplings") PASS → REVIEW |
| Batch W, any rule firing | 16 / 30 | **15 / 30** | — |
| Batch W, out-of-vocabulary items W-P-01..20, per-rule | 16 / 20 | 15 / 20 | — |
| Author diagnostics D-01..D-12 (not controls) | 7 / 12 | 7 / 12 | — |
| Record and exit-code controls | 41 / 41 r3 controls hold | **73 / 73 hold** | see below |
| M2 (segmentation check) | 14,080, 0 PASS | 14,080, 0 PASS | 2,048 FAIL, 12,032 REVIEW |
| Injection, earlier 162 sentences × 6,883 paragraphs | 0 PASS | 0 PASS | — |
| Injection, batch W's 30 must-not-pass × 6,883 | 116,494 PASS | 109,679 PASS | see note |

The exact SHA-256 of batch W is `6317946b6fae4d58c2c78be5e718b06fd002c1edc6d37280f6821c9876d6b9a9`.

**Record and exit-code controls (73), `results-r4/exitcodes.txt`.**

- The 41 r3 controls hold, with one expectation reversed by correction 2. A `question` record whose
  evidence is "Is the Hawking temperature" (no cue) gave 0 under r3 and gives 3 under r4. A new
  control with the full question as evidence gives 0.
- **The review's record-loophole probes (9), each exit 3 under r4.** The `mention`, `supposition`
  and rhetorical-`question` records on H-slope sentences, and the `W-KDEG` `other-subject` record
  citing "Coupling-degree minimization", gave exit 0 under r3 and give 3 under r4. Correction 1
  refuses the first three, because their sentences contain H-slope; correction 3 refuses the
  fourth. Correction 2 is not what refuses them (§5). The other five
  probes (`governed` with `licence: ""` and with no licence; record for another path; revision on a
  research branch; bogus `--repo`) were already 3.
- **Correction 1 (7).** A clean `negated` record and an H-χ `other-subject` record on H-token
  sentences are refused, and a `governed` record with a valid synthetic licence still clears an
  H-token sentence. Correction 1 is checked first, so it would mask the r3 checks that the r3
  controls exercised on H-token sentences. Four controls re-exercise those checks on sentences
  without an H-token (qualifier as evidence, own subject as `other-subject`, `mention` outside
  quotation, concessive `negated`), so none of them becomes vacuous.
- **Correction 2 (10).** For each of `mention`, `supposition` and `question`, and for codes C, A and
  P, one record whose evidence lacks the rule's match is refused and one that carries it is
  accepted.
- **Correction 3 (3).** A record naming `W-KDEG` for a `W-KDEG-ANSWER` finding is stale (3). The
  same record naming `W-KDEG-ANSWER` clears it (0). An `other-subject` record citing "the
  framework's answer" is refused.
- **`--main` (2).** With no `--main`, a record at a revision on main is accepted, and one at a
  research-branch revision is refused. Under r3's `HEAD` default, the first case depended on the
  local checkout's branch: it gave 3 in the measuring clone, whose `main` is behind `origin/main`.
- **Documented residual (1)**, §5.

**Injection note.** For the earlier 162 sentences both revisions give 0 PASS, as their standalone
verdicts imply. For batch W, r4 removes all 6,846 PASS of W-P-09. Three items gain a few PASS:
W-P-04 (+14), W-P-07 (+9) and W-P-08 (+9); W-P-10 loses one. In each of those paragraphs the injected sentence passes
under both revisions. Under r3 the paragraph's verdict came from one of the host paragraph's own
sentences, flagged through a bare head (`horizon`, `symmetr…`) that correction 4 removes. None of the three sentences contains its rule's cue (`kinematic`, `Euclid…`), so it cannot be a
candidate under either revision. These are host-paragraph findings of the kind listed in §4. They are not detections of the injected sentence.

***

## 4. Review load (tree M = `main` at `4c3ad0796b578c6258d5aae58c9502d5155d74dc`, 1,133 `.md` files)

| | r3 | r4 |
|---|---|---|
| Exit | 2 | 2 |
| Active FAIL | 0 | 0 |
| Active REVIEW findings (records needed) | 256 | **234** |
| … by code C / A / P | 172 / 76 / 8 | 158 / 68 / 8 |
| … distinct (path, sentence) | 219 | 198 |
| … distinct sentence texts | 160 | 145 |
| Files | 23 | 22 |
| Record-file REVIEW (exit unaffected) | 921 | 876 |

r3's 248 in `DESIGN-r3.md` was measured at `e2e2a623`. At the current main, r3 gives 256.

- **What changed.** 23 active findings fall away: 9 `W-BM-EUCLID` and 14 `W-GR-THERM-KIN`, all
  raised by a bare head ("Euclidean KMS periodicity", "finite-horizon", "background kinematics",
  "Euclidean action functional"). The `W-GR-THERM-KIN` count drops from 16 to 2, and `W-BM-EUCLID`
  from 14 to 5. One finding is added: `W-KDEG` at `papers/SM.md:527`, which co-occurs through
  "couplings". The `W-BM-EUCLID` candidate manuscript finding at `book/ch05-gauge-structure.md:13`
  and `book/The-Incompleteness-of-Observation-FULL.md:1328` is still flagged (C).
- **What correction 1 costs.** 36 of the 234 active findings (34 distinct path and sentence pairs,
  23 distinct texts) are sentences that contain a hypothesis token: H-slope, H-count, H-link, H-BD,
  H-Hawking, H-spectrum, H-χ, H-cust, H-BG, H-state. With the deployed licence list empty, none of
  them can be cleared by a record. Each must be reworded, or a licence must be adopted for it under
  the procedure of `DESIGN-r2.md` §3.6 (`results-r4/treeM-hypothesis-token.txt`).
  The gate cannot be green at main until those 36 are resolved and records exist for the other 198.

***

## 5. Residuals, and guidance for reviewers who write records

- **Rewording outside the defined patterns** (§0): carried by independent scientific review.
- **Correction 2 checks evidence that the record writer chooses.** It requires the quoted evidence,
  supposition clause or question to contain some match of each required set. It does not require
  the evidence to be the qualifying phrase alone, or to cover every occurrence of the match in the
  sentence, so a writer can meet it by choosing a wider span. On a sentence without a hypothesis
  token, a `supposition` record whose evidence is "The Hawking temperature $T_Q$ is
  state-independent, as one would" (for "…, as one would expect."), a `mention` record on a
  quotation of the claim that the sentence also asserts outside the quotation, and a `question`
  record on a rhetorical "Why else would … be state-independent?" with the full clause as evidence
  are all accepted (exit 0; r4 review finding 1). The review's three record probes on H-slope sentences give exit 3
  because correction 1 refuses them, not because of correction 2. On sentences without a hypothesis
  token, whether a misleading-qualifier record (for example one citing "as one would expect") is
  correct remains the reviewer's judgment.
- **Hypothesis token outside the flagged sentence.** Correction 1 reads the flagged sentence only.
  - *Code A.* The hypothesis may sit in the preceding sentence, as in "Under H-slope, the
    calibration fixes $T_Q$ on the de Sitter horizon. It is state-independent." An
    `other-subject` record on the second sentence is accepted (exit 0, the documented-residual
    control).
  - *Code C.* The same holds for a code-C finding whose hypothesis is in a preceding sentence:
    "Assume H-slope. Then the Hawking temperature $T_Q$ is state-independent in this regime.", with
    an `other-subject` record whose evidence is "Then", is accepted (exit 0; r4 review finding 3). A hypothesis assumed
    for a whole paragraph or section is likewise not seen.
  - *Size at tree M.* No code-A finding has a hypothesis token in its window. One code-C finding
    has one in the preceding sentence: `papers/Substratum.md`, `W-KDEG`, "Coupling-degree
    minimization leaves the single-copy clause open".
  - Each case needs a false record, so it also lies within reviewer misjudgment. Extending
    correction 1 to the code-A anaphora window would close only the anaphora part, not the code-C
    case or a paragraph- or section-level hypothesis. No extension is among the authorized
    corrections, so it is put to the owner.
- **Typographic variants of the hypothesis token.** Correction 1 matches `H-` followed by a word
  character, at a word boundary, case-insensitively; lower case, digits and H-χ are caught. These
  forms are not caught: Markdown underscore italics (`_H-slope_`, where no word boundary precedes
  `H`), a non-ASCII hyphen (U+2011 non-breaking hyphen, or an en dash), `$H$-slope`, and a
  zero-width space after the hyphen (r4 review finding 2). None of these forms occurs in active material at tree M. The
  pattern is not changed in r4.
- **`negated` that asserts invariance (review nit 8).** The `negated` basis accepts "The Hawking
  temperature does not vary from one state to another", which asserts the withdrawn invariance
  through a negated predicate. A reviewer must not record a negated predicate as `negated` when the
  negation itself expresses invariance, independence or universality ("does not vary", "does not
  change", "does not depend"). Such a sentence is reworded, not recorded.
- **Reviewer misjudgment within the bounds.** Unchanged from `DESIGN-r3.md` §3.6: governed by the
  reviewer's independence, the owner authority each record cites, and staleness on any edit.

***

## 6. Reproduction

From this directory, with a full clone of the repository as `<git dir>` and tree M a checkout of
`4c3ad0796b578c6258d5aae58c9502d5155d74dc` with every file (a `git archive` export omits the
`export-ignore` paths of `.gitattributes`):

- `python3 work/proto.r4.py --self-test` (`results-r4/self-test.txt`)
- `python3 work/proto.r4.py --controls work/reviewer-heldout-W.json` (`results-r4/controls-W.txt`)
- `python3 work/run_r4.py compare` (`results-r4/compare.txt`)
- `python3 work/run_r4.py exitcodes <git dir> 4c3ad0796b578c6258d5aae58c9502d5155d74dc`
  (`results-r4/exitcodes.txt`; the `--main` controls need `origin/main` in `<git dir>` to contain
  `e2e2a623`)
- `python3 work/run_r4.py m2 <tools/claims_check.py at e2e2a623>` (`results-r4/m2.txt`)
- `python3 work/run_r4.py inject <tree M> r4` and `… r3` (`results-r4/injection-r4.txt`,
  `results-r4/injection-r3.txt`)
- `python3 work/run_r4.py scan <tree M> <out dir>` (`results-r4/treeM-scan.txt`,
  `results-r4/treeM-scan-summary-r4.json`)

***

## 7. Next step

One focused independent review of r4, as the owner's decision requires, before the design is
presented for adoption. Questions for the owner, after that review:

1. Extend correction 1 to the anaphora window of code-A findings (§5)? That would close only the
   anaphora part of the residual; code-C findings with a hypothesis in a preceding sentence remain.
2. The 36 H-token findings at main: reword, or propose licences?
3. `DESIGN-r3.md` §9 questions 1–5 stand. The landing cost is now 234 records, of which 36 can be
   cleared only by rewording or an adopted licence.
