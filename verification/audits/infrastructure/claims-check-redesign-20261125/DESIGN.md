# Withdrawn-claim checker: investigation and redesign (Issue #1565)

Paper-only design for independent review and the owner's adoption decision. Nothing here modifies
`tools/claims_check.py` or any other repository file. Base: `main` at
`e2e2a623265187a28ebec604ab8bcc672742888f`.

**Goal link.** Verification integrity (Issue #1565): decides whether the release gate's
withdrawn-claim step can be specified so that it rejects prohibited assertions and accepts governed
or unrelated uses across all existing rules, and sends what it cannot decide to recorded human
review instead of accepting it. It would decide the specification an implementation is held to; it
does not decide any manuscript claim.

**Authority.** Owner decision of 2026-11-25 quoted in Issue #1565 (paper-only investigation and
redesign; no implementation before independent design review and adoption).

**Evidence base.** Three trees were scanned, each extracted blob by blob from the commit (a plain
`git archive` omits `verification/programmes` and `verification/audits`, which carry
`export-ignore`; a scan of such an archive misses 1,077 of the 1,133 Markdown files):

| Tree | Commit | Role |
|---|---|---|
| M | `e2e2a623` (`main`) | regression base |
| A | `adfe7138e` (PR #1560, first commit) | the tree on which the current checker flagged the CLPW sentences |
| H | `9971a61` (PR #1560 head) | the tree after the CLPW sentences were reworded to pass the checker |

The measurements in §6–§7 come from a throwaway prototype (regex-based, about 400 lines) written
only to test this design. It is not proposed for landing; §6.4 lists how it was developed against
the controls, which limits what its scores show.

***

## 1. Findings on the existing checker

The checker splits each `.md` file under the root on blank lines, and for each paragraph and rule
reports a hit when the rule's pattern matches and none of the rule class's marker strings occurs
anywhere in the paragraph. General rules (`CLAIMS`) use `MARKERS`; the OI-necessity rules
(`OI_CLAIMS`) use `OI_MARKERS`. One exemption entry exists.

**F1. Patterns name the subject or the predicate, not the assertion.** Five of the ten general
rules have a pattern, or a pattern alternative, that matches a bare subject or a bare predicate:
`state-independent`, `purely kinematic`, `coupling-degree minimi\w*`, `any QFT on this
background`, `any QFT on a bifurcate`. Every use of the word is then treated as a candidate
assertion of the withdrawn claim, whatever it describes. In tree M, 26 paragraphs match a pattern;
on reading, none asserts a withdrawn claim in its own voice, and two quote one inside a record that
corrects it (§7).

**F2. Acceptance is co-occurrence of any marker anywhere in the paragraph.** The marker need not
govern the matched text, need not be in the same sentence, and need not be the condition the
withdrawn claim requires. Measured exposure: a prohibited sentence ("The Hawking temperature
$T_Q$ is state-independent.") appended to each of the 6,828 manuscript paragraphs longer than 200
characters in `papers/` and `book/` of tree M is accepted in 2,532 of them (37.1%); in 2,104 of
those no named hypothesis is present, and the acceptance rests on generic words (`does not` occurs
in 1,021 paragraphs, `conditional` in 997, `assumption` 381, `premise` 372, `cannot` 308). For the
OI class the same test accepts 55 of 6,828 (0.8%), mostly through `not a theorem` and `redundant`.

**F3. Markers are raw substrings.** `conditional` matches inside `unconditional`: in 20
manuscript paragraphs of tree M the only occurrence of `conditional` is inside `unconditional`, so
"$T_Q$ is unconditionally state-independent" would be accepted by the word that strengthens it.
Named hypotheses are accepted regardless of which one the rule needs: `H-link` (225 paragraphs)
accepts a $T_Q$ assertion. `definition*` matches only the literal asterisk form. `kinematic in its
parameter` occurs nowhere in the corpus.

**F4. The formula rule is excused by any marker.** `GR: epsilon*kappa/c should be
epsilon*kappa/c^2` records a dimensional error, which no qualifier repairs; the current mechanism
accepts the erroneous formula in any paragraph containing `does not`, `cannot`, or another general
marker (control P-EPS-1).

**F5. Case and inflection gaps (false negatives of the patterns themselves).** Patterns are case
sensitive: sentence-initial `Coupling-degree minimization` (10 occurrences in tree M, 8 of them in
`papers/` and `book/`, among them
`papers/SM.md:72`, the authoritative scope statement) is never examined. The b_m pattern matches
only the ungrammatical `forces an Euclidean`; the grammatical `forces a Euclidean metric` escapes
(held-out control H-P-8). The OI patterns require `QM|quantum mechanics` immediately before the
verb, so `quantum theory requires observational incompleteness` and `quantum mechanics
presupposes ... ` with an intervening adverb escape. Paraphrases of the assertion
("$T_Q$ does not depend on the state", "independent of the state") are not covered.

**F6. The exemption.** The single entry exempts `unamended Q3 (state-independent gate records of
the model 𝔔)` in the frozen record
`verification/programmes/oi-qm/reconstruction/drafts/tune-1-20261111/TUNE-1-STEP2-AMENDMENT-1.md:286`
from the $T_Q$ rule. The file and phrase exist on `main`. The use is a false positive of F1 (the
adjective modifies "gate records"); the exemption treats the symptom for one file.

**F7. The false-positive cost is paid in the text.** Records on `main` were reworded to avoid the
pattern rather than because the wording was wrong:
`verification/programmes/oi-qm/reconstruction/drafts/bell-scope-868-20261111/REVIEW-BS-r2-NONAUTHOR.md:351`,
`verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/CHANGES.md:49`
(row Δ27) and its review response `.../review/RESPONSE-CORR322.md:34` state this explicitly. PR
#1560's head commit `9971a61` rewrote the three book occurrences of "a state-independent additive
constant" (CLPW renormalized entropy) as "an additive constant that does not depend on the state",
while `papers/Main.md:720` and `:724` keep the hyphenated form and pass only because their
paragraphs contain `cannot` and `assumption`, which are unrelated to the phrase.

**F8. Scan scope.** The checker scans every `.md` under the root, including frozen records under
`verification/`, which cannot be corrected by editing (§A.39, §A.42 item 6). In tree M, 13 of the
26 matching paragraphs are in verification records. A FAIL there can only be resolved by an
exemption.

**F9. Output.** The verdict is the exit status (0/1), which satisfies §A.44; the per-hit detail is
printed text only.

Root cause, confirmed: F1 and F2 together. Subject anchoring is absent, and governance is replaced
by paragraph co-occurrence of a vocabulary that includes generic negation and conditionality
words.

***

## 2. Rule inventory

For each existing rule: the withdrawn claim it protects, where the corpus withdraws or scopes it
(authoritative anchor on `main`), its subject, the prohibited assertion, and its measured exposure.
"Hits" counts paragraphs matched by the current pattern in trees M / A / H.

| Current rule (message) | Withdrawn claim and anchor | Subject | Prohibited assertion | Hits M/A/H | Current FP / FN exposure |
|---|---|---|---|---|---|
| `K=2d: coupling-degree minimization` | Coupling-degree minimization fixes $K=2d=6$ (or $m=1$, or the site factorization). Anchor: `papers/SM.md:72` ("Scope of $K = 2d$"), `:364`, Theorem 6 at `:366` (conditional link count under H-link); `book/appendix-b-derivations.md:291`. | coupling-degree minimization | fixes / selects / derives / establishes $K$, $2d$, $m=1$, sites; "$K=2d$ follows from" it; "consequence of" it | 15/15/15 | Pattern is the subject alone: every mention is a candidate (15 in M: 13 correct uses, 2 quotations of the withdrawn claim in a correcting record, accepted only through markers that do not govern them). Sentence-initial capital never checked (F5). Accepts an inserted assertion via `link count`, `H-link`, `does not` elsewhere (P-KDEG-2, -4). |
| `K=2d asserted as the answer` | Same claim, phrased as "the framework's answer is $K=2d$". Anchor as above. | the framework's answer | is $K = 2d$ | 0/0/0 | Literal; accepted with `not a proof` in a relative clause (P-KDEG-3). |
| `b_m: 'forces a Euclidean quadratic symbol'` | Cubic equivariance forces a Euclidean quadratic symbol; it forbids anisotropy only, $b_m$ may vanish. Anchor: `papers/SM.md:268`. | cubic equivariance / symmetry, projected memory | forces a Euclidean (quadratic symbol / metric) | 0/0/0 | Matches only "an Euclidean" (F5, H-P-8). |
| `b_m: leading geometry asserted Euclidean` | Same; nondegeneracy is supplied separately. Anchor: `papers/SM.md:268`. | leading scalar propagation geometry | is Euclidean (without nondegeneracy / $b_m\neq0$) | 0/0/0 | Accepted with `cannot` in a later clause (P-BM-2); governed use "When $b_m\neq0$ ..." rejected (N-BM-2). |
| `GR: T_Q asserted state-independent (H-balance)` | $T_Q$ (horizon thermality) holds for every state; it requires the state condition H-balance, and the infrared limit does not remove state dependence. Anchor: `papers/GR.md:62` (H-balance), `:72`, `:76`. | $T_Q$, $T_{\rm dS}$, Hawking / de Sitter / horizon / Unruh / KMS temperature, thermality, thermal ratio | is state-independent / independent of the state / does not depend on the state | 6/14/8 | Pattern is the predicate alone (F1). 6 false positives in A (CLPW book sentences), 2 accepted only by unrelated markers (Main:720, :724). 6 further matches in records, all unrelated uses (gate records, graph of an additive update, timing marginal, support of a rule). Paraphrases not covered. |
| `GR: thermality asserted purely kinematic (H-balance)` | Horizon thermality is purely kinematic; it rests on H-balance, a selection condition. Anchor: `papers/GR.md:72`, `:76`. | thermality, thermal spectrum, $T_Q$ and the temperature terms | is purely kinematic | 0/0/0 | Predicate alone: "the Lorentz boost is purely kinematic" is rejected (N-KIN-2). |
| `GR: unconditional KMS periodicity (H-Hawking)` | Any QFT on the horizon background must be periodic in imaginary time / KMS; it holds only under the H-Hawking conditions. Anchor: `papers/GR.md:653` (H-Hawking), `book/appendix-b-derivations.md:206`. | any / every / a QFT on the background | must be periodic in imaginary time / must be KMS / is a KMS state | 2/2/2 | `any QFT on this background` is a subject-only alternative: every mention is a candidate. Both hits pass through `H-Hawking`, which here does govern. Accepted with `does not` in another clause (P-KMS-2). |
| `GR: paraphrase of a superseded unconditional claim` | Same KMS claim (`any QFT on a bifurcate`), and the exact free-level cone per channel. Anchors as for KMS and cone. | as KMS / free-level cone | as KMS / exact per channel | 0/0/0 | Mixed rule: one subject-only alternative, one literal. Split in the redesign. |
| `GR: exact free-level cone (false on the normalized d=3 branch)` | The free-level cone is exact per channel; false on the normalized $d=3$ observer branch. Anchor: `papers/GR.md:643`. | free-level cone | is exact (per channel); "exact free-level cone" | 0/0/0 | Accepted with `cannot` in a relative clause (P-CONE-1). |
| `GR: epsilon*kappa/c should be epsilon*kappa/c^2` | Dimensional error. Anchor: `papers/SM.md:164` ($\varepsilon\kappa/c^2$). | (formula) | the expression $\varepsilon\kappa/c$ without the square | 0/0/0 | Excused by any general marker (F4). |
| OI: `QM asserted to require OI` | QM requires (presupposes) OI. Only containment (`qm_implies_oiCore`) and forward redundancy (`completedOI_iff_physical`) are proved. Anchor: `verification/README.md:630–641`; `verification/lean-mathlib/OIBridge/CompletedOI.lean`; `verification/audits/foundations/oi-core-forward-redundancy.md`. | QM, quantum mechanics, quantum theory | requires / needs / presupposes / depends on OI or observational incompleteness | 2/2/2 | Accepted through `containment`, `is not proved`, `not a theorem` anywhere in the paragraph (P-OI-2, P-OI-3, H-P-4). "No theorem shows that ..." rejected (N-OI-3). |
| OI: `cannot exist without` | Same claim. | QM | cannot exist without ... | 0/0/0 | Accepted through `redundant` (P-OI-4). |
| OI: `requires a hidden sub-quantum level` | QM requires hidden variables / ontology. Anchor as above ("No ontological necessity"). | QM | requires / needs hidden information, variables, states, ontology, a sub-quantum level | 0/0/0 | Requires adjacency and a fixed noun list: "needs a hidden sub-quantum level" escapes. |
| OI: `OI asserted to explain quantum structure` | OI causes / explains / produces quantum mechanics. Anchor as above (redundancy). | OI, observational incompleteness, ignorance | causes / produces / explains / generates / gives rise to QM, quantum (structure) | 1/1/1 | Accepted with `not a theorem` in a relative clause (H-P-5). |
| OI: contrapositive | "Without OI there is no QM." | (fixed form) | as stated | 0/0/0 | Literal. |
| Exemption (TUNE-1 Q3) | — | gate records | — | 1/1/1 | Path-bound and phrase-bound; would be unnecessary if the predicate were bound to its subject (F6). |

`MARKERS` (29 strings) and `OI_MARKERS` (15 strings) are not rules but the acceptance mechanism;
F2 and F3 give their measured behaviour. The guard R7-FWD pins the presence of the separate OI
class with its own marker list (§8).

***

## 3. Mechanism

### 3.1 Per-rule specification

Each rule is a data record (in the checker or a sibling JSON file), with a stable identifier that
is never reused (§A.30):

| Field | Content |
|---|---|
| `id` | e.g. `W-GR-TQ-STATE`; one rule per withdrawn claim, several templates per rule |
| `claim` | the withdrawn claim, one sentence |
| `anchor` | path and section of the authoritative statement on `main` that withdraws or scopes it |
| `subject` | subject lexicon: terms and symbols naming the claim's subject (case-insensitive, word-bounded), plus `heads`, the head nouns of the subject class (e.g. *temperature*), used only to detect demonstrative anaphora |
| `templates` | the assertion forms, each one of: *copular* (SUBJECT copula PREDICATE), *attributive* (PREDICATE SUBJECT), *causative* (makes/renders SUBJECT PREDICATE), *verbal* (SUBJECT VERB OBJECT, with an object lexicon), *passive / nominal* (OBJECT follows from SUBJECT; consequence of SUBJECT), *literal* (a fixed formula or phrase) |
| `inherent_negation` | true where the predicate contains its own negation ("cannot exist without", "does not depend on the state"); a negation inside the predicate is part of the assertion, never a qualifier of it |
| `licensed` | the qualifiers under which the assertion is the corpus's stated result: named hypotheses or scope phrases (e.g. `H-balance`, `H-spectrum` for $T_Q$; `H-Hawking` for KMS; "in the core-containment sense", `qm_implies_oiCore` for OI-REQ; `b_m \neq 0`, "nondegenerate" for b_m). Empty for claims that are false outright (cone on the normalized branch, the formula). Each entry cites its anchor |
| `non_governing` | phrases that look like qualifiers but state the setting in which the claim is false (e.g. "on the normalized $d=3$ branch" for the cone rule) |
| `foreign_subject` | `pass` or `review`: what to do when the predicate is bound to a subject outside the lexicon. `pass` for generic predicates (*state-independent*, *purely kinematic*, *exact*); `review` for predicates that carry the claim's content by themselves ("must be KMS", "periodic in imaginary time", "forces a Euclidean ...") |
| `controls` | at least one positive, one negative and one ambiguous control (§4) |

The general and OI marker lists are retired. Their legitimate content survives as rule-specific
`licensed` entries and as the shared frame lexicon of §3.4.

### 3.2 Units: paragraph, sentence, clause

Normalization before matching: emphasis markers (`*`, `_`) are blanked; line breaks become spaces
after sentence segmentation; math (`$…$`, `$$…$$`) and code spans are protected so that their
punctuation does not segment.

- **Paragraph**: blank-line separated, as now; used only for anaphora windows and line numbers.
- **Sentence** (the scope unit at which governance is decided): split after `.`, `!`, `?`
  (optionally followed by closing quotes, brackets or emphasis) before whitespace and a capital,
  quote, bracket, `$` or end of text, except after a fixed abbreviation list (`e.g.`, `i.e.`,
  `cf.`, `vs.`, `et al.`, `Fig.`, `Eq.`, `Ref.`, `No.`); after a display formula followed by a
  capital; at each table-row separator, list-item start and display-math line, which are their
  own units.
- **Clause**: within a sentence, (a) parentheticals `( … )`, paired dashes ` — … — ` and
  comma-introduced relative clauses (`, which|whose|who|where …`) are extracted as their own clauses;
  (b) the remainder is split at `;`, `: `, an unpaired ` — `, and at a comma followed by a
  coordinator (`and`, `but`, `while`, `whereas`, `so`, `though`, `although`, `yet`) and at a bare
  ` but `. A clause that begins with a verb after a coordinator split inherits the subject of the
  preceding clause (verb-phrase coordination).

The paragraph is not the governance unit, and proximity is not governance: co-occurrence in the
same paragraph, the same sentence or the same clause is never by itself sufficient.

### 3.3 Binding: is the assertion made of the rule's subject?

A *bound assertion* is a template match in one clause in which the predicate's grammatical subject
(or the attributive head) is a subject-lexicon term:

- **attributive**: the predicate is immediately followed by its head noun phrase (up to three
  tokens). If the head is a subject term, the assertion is bound. If the head is another noun
  ("additive constant", "gate records", "graph", "timing marginal"), the use is **unrelated** and
  passes, whatever else the sentence or paragraph contains. If the head is a generic noun
  (*quantity, value, result, one, answer*) and a subject term is in the anaphora window, REVIEW.
- **copular**: the subject is the noun phrase ending immediately before the copula (last seven
  tokens). A subject term there binds it, unless the phrase's last token is a generic noun (REVIEW).
  A pronoun or demonstrative subject (*it, this, that, these, they, which*), or a demonstrative noun
  phrase of the subject class (*this temperature*), goes to REVIEW when a subject term occurs in the
  same or the preceding paragraph, and passes otherwise. Any other noun phrase is a foreign subject
  (pass).
- **verbal / causative**: the subject term precedes the verb within the clause, within a binding
  distance of eight tokens. A subject term in the clause beyond that distance goes to REVIEW. A
  relative pronoun (`that|which|who`) resolves to the noun phrase immediately before it. A verb with
  another explicit subject is foreign: pass if `foreign_subject = pass`, REVIEW if `review`.
- **literal**: the match is the assertion.

Dominance: when binding is undetermined but a G2 or G3 qualifier in the clause would govern the
assertion if it were bound, the outcome is PASS either way, and the candidate passes without
REVIEW (recorded as such).

### 3.4 Governance

A qualifier **governs** a bound assertion A only in one of the following positions. Nothing else
governs.

- **G1 Negation in the assertion's slot.** A negator (`not`, `never`, `no longer`, `cannot`,
  `fails to`, `rather than`) between the subject and the predicate (copular: between copula and
  predicate; verbal: in the auxiliary position immediately before the verb); a negative determiner
  on the subject (`no`, `nothing`, `neither`, `none`); a negative object quantifier (`explains
  nothing`); `no`/`rather than` immediately before an attributive predicate. A negation inside an
  `inherent_negation` predicate is not G1.
- **G2 Negative or non-assertive frame with A in its complement.** A frame from a shared lexicon
  precedes A in the same sentence, with no `;` between, and A lies in its complement: `not
  claimed (that|:)`, `it is not (proved|shown|established|the case) that`, `(no|neither|none of|nothing
  in) NP (shows|proves|establishes|derives|says|implies) that`, `(does|do|did) not (show|establish|
  prove|imply|say|claim)`, `whether`, `the necessity reading`; or the post-frame `the (claim|statement|
  reading) that A (is|remains) (withdrawn|false|unproved|not established|unsupported)`. A sentence that
  is a bare `That …` fragment is governed only when the nearest preceding heading, or a preceding
  paragraph ending in a colon, is itself such a frame ("What the freeze does not claim").
- **G3 Licensed condition governing the clause.** A `licensed` qualifier of this rule occurs in A's
  clause, or in a sentence-initial antecedent clause of A's sentence (`If|Under|Given|Assuming|When|
  Provided … ,`). A licensed qualifier in another clause, sentence or paragraph does not govern.

**Non-governing by construction** (the cases the owner's decision names): a qualifier in another
paragraph; in another sentence; in another clause of the same sentence (a coordinated clause, a
relative clause, a parenthetical); a negator after the predicate attached to another verb ("is
state-independent and does not depend on the cutoff"); discourse adverbials (`not surprisingly`,
`not only`, `not least`); `unconditional(ly)`, which strengthens.

### 3.5 Outcome: PASS / FAIL / REVIEW

Decision for each candidate (a predicate, verb or literal match of a rule), in order:

1. No bound assertion and no REVIEW trigger (foreign head or subject, no subject term in the
   window): **PASS** (recorded as *unrelated* in the structured output).
2. Bound assertion governed by G1, G2 or G3: **PASS** (recorded with the governing position).
3. REVIEW triggers, each recorded with its code:
   - **R1** anaphora: pronoun, demonstrative or generic-head subject with a subject term in the window;
   - **R2** binding undetermined: subject term in the sentence or clause but not in a binding
     position; subject beyond the binding distance; a content-carrying predicate with a foreign
     subject;
   - **R3** a qualifier in A's clause that is not in a governing position: a generic condition word
     (`conditional`, `assum*`, `premise`, `hypothes*`, `under`, `if`, `given`, `provided`, `when`,
     `on the … branch`, `in the … sense`, `on the … reading`) naming no licensed qualifier; a named
     hypothesis that is not licensed for this rule ("Under H-link, $T_Q$ is state-independent"); a
     negator in the clause before the subject that is not a discourse adverbial;
   - **R4** A inside a quotation or a code span (a mention, not a use);
   - **R5** a bare `That …` fragment with no visible frame.
4. Otherwise: **FAIL**.

The literal formula rule has no governance: every match FAILs; a quotation of the error in a
record is resolved by a review record.

REVIEW is never silent acceptance: an unresolved REVIEW fails the gate step exactly as a FAIL does,
and is reported separately so that a reviewer sees which kind of finding it is.

### 3.6 Resolving REVIEW: review records

A REVIEW is resolved only by a review record, kept in one maintained file (proposed:
`verification/infrastructure/claims-reviews.json`, placed under §A.36), each entry bound to:

- `rule` (the rule `id`), `path`, and `sentence_sha256`: SHA-256 of the scope sentence after
  whitespace normalization; plus `sentence`, the sentence verbatim (so a reviewer can read the record
  without the tree);
- `decision`: `governed` (the reviewer identifies the governing text and its position) or
  `unrelated` (the reviewer names the actual subject). There is no decision that accepts an
  assertion of a withdrawn claim: if the sentence asserts it, the text is corrected;
- `reviewer`, `date`, and the owner record that admits it (§A.42 item 7, quoted with author and
  time where automation writes it).

Rules for records: one record covers one (rule, path, sentence); no patterns, wildcards, file-wide
or directory-wide entries; mirrors (`book/ch*.md` and the FULL book) need one record each. Any edit
to the sentence changes its hash and reopens REVIEW. A record whose sentence no longer occurs in its
file is **stale** and fails the step, so the file cannot accumulate dead entries (the present
checker's import-time assertion has the same purpose for exemptions). The checker validates the
file's schema at start and refuses a record with an unknown rule, a missing field or a FAIL-class
finding (a record cannot convert FAIL to PASS).

### 3.7 Exemptions

`EXEMPTIONS` is removed. Its one entry (TUNE-1 Q3) becomes unnecessary: under §3.3 the phrase is an
attributive use with head "gate records" and passes mechanically (control N-TQ-TUNE1; regression
row in §7). No review record is created for it. If an implementation finds a different outcome,
the entry becomes a review record of decision `unrelated`, bound to its sentence, not a phrase.

### 3.8 Output and exit status (§A.44)

- Exit 0 iff there is no FAIL, no unresolved REVIEW, and no stale or invalid review record; exit 1
  otherwise. The release-gate step reads only the exit status.
- `--json PATH` writes the findings in a stated schema: per candidate `rule`, `path`, `line`,
  `verdict` (PASS/FAIL/REVIEW), `code` (unrelated, G1–G3, R1–R5, asserted), `match`,
  `sentence_sha256`, and the review record that resolved it, if any; plus counts.
- `--self-test` runs the control suite of §4 from a data file and fails on any mismatch; the gate
  step runs it on every invocation (as `dependency_label_check.py --strict` does).

### 3.9 Scan scope

The redesign does not by itself change which files are scanned. Two options for the owner (Q1):
(a) keep scanning every `.md` (frozen records then need review records for genuine mentions:
4 in tree M, §7.2); (b) apply FAIL/REVIEW to active material as §A.48 defines it (`papers/`,
`book/`, READMEs, `AGENTS.md` outside its record sections) and report on records without failing.

### 3.10 What is decided mechanically, and what is not

Mechanically decided: whether a subject-lexicon term is in a binding position of a template in the
same clause; whether a qualifier sits in one of the three governing positions; whether a qualifier
is a licensed one for the rule. These are fixed, deterministic pattern decisions over the
segmented text, and their outcome is reproducible from the text and the rule data.

Not decided mechanically, and sent to REVIEW instead: anaphora; subjects or objects outside the
lexicons when the predicate carries the claim's content; condition words that do not name a
licensed qualifier; mentions in quotation or code; frames outside the lexicon in complement-shaped
sentences.

Not detected at all (the residual false-negative class, stated rather than hidden): an assertion
whose wording falls entirely outside a rule's predicate and verb lexicons (e.g. "horizon thermality
is the same for every state" if *the same for every state* is not listed), or whose subject is
named only by a term outside the lexicon when `foreign_subject = pass`. Regex segmentation is not a
parser; it does not resolve scope in nested or elliptical constructions, and the design does not
claim that it does. The controls (§4) and the requirement that every new rule carry its own
controls bound this class; they do not eliminate it.

***

## 4. Control suite

92 controls in four batches, each a paragraph (optionally with a preceding context paragraph), a
rule, and an expected verdict. The text of every control is in the companion data (§6.5); the table
gives the expected verdict, the current checker's verdict for the corresponding current rule(s),
and the prototype's verdict.

**Kinds.** Positive: the prohibited assertion is made, and must FAIL, including with an unrelated
negation or generic marker in the same sentence (other clause) and in the same paragraph, with an
unlicensed named hypothesis elsewhere, with `unconditionally`, and in paraphrase. Negative: governed
(G1/G2/G3) or unrelated uses that must PASS, including `papers/Main.md:720`, `:724`, the three CLPW
book sentences, the TUNE-1 phrase, the reworded CLPW sentence of tree H, and the authoritative
anchors themselves. Ambiguous: anaphora, generic heads, unlicensed or generic conditions in the
clause, quoted mentions, that-fragments; must be REVIEW.

| Batch | Written | Controls (pos / neg / amb) |
|---|---|---|
| 1 | before any prototype run; frozen by hash | 63 (25 / 29 / 9) |
| H | after batch 1 passed, before its own first run; not adjusted after | 20 (8 / 8 / 4) |
| C | after the paraphrase predicate and the quotation trigger were added | 5 (1 / 3 / 1) |
| D | from the corpus findings of §7.2 (frames and fragments in records) | 4 (1 / 2 / 1) |

| id | rule | expected | current | prototype |
|---|---|---|---|---|
| P-TQ-1 | TQ | FAIL | FAIL | FAIL |
| P-TQ-2 (unrelated `does not`, other clause) | TQ | FAIL | PASS | FAIL |
| P-TQ-3 (`cannot`, `assumption`, `conditional on H-link` in later sentences) | TQ | FAIL | PASS | FAIL |
| P-TQ-4 (`unconditionally`) | TQ | FAIL | PASS | FAIL |
| P-TQ-5 (attributive; `cannot` after `;`) | TQ | FAIL | PASS | FAIL |
| P-TQ-6 (`Not surprisingly`; `does not` in a relative clause; paraphrase) | TQ | FAIL | PASS | FAIL |
| N-TQ-1 (G1) | TQ | PASS | FAIL | PASS |
| N-TQ-2, N-TQ-3 (G3, H-balance) | TQ | PASS | PASS | PASS |
| N-TQ-4 (G2 "No theorem shows that") | TQ | PASS | FAIL | PASS |
| N-TQ-MAIN720, N-TQ-MAIN724 | TQ | PASS | FAIL | PASS |
| N-TQ-CH07, N-TQ-CH09A, N-TQ-CH09B | TQ | PASS | FAIL | PASS |
| N-TQ-TUNE1 | TQ | PASS | FAIL (without exemption) | PASS |
| N-TQ-5 (foreign subject after `;`) | TQ | PASS | PASS | PASS |
| A-TQ-1 (pronoun, context names $T_Q$) | TQ | REVIEW | FAIL | REVIEW |
| A-TQ-2 ("in the conditional sense") | TQ | REVIEW | PASS | REVIEW |
| A-TQ-3 ("Under H-link", unlicensed) | TQ | REVIEW | PASS | REVIEW |
| A-TQ-4 (generic head "the relevant quantity") | TQ | REVIEW | FAIL | REVIEW |
| P-KIN-1 | KIN | FAIL | PASS | FAIL |
| N-KIN-1 (G1) | KIN | PASS | PASS | PASS |
| N-KIN-2 (Lorentz boost, foreign) | KIN | PASS | FAIL | PASS |
| A-KIN-1 (pronoun) | KIN | REVIEW | FAIL | REVIEW |
| P-KMS-1 | KMS | FAIL | FAIL | FAIL |
| P-KMS-2 (`does not` in a `though` clause) | KMS | FAIL | PASS | FAIL |
| N-KMS-1 (G3 "only under the H-Hawking conditions", dash parenthetical) | KMS | PASS | PASS | PASS |
| N-KMS-2 (G2 "It is not proved that") | KMS | PASS | FAIL | PASS |
| A-KMS-1 ("conditional on the assumptions above") | KMS | REVIEW | PASS | REVIEW |
| P-CONE-1 (`cannot` in relative clause) | CONE | FAIL | PASS | FAIL |
| P-CONE-2 (on the normalized branch: non-governing) | CONE | FAIL | FAIL | FAIL |
| N-CONE-1 (`papers/GR.md:643` form) | CONE | PASS | PASS | PASS |
| A-CONE-1 (other branch) | CONE | REVIEW | FAIL | REVIEW |
| P-EPS-1 (`does not` in relative clause) | EPS | FAIL | PASS | FAIL |
| N-EPS-1 (`papers/SM.md:164` form) | EPS | PASS | PASS | PASS |
| P-BM-1 | BM | FAIL | FAIL | FAIL |
| P-BM-2 (`cannot` after `;`) | BM | FAIL | PASS | FAIL |
| N-BM-1 (G1 in coordinated verb phrase) | BM | PASS | PASS | PASS |
| N-BM-2 (G3 "When $b_m\neq0$") | BM | PASS | FAIL | PASS |
| P-KDEG-1 | KDEG | FAIL | PASS (capitalized) | FAIL |
| P-KDEG-2 (`does not` in coordinated clause) | KDEG | FAIL | PASS | FAIL |
| P-KDEG-3 ("answer is $K=2d$, which is not a proof ...") | KDEG | FAIL | PASS | FAIL |
| P-KDEG-4 (passive; `H-link`, `link count` in the next sentence) | KDEG | FAIL | PASS | FAIL |
| N-KDEG-1 … N-KDEG-4 (anchor sentences, G1) | KDEG | PASS | PASS | PASS |
| N-KDEG-5 (heading mention) | KDEG | PASS | FAIL | PASS |
| N-KDEG-6 (Theorem 6 form, no subject) | KDEG | PASS | PASS | PASS |
| A-KDEG-1 ("as the assumption list records") | KDEG | REVIEW | PASS | REVIEW |
| P-OI-1 | OI-REQ | FAIL | FAIL | FAIL |
| P-OI-2 (`containment`, `qm_implies_oiCore` in the next sentence) | OI-REQ | FAIL | PASS | FAIL |
| P-OI-3 ("quantum theory"; `is not proved` in coordinated clause) | OI-REQ | FAIL | PASS | FAIL |
| P-OI-4 (`redundant` in relative clause) | OI-NOEXIST | FAIL | PASS | FAIL |
| P-OI-5, P-OI-6, P-OI-7 | OI | FAIL | FAIL | FAIL |
| N-OI-1 (`verification/README.md:791` form, G2) | OI-REQ | PASS | PASS | PASS |
| N-OI-2 (G1) | OI-REQ | PASS | PASS | PASS |
| N-OI-3 (G2 "No theorem shows that") | OI-REQ | PASS | FAIL | PASS |
| N-OI-4 (G3 core-containment sense) | OI-REQ | PASS | PASS | PASS |
| A-OI-1 ("an assumption examined in §4", appositive) | OI-REQ | REVIEW | FAIL | REVIEW |
| H-P-1 … H-P-7 | various | FAIL | 2 FAIL, 5 PASS | FAIL |
| H-P-8 ("forces a Euclidean metric") | BM | FAIL | PASS | FAIL (PASS at first run) |
| H-N-1, H-N-3, H-N-5, H-N-6, H-N-7 | various | PASS | PASS | PASS |
| H-N-2 ("Nothing makes $T_Q$ ...") | TQ | PASS | FAIL | PASS (REVIEW at first run) |
| H-N-4 ("It is not the case that") | OI-REQ | PASS | FAIL | PASS |
| H-N-8 (redshift factor, foreign) | KIN | PASS | FAIL | PASS |
| H-A-1 ("This temperature", demonstrative) | TQ | REVIEW | FAIL | REVIEW (PASS at first run) |
| H-A-2, H-A-3, H-A-4 | various | REVIEW | 2 FAIL, 1 PASS | REVIEW |
| C-P-1 ("$T_Q$ does not depend on the state") | TQ | FAIL | PASS | FAIL |
| C-N-1 (tree H reworded CLPW sentence) | TQ | PASS | PASS | PASS |
| C-N-2, C-N-3 | TQ | PASS | PASS | PASS |
| C-A-1 (quoted OLD text in code span) | KDEG | REVIEW | FAIL | REVIEW |
| D-P-1 (restrictive relative "quantum mechanics that requires ...") | OI-REQ | FAIL | PASS | FAIL |
| D-N-1 (`oi-core-forward-redundancy.md:28`, "Neither statement shows that") | OI-HIDDEN | PASS | PASS | PASS |
| D-N-2 (`oi-n-exploratory.md:16`, "It does not say ...") | OI-HIDDEN | PASS | FAIL | PASS |
| D-A-1 (bare that-fragment, no heading frame) | OI-REQ | REVIEW | PASS | REVIEW |

**Mutation controls.**

- *M1, deletion.* For each of the 17 negative controls whose PASS rests on a governing qualifier,
  the qualifier is deleted (or the negated verb replaced by its positive form). Expected: FAIL.
- *M2, marker insertion.* Each of the 44 current marker strings is inserted into each of the 25
  positive controls of batch 1, as a separate sentence and as a coordinated clause in the same
  sentence. Expected: FAIL in every case.
- *M3, countercontrol.* The current checker on the M2 sentence-insertions; it must accept a
  substantial share, which shows that M2 discriminates.

**Corpus injection.** The positive sentence of P-TQ-1 and of P-OI-1, and the governed sentences of
N-TQ-2 and N-OI-3, appended to each of the 6,828 manuscript paragraphs of tree M. Expected: FAIL
(positives) and PASS (governed) in every paragraph whose last sentence is complete; REVIEW is
admissible where the paragraph ends mid-sentence.

**Regression.** Every paragraph matched by the current checker in trees M, A and H (26 / 34 / 28)
and the exemption, with the current and the proposed verdict and the reason for each change (§7.1).

***

## 5. Acceptance rule (stated before the implementation is measured)

The design is accepted for implementation, and an implementation is accepted for landing, only if
all of the following hold on the frozen control data and the trees of §0, with the control data
fixed before the implementation under test is run:

1. Every positive control FAILs, every negative control PASSes, every ambiguous control is REVIEW.
2. M1: every deletion mutant FAILs. M2: no insertion of a current marker string changes a positive
   control from FAIL. M3: the current checker accepts a non-trivial share of the M2 insertions (the
   control is not vacuous).
3. Corpus injection: no injected positive sentence PASSes; every injected governed sentence whose
   preceding text ends a sentence PASSes.
4. Regression: every change of verdict on a corpus paragraph is listed with a justification in the
   change record; any corpus FAIL that, on reading, is a governed or unrelated use is a defect of the
   implementation (false positive); any corpus REVIEW is either resolved by a review record or
   justified as genuinely ambiguous.
5. Each rule has at least one positive, one negative and one ambiguous control, and at least the
   anchor sentence of its withdrawal as a negative control.
6. An independent reviewer adds a held-out batch of at least 20 controls written without access to
   the implementation's results; criteria 1–2 must hold on it at first run. A held-out failure is
   repaired in the specification and re-tested on a new held-out batch, never by editing the failing
   control.

***

## 6. Prototype measurements

### 6.1 Controls

| Batch | Prototype at first run | Prototype at last version | Current checker |
|---|---|---|---|
| 1 (63) | 54 / 63 | 63 / 63 | 24 / 63 correct (no REVIEW available) |
| H (20) | 17 / 20 | 20 / 20 | 7 / 20 |
| C (5) | 4 / 5 | 5 / 5 | 3 / 5 |
| D (4) | 4 / 4 | 4 / 4 | 1 / 4 |

Current checker over all 92: of 35 positives it FAILs 10 and PASSes 25 (false negatives); of 42
negatives it PASSes 25 and FAILs 17 (false positives); of 15 ambiguous controls it FAILs 9 and
silently PASSes 6.

The three held-out failures at first run were: H-P-8, a false negative (subject lexicon was case
sensitive and the verb had a subject outside it; fixed by case-insensitive lexicons and the
`foreign_subject = review` policy for content-carrying predicates); H-A-1, a silent acceptance of a
demonstrative noun phrase (fixed by the `heads` field and trigger R1); H-N-2, a REVIEW where PASS
was expected (causative template added). The batch-1 first-run failures were implementation
defects (offsets, case, foreign-subject handling) in the prototype, not in the controls.

### 6.2 Mutations

M1: 17 / 17 deletion mutants FAIL. M2: 0 of 2,200 insertions (44 markers × 2 forms × 25 positive
controls of batch 1) change a FAIL; before a fix to the
relative-clause extent, 12 did (relative clause extraction absorbed a following coordinated clause),
which the mutation exposed. M3: the current checker accepts 924 of 1,100 sentence-insertions (84%).

### 6.3 Corpus injection (tree M, 6,828 paragraphs)

| Injected sentence | Expected | Prototype | Current checker |
|---|---|---|---|
| "The Hawking temperature $T_Q$ is state-independent." | FAIL | 6,825 FAIL, 3 REVIEW, 0 PASS | 2,532 PASS |
| "Quantum mechanics requires observational incompleteness." | FAIL | 6,825 FAIL, 3 REVIEW, 0 PASS | 55 PASS |
| "Under H-balance, the Hawking temperature $T_Q$ is state-independent." | PASS | 6,828 PASS | — |
| "No theorem shows that quantum mechanics requires observational incompleteness." | PASS | 6,828 PASS | — |

The three REVIEWs are paragraphs whose last line is an unfinished sentence leading into a display
or list, so the injected text continues that sentence; REVIEW is the correct outcome there. At an
earlier version the injection found 73 REVIEWs and 2 PASSes caused by sentence segmentation after
closing quotes, table rows, list items and display math; those segmentation rules (§3.2) were added
in response.

### 6.4 Limits of these measurements

The prototype was revised after batch 1, after batch H and after the corpus scan of §7.2, so
batches 1, C and D and the corpus are development data for it, not tests. Batch H at first run
(17 / 20) is the only held-out evidence, and it was written by the same author as the prototype.
These numbers show that the mechanism of §3 can be made to separate the controls; they do not
establish an error rate. Criterion 6 of §5 exists for this reason.

### 6.5 Reproduction

The control data (four JSON files), the prototype and the measurement scripts are kept with this
design for the reviewer; they are not proposed for the repository (§A.28). SHA-256 of the files
used for the figures above:

| File | SHA-256 |
|---|---|
| controls batch 1 | `d185865270c1bb0957e70147050bd717b51031de6846808004cce9219078e34b` |
| controls batch H | `d17e0d0b190758c6292f7dc96266fea0442cca0c4c3442642e7dda5f3c1b7f16` |
| controls batch C | `17eccf2901c7b48c2cedf9ee43b7958b74a007df5970e6b39bd16771532d3aab` |
| controls batch D | `e11d72f5ed94155b9b84e704c6bc9ce9fe477f5a56eb341ab9b56a9a0213a8aa` |
| prototype (final) | `04a8b30e589648b50d1a426066a4b7f6860a6a11d7edf17e601db2ecfff3e9ab` |

***

## 7. Regression against the current checker

### 7.1 Every paragraph the current checker matches

Tree M (26 matched paragraphs; current verdict: all PASS, one by exemption). Proposed verdicts:
24 PASS, 2 REVIEW, 0 FAIL.

| Location | Rule | Current (accepting markers) | Proposed | Reason |
|---|---|---|---|---|
| `book/The-Incompleteness-of-Observation-FULL.md:2611` | KDEG | PASS (`H-link`, `does not`) | PASS | G1 negated; subject elided; passive/nominal; G1 negation in the assertion's slot |
| `book/The-Incompleteness-of-Observation-FULL.md:5292` | KDEG | PASS (`H-link`, `H-spin`, `H-cust`) | PASS | no bound assertion (subject mentioned, no assertion template) |
| `book/The-Incompleteness-of-Observation-FULL.md:5883` | GR-KMS | PASS (`H-Hawking`, `H-spectrum`, `conditional`) | PASS | G3 licensed hypothesis governs the clause |
| `book/The-Incompleteness-of-Observation-FULL.md:5966` | KDEG | PASS (`conditional`, `does not answer`, `does not`) | PASS | no bound assertion (subject mentioned, no assertion template) |
| `book/The-Incompleteness-of-Observation-FULL.md:5968` | KDEG | PASS (`does not`) | PASS | G1 negation in the assertion's slot |
| `book/appendix-b-derivations.md:206` | GR-KMS | PASS (`H-Hawking`, `H-spectrum`, `conditional`) | PASS | G3 licensed hypothesis governs the clause |
| `book/appendix-b-derivations.md:289` | KDEG | PASS (`conditional`, `does not answer`, `does not`) | PASS | no bound assertion (subject mentioned, no assertion template) |
| `book/appendix-b-derivations.md:291` | KDEG | PASS (`does not`) | PASS | G1 negation in the assertion's slot |
| `book/ch09-universality.md:196` | KDEG | PASS (`H-link`, `does not`) | PASS | G1 negated; subject elided; passive/nominal; G1 negation in the assertion's slot |
| `book/ch19-open-problems.md:222` | KDEG | PASS (`H-link`, `H-spin`, `H-cust`) | PASS | no bound assertion (subject mentioned, no assertion template) |
| `papers/SM.md:364` | KDEG | PASS (`not establish`, `does not`, `link count`) | PASS | G1 negation in the assertion's slot; unrelated: verb has another subject |
| `papers/SM.md:479` | KDEG | PASS (`H-link`, `H-spin`, `conditional`) | PASS | passive/nominal; G1 negation in the assertion's slot |
| `papers/SM.md:1426` | KDEG | PASS (`assumption`, `rather than facts`) | PASS | no bound assertion (subject mentioned, no assertion template) |
| `verification/README.md:791` | OI | PASS (`containment`, `qm_implies_oiCore`, `not a theorem`) | PASS | G2 assertion inside a negative/non-assertive frame |
| `verification/audits/foundations/a1-main-roots-20261118/AUDIT.md:87` | GR-TQ-STATE | PASS (`conditional`, `premise`, `does not`) | PASS | unrelated: predicate modifies 'support of a' |
| `verification/audits/foundations/p7-boundary-count-20261116/P7-BOUNDARY-COUNT.md:129` | KDEG | PASS (`H-link`, `not establish`, `premise`) | PASS | G1 negation in the assertion's slot; unrelated: verb has another subject |
| `verification/audits/manuscript/oi-n-exploratory.md:17` | OI | PASS (`containment`, `qm_implies_oiCore`) | PASS | G2 assertion inside a negative/non-assertive frame |
| `verification/audits/manuscript/oi-n-freeze.md:81` | OI | PASS (`containment`, `qm_implies_oiCore`) | PASS | G2 that-fragment under a negative-frame heading |
| `verification/audits/manuscript/pr982-minimization-20261028/reports/book.md:455` | KDEG | PASS (`H-link`, `assumption`, `does not`) | REVIEW | R2 rule subject in the clause beyond the binding distance |
| `verification/audits/manuscript/pr982-minimization-20261028/reports/book.md:499` | KDEG | PASS (`H-spin`, `does not`) | REVIEW | R4 assertion inside a quotation or code span (mention) |
| `verification/audits/manuscript/pr982-minimization-20261028/reports/companions.md:22` | KDEG | PASS (`H-link`, `not establish`, `premise`) | PASS | G1 negation in the assertion's slot; unrelated: verb has another subject |
| `verification/programmes/oi-qm/reconstruction/drafts/bell-scope-868-20261111/REVIEW-BS-r2-NONAUTHOR.md:351` | GR-TQ-STATE | PASS (`withdrawn`) | PASS | unrelated: no rule subject bound |
| `verification/programmes/oi-qm/reconstruction/drafts/tune-1-20261111/TUNE-1-STEP2-AMENDMENT-1.md:286` | GR-TQ-STATE | PASS (exemption) | PASS | unrelated: predicate modifies 'gate records of' |
| `verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/CHANGES.md:49` | GR-TQ-STATE | PASS (`H-balance`, `conditional`, `premise`) | PASS | unrelated: predicate modifies 'graph'; unrelated: verb has another subject |
| `verification/programmes/oi-qm/reconstruction/intervene-substate-results-20261113/review/RESPONSE-CORR322.md:34` | GR-TQ-STATE | PASS (`H-balance`, `conditional`, `withdrawn`) | PASS | unrelated: predicate modifies 'graph'; unrelated: verb has another subject |
| `verification/programmes/oi-qm/reconstruction/states-dynamics-audit-20261024/stopping-source-v2/REPORT.md:89` | GR-TQ-STATE | PASS (`conditional`, `cannot`) | PASS | unrelated: predicate modifies 'timing marginal into' |

Tree A adds the eight `state-independent` paragraphs of PR #1560's first commit; the six current
FAILs become PASS:

| Location | Current | Proposed | Reason |
|---|---|---|---|
| `book/The-Incompleteness-of-Observation-FULL.md:2062` | FAIL | PASS | attributive; head "additive constant" (CLPW entropy), not $T_Q$ |
| `book/The-Incompleteness-of-Observation-FULL.md:2709` | FAIL | PASS | same |
| `book/The-Incompleteness-of-Observation-FULL.md:2713` | FAIL | PASS | same |
| `book/ch07-gravity.md:197` | FAIL | PASS | same (mirror of FULL:2062) |
| `book/ch09-universality.md:294` | FAIL | PASS | same (mirror of FULL:2709) |
| `book/ch09-universality.md:298` | FAIL | PASS | same (mirror of FULL:2713) |
| `papers/Main.md:720` | PASS (via `cannot`) | PASS | same reason; the accepting marker is unrelated to the phrase |
| `papers/Main.md:724` | PASS (via `assumption`) | PASS | same |

Tree H: the 28 current matches have the same proposed verdicts as their counterparts in M and A
(Main:720 and :724 PASS, unrelated); the reworded book sentences ("an additive constant that does
not depend on the state") are evaluated under the new paraphrase predicate and PASS (relative
clause with antecedent "additive constant").

Expected changes of verdict, justified: six FAIL → PASS (tree A, CLPW, false positives of F1); two
PASS → REVIEW (tree M, `verification/audits/manuscript/pr982-minimization-20261028/reports/book.md:455`
and `:499`, quotations of the withdrawn claim, "the framework's coupling-degree minimization argument
... rules out this alternative by forcing $K = 2d = 6$" and "coupling-degree minimization fixes K=6",
inside a record that corrects them; the current PASS rested on `H-link`, `H-spin`, `assumption` and
`does not`, none of which governs the quoted assertion). Every
other current verdict is unchanged, and its reason changes from "a marker occurs in the paragraph"
to a stated governing position or an unrelated subject.

### 7.2 Paragraphs the proposed design evaluates that the current checker never matched

New FAIL or REVIEW findings in tree M (identical in A and H):
| Location | Rule | Proposed | Content |
|---|---|---|---|
| `verification/audits/manuscript/pr982-minimization-20261028/reports/book.md:446` | KDEG | REVIEW (R4) | quoted OLD text "(i) Coupling-degree minimization on the $d = 3$ cubic lattice fixes $K = 6$ ..." in a record that replaces it; capitalized, so the current checker never examined it |
| `verification/audits/manuscript/pr982-minimization-20261028/reports/book.md:480` | KDEG | REVIEW (R3) | quoted OLD text "Coupling-degree minimization, which fixes $K=2d=6$, is a definition of a site ..."; capitalized, never examined by the current checker |

With rows 455 and 499 of §7.1, all four REVIEWs in tree M are quotations of the withdrawn
K=2d claim inside one audit record that corrects it: genuine mentions, which a review record
(decision `unrelated`: the sentence quotes the superseded text) resolves under scan scope (a), and
which scope (b) does not fail.

Manuscripts (`papers/`, `book/`): no FAIL and no REVIEW in any of the three trees. Newly evaluated
manuscript sentences, all PASS: `papers/SM.md:68` and `:72` (capitalized subject, G1),
`papers/GR.md:643` (G1).

Development history on this corpus, for the reviewer. The first full-tree run produced 3 FAIL and
14 REVIEW in tree M, all in verification records. The 3 FAILs were false positives (the frame
"Neither statement shows that", and a `That …` fragment under the heading "What the freeze does
not claim"). The frame lexicon ("neither … shows", "does not say"), heading frames for
that-fragments, the subject lexicon ("a QFT"), relative-pronoun resolution, negative object
quantifiers, and narrowing `foreign_subject = review` to predicates that name KMS or imaginary time
were added, giving 0 FAIL and 3 REVIEW; a binding-distance REVIEW was then added after the
prototype was found to pass a quoted assertion whose subject lay nine tokens before the verb (a
false negative, row 455), giving 8 REVIEW; the dominance rule of §3.3 and relative-pronoun
resolution before the distance test reduced these to the 4 above. These extensions are part of §3;
they were found on the corpus, which is why criterion 6 requires a held-out batch.

***

## 8. Migration and propagation

- **Release gate.** `tools/release_gate.py` step `claims` keeps its name and its exit-status
  contract; its command gains `--self-test` (or the checker runs its self-test unconditionally). The
  docstring entry for `claims_check` (line 20) is updated to the new mechanism.
- **Guard R7-FWD** (`verification/lean/edge_rigidity_probe.py`, about line 2254) reads
  `tools/claims_check.py` and requires the substrings `OI_CLAIMS`, `OI_MARKERS`, `cannot exist
  without`, `(requires|needs) hidden` and `core-containment`. Retiring `OI_MARKERS` and rewriting the
  patterns breaks that guard. The implementing change either keeps those tokens as identifiers of the
  OI rule data (the guard's purpose, a separate OI class that general negation words cannot rescue,
  is met more strongly by §3.4) or amends the guard in the same commit to pin the new structure
  (the OI rule ids, their empty generic-acceptance, their licensed lists). Either choice is decided
  with the implementation and reviewed with it.
- **Descriptions of the mechanism elsewhere.** `verification/README.md:641` ("an `OI_CLAIMS`
  class carrying its own marker list"), `tools/dependency_label_check.py:8` and `:21` ("Paragraph
  scope, as in claims_check"), `tools/proof_census.py:11`. The README sentence is in a mutable
  record and is corrected in place (§A.27); the two tool docstrings are code comments (active
  material, §A.48).
- **Exemption and review records.** `EXEMPTIONS` is removed (§3.7). Under scan scope (a) four review
  records are needed for tree M (the pr982 quotations); under (b) none.
- **Records reworded to avoid the checker** (F7) are not edited: frozen records stay as they are
  (§A.39, §A.42 item 6). Whether PR #1560 restores "state-independent additive constant" in the book
  is a manuscript decision for that PR, not part of this design.
- **No manuscript change** follows from the redesign itself: no paragraph of `papers/` or `book/`
  changes verdict to FAIL or REVIEW in trees M, A or H.
- **Rule additions after adoption** carry a full specification and their own controls (§3.1); a
  rule without controls fails the self-test.

***

## 9. Open questions for the owner

- **Q1 Scan scope.** Keep every `.md` (frozen records then need review records for genuine
  mentions) or limit FAIL/REVIEW to active material (§A.48) and report on records without failing
  (§3.9)?
- **Q2 Licensed qualifiers.** The `licensed` lists are scientific statements (e.g. that H-spectrum,
  being stronger than H-balance, also licenses the $T_Q$ assertion; whether H-slope does; that only
  H-Hawking licenses KMS periodicity). They need confirmation against the anchors before adoption;
  this design proposes them from `papers/GR.md` and `papers/SM.md` and does not settle them.
- **Q3 Review records.** Location and format of the review-record file; whether a mirror pair
  (chapter and FULL book) may share one record; who may write a record (owner only, or a reviewer
  under a work package with owner admission).
- **Q4 REVIEW exit status.** One non-zero exit for FAIL and unresolved REVIEW (proposed), or a
  distinct code for REVIEW?
- **Q5 Implementation form.** Regex specification as here, or a dependency on a syntactic parser;
  a parser would reduce R1/R2 cases but adds a toolchain dependency and non-determinism across
  versions, which the release gate currently avoids.
- **Q6 Paraphrase lexicons.** How far the predicate and verb lexicons should extend beyond the
  current patterns (each extension needs controls and will evaluate more corpus text).
