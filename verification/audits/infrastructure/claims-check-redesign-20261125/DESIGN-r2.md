# Withdrawn-claim checker: redesign, revision r2 (Issue #1565)

Paper-only design for independent review and the owner's adoption decision. Nothing here modifies
`tools/claims_check.py` or any other repository file. Base: `main` at
`e2e2a623265187a28ebec604ab8bcc672742888f`. This revision supersedes `DESIGN.md` of PR #1567 at
`1d768f7d8639fc45ec94fbe6d9fd2d27d825ddf5`; `CHANGES-r2.md` maps every finding of the independent
review (PR #1567 comment 7166791821) and every owner direction to the change made here.

**Goal link.** Verification integrity (Issue #1565): decides whether the release gate's
withdrawn-claim step can be specified so that it rejects prohibited assertions, accepts only
assertions that are logically qualified by an independently established condition or that are
unrelated, and sends what it cannot decide to recorded human review. It would decide the
specification an implementation is held to; it decides no manuscript claim and licenses no
hypothesis.

**Authority.** Owner decision of 2026-11-25 quoted in Issue #1565 (paper-only investigation and
redesign; no implementation before independent design review and adoption). Owner decision
(`amaybaum`, 2026-11-25) on PR #1567, verbatim: "#1567 | Correct the claims-checker design against
the independent findings." with: "The prototype's improvement over the existing checker is
encouraging, but three silent misses remain unacceptable without correction. Require actual logical
qualification of the scientific claim, not merely proximity to a qualifying phrase. Do not treat
H-slope or any other hypothesis as licensing a withdrawn claim without independently established
scientific justification. Preserve the reviewer's held-out controls and require additional
independent controls for the revised design." The owner's six design directions are Issue #1565
comment 7165663427.

**What changed in substance.** (1) A qualifier governs only from a fixed logical position: the head
of an antecedent or restrictor (G3), the immediate complement position of a negative frame (G2), or
the assertion's negation slot (G1). Proximity in a clause or sentence is never governance.
(2) Negated or contrasted qualifiers ("even without H-balance", "if H-balance fails") are a REVIEW
trigger. (3) Licensed lists are empty: no hypothesis, H-slope included, licenses any withdrawn claim
until a licence record carrying an anchor quotation and an independent scientific review exists.
(4) Distinct exit codes. (5) Review records bind a full commit. (6) FAIL and REVIEW block only in
active material, defined mechanically. (7) Per-rule frozen equivalence sets and a lexical near-miss
scan close the paraphrase class of silent passes without unrestricted language understanding.

***

## 1. Findings on the existing checker

Unchanged from `DESIGN.md` §1 except where stated. The checker splits each `.md` file on blank
lines and, per paragraph and rule, reports a hit when the rule's pattern matches and none of the rule
class's marker strings occurs anywhere in the paragraph.

- **F1.** Patterns name the subject or the predicate, not the assertion (five of ten general rules).
- **F2. Acceptance is co-occurrence of any marker anywhere in the paragraph.** Definitions used for
  every figure in this revision: a *manuscript paragraph* is a string obtained by splitting each
  `.md` file under `papers/` and `book/` of tree M at the two-character sequence of two newlines
  (`"\n\n"`), keeping those longer than 200 characters (Python `len`); files are visited in sorted
  order. There are 6,883 such paragraphs. "No named hypothesis" means the paragraph contains no
  match of `\bH-[A-Za-z]`. Appending "The Hawking temperature $T_Q$ is state-independent." to each,
  the current checker accepts 2,539 (36.9%); in 1,972 of those no named hypothesis is present. `does
  not` occurs in 1,023 paragraphs, `conditional` in 1,000, `assumption` 382, `premise` 372, `cannot`
  310. For the OI class the same test accepts 55 of 6,883. (`DESIGN.md` gave 6,828 / 2,532 / 2,104
  under an unstated paragraph definition; the independent reviewer's figures, which these reproduce
  exactly, used the definition stated here.)
- **F3.** Markers are raw substrings: in 19 manuscript paragraphs the only `conditional` is inside
  `unconditional`. Named hypotheses are accepted regardless of which one the rule needs.
- **F4.** The formula rule is excused by any marker.
- **F5.** Case, inflection and paraphrase gaps.
- **F6.** The single exemption treats an F1 false positive for one file.
- **F7.** Correct text was reworded to pass the checker (records cited in `DESIGN.md` §1, PR #1560).
- **F8.** Every `.md` is scanned, including frozen records that cannot be edited.
- **F9.** One exit status for every kind of finding.

Root cause: F1 and F2 together.

***

## 2. Rule inventory

As `DESIGN.md` §2, with two changes: the column *Licensed* now reads "none (empty until a licence
record exists, §3.6)" for every rule; the candidate qualifiers that `DESIGN.md` proposed (H-balance
and H-spectrum for W-GR-TQ-STATE and W-GR-THERM-KIN, H-Hawking for W-GR-KMS, the core-containment
sense for W-OI-REQ, $b_m\neq0$ for W-BM-EUCLID) are candidates for the licensing procedure of §3.6,
not rule data. H-slope is not a candidate: `papers/GR.md:76` states that "by the $\alpha$-vacuum slope
above the failure already occurs at H-slope", and `:72` that "the infrared limit does not remove state
dependence"; licensing H-slope for the state-independence of $T_Q$ would license the withdrawn claim.

Rule identifiers (stable, never reused, §A.30): `W-GR-TQ-STATE`, `W-GR-THERM-KIN`, `W-GR-KMS`,
`W-GR-CONE`, `W-GR-EPSKAPPA`, `W-BM-EUCLID`, `W-KDEG`, `W-OI-REQ`, `W-OI-HIDDEN`, `W-OI-NOEXIST`,
`W-OI-EXPLAINS`, `W-OI-CONTRA`.

***

## 3. Mechanism

### 3.1 Per-rule specification and where it lives

Each rule is a data record with the fields of `DESIGN.md` §3.1 (`id`, `claim`, `anchor`, `subject`,
`heads`, `templates`, `inherent_negation`, `non_governing`, `foreign_subject`, `controls`), plus
`equivalence` (§3.11) and `near_miss` (§3.12). The `licensed` field is removed from rule data:
licences live only in the licence file of §3.6, so that no scientific licence can enter through an
edit to pattern data.

**Location (decided).** Rule data are Python data inside `tools/claims_check.py`, one record per rule,
the OI rules in a separate `OI_RULES` list. The licence file and the review-record file are JSON
under `verification/infrastructure/claims-check/` (`licences.json`, `reviews.json`), placed under
§A.36; the control suite is `tools/claims_check_controls.json` beside the checker. Keeping rule data
in the checker keeps guard R7-FWD (§8) a single-file read.

The general and OI marker lists are retired; nothing replaces them as an acceptance mechanism.

### 3.2 Units: paragraph, sentence, clause

As `DESIGN.md` §3.2, with these changes.

- **Sentence.** Additionally split after an end-of-proof mark (`$\square$`, `$\blacksquare$`,
  `$\Box$`, `∎`) followed by whitespace and a capital.
- **Clause boundaries** (the set referred to as *boundary* below): `;`, `: `, an unpaired ` — `, a
  comma followed by `and`, `but`, `while`, `whereas`, `so`, `though`, `although`, `yet`, `since` or
  `because`, and a bare ` but `. Parentheticals, paired dashes and comma-introduced relative clauses
  (`, which|whose|who|where …`) are extracted as their own clauses. A comma followed by `as` or `for`
  is not a boundary (`, as is well known,` is a parenthetical, not a new clause).
- **Fronted phrases.** Within A's clause, the text before A's subject is split at its top-level
  commas into *fronted phrases*; the last piece (between the last comma and the subject) is the
  *near lead*. When A's clause is not the first clause of the sentence and no `;` or `: ` precedes
  it, the sentence's earlier text is prepended (a sentence-initial antecedent scopes over coordinated
  clauses).
- **Following comment clause.** When A's clause is followed by a boundary of the form `, since`,
  `, because`, `, though`, `, although`, `, while` or `, whereas`, that clause is appended to A's
  *tail* for the qualifier checks R3 and R6 only (never for G3).

Proximity is never governance: co-occurrence in the same paragraph, sentence or clause is never by
itself sufficient for PASS.

### 3.3 Binding

As `DESIGN.md` §3.3, with one change (review nit on `which`): a copular clause whose subject is the
relative pronoun `which`, in a comma-introduced relative clause, is bound when the last five tokens
before the relative clause contain a subject-lexicon term, exactly as the verbal rule resolves a
relative pronoun. "The Unruh temperature, which is state-independent, sets the calibration" is then a
bound assertion (FAIL), not R1.

The dominance rule of `DESIGN.md` §3.3 is kept: when binding is undetermined but a governing
position would apply if it were bound, the candidate passes.

### 3.4 Governance: logical position, not proximity

A qualifier governs a bound assertion A only from one of three positions. They are tried in the
order G1, G2, then the qualifier analysis (R6, G3, R3). Nothing else governs.

**G1 Negation in the assertion's slot.** As `DESIGN.md` §3.4.

**G2 A is the immediate complement of a negative frame.** Let `c` be the nearest complementizer
(`that`, `whether`, or a colon after `not claimed …`) before A's subject in the sentence. G2 applies
only when all of the following hold:

1. *Immediacy.* The text between `c` and A's subject has at most six tokens, contains no clause
   boundary, and contains no auxiliary or copula (`is, are, was, were, be, been, has, have, had,
   does, do, did, can, could, will, would, may, might, must, shall, should`). A comma phrase without
   a verb is allowed ("It is not proved that, on the probed window, $T_Q$ is …").
2. *Frame.* The *local matrix* (the text before `c`, back to the last clause boundary before `c`)
   ends with a known frame: `not claimed[ …]:`, `no (statement|claim|evidence|proof|theorem|result|
   assertion|derivation)`, `it is (not proved|not shown|not established|not the case|not true|not
   known|false|unproved|open|unknown|unclear)`, `is not proved`, `unproved`, `(it) has/have not been
   (shown|proved|established|derived|demonstrated)`, `(no|neither|none of|nothing in|nobody|no one|
   nothing) … (shows|proves|establishes|derives|says|implies|demonstrates|has shown|has proved …)`,
   `(does|do|did) not (show|establish|prove|imply|say|claim|assert|state)`, `the (open) question
   (of)`; or `c` is `whether` not followed by `or not`. With a zero complementizer, `(does|do|did) not
   (say|claim|assert|state|show)` immediately before A's subject (after a determiner) is a frame.
3. *Coordination.* When the local matrix ends in `and`/`or`/`nor` after a comma, the complement is
   coordinated with an earlier one, and G2 applies when the local matrix contains a known frame
   ("Nobody has shown that X or that A").
4. *Claim noun.* When the local matrix ends with `the (claim|statement|reading|assertion|conjecture|
   thesis|view|idea|suggestion)`, G2 applies only when the text after A's predicate in the sentence
   reads `(is|was|remains) (withdrawn|false|unproved|not proved|not established|unsupported|not a
   theorem|open|refuted)`. This post-frame is implemented for every template, adjectival ones
   included (review R5(a)). Without that predicate the outcome is R7 (REVIEW).

A frame earlier in the sentence whose complement is not A, or is separated from A by a clause
boundary, does not govern ("We settle whether X: A"; "No theorem shows that X, yet A"; "No experiment
shows otherwise, and A"; "The question is not whether A but …, since A" governs only the first A).
An adverbial `whether or not …,` or `whether X or Y,` clause is never a frame: the first is excluded
by name, and the second fails immediacy because its own verb lies between `whether` and A. `the
necessity reading` is not a frame (it is a generic qualifier, R3).

**R7 Unknown frame (REVIEW; review R4).** When A is the immediate complement (condition 1) of
`that` and the local matrix is not a known frame, the outcome is REVIEW if the local matrix contains a
negative, non-factive or reporting cue (`not, no, never, nobody, nothing, none, neither, nor, false,
doubt…, deny, unclear, unknown, open, unproved, unestablished, unsupported, conjecture…, hypothes…,
suppose…, might, may, could, would, claim…, argue…, suggest…, believe…, propose…, ask…, question…,
hope…, speculate…, wonder…`). Two affirming double negations are treated as assertion, not frame:
`(do|does|did) not doubt that`, `no doubt that`, `not surprising that`, `cannot be doubted`,
`undeniabl…` (review nit). An affirmative matrix ("We show that A", "It follows that A") is not a
frame and A is asserted.

**The qualifier analysis.** A *qualifier token* for a rule is any named hypothesis (`H-` followed by
a letter), any licensed qualifier of the rule (§3.6; none at present), and the rule's qualifier stem
where one is listed (`b_m` for W-BM-EUCLID, `containment` for W-OI-REQ; stems feed R6 only).

- **R6 Negated or contrasted qualifier (REVIEW; review R1).** A negating or contrasting operator
  whose scope contains a qualifier token, within A's fronted phrases or tail: an operator from
  `without, even, regardless of, irrespective of, independently of, independent of, whether or not,
  or not, with or without, stronger than, beyond, except, apart from, unless, not` followed within
  forty characters (no `,;:.`) by a qualifier token; or a qualifier token followed within thirty
  characters by `fails, failing, failed, is/are violated, is dropped, is relaxed, does/do not hold,
  is not assumed, or not, is false, is absent`. R6 takes precedence over G3. It never applies when G1
  or G2 has already governed ("Without H-balance, $T_Q$ is not state-independent" is G1).
  These sentences assert the withdrawn claim at least as strongly as the bare form; the design
  sends them to REVIEW, which blocks, and whose record cannot accept an assertion (§3.7), so the text
  must be corrected. Making R6 a FAIL is a one-line change if the owner prefers it (§9 Q3).
- **G3 Licensed qualifier heads the antecedent or the restrictor.** G3 applies only when a
  licensed qualifier `Q` of this rule is the head of: a fronted phrase of the form
  `(only)? (If|When|Under|Given|Assuming|Provided (that)?|In|On|For) (that)? (the)? Q …`; or a
  post-posed restrictor in A's tail, before any comma, of the form `… (only)? (if|when|under|given|
  assuming|provided (that)?|in|on|for) (the)? Q`. Nothing else in the clause counts: a licensed
  qualifier elsewhere in the clause, in a coordinated clause, in a relative clause, in a following
  comment clause, or in another sentence does not govern.
- **R3 Ungoverning qualifier (REVIEW).** A fronted phrase headed by a conditional word (`if, when,
  whenever, under, given, assuming, provided, once, in case, unless, so long as, as long as`) whose
  head is not a licensed qualifier; a causal, concessive or contrastive fronted phrase (`since,
  because, as, although, though, while, whereas, after, before, for, now that, even, regardless,
  irrespective, independently, no matter, whether, with or without, without`) that contains a named
  hypothesis, a licensed qualifier or a generic condition word; any other fronted phrase, near lead or
  tail containing a named hypothesis, a licensed qualifier, or a generic condition word (`conditional,
  assum…, premise…, hypothes…, in the … sense, on the … reading, under, if, given, provided, when,
  whenever, unless, on the … branch`); a negator in the near lead that is not a discourse adverbial.
  A causal or strengthening fronted phrase with no qualifier is ignored ("Since the cutoff does not
  enter the calibration, A" is FAIL; "Whether or not the detector is inertial, A" is FAIL).

Decision of the qualifier analysis: R6 if any; else G3 if any; else R3 if any; else FAIL.

**Non-governing by construction:** a qualifier in another paragraph, sentence or clause; a negator
attached to another verb; discourse adverbials (`not surprisingly`, `not only`, `not least`, `not
just`, `not coincidentally`, `not unexpectedly`); `unconditional(ly)`; and a rule's `non_governing`
phrases.

### 3.5 Outcome: PASS / FAIL / REVIEW

For each candidate (a template match of a rule, or a near-miss of §3.12), in order:

1. No bound assertion and no REVIEW trigger: **PASS** (*unrelated*).
2. Bound assertion governed by G1, G2 or G3: **PASS** (with the position).
3. REVIEW triggers: **R1** anaphora; **R2** binding undetermined; **R3** ungoverning qualifier;
   **R4** A inside a quotation or code span; **R5** bare `That …` fragment with no visible frame;
   **R6** negated or contrasted qualifier; **R7** unknown or claim-noun frame; **N1** near-miss.
4. Otherwise **FAIL**.

The literal formula rule has no governance: every match FAILs.

### 3.6 Licensed qualifiers: empty until independently reviewed (directions 2, review R5(b), R9)

**State.** `verification/infrastructure/claims-check/licences.json` holds `{"schema":
"claims-licences/1", "fixture": false, "entries": []}`. With no entry, G3 never applies; every
condition-qualified assertion of a withdrawn claim is REVIEW (R3), never PASS. In particular no
hypothesis — H-slope, H-balance, H-spectrum, H-Hawking or any other — licenses any withdrawn claim.

**Entry.** Each entry carries: `rule`; `qualifier` (a regular expression naming the hypothesis or
scope phrase); `proposer`; `anchor` = {`path`, `revision` (a full 40-hex commit reachable from
`main`), `quote` (a verbatim quotation at that revision stating that the withdrawn claim holds under
exactly this qualifier)}; `review` = {`reviewer`, `revision`, `date`, `record` (the path of the
review record on `main`, stating the scientific justification)}.

**Licensing procedure (R9).**

1. The proposer states, for one rule and one qualifier, the anchor quotation and why it establishes
   that the withdrawn claim holds under that qualifier — not merely that the qualifier is discussed
   near the claim, and not that a stronger or weaker condition suffices. A qualifier that the corpus
   states to be insufficient for the claim (H-slope for W-GR-TQ-STATE, `papers/GR.md:72`, `:76`) is
   not eligible.
2. An independent non-author reviewer checks the anchor and its proof dependencies across the corpus
   (the Code Review Rules' whole-framework scope; a claim takes its weakest link) and records the
   verdict, with the commit read, in a review record on `main`.
3. The owner admits the entry (an addition is an adoption of scientific content; §A.50 item 6 where
   it changes what a premise licenses). The entry and its controls (one PASS control headed by the
   qualifier, one R6 control with the qualifier negated, one R3 control with an unlicensed qualifier)
   land in one change.
4. When the anchor changes, the entry is re-reviewed: the checker validates, at every run with
   repository access, that the anchor revision is an ancestor of the commit under check and that the
   quotation occurs at that revision; a licence whose anchor statement is later weakened is withdrawn
   by the same procedure.

**Validation.** The checker refuses (exit 3) a licence file in which any entry lacks an anchor
quotation, a full anchor revision, or a review record with reviewer, record, date and full revision,
or whose reviewer is its proposer, or whose qualifier does not compile; with repository access it
also refuses an anchor revision not reachable from `main` or a quotation absent at it. `--self-test`
validates the deployed licence file the same way; an unreviewed list fails the self-test.

**Fixture.** The control suite's expected verdicts for governed controls were written assuming the
candidate qualifiers. The self-test therefore runs every control twice: (a) under a *fixture* licence
file marked `"fixture": true`, containing the candidate qualifiers (H-slope deliberately absent),
against the controls' written expectations; (b) under the deployed licence file, against
expectations derived mechanically from (a): a control expected PASS whose run (a) rests on G3 is
expected REVIEW; every other expectation is unchanged. A scan refuses a fixture file (exit 3). The
fixture tests the positional mechanism; it licenses nothing, and its entries are not reviewed.

### 3.7 Review records (direction 3, review R7)

A REVIEW is resolved only by a record in `verification/infrastructure/claims-check/reviews.json`:

- `rule`, `path`, `sentence_sha256` (SHA-256 of the sentence after whitespace normalization),
  `sentence` (verbatim), `code` (the REVIEW code being resolved);
- `window_sha256` for codes that depend on context (R1, R5, N1): SHA-256 of the preceding paragraph,
  two newlines and the containing paragraph, whitespace-normalized;
- `decision`: `governed` (the reviewer quotes the governing text and its position), `unrelated` (the
  reviewer names the actual subject), or `mention` (quotation of a withdrawn claim, with the quoted
  source). No decision accepts an assertion of a withdrawn claim, and `governed` may not rest on a
  qualifier without a licence entry: a sentence whose only qualification is an unlicensed hypothesis
  is corrected or waits for the licence procedure;
- `reason`, `reviewer`, `date`, `authority` (the owner record admitting it, quoted with author and
  time where automation writes it, §A.42 item 7);
- `revision`: the full 40-hex commit at which the reviewer read the sentence, which must resolve and
  be reachable from `main` (§A.42 item 3).

**Rule for later commits.** A record remains valid at a later commit C iff (i) its `revision` is an
ancestor of C; (ii) the file at `path` in C still contains the sentence with the same hash, and, for
R1/R5/N1, the same window hash; and (iii) the checker at C still produces a REVIEW finding with the
same rule and code for that sentence. Any of (i)–(iii) failing makes the record *stale* (exit 3): an
edit to the sentence or its window, a rename of the file, or a change of rule data that changes the
finding reopens review. A record that matches a FAIL is invalid (exit 3): records cannot convert FAIL.
Records do not use patterns, wildcards, or file- or directory-wide scope; mirrors need one record
each. In CI the checkout must contain the history needed for (i); a missing object is exit 3, never a
pass.

### 3.8 Output and exit status (direction 4, review R6; §A.44)

| Exit | Meaning | Blocks the gate |
|---|---|---|
| 0 | no FAIL and no unresolved REVIEW in active material; all records valid | no |
| 1 | at least one FAIL in active material (confirmed violation) | yes |
| 2 | no FAIL, at least one unresolved REVIEW in active material | yes |
| 3 | an invalid or stale licence or review record, or an unreadable record file | yes |
| 4 | self-test mismatch, usage error or internal error | yes |

Precedence: 4 > 3 > 1 > 2 (a run with an untrustworthy configuration reports that first). An uncaught
exception maps to 4, so that a crash never reads as a confirmed violation. `tools/release_gate.py`
treats any non-zero return code as failure (`r.returncode == 0`, line 87), so all four stay blocking
with no gate change. `--json PATH` writes `{"schema": "claims-findings/1", "counts", "record_problems",
"findings"}`, each finding with `rule`, `path`, `active`, `line`, `verdict`, `why` (code first),
`match`, `sentence`, `sentence_sha256`, `window_sha256` and `resolved_by`. `--self-test` runs on
every invocation of the gate step.

### 3.9 Scan scope: option (b), active material defined mechanically (direction 1, review R8)

Every `.md` file under the root is scanned. FAIL and REVIEW affect the exit status only in *active
material* (§A.48), classified by path:

- every `.md` under `papers/` and under `book/`;
- every file named exactly `README.md` outside `verification/`, and `verification/README.md` itself
  (§A.48 counts it as a README). Every other `README.md` under `verification/` lies in a programme,
  audit or round directory and is a record;
- `AGENTS.md`, except its *record sections*: a record section starts at a level-two heading line
  (`## `) whose text ends with `(record)` and extends to the next level-two heading. At `main` this
  delimits §A.37 ("Round lifecycle before V3 (record)"). The provenance paragraphs of §A.42 carry no
  such delimiter and are scanned as active (over-inclusion only adds strictness to a mutable file);
  marking them would need an edit to AGENTS.md and is left to the owner (§9 Q4);
- everything else (frozen and mutable verification records, `.md` files elsewhere) is *record*
  material: scanned, and every FAIL, REVIEW and PASS reported in the JSON with `active: false` and in
  the counts (`record/FAIL`, `record/REVIEW`), with exit status unaffected.

Code comments and Lean docstrings are active material under §A.48 but are not Markdown; the checker
does not scan them (unchanged scope). Under (b) the four pr982 review records that `DESIGN.md` §8
required are unnecessary.

### 3.10 What is decided mechanically, and what is not

Mechanically decided: binding in a template position; whether a qualifier occupies one of the
governing positions G1–G3 as defined positionally in §3.4; whether an operator scopes a qualifier
(R6); whether a qualifier is licensed (a licence entry exists); whether a sentence contains a rule
subject followed by a rule cue (N1). These are deterministic regular-expression decisions over the
segmented text, reproducible from the text, the rule data and the licence file.

Sent to REVIEW: anaphora; unresolved binding; ungoverning or unlicensed qualifiers; negated
qualifiers; quotations; bare that-fragments; unknown frames; near-misses.

**Residual false-negative class.** An assertion that uses neither a rule's equivalence set nor any of
its near-miss cues together with a subject term (e.g. a paraphrase whose subject is named only by a
term outside both the subject set and the near-miss subject set); a near-miss whose slot contains an
negator that does not negate the assertion (measured: "The Hawking temperature never fails to take
one value for every state" and "… is not unlike one value for every state" pass as negated); and an affirming construction that the frame rules misread as negative,
which errs towards REVIEW (R7), not PASS. The opposite error — a correct sentence under a negative
frame outside the known lexicon — errs towards REVIEW (R7) when the frame carries a cue word, and
towards FAIL otherwise (remedy §3.13). Regex segmentation is not a parser and does not
resolve scope in nested or elliptical constructions. The controls and the requirement of new
independent held-out controls (§5 criterion 6) bound this class; they do not eliminate it.

### 3.11 Equivalence sets (direction 6, review R10)

Each rule carries a frozen equivalence set: the subject terms, predicate or verb forms and object
terms that the rule treats as the withdrawn assertion itself (FAIL when bound and ungoverned). Each
set is derived from the rule's anchor — the wording of the withdrawn claim and of its correction —
by the closed operations below, and each entry has at least one positive control. An extension is a
rule-data change (§3.13), never a review record.

Derivation operations: (i) the anchor's own subject and predicate; (ii) inflection and hyphenation
variants; (iii) the nominalized and gerund forms of a subject that is itself a nominalization
("coupling-degree minimization" → "minimization of the coupling degree", "minimizing the coupling
degree"); (iv) predicate synonyms that state the same quantified content as the anchor predicate
("state-independent" ≡ "independent of the state" ≡ "the same / identical / unchanged in every
state" ≡ "insensitive to the state"); (v) verbs that state the same modal relation as the anchor
verb (necessity for W-OI-REQ: requires, needs, presupposes, depends on, necessitates, demands, is
impossible without; fixing for W-KDEG: fixes, determines, selects, derives, forces, establishes,
yields, gives, implies, produces, picks out, singles out, entails); (vi) the quantifier family of a
quantified subject (any / every / each / all QFTs). Verbs that are weaker or ambiguous relative to
the anchor go to the near-miss set, not the equivalence set: "QM implies the OI core" is the proved
containment `qm_implies_oiCore`, so `implies`/`entails` for W-OI-REQ are near-miss cues (REVIEW),
not FAIL.

Sets as frozen in the prototype (`work/proto.r2.py`, `RULES`): W-GR-TQ-STATE adds the temperature
"of the (de Sitter / black-hole) horizon" subject, "independent of the choice of state", "the same /
identical / unchanged in / for / across every / all / any / each … state(s)", "insensitive to the
state"; W-GR-THERM-KIN adds "entirely / wholly / solely / merely kinematic(al)"; W-GR-KMS adds "each
QFT", "all QFTs", "every quantum field theory", "must be in a KMS state", "is necessarily / always KMS
/ periodic in imaginary time"; W-BM-EUCLID adds "substratum symmetry" and "implies / guarantees /
entails a Euclidean"; W-KDEG adds the nominalized subjects and "picks out", "singles out", "entails";
W-OI-REQ adds "necessitates", "demands", "is (not) possible / impossible without"; W-OI-HIDDEN adds
"presupposes", "depends on", "necessitates"; W-OI-EXPLAINS adds "accounts for", "underlies".
Provenance: three of these entries ("the same in every state", "minimization of the coupling
degree", "necessitates") correspond to the reviewer's controls X-P-07, X-P-10 and X-P-13, which this
revision's author had read; they are derivable by operations (iv), (iii) and (v), but their presence
is not independent evidence. The near-miss scan (§3.12) is the mechanism that generalizes beyond the
listed forms.

### 3.12 Near-miss scan (review R10)

For each rule with a near-miss record (subject set S′ ⊇ subject terms, cue set K), a sentence that
produces no bound candidate of the rule is examined clause by clause: when a term of S′ (not followed
by a possessive `'s`) precedes a term of K in the same clause, the outcome is **REVIEW (N1)**, unless
a negator lies between the two, a negative determiner precedes the subject, the subject is the
immediate complement of a known G2 frame, or the sentence is a `That …` fragment under a
negative-frame heading (then PASS, recorded). Cue sets (prototype): W-GR-TQ-STATE — sameness or
independence words before `state(s)/vacua`, or a universal quantifier before `state(s)/vacua`;
W-GR-THERM-KIN — `kinematic…`; W-GR-KMS — `KMS`, `periodic in imaginary time`, with a universal
quantifier on the subject; W-GR-CONE — `exact…`; W-BM-EUCLID — `Euclidean`; W-KDEG — `K =`, `2d`,
`six`, `m = 1`, `site(s)`, `carrier` after `coupling degree`; W-OI-REQ — necessity-like verbs
(`necessit…, entail…, imply, demand…, forc…, presuppos…, depend…, rests on, relies on, requir…, need,
without, impossible, grounded, calls for, mandat…, compel…`) before the OI object; W-OI-HIDDEN —
the same before `hidden`; W-OI-EXPLAINS — causal or explanatory words (`explain…, caus…, produc…,
generat…, gives rise, accounts for, origin, source, underl…, yields, deriv…`) before QM. The scan is
lexical and bounded: it does not decide meaning, it only refuses to pass silently.

### 3.13 Remedy for a false-positive FAIL (review R4)

A FAIL on correct text is a defect of the rule data, never of the text and never resolved by a
record. The remedy is a rule-data amendment: (1) the sentence becomes a negative control with its
correct verdict; (2) the frame lexicon, equivalence set, binding rule or non-governing list is
amended so that the control passes; (3) the self-test runs on the whole suite, including every
preserved held-out control; (4) the change is independently reviewed like any checker change and
merged with owner approval. Until it lands, the sentence may be reworded only if the rewording is
correct on its own terms; the F7 practice of rewording correct text to pass the checker is what this
path exists to end. Unknown frames that are probably correct go to REVIEW (R7), not FAIL, so the
cost of a gap in the frame lexicon is a review record, not a rewording.

***

## 4. Control suite

| Batch | Author / provenance | Controls (pos / neg / amb) |
|---|---|---|
| 1 | PR #1567 author, before any prototype | 63 (25 / 29 / 9) |
| H | PR #1567 author, held out from the first prototype | 20 (8 / 8 / 4) |
| C | PR #1567 author | 5 (1 / 3 / 1) |
| D | PR #1567 author, from corpus findings | 4 (1 / 2 / 1) |
| X | independent reviewer, held out from the r1 prototype (hash `c4591b6d…`) | 34 (16 / 11 / 7) |
| R2 | this revision's author, for the new mechanisms (not held out) | 26 (7 / 7 / 12) |

Batch X is preserved byte-identical as `work/reviewer-heldout.json` (SHA-256
`c4591b6d8ec77f205f2eade8b563d7ed5fc3cf9434ba23b536fc570be98424e3`, matching the hash the review
published); no control in it is edited. The review's post-hoc adversarial probes are preserved
byte-identical under `work/reviewer-probes/` (diagnostic, not acceptance controls).

Every control is run under both licence configurations of §3.6. Exit-code, licence and record
controls (`work/run_r2.py exitcodes`, 23 cases) exercise §3.6–§3.9 on synthetic trees.

Corpus injection (criterion 3) appends each of eleven sentences to every manuscript paragraph (§1
F2 definition): the positives of P-TQ-1 and P-OI-1; the governed sentences of N-TQ-2 and N-OI-3 (the
latter with "OI" written out in full as "observational incompleteness"); three polarity-flipped
look-alikes ("Even without H-balance, …", "If H-balance fails, … still …", "… in a sense stronger
than the core-containment sense"); three cross-clause look-alikes ("No theorem shows that hidden
sectors are finite, yet …", "Whether or not the detector is inertial, …", "On the necessity reading,
which we adopt, …"); one near-miss ("Quantum mechanics rests on observational incompleteness.").

***

## 5. Acceptance rule (stated before the implementation is measured)

The design is accepted for implementation, and an implementation for landing, only if all hold on
frozen control data, with the control data fixed before the implementation under test is run:

1. Every positive control FAILs, every negative control PASSes, every ambiguous control is REVIEW,
   under the fixture; under the deployed licence file, the mechanically derived expectations of §3.6
   hold.
2. M1 (deletion), M2 (marker insertion) and M3 (countercontrol) as in `DESIGN.md` §5.
3. Corpus injection: no injected positive, polarity-flipped, cross-clause or near-miss sentence
   PASSes; every injected governed sentence whose preceding text ends a sentence PASSes (under the
   fixture, for the G3 sentence; under the deployed licence file it is REVIEW); REVIEW is admissible
   only where the preceding text does not end a sentence.
4. Regression: every change of verdict on the corpus is listed and justified; any active-material
   FAIL that is a governed or unrelated use is an implementation defect (remedy §3.13); every
   active-material REVIEW is resolved by a review record or justified as genuinely ambiguous.
5. Each rule has at least one positive, one negative and one ambiguous control and its anchor
   sentence as a negative control; each equivalence-set entry and each near-miss cue family has a
   control; each licence entry has the three controls of §3.6 step 3.
6. **Independent held-out controls.** A new held-out batch of at least 20 controls, written by an
   independent non-author reviewer without access to this revision's results, must satisfy
   criterion 1 at first run, with every rule touched by §3.4, §3.11 and §3.12 represented. The
   reviewer's batch X is not held out for this revision (its author read it), and batch R2 was written
   by the author. A held-out failure is repaired in the specification and re-tested on a further new
   batch, never by editing the failing control. All earlier held-out batches remain in the suite.
7. The deployed licence file passes validation (§3.6); no licence entry exists without its review.
8. Exit codes: the exit-code controls hold (each of 0–4 reached by a case that should reach it).

***

## 6. Prototype measurements (revision r2)

The prototype `work/proto.r2.py` is a regex implementation for measurement; it is not proposed for
landing. `work/run_r2.py` runs the exit-code controls and the corpus injection.

### 6.1 Controls

| Batch | First complete r2 run | Final r2 | Final r2, deployed (empty) licences |
|---|---|---|---|
| 1 (63) | 61 / 63 | 63 / 63 | 63 / 63 (derived expectations) |
| H (20) | 19 / 20 | 20 / 20 | 20 / 20 |
| C (5) | 5 / 5 | 5 / 5 | 5 / 5 |
| D (4) | 4 / 4 | 4 / 4 | 4 / 4 |
| X, reviewer (34) | 32 / 34 | 34 / 34 | 34 / 34 |
| R2 (26) | 25 / 26 | 26 / 26 | 26 / 26 |

First-run failures of r2, all repaired in the specification without editing any control:
batch 1 A-KDEG-1 (FAIL for REVIEW: the generic word lay after a `, as` that r2 had first made a
clause boundary) and N-OI-1 (FAIL for PASS: the `not claimed:` frame was cut at its own colon);
batch H H-P-4 (REVIEW for FAIL: the qualifier stem `containment` was first used for R3); batch X
X-P-08 (REVIEW for FAIL: double negation) and **X-P-12 (PASS for FAIL: a silent false negative that
r2 itself introduced by making `, as` a clause boundary)**; batch R2 R2-A-09 (PASS for REVIEW: a
template match with a foreign subject suppressed the near-miss scan).

**Batch X is not held-out evidence for r2.** The author of r2 read the reviewer's table, controls and
diagnosis before writing r2, and several r2 changes target them directly (R1–R5, R10; §3.11
provenance). The 34 / 34 shows that the r2 specification is consistent with those controls; it does
not show an error rate. The r1 first-run score on batch X (24 / 34) remains the only independent
held-out measurement so far. Criterion 6 requires a new independent batch.

### 6.2 Review's adversarial probes (diagnostic)

| Probe set | Reviewer's expectation | r2 outcome |
|---|---|---|
| `probe.json` (13: post-frame, frames, `whether or not`, `No matter`) | 4 PASS, 9 FAIL | 12 exact; v13 "$T_Q$ is state-independent whenever H-balance fails" REVIEW (R6) |
| `probe2.json` (9: polarity-flipped qualifiers, adverbial whether, cross-clause) | 9 FAIL | 3 FAIL; g1–g6 REVIEW (R6); 0 PASS |
| `probe3.json` (2: H-slope) | 2 REVIEW | 2 REVIEW (R3: H-slope licenses nothing) |
| `probe4.json` (6: cross-clause frames) | 6 FAIL | 5 FAIL; f1 "On the necessity reading, which we adopt, …" REVIEW (R3) |

No probe the reviewer expected to FAIL passes. The seven REVIEW outcomes are the design's stated
outcome for negated or contrasted qualifiers and for generic readings (blocking; a record cannot
accept them).

### 6.3 Exit-code, licence and record controls

23 / 23 (`work/run_r2.py exitcodes`): clean tree 0; FAIL in `papers/` 1; REVIEW only 2; FAIL and
REVIEW 1; FAIL in a verification record 0 (reported); FAIL in `verification/README.md` 1; FAIL in a
README under a verification subdirectory 0; FAIL in `tools/README.md` 1; FAIL in an AGENTS.md
`(record)` section 0 and in an ordinary section 1; REVIEW resolved by a valid record (revision on
`main`) 0; record revision not on `main`, abbreviated revision, missing reviewer, edited sentence,
changed window for N1, record against a FAIL, unreadable record file, unreviewed licence entry
(H-slope), licence reviewed by its proposer, licence quotation absent at its revision, fixture file
given to a scan: each 3; usage error 4.

### 6.4 Corpus injection (tree M, 6,883 manuscript paragraphs)

| Injected sentence | Expected | r2, fixture | r2, empty licences | Current checker |
|---|---|---|---|---|
| "The Hawking temperature $T_Q$ is state-independent." | not PASS | 6,874 FAIL, 9 REVIEW | same | 2,539 PASS |
| "Quantum mechanics requires observational incompleteness." | not PASS | 6,874 FAIL, 9 REVIEW | same | 55 PASS |
| "Under H-balance, the Hawking temperature $T_Q$ is state-independent." | PASS (fixture) | 6,757 PASS, 126 REVIEW | 6,883 REVIEW | 6,883 PASS |
| "No theorem shows that quantum mechanics requires observational incompleteness." | PASS | 6,883 PASS | 6,883 PASS | 55 PASS, 6,828 FAIL |
| "Even without H-balance, the Hawking temperature $T_Q$ is state-independent." | not PASS | 6,883 REVIEW (R6) | same | 6,883 PASS |
| "If H-balance fails, the Hawking temperature $T_Q$ is still state-independent." | not PASS | 6,883 REVIEW (R6) | same | 6,883 PASS |
| "… in a sense stronger than the core-containment sense." (OI) | not PASS | 6,883 REVIEW (R6) | same | 6,883 PASS |
| "No theorem shows that hidden sectors are finite, yet quantum mechanics requires …" | not PASS | 6,879 FAIL, 4 REVIEW | same | 55 PASS |
| "Whether or not the detector is inertial, the Hawking temperature $T_Q$ is …" | not PASS | 6,877 FAIL, 6 REVIEW | same | 2,539 PASS |
| "On the necessity reading, which we adopt, quantum mechanics requires …" | not PASS | 6,883 REVIEW (R3) | same | 55 PASS |
| "Quantum mechanics rests on observational incompleteness." | not PASS | 6,883 REVIEW (N1) | same | 6,883 PASS |

No injected positive, polarity-flipped, cross-clause or near-miss sentence passes in any of the
6,883 paragraphs. The 9 REVIEWs of the $T_Q$ positive and the 126 REVIEWs of the governed G3 sentence
(the two cases checked one by one) all occur where the paragraph's last line is an unfinished sentence (a lead-in to a display or list, or
a line ending without terminal punctuation), so that the injected text continues it; checked
mechanically: in none of them is the injected sentence segmented as a sentence of its own. r1 had 3
such REVIEWs for the governed sentence because r1's G3 accepted a licensed qualifier anywhere in the
clause; r2 requires it to head the antecedent, which a merged sentence no longer satisfies — the
intended strictness, REVIEW being admissible there under criterion 3. The current checker accepts all
three polarity-flipped sentences in every paragraph (the defect the review found, at corpus scale).

**Mutation M2/M3** (`work/m2_r2.py`): each of the 44 current marker strings inserted into each of the
25 batch-1 positive controls, as a separate sentence ("The text notes X.") and as a coordinated
clause (", and the text notes X."): 0 of 4,400 insertions (two forms, two licence configurations)
changes a FAIL. M3: the current checker accepts 924 of the 1,100 sentence insertions. M1 (deletion
mutants of the governed negative controls) was not re-run for r2: the r1 mutant set is not among the
work files; it must be regenerated and run before acceptance (criterion 2).

### 6.5 Tree-M scan (every `.md` of tree M, 1,133 files, deployed empty licences)

Exit status 2. Counts: active PASS 1,312, active REVIEW 3, active FAIL 0; record PASS 7,860, record
REVIEW 27, record FAIL 0 (`results/treeM-scan-summary.json` lists every non-PASS finding with its
code and r1 verdict).

Active-material REVIEWs (each blocks the gate until resolved):

| Location | Rule | Code | Reading |
|---|---|---|---|
| `book/The-Incompleteness-of-Observation-FULL.md:5883` | W-GR-KMS | R3 | "any QFT on this background … is periodic in imaginary time with that period only under the H-Hawking conditions": correctly qualified, but H-Hawking has no licence entry; G3 cannot apply until one passes §3.6 |
| `book/appendix-b-derivations.md:206` | W-GR-KMS | R3 | mirror of the above |
| `papers/GR.md:144` | W-GR-THERM-KIN | N1 | "the KMS temperature parameter is fixed kinematically by $\kappa$; whether the emergent state belongs to that KMS class is state-dependent": the scope statement itself; a near-miss false positive, resolvable by a review record of decision `unrelated`, or removed by narrowing the cue to the adjective (§9 Q5) |

No active-material FAIL. The two KMS findings are the sequencing consequence stated in §8.

Record REVIEWs (27, reported, exit unaffected): 16 near-misses (N1) in audit and programme records —
quotations of guarded forms, lists of non-claims, and unrelated uses of "Euclidean" near "cubic";
3 quotations (R4) and 8 R2/R3 findings, all in records that quote superseded KMS or K=2d text in
order to correct it (`hbar-theta0-20261026`, `pr982-minimization-20261028`).

### 6.6 Reproduction

From this directory: `python3 work/proto.r2.py --self-test`; `python3 work/proto.r2.py --controls
work/<file>.json`; `python3 work/run_r2.py exitcodes <git dir> <main ref>`; `python3 work/run_r2.py
inject <tree M> <tools/claims_check.py at e2e2a623>`; `python3 work/proto.r2.py --scan <tree M>
--json <out>`. Tree M is every `.md` blob of `e2e2a623` extracted with `git cat-file` (a `git
archive` omits `verification/` paths marked `export-ignore`). SHA-256 of every file is in
`CHANGES-r2.md`.

***

## 7. Regression against the current checker and against r1

Tree M, current checker: 26 matched paragraphs, all PASS (one by exemption). r1 (`DESIGN.md` §7):
24 PASS, 2 REVIEW, plus 2 new REVIEW (all four in one pr982 record). r2 changes, each justified:

- **Unchanged.** The four pr982 REVIEWs of r1 stay REVIEW; every other r1 PASS among the 26 paragraphs
  the current checker matches stays PASS, with the same governing position or unrelated reason.
- **PASS → REVIEW, active (3).** FULL:5883 and appendix-b:206 (W-GR-KMS): r1 passed them through a
  licensed H-Hawking anywhere in the clause; r2 has no licence (owner requirement) and requires the
  licence to head a restrictor. With a reviewed H-Hawking licence they would pass as G3 (the
  restrictor "only under the H-Hawking conditions" has the required form; under the fixture both
  sentences' analogue control N-KMS-1 passes). `papers/GR.md:144` (W-GR-THERM-KIN): new near-miss.
- **PASS → REVIEW, records (21 lines).** Five KMS lines (six findings) in `hbar-theta0-20261026`
  (quoted OLD text with H-Hawking, no licence); one quotation (R4) in
  `verification/audits/foundations/oi-core-forward-redundancy.md:33`; fifteen near-miss lines. None is a FAIL; none affects the exit status (§3.9).
- **No FAIL anywhere in tree M**, and no change of any manuscript verdict to FAIL.

Trees A and H were not re-scanned for r2. Their distinguishing paragraphs (the six CLPW book
sentences, `papers/Main.md:720`, `:724`, and the reworded tree-H sentence) are controls N-TQ-CH07,
N-TQ-CH09A, N-TQ-CH09B, N-TQ-MAIN720, N-TQ-MAIN724 and C-N-1, all PASS in r2 under both licence
configurations.

***

## 8. Migration and propagation

- **Release gate.** Step `claims` keeps its name and its contract (any non-zero exit fails); the
  docstring entry for `claims_check` (line 20) is updated. The checker runs `--self-test` on every
  invocation, including licence-file validation.
- **Guard R7-FWD (decided: amended in the same change; review R11).** The guard
  (`verification/lean/edge_rigidity_probe.py`, about lines 2254–2260) requires `OI_CLAIMS`,
  `OI_MARKERS`, `cannot exist without`, `(requires|needs) hidden` and `core-containment` in
  `tools/claims_check.py`. Keeping `OI_MARKERS` as a vestigial identifier would preserve a token
  while emptying its meaning and leave the guard's message ("with its own marker list") false, which
  §A.48 forbids. The implementing change amends the guard to pin the new structure in the same file:
  the presence of `OI_RULES` with the identifiers `W-OI-REQ`, `W-OI-NOEXIST`, `W-OI-HIDDEN`,
  `W-OI-EXPLAINS`, `W-OI-CONTRA`; the absence of any marker-list acceptance (`MARKERS`,
  `OI_MARKERS`); the strings `cannot exist without` and `hidden` in those rules; and, in the
  licence file, that no W-OI-REQ entry exists without a review record. The guard's message is
  rewritten to state that OI assertions are governed only positionally and that no generic
  negation word can rescue them. `core-containment` survives as a near-miss and R6 stem, not as an
  acceptance token. Because licences live in a JSON file, the amended guard reads that file too.
- **Descriptions elsewhere.** `verification/README.md:641`, `tools/dependency_label_check.py:8`,
  `:21`, `tools/proof_census.py:11` — corrected in place (§A.27, §A.48), as in `DESIGN.md` §8.
- **Exemptions.** `EXEMPTIONS` is removed; the TUNE-1 phrase is an unrelated attributive use.
- **Records reworded to avoid the checker** are not edited.
- **Sequencing forced by the empty licence file.** With no licence, the two mirrored active-material
  sentences governed by "only under the H-Hawking conditions" (book FULL and appendix B, §7) are
  REVIEW and the gate fails until either a W-GR-KMS licence for H-Hawking passes the §3.6 procedure or
  each sentence receives a review record. Under §3.7 a record of decision `governed` may not rest on
  an unlicensed qualifier, so the licence procedure is the only route: the implementation lands
  after, or together with, the reviewed licence entries that the active material needs. This is the
  intended consequence of the owner's requirement, not a defect.
- **No manuscript change** follows from the redesign itself.

***

## 9. Remaining questions for the owner

Directions 1–4 are adopted as decided above (scope (b); licences only by reviewed record; records with
reviewer and commit; exit codes 1/2/3/4). Open:

- **Q1 Licensing.** Who may serve as the independent scientific reviewer of a licence entry, and
  whether each entry needs a separate owner admission (proposed: yes, §3.6 step 3).
- **Q2 Licences needed before landing.** Whether to start the §3.6 procedure for H-Hawking on
  W-GR-KMS (the only licence the tree-M active material needs, §7) before the implementation.
- **Q3 R6 severity.** REVIEW (proposed) or FAIL for negated or contrasted qualifiers.
- **Q4 AGENTS.md delimiters.** Whether to mark §A.42's provenance paragraphs as a record block
  (an AGENTS.md edit); until then they are scanned as active.
- **Q5 Near-miss review load.** The near-miss scan's active-material REVIEWs at tree M (§6.5) each
  need a review record; the owner may prefer narrower cue sets at the cost of a larger residual class.
