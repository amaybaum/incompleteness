# Withdrawn-claim checker: redesign, revision r3 (Issue #1565)

Paper-only design for independent review and the owner's adoption decision. Nothing here modifies
`tools/claims_check.py` or any other repository file. Base: `main` at
`e2e2a623265187a28ebec604ab8bcc672742888f`. This revision follows `DESIGN-r2.md` of PR #1567 at
`23395aecbe2514c170705b6d85695847c4c67b72`. `CHANGES-r3.md` maps the delta review's findings F1–F7,
the owner's r3 items, and every removed or kept mechanism to this text.

**Goal link.** Verification integrity (Issue #1565). This revision decides which of two architectures
the release gate's withdrawn-claim step should be specified in: r2's automated governance, or
conservative detection followed by revision-bound independent review. It also measures what the
choice costs in review load. It decides no manuscript claim and licenses no hypothesis.

**Authority.** Owner decision (`amaybaum`, 2026-11-25) authorizing a bounded r3 addressing F1–F3,
verbatim excerpts: "Ambiguous claims should require review rather than silently pass." "Licensing
must be enforced mechanically, including when processing human review records." "Negated hypotheses
and misleading qualifying phrases must not license withdrawn claims." "Preserve all previous
independent controls." "If r3 still exhibits substantial silent misses, reassess the architecture
before authorizing another incremental correction round. Do not indefinitely accumulate special-case
patterns." The owner's simplification direction (same date): "Scan for potentially prohibited claims
(simple, conservative detection) → no concern: pass; potential concern: require review → independent
review: accept or reject, tied to the exact text and revision." "The checker should not attempt to
determine whether H-balance, H-slope or another scientific hypothesis logically licenses a claim.
That is a scientific judgment, not a string-matching problem." "Before adding any new mechanism,
establish: 1. What concrete failure it prevents. 2. Why an existing mechanism cannot prevent that
failure. 3. Whether a simpler solution provides equivalent protection." Owner note
(2026-11-25T16:29:44Z), as relayed by the coordinating session: "converge; do not add mechanisms
where existing ones suffice."

***

## 0. Verdict of this revision

**The simpler architecture gives stronger protection against silent misses, at a much higher review
cost. This revision adopts it.**

- **Silent misses.** On every preserved control and every diagnostic probe of the earlier reviews,
  r3 has no silent miss: no positive or ambiguous control passes, and no control expected PASS or
  REVIEW gets an unresolvable FAIL. r2 has 9 silent misses on batch Y under the deployed empty
  licence file (11 under its fixture), 3 on the Y-review's post-hoc probes (10 under the fixture),
  and two false-positive FAILs.
- **Corpus injection.** 162 sentences (every control and probe expected FAIL or REVIEW) were each
  appended to all 6,883 manuscript paragraphs. r3 passes none of the 1,115,046 results. r2, under
  the deployed licence file, passes 82,572 of them.
- **Review load.** At tree M, r3 gives 248 active-material REVIEW findings, all of which block the
  gate until review records exist. They fall on 211 distinct sentences, or 155 distinct sentence
  texts once mirrors are merged. r2 gave 3. On the control suite, r3 sends 74 of the 76 negative
  controls to REVIEW. r2 automated most of these as PASS.
- **Residual.** Detection is lexical. A paraphrase whose subject or relation word lies outside the
  frozen sets passes silently. Seven of the author's twelve post-hoc diagnostic sentences, written to
  probe exactly that class, pass (§6.6). No pattern scanner closes this class. It is bounded only by
  the lexicons and by ordinary independent review of manuscript changes.

Batch Y is **not** held out for r3: the author read the Y review's table before writing r3. No r3
number in this document is a held-out measurement. Acceptance criterion 6 (§5) needs a further
independent batch from the next reviewer.

***

## 1. Why the architecture changes

r1 and r2 tried to decide automatically when a withdrawn claim is *governed*. They tried to show that
a qualifier, a negation or a frame takes logical scope over the assertion, and to PASS the sentence
when it did. Each round's independent held-out batch found silent misses in that decision:

| Round | Held-out batch | Silent misses at first run (deployed licences) |
|---|---|---|
| r1 | X (34) | 3 positives PASS among 16 (X-P-07, -10, -13; 24 / 34 exact) |
| r2 | Y (43) | 9 positives PASS among 22 |

The Y misses fall into two kinds. Two are failures of the governance decision. In "Under H-balance
violations, …" and "Under H-spectrum or H-slope, …", a licensed token in head position was taken as
logical qualification; these pass under the fixture (F1). The other nine are vocabulary or direction
failures, such as reversed roles, negated idioms and ellipsis, on which r2's negation and frame rules
decided PASS (F3). Both kinds come from the same design choice: **a sentence that uses the rule's
vocabulary can PASS automatically when a governance rule says it is governed.** Each repair added
patterns, and each new batch found the next gap. This is the accumulation the owner rules out.

r3 removes the choice. A sentence that uses a rule's vocabulary never passes automatically. The
scientific question, whether the sentence asserts the withdrawn claim or asserts it only under an
established condition, goes to an independent reviewer. The reviewer's record binds to the exact
sentence and revision. The mechanism checks what a record may decide, but it does not make the
decision.

***

## 2. Rule inventory

The same twelve rule identifiers as r2 (stable, §A.30): `W-GR-TQ-STATE`, `W-GR-THERM-KIN`,
`W-GR-KMS`, `W-GR-CONE`, `W-GR-EPSKAPPA`, `W-BM-EUCLID`, `W-KDEG`, `W-OI-REQ`, `W-OI-HIDDEN`,
`W-OI-NOEXIST`, `W-OI-EXPLAINS`, `W-OI-CONTRA`. The withdrawn claims and their anchors are as in
`DESIGN.md` §2. No rule carries a licensed qualifier, a governing position, a frame lexicon or a
non-governing list.

***

## 3. Mechanism

### 3.1 Units

Sentences are segmented as in r2 (§3.2 of `DESIGN-r2.md`), with two changes. A table row is one
unit, because cells are no longer split. A `§` or `#` after a full stop starts a new sentence. There
is no clause segmentation, because nothing in r3 depends on clause structure.

### 3.2 Frozen lexicons, and the criterion that fixes them

Each rule carries:

- **argument sets** (one set for a property claim; two, both required, for a relational claim such
  as QM–OI). These hold the anchor's subject (and object) terms, their r2 equivalence variants, and
  the multi-word head nouns of r2's near-miss subject sets.
- **cue sets.** These hold the anchor predicate's stems, the object noun of an invariance claim
  (`state`, `vacuum`), and one closed **relation family** for the claim's type:
  - *invariance:* `universal`, `invariant`, `single value`, `one value`, `unique`, `regardless`,
    `irrespective`, `whatever`, `blind`, `agnostic`;
  - *necessity:* `requir…`, `need…`, `presuppos…`, `prerequisite`, `precondition`, `necess…`,
    `depend…`, `rests on`, `relies on`, `(im)possible`, `without`, `demand…`, `entail…`, `imply`,
    `condition for`, `ground…`, `calls for`, `mandat…`, `compel…`, `indispensab…`, `essential`,
    `exist…`, `do without`, `basis`, `presence`, `absence`;
  - *causation:* `explain…`, `explanat…`, `caus…`, `produc…`, `generat…`, `give/gave rise`,
    `account for`, `underl…`, `origin…`, `source`, `yield…`, `deriv…`, `consequen…`,
    `result from/of`, `emerg…`, `follows from`, `leads to`, `due to`, `responsib…`;
  - *selection* (`W-KDEG`): the object `K`, `2d`, `six`, `m = 1`, `single-copy`, `site(s)`,
    `carrier`, and the r2 fixing verbs.
- **a strong cue** (the code-P set; see §3.3 C3). This is the predicate phrase that the existing
  checker's own pattern named for the rule: "state-independent / independent of the state / does
  not depend on the state", "purely (entirely, …) kinematic", "is KMS / periodic in imaginary
  time", "exact per channel", "Euclidean (quadratic) symbol/metric", "cannot exist without".

**Criterion, fixed for every later extension.** An argument term enters a set only if it is the
anchor's subject or object, an inflection of either, or a multi-word noun phrase that denotes the
same referent. A bare generic head such as "temperature", "quantum" or "symmetry" alone does not
enter. A cue enters only as a stem of the anchor predicate, the object noun of an invariance claim, a
member of the claim type's relation family, or the existing checker's predicate phrase. An extension
is a rule-data change, made through the remedy of §3.9, and never through a review record. The sets
are recorded in `work/proto.r3.py` (`RULES`).

**How the sets were reached, stated plainly.** The first r3 run used wider sets: the bare head
"temperature", bare "quantum", sameness verbs such as `vary`, `change`, `same`, `depend`,
function-word causation cues (`from`, `because`, `follows`), and an anaphora window of the whole
previous paragraph. It gave 1,427 active REVIEW findings (1,058 distinct sentences) at tree M. The
sets were then narrowed to the criterion above, in order to reduce review load, and at each step
every control file and probe was re-run. The narrowing gives up recall: two of the author's
diagnostic sentences (D-01 "never varies", D-02 "the temperature … is the same") would have been
flagged by the first sets. The owner may move this dial. §6.5 gives the cost at each end.

### 3.3 Detection

For each rule and each sentence unit:

- **C1, co-occurrence (code C).** Every argument set and every cue set has a match in the unit, in
  any order, whether negated or not.
- **C2, anaphora (code A).** Every cue set matches. Some argument is missing. The unit contains an
  anaphor (`it`, `this`, `these`, `they`, `such`, `the latter`, `the former`, or a definite
  description such as "this temperature", "the minimization" or "the theory"). The missing arguments
  occur in the immediately preceding unit, which is the last unit of the previous paragraph for a
  paragraph's first sentence.
- **C3, strong cue (code P).** The rule's strong cue matches, whatever the subject.
- **Literal (code L).** The formula of control EX-4 (`work/design-example-sentences.json`), without the square (`W-GR-EPSKAPPA`).

A unit with none of these is **PASS** and has no finding. No other route leads to PASS.

### 3.4 Outcome

- **FAIL (code B).** A C1 candidate whose unit contains a *bare template*: the plain canonical
  assertion with tight binding, such as "The Hawking temperature $T_Q$ is state-independent",
  "Coupling-degree minimization fixes $K = 6$" or "Quantum mechanics requires observational
  incompleteness". In addition, the rest of the unit must contain no token of the *risk lexicon*:
  negation words; qualifier tokens (`H-…`, `if`, `unless`, `under`, `given`, `assum…`, `when…`,
  `only`, `conditional…`, `sense`, `reading`, `branch`, …); frame, attitude and modal words (`that`,
  `whether`, `claim…`, `suppos…`, `might`, `would`, `argu…`, …); concessive or contrastive words;
  question marks; quotation marks.
- **FAIL (code L).** Every literal-formula match.
- **REVIEW.** Every other candidate (codes C, A, P).

FAIL marks the plain canonical assertion. It exists so that no record can wave such a sentence
through (§3.6 R2). The risk lexicon only *lowers* FAIL to REVIEW. It never produces PASS, so a gap
in it costs a review, never a silent pass.

**No safe-PASS form is adopted.** The owner's direction allows a small set of exactly specified,
mechanically safe PASS forms, such as explicit negation in the assertion slot. Measured: among the
266 active findings of the intermediate lexicon, a negated bare template matched anywhere in only 6
sentences. A form strict enough to be safe (single negation, nothing else in the unit, no anaphor,
no second cue, which excludes the ellipsis "X does not Y; X does.") would cover fewer. A mechanism
that saves at most 6 reviews and reopens the governance-decision class fails question 3.

### 3.5 What is decided mechanically, and what is not

Mechanical: whether the terms of the frozen sets co-occur in a unit; whether a strong cue or literal
occurs; whether a bare template matches in an otherwise clean unit; whether a review record is bound,
current and within its permitted bounds (§3.6); whether a licence entry is complete and validated
(§3.7).

Not mechanical, and never automated: whether a qualifier, negation, frame, quotation or question
removes the assertion; whether a hypothesis licenses a claim; whether a flagged sentence is about
something else. These are decided by the independent reviewer, in a record.

### 3.6 Review records: what a record may and may not decide

A REVIEW is resolved only by a record in `verification/infrastructure/claims-check/reviews.json`.
Binding is unchanged from r2: `rule`, `path`, `sentence` (verbatim), `sentence_sha256` (which must
equal the hash of `sentence`), `code` (matched exactly against the finding's code; F5), `revision`
(a full 40-hex commit), `reviewer`, `date`, `authority`, `reason`, and `window_sha256` for code A. A
record stays valid at a later commit under r2's rule (§3.7 of `DESIGN-r2.md`). Otherwise it is
stale (exit 3).

**Mechanical bounds, each refused with exit 3:**

- **R1.** Records given without `--repo` (F6). The revision's ancestry cannot be checked, so the
  record is refused, never passed.
- **R2.** A record that matches a FAIL. A record can never convert a detected positive assertion.
- **R3.** `decision` is neither `governed` nor `unrelated`.
- **R4, `governed`.** The record must cite `licence`, the `id` of an entry in the licence file
  (§3.7) for the same rule. Its `evidence` must be a verbatim substring of the sentence that contains
  a match of that entry's qualifier. **The deployed licence list is empty, so every `governed`
  record is refused.** A `governed` decision on H-slope, or on any other hypothesis, fails
  mechanically until the owner adopts a reviewed licence entry for it (F2).
- **R5, `unrelated`.** The record must give a `basis` from a closed list and `evidence`, a verbatim
  substring of the sentence. The evidence must contain **no qualifier token**, so a non-assertion
  cannot rest on a hypothesis or condition (F2, the second back door). Each basis has its own check:
  - `negated`: the evidence contains a negation word and the rule's cue; the sentence contains
    exactly one negation word, so double negation is refused; and the sentence contains no
    concessive or polarity-flipping token (`still`, `even`, `regardless`, `irrespective`,
    `nevertheless`, `whether or not`, `with or without`, `also`, `both`). This refuses "If H-balance
    fails, … still …" (F1, F3);
  - `mention`: the evidence lies inside a quotation or code span of the sentence;
  - `question`: the sentence ends with `?`;
  - `supposition`: the evidence contains a supposition marker (`suppose`, `were`, `would`,
    `hypothetical`, …);
  - `other-subject`: the evidence contains neither an argument term nor a full cue match of the
    rule.

These bounds limit what a record can claim. They do not establish that its claim is true. A reviewer
who misreads a sentence can still write a record that passes the bounds. That residual is governed
by the reviewer's independence, the owner authority each record cites, and staleness on any edit,
not by pattern matching.

### 3.7 Licences

The licence list exists only for R4. No automated verdict reads it. Schema `claims-licences/3`.
Each entry carries:

- `id`;
- `rule`;
- `qualifier` (a regular expression);
- `proposer`, which must be present;
- `anchor` {`path`, full `revision`, verbatim `quote`};
- `review` {`reviewer` ≠ `proposer`, `record` (a path that must exist on the main ref), `date`, full
  `revision`};
- `adoption` {`author`, `time`, `quote`}, the owner's admission quoted with author and time
  (§A.42 item 7).

With `--repo`, the checker verifies anchor and review ancestry, the quotation at its revision, and
the review record's existence. Without `--repo`, a non-empty list is refused (exit 3). The deployed
list is `{"schema": "claims-licences/3", "entries": []}`, and the self-test fails (exit 3) if it is
not empty. The licensing procedure of `DESIGN-r2.md` §3.6 (proposal, independent scientific
review, owner admission; H-slope not eligible for `W-GR-TQ-STATE`) is unchanged. It is a scientific
procedure, and the checker only verifies that its record is complete.

### 3.8 Output, exit status and scope

These are unchanged from r2. Exit 0 means clean. Exit 1 means a FAIL in active material. Exit 2
means an unresolved REVIEW in active material and no FAIL. Exit 3 means an invalid or stale licence
or review record, an unreadable record file, or records or licences given without `--repo`. Exit 4
means a self-test failure, a usage error or an internal error. Precedence is 4 > 3 > 1 > 2. An
uncaught exception maps to 4. Active material is defined mechanically as in r2 §3.9. The JSON finding
carries `code` as its own field (F5); its schema is `claims-findings/3`. The gate invokes the scan
with `--repo` and full history (F6).

### 3.9 Remedies

A false-positive **FAIL** is a rule-data defect. The remedy, the control and the review are as in
r2 §3.13. None occurred on any control or at tree M. A false-positive **REVIEW** is the designed
cost and is resolved by a record. A **silent miss** is a lexicon defect. The term is added under the
criterion of §3.2, with a control, through independent review and owner approval. It is never added
because a reviewer found it convenient.

***

## 4. Control suite

| Batch | Author / provenance | Controls (pos / neg / amb) |
|---|---|---|
| 1, H, C, D | PR #1567 author ("original 92") | 92 (35 / 42 / 15) |
| X | independent reviewer of r1 (SHA-256 `c4591b6d…24e3`) | 34 (16 / 11 / 7) |
| R2 | r2 author | 26 (7 / 7 / 12) |
| Y | independent reviewer of r2 (SHA-256 `ce31e49c69b188c6ccfa4eaac6a8ed431f234f51261114af5878972d79dd5c3d`) | 43 (22 / 16 / 5) |

Batch Y is preserved byte-identical as `work/reviewer-heldout-Y.json`. Its hash was verified against
the one the review published. Batch X is unchanged in `work/reviewer-heldout.json`. The Y review's
post-hoc probes (Z-01..Z-10) and M1 diagnostics are preserved byte-identical under
`work/reviewer-probes-Y/`, and r1's under `work/reviewer-probes/`. No control was edited. The author's
diagnostic sentences `work/r3-author-diagnostics.json` (D-01..D-12) were written after r3's design
to characterize the residual class. They are not acceptance controls.

**Outcome classes under r3** (`proto.r3.py outcome`):

| Class | Meaning |
|---|---|
| exact | the verdict the control expects |
| blocked | positive → REVIEW: safe, blocks the gate |
| load | negative → REVIEW: a review record is needed |
| **MISS** | positive or ambiguous → PASS |
| **FPFAIL** | negative or ambiguous → FAIL: no record can resolve it |

***

## 5. Acceptance rule

Stated before r3's numbers were taken, following the owner's direction: silent passes are the
failure, and review is the designed outcome of doubt.

1. **No MISS and no FPFAIL** on any control file, under the deployed (empty) licence list.
2. M1: no deletion mutant of a negative or ambiguous control, one of whose units still contains
   every argument and cue of its rule, passes. M2: no marker insertion into a positive control
   passes.
3. Corpus injection: no injected positive or ambiguous control or probe passes in any paragraph.
4. Every active-material FAIL at tree M is a real assertion (none expected). Every active-material
   REVIEW is listed, and its count is reported to the owner as the landing cost.
5. Exit-code and record controls hold, including the F2 back doors.
6. **Independent held-out batch.** A new batch of at least 20 controls, by an independent non-author
   reviewer without access to r3's results, meets 1 at first run. It should include out-of-lexicon
   paraphrases, because that is r3's residual class. A failure is repaired in the lexicon under the
   criterion of §3.2 and re-tested on a further batch. All earlier batches stay in the suite.
7. The deployed licence list is empty and validates.

***

## 6. Measurements (prototype `work/proto.r3.py`, harness `work/run_r3.py`)

### 6.1 Controls

| Batch | r3 first complete run | r3 final | r2 final, deployed licences | r2 final, fixture |
|---|---|---|---|---|
| original 92 | 1 MISS (P-KDEG-3) | 0 MISS, 0 FPFAIL (31 exact, 21 blocked, 40 load) | 0 MISS (84 exact, 8 load) | 0 MISS (92 exact) |
| X (34) | 0 MISS | 0 MISS, 0 FPFAIL (15 / 8 / 11) | 0 MISS | 0 MISS |
| R2 (26) | 0 MISS | 0 MISS, 0 FPFAIL (15 / 4 / 7) | 0 MISS | 0 MISS |
| **Y (43)** | **0 MISS, 0 FPFAIL** | 0 MISS, 0 FPFAIL (6 / 21 / 16) | **9 MISS, 2 FPFAIL** | **11 MISS, 2 FPFAIL** |
| All 195 | — | 0 / 0 (67 exact, 54 blocked, 74 load) | 9 / 2 | 11 / 2 |

The figures in brackets are exact / blocked / load. The r2 numbers reproduce the Y review's figures
(19 / 43 and 17 / 43 exact). In this table a negative that r2 sent to REVIEW under the empty file
counts as load, not as a mismatch.

- **The single first-run failure.** P-KDEG-3 (control EX-5) passed. r2's
  literal rule had a subject ("the framework's answer") that the first r3 argument set omitted. This
  was a transcription defect of the inventory, and it was repaired by adding the subject.
- **Batch Y's first run** under r3 had no silent miss. This is not held-out evidence: the author had
  read which Y controls r2 missed.
- **Every r3 Y positive except Y-P-15 is REVIEW, not FAIL.** r3 FAILs only bare canonical forms. All
  16 Y negatives are REVIEW, so each needs a record.

### 6.2 Diagnostic probes (not held out)

| Probe set | r3 | r2, deployed | r2, fixture |
|---|---|---|---|
| r1-review probes (30) | 0 MISS; 23 blocked, 5 load (`probe.json` PASS controls), 2 exact | 0 MISS | 0 MISS |
| Y-review Z-01..Z-10 | 10 blocked, 0 MISS | 3 MISS (Z-08, -09, -10) | 10 MISS |
| Y-review M1 diagnostics (8) | 6 FAIL, 2 REVIEW | 7 FAIL, 1 REVIEW | same |

### 6.3 Records, licences, exit codes

All 41 of 41 controls hold (`run_r3.py exitcodes`, synthetic trees, repository at `e2e2a623`). They
include:

- every r2 case;
- records without `--repo` (3);
- a code mismatch (3; F5);
- **`governed` on H-slope with no licence (3), and citing an absent licence id (3);**
- `unrelated` with the qualifier as evidence (3);
- `other-subject` citing the rule's own subject (3);
- `negated` on "If H-balance fails, … still …" (3);
- double negation as `negated` (3);
- `mention` outside quotes (3);
- valid `negated`, `question` and anaphora records (0);
- a stale anaphora window (3);
- a synthetic valid H-Hawking licence with a `governed` record (0), and that licence used for
  another rule (3);
- licence without proposer, self-reviewed, without quoted adoption, with review record absent on
  main, with quotation absent, without `--repo`, or with the r2 schema (3 each);
- usage error (4).

### 6.4 M1, M2, injection

- **M1.** 2,895 single-word and two-word deletion mutants of the 115 negative and ambiguous controls.
  In 1,558 of them one unit still carries every argument and cue: 1,522 REVIEW, 36 FAIL, **0 PASS**.
- **M2.** The 44 current marker strings inserted into the 80 positive controls in four positions
  (separate sentence, coordinated clause, colon lead-in, `Under X,` lead-in), 14,080 insertions:
  2,048 FAIL, 12,032 REVIEW, **0 PASS**.
- **Injection.** 162 sentences × 6,883 paragraphs = 1,115,046 results:
  - r3: 216,086 FAIL, 898,960 REVIEW, **0 PASS**;
  - r2 (deployed licences): **82,572 PASS**, in Y-P-01, -07, -09, -10, -12, -13, -18, -19, -20 and
    Z-08, -09, -10 (about 6,880 each), and 3–6 paragraphs each for P-CONE-2, P-KDEG-4 and X-P-04.

### 6.5 Tree-M scan (1,133 `.md` files; review load)

| | r3 final | r3 first lexicon | r2 |
|---|---|---|---|
| Active FAIL | 0 | 0 | 0 |
| Active REVIEW findings | **248** | 1,427 | 3 |
| … distinct (path, sentence) | 211 | 1,058 | 3 |
| … distinct sentence texts (mirrors merged) | 155 | — | 2 |
| Files with an active REVIEW | 23 | — | 3 |
| Record REVIEW (exit unaffected) | 921 | 5,675 | 27 |

- **By code:** 172 C and 76 A. Code P adds none in active material, because every strong-cue
  sentence there already co-occurs.
- **By rule:** `W-OI-EXPLAINS` 43, `W-KDEG` 38, `W-OI-REQ` 33, `W-OI-HIDDEN` 33, `W-GR-KMS` 26,
  `W-GR-TQ-STATE` 23, `W-GR-THERM-KIN` 16, `W-OI-NOEXIST` 14, `W-BM-EUCLID` 14, `W-OI-CONTRA` 5,
  `W-GR-CONE` 3.
- **Most findings are correct prose**, such as scope statements, non-claim lists and unrelated uses.
  Each needs one record per rule and path: 248 records before the gate can be green at `main`.
- **Records are per sentence and revision**, so the load recurs only when a flagged sentence or its
  anaphora window is edited.
- **The two r2 REVIEWs** that need an H-Hawking licence (book FULL:5883, appendix B:206) are still
  REVIEW. They can be resolved only by a `governed` record citing an adopted licence. As in r2, the
  gate cannot be green until that licence passes its procedure or the sentences change.

**A detection r2 and the current checker do not make.** `book/ch05-gauge-structure.md:13` and its
mirror `book/The-Incompleteness-of-Observation-FULL.md:1328` read "finite equivariant projection
gives an Euclidean quadratic observer symbol". The `W-BM-EUCLID` anchor `papers/SM.md:264` states
that equivariant finite observation "does not by itself produce a Euclidean metric" because $b_m$
may vanish. r3 flags the sentence (REVIEW, C); r2 does not. Whether it asserts the withdrawn claim is
a scientific judgment for the reviewer and the owner. It is reported here as a candidate manuscript
finding (§A.25), not adjudicated or edited.

### 6.6 Residual class (author diagnostics D-01..D-12, post-hoc)

r3 flags 5 of the 12 diagnostic sentences: D-03, D-07 and D-08 through code P, and D-11 and D-12
through code C. Seven pass:

| Id | Sentence | Why it passes |
|---|---|---|
| D-01 | "$T_Q$ never varies" | no state word |
| D-02 | "the temperature … is the same whatever is prepared" | generic subject |
| D-04 | "The Born-rule theory needs it" | QM not named |
| D-05 | "built on" | outside the necessity family |
| D-06 | "the light cone at free level" | subject outside the set |
| D-09 | "is why" | outside the causation family |
| D-10 | "choosing the fewest couplings" | minimization not named |

r2 passes the same seven, and also D-08 and D-12. r2 flags D-03 and D-07, which r3 flags only
through code P (§7). This class is common to every lexical design. r3 does not claim to close it.

### 6.7 Reproduction

From this directory:

- `python3 work/proto.r3.py --self-test`
- `python3 work/proto.r3.py --controls work/<file>.json`
- `python3 work/run_r3.py compare`
- `python3 work/run_r3.py exitcodes <git dir> e2e2a623265187a28ebec604ab8bcc672742888f`
- `python3 work/run_r3.py m1`
- `python3 work/run_r3.py m2 <tools/claims_check.py at e2e2a623>`
- `python3 work/run_r3.py inject <tree M> [r2]`
- `python3 work/proto.r3.py --scan <tree M> --json <out>`

Tree M is as in r2 §6.6. The outputs are in `results-r3/`; `results/` holds r2's outputs unchanged.

***

## 7. Mechanisms added after the first measurements

**Code P** was added after the author diagnostics showed that narrowing the lexicon (§3.2) let r3
lose two sentences that r2 caught. D-03 is the sentence of control EX-6, with the antecedent two
sentences back. D-07 is "Every field state on this background is KMS."

- **What it prevents:** a regression against r2 on a predicate stated without its subject in reach.
- **Why existing mechanisms do not:** C1 needs the subject in the unit, and C2 needs it in the
  previous unit.
- **Simpler alternative:** widening C2's window to the whole paragraph, the first r3 setting, costs
  about four times the review load.

Code P reuses the existing checker's own predicate patterns, which r2 also kept as a subject-free
trigger (its R2 code). At tree M it adds no active REVIEW. No other mechanism was added after the
measurements.

***

## 8. Migration

As in r2 §8, with these changes:

- **Rule data** become argument, cue, strong-cue and bare-template sets. G1–G3, R3–R7, the frame
  lexicons and the licence-driven PASS are removed.
- **Guard R7-FWD** is amended in the same change to pin `OI_RULES` and the OI identifiers, the
  absence of `MARKERS` and `OI_MARKERS`, the strings `cannot exist without` and `hidden` in the OI
  rules, and an empty licence list unless adopted entries exist.
- **The gate step** runs the scan with `--repo` and full history.
- **Landing needs** 248 review records at tree M (fewer if the owner prefers to reword some
  sentences) and the H-Hawking licence for the two `W-GR-KMS` sentences, or their rewording.

No manuscript change follows from the redesign itself. The ch05 / FULL:1328 sentence of §6.5 is a
separate candidate finding.

***

## 9. Questions for the owner

1. **Adopt r3's architecture** at a landing cost of about 248 records (155 distinct texts), against
   r2's demonstrated silent-pass rate?
2. **Lexicon dial.** Keep the criterion of §3.2 (248), or widen it (first lexicon: 1,427) to reduce
   the residual class of §6.6?
3. **Reviewer pool for records.** Each record needs an independent non-author reviewer. Should
   records for prose that is plainly unrelated (for example `other-subject`) be batched under one
   owner authority?
4. **The ch05 / FULL:1328 `W-BM-EUCLID` candidate.** Route it to manuscript review?
5. **The next independent held-out batch** (criterion 6): who writes it?
