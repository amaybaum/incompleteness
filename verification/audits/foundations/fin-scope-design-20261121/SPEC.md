# FIN-SCOPE: design specification

**Status.** Writer's design, revision 9, WIP / UNVERIFIED. This is a plan only. No checker exists and
nothing has been run, so no verdict below is a measurement. The corpus inventory in §2.3 is a read-only
`grep` count. Independent non-author review is required before any implementation is proposed.
Implementation, the governance change and any merge each need a separate owner decision. Revision 2
answered review c.7064941939 (B1–B7, N-a–N-j). Revision 3 answers the delta review c.7065126686 (R1–R5,
and generality moved into proofs and post-proof prose). It makes the guarantee structural (§1.1), and
the lexical rules of §3 become a screen that prioritises review. Revision 4 answers review c.7065227255
(C1–C3): hypothesis nodes join the dependency graph, multi-paragraph statements keep their proofs, and
O7 is costed. Revision 5 answers c.7065296420: named conditions resolve corpus-wide, deleted scoped
blocks are members, the cost is reconciled, and reductions (r1) and (r3) are limited. Revision 6
answered c.7065333755 with a frozen canonical-definition map (§2.5). Revision 7 answers c.7065410306:
copies are recognized whatever their form, every book file that `FULL.md` mirrors is a surface, the
worked groups are re-derived in full, and every deleted block is a member. Revision 8 answers
c.7065459234: copy recognition no longer enumerates forms. Every occurrence of a mapped name is
classified by a recorded review, and an unclassified occurrence fails the gate. Revision 9 applies
the nits of c.7065519776 (CONFIRMED WITH NITS) and owner criterion 5 of c.7065520418:
- headings, whole lists and whole tables are occurrence units;
- the matcher's input is stated;
- the upper group sizes are labelled as estimates;
- copies are classed by fidelity as exact, equivalent or different.

It also folds in the reviewer's addendum c.7065535973, which applies the owner's five criteria:
- a designated classifier role;
- pending as a blocking state;
- controls for ambiguous, incorrectly mapped and misclassified occurrences;
- prose citers;
- a blocking rule for different formulations.

The map from findings to sections is in §14.

**Authority.**
- #1169 c.7061660930, item 1, owner decision of 2026-11-21:
  - FIN-SCOPE is the permanent name. `A1` stays retired and its identifier is not reused.
  - "the relevant #1483 checks are reused as a standing release gate for new or materially revised
    theorem statements. Wherever automation cannot decide whether a hypothesis is sufficient, independent
    mathematical review is required".
  - `FiniteConf` (#1482) stays as the explicit Lean predicate.
  - "FIN-SCOPE verifies the scope of claims; it does not require finiteness. A theorem may apply only to
    infinite systems, only to finite systems, or to both, provided its assumptions and proof justify that
    scope."
  - Its governance PR is prepared after the A1-retirement edits land.
- #1169 c.7063843557, stream 5: design and adversarial tests only, and no `AGENTS.md` change until the A1
  retirement lands.
- #1169 c.7064767045: research, planning and preregistration only.
- Background decisions:
  - c.7057297534: a regression check against new global infinity assumptions, and cardinality
    neutrality.
  - c.7058446475: the configuration-space sentence; "Finiteness stays explicit wherever an individual
    theorem requires it".
  - c.7058783437: the safeguard sentence.
  - c.7061062574, item 6: the #1483 criterion.

**Dependencies.** None of these is treated as established.
- **D1. #1477 has landed.** FIN-SCOPE's baseline is enrolled only on a `main` that contains it.
- **D2. #1483 has landed on `main`.** FIN-SCOPE reuses the normalization, allowlist and term lists of its
  `compare/verdict.py` from the landed blobs (§4). If #1483 does not land, see §12, O2.
- **D3. #1482 renames `Substratum.A1`.** Both the old name and `FiniteConf` are in the binder list (§5.3),
  so the design does not depend on the rename.

This design does not modify, and does not require changes to, #1477's frozen material, #1483's tools or
inputs, or any manuscript line under the #1477 ledger.

## 1. Purpose

FIN-SCOPE is a permanent safeguard for the A1 retirement. With no global cardinality assumption, every
result carries its own scope, and FIN-SCOPE checks that the scope a statement claims is the scope its
local hypotheses state. It guards against two failures:

- **(a) Silent finiteness.** A new or revised statement uses finiteness without stating it as a local
  hypothesis. Examples are counting, a uniform prior, pigeonhole, a maximum over the configurations, a
  finite-only lemma it cites, and `Fintype`.
- **(b) Unsupported generality.** A new or revised statement asserts validity for infinite systems, or
  for systems of every cardinality, without a proof that covers that scope.

The rules are symmetric between finite and infinite scope (§9). FIN-SCOPE decides nothing about
sufficiency.

### 1.1 The guarantee is structural; the lexical rules are a screen

No lexical rule can be complete here. Negation, paraphrase, notation and the placement of a claim
are open-ended, and each review of this design has found a new escape class (§9). FIN-SCOPE's guarantee
therefore does not rest on the lexical rules. It is this:

> **Every member of a pull request's review set carries a current review record by a reviewer other
> than its author, answering the fixed checklist. The gate fails otherwise.**

The **review set** of a pull request, computed against its merge base, is the union of:
- **(R-a)** every new or revised statement block (§2.4), including a block whose resolved citation
  targets, or whose *hypothesis digest*, changed while its masked digest did not (§2.4); and **every
  disappeared block, unconditionally**. A deleted block is reviewed against checklist item 4, extended:
  does any surviving result rely on it, and is each scope obligation it carried (finite or infinite
  hypotheses, a stated generality) carried by a surviving statement or deliberately withdrawn? Its
  scope counts are carried into the record from its reference entry. A deletion with `FS_L + IS > 0`
  also raises an L hit, as a pointer for the reviewer. The membership never depends on the screen,
  since a clean lexical result never substitutes for review (c.7065358283);
- **(R-e)** every new, changed or deleted *hypothesis node* (§2.5);
- **(R-b)** every block in the *dependency closure* of (R-a) and (R-e): a block that cites, directly or
  through a chain of citations among parsed blocks and hypothesis nodes, a block of (R-a) whose
  statement digest, `FS_A` or `IS` changed, or a hypothesis node of (R-e). This includes **every prose
  unit classified as a citation** (§2.5) of a changed node group, wherever it stands: inside or outside
  a block, and on or off a claim surface. An example is a Methodology paragraph that applies `(C1)`.
  Such a unit is reviewed against checklist items 1, 2 and 4, for its reliance on the changed
  condition;
- **(R-c)** every changed paragraph that is a proof of, or the *post-block paragraph* (§2.2) of, any
  block, and the block it belongs to;
- **(R-d)** every changed sentence or table row on a claim surface (§2.1).

The **checklist** is fixed, and each answer is recorded:
1. *Finite hypotheses used.* Does the proof, or any result it cites, use finiteness of a configuration
   space or of another object? If so, is that finiteness stated in the statement or its cited local
   hypotheses?
2. *Infinite hypotheses used.* The same question for infiniteness, a limit or a measure structure.
3. *Generality claimed.* Does the statement, its proof, or the post-block paragraph claim validity for
   infinite systems, or for systems of every cardinality? If so, which proof covers that scope?
4. *Lost scope.* Did the change remove or weaken a finite or infinite hypothesis? If so, which proof
   establishes the result without it?
5. *Screen hits.* Each blocking screen hit (§3.3) on this member is answered: justified, with a basis
   and, for G and L hits, a proof citation; or the member is narrowed.

**The screen** is the set of lexical rules of §3. Its role is to prioritise:
- it orders the review set (members with blocking hits first);
- it names, in each hit, the span the reviewer must look at;
- a *blocking* hit adds checklist item 5 for that member;
- an *advisory* hit (G5, `scope-unclear`; §3.3) is listed, and needs no answer.

A member with no screen hit still needs its review record. A screen pass is never evidence that a
statement's scope is right, and a screen hit is never evidence that it is wrong.

Two safeguards from the owner's O7 decision (#1169 c.7065358283) bind the whole design:
- **A clean lexical result never substitutes for mathematical review.** The screen finds potential
  problems. Whether a member's scope is right is decided only by its review record.
- **Mechanically identical is not mathematically equivalent.** A *mechanically identical* change is the
  same token substitution at every site, which the tool can check. A *mathematically equivalent* change
  is one that leaves the mathematics unchanged, which only a reviewer can judge. Examples are rewriting
  "$S$ is finite" as "$|S| < \infty$", or reordering hypotheses. Mechanical identity licenses batching
  only together with an independent verification of scope neutrality ((r1), §12.1). A claimed
  mathematical equivalence never licenses batching: each such site has its own record.

## 2. Scope and block recognition

### 2.1 Surfaces

| Surface | Units | Mode |
|---|---|---|
| `papers/*.md` | statement blocks (§2.2) | gate (§5.1) |
| `book/The-Incompleteness-of-Observation-FULL.md`, and every `book/*.md` whose content it mirrors: `ch*.md` (with `ch00-introduction.md`), `appendix-*.md`, `glossary.md`, `preface.md`, `readers-guide.md`, `acknowledgments.md` and `bibliography.md` | statement blocks, hypothesis nodes and their copies; mirror pairs (§3.4, rule M) | gate |
| Lean declarations that the census resolves in a block's paragraph (§5.3) | declarations | gate |
| *Claim surfaces* outside blocks: abstracts, sections titled Conclusion(s) or Summary, and Markdown table rows | sentences and table rows | gate (§6.2) |
| other manuscript prose outside blocks | sentences | PR layer, advisory (§6.2; §12, O3) |

The following are out of scope:
- `verification/` records, which are kept by `G13` and by the `legacy-records` step;
- Git history and frozen records;
- generated `.tex` and `.pdf` files.

### 2.2 Block grammar

A *statement block* starts at a *label*. Its extent is defined below. A label is any of:

- a bold opener at the start of a paragraph: `**K[ ID][ (TITLE)][.|:]**`, where:
  - `K` is one of `Theorem`, `Lemma`, `Proposition`, `Corollary`, `Claim`, `Remark` or `Prediction`;
  - `ID` matches `[A-Z]?\.?\d+(\.\d+)*[a-z]?'*` (for example `24`, `A.3`, `B.2.1`, `5b`, `9'`), or is
    absent;
  - `TITLE` is any parenthetical. The closing `.` or `:` may stand inside or outside the parenthesis;
- `**Theorem statement.**`;
- a heading `#{2,4} K[ ID][ (TITLE)]`, with `K` and `ID` as above.

A block has three parts, and its extent ends with the last of them. Its extent depends on whether a
proof opener (below) occurs before the next label or heading:
- **Statement, block with a proof.** From the label to the proof opener, across every paragraph between
  them. This is how multi-paragraph statements keep their proofs, for example a theorem with clauses
  `*(i) …*` to `*(iv) …*`, or a lemma continued by `$$…$$` and `*so that …*` (C2). Paragraphs between
  them are of two kinds:
  - *statement paragraphs*: italic paragraphs, continuation paragraphs (below) and the label's own
    paragraph. They form the local hypotheses;
  - *interposed prose*: any other paragraph. It belongs to the block's extent for review membership
    (R-a, R-c), and the screen reads its `GEN` and `IS` (rule E). It is not part of the local
    hypotheses, so it can neither supply `FS_A` nor hide scope.
- **Statement, block with no proof.** The label's paragraph, continued across directly following
  *continuation paragraphs*: list items (lines opening with `-`, `*`, `+` or `N.`), display math (`$$`,
  `\[`, an `equation` or `align` environment), block quotes, and italic paragraphs that open with a
  clause marker `*(i)`, `*(a)` or `*(1)`. It stops at the first other paragraph, at the next label, or
  at a heading. Remarks and Predictions always take this form. Prose after a proofless block is
  therefore never part of it, and cannot supply or hide scope.
- **Local hypotheses.** The statement, together with the text of each hypothesis or setting label the
  statement cites, for example `(F)`, `(H2)` or `Setting 3`, defined in the same file. A label defined in
  another file counts only when the statement cites it with its file.
- **Proof.** It opens at the first paragraph before the next label or heading that begins with
  `*Proof*` or `**Proof**`,
  either followed by any words or a parenthetical and then `.` and the closing emphasis. This covers
  *Proof.*, *Proof sketch.*, *Proof outline.*, *Proof structure.*, *Proof setup.*, *Proof of X.*,
  *Proof (construction).*, and the bold `**Proof.**` (4 in the corpus) and `**Proof outline.**` (2).
  It closes at the first `$\square$`, `∎`, `\qed` or `$\blacksquare$`. A proof that reaches the next
  label or heading without a closer is closed there, and the run records a parse note (§3.3, rule P).
- **Post-block paragraph.** This is not part of the block. It is the first ordinary paragraph after
  the block's extent, before the next label or heading. The screen reads it for generality (rule E),
  and the review set includes it when it changes (§1.1, R-c).

Remarks and Predictions have no proof part.

**Footnotes.** Normalization (§4) always receives the block's file text, so every `[^id]` reference is
expanded inline. A reference with no definition in its file raises rule P.

### 2.3 The measured inventory the grammar is fitted to

This inventory comes from a read-only `grep` of `papers/*.md` and `book/*.md` at `df6da1c6`. It is the
grammar's design input, and it is not a measurement of FIN-SCOPE. The implementation's self-test must
re-derive it at enrollment and report any label form the grammar misses.

**Bold labels (digits shown as N):**

| Count | Form |
|---|---|
| 26 | `**Prediction N:**` |
| 17 | `**Theorem (T).**` |
| 16 | `**Remark (T).**` |
| 13 | `**Theorem N**` |
| 12 | `**Theorem B.N.N (T).**` |
| 12 | `**Lemma N (T).**` |
| 12 | `**Lemma B.N.N (T).**` |
| 11 | `**Lemma (T).**` |
| 7 | `**Corollary (T).**` |
| 6 | `**Theorem A.N**` |
| 6 | `**Proposition N.N**` |
| 6 | `**Corollary N.**` |
| 6 | `**Remark**` |
| 5 | `**Theorem N.**` |
| 5 | `**Corollary.**` |
| 2 | `**Theorem Nb**` |
| 2 | `**Proposition Na**` |
| 2 | `**Lemma.**` |

Other forms also occur: `**Lemma B.N**`, `**Corollary N.N**` and `**Theorem B.N.Na (T).**`.

**Other forms:**
- Heading theorems: four `### Theorem A.N`, all in SM.
- Proof openers: 146 `*Proof.*`, and 11 other `*Proof …*` forms.
- Proof closers: 172 `$\square$`/`∎`/`\qed`, and 6 `\blacksquare`.

`**Definition …**` labels are not blocks. A scope claim inside a definition reaches the gate through
the local-hypothesis citation of §2.2.

### 2.4 Keys, digests and matching

The *masked text* of a block is its normalized text (§4), with these masks applied:
- its own `ID` is replaced by `#`;
- every cross-reference of the form `(Theorem|Lemma|Proposition|Corollary|Claim|Remark|Prediction|
  Definition|§|Eq\.?|Equation|Section|Chapter|Appendix) ID` is replaced by the token `#ref`. The
  kind word is removed too, so that no vocabulary reads it;
- whitespace is collapsed.

The *digest* of a block is the SHA-256 of its masked text. Renumbering a block, or retargeting one of its
cross-references, therefore leaves its digest unchanged.

The reference record (§6.1) also keeps, for each block:
- its *resolved citation targets*: the keys of the parsed blocks and hypothesis nodes (§2.5) its
  citations resolve to, after renumbering is undone by the pairing below;
- its *hypothesis digest*: the SHA-256 of the normalized text of every hypothesis node in its local
  hypotheses, in citation order.

A change in either makes the block revised for the review set (R-a) and for the screen, although its
digest is unchanged. The transitive clauses (§3.1) and the dependency closure (R-b) use the resolved
targets.

Blocks of the before-version and the after-version of a file are paired in three ordered steps:
1. **By digest.** Equal digests pair. If several blocks share a digest, they pair by order of occurrence,
   which resolves duplicate unnumbered labels such as the two `**Corollary.**` blocks in `FULL.md`.
2. **By content.** Each remaining after-block pairs with the remaining before-block of the same kind `K`,
   in the same file and the same FULL chapter segment, with the highest token-Jaccard similarity of
   masked text, provided that similarity is at least 0.6. The threshold is frozen with the tool. Ties
   are broken by order of occurrence. A pair made here is *revised*.
3. **Unpaired.** A remaining before-block has *disappeared*, and a remaining after-block is *new*.

"Materially revised" (c.7061660930) means that the digest changes. A whitespace-only change does not
change the digest. Neither does renumbering, nor retargeting a cross-reference.

### 2.5 Hypothesis nodes (C1)

A *hypothesis node* is a paragraph that defines a named hypothesis, condition or setting, or that states
a standing scope. Each is a node of the dependency graph, with key `(file, name)` and a digest of its
normalized text. The node forms are:
- a paragraph that opens by defining a parenthesised label, `(F): …`, `(H2) …`, `**(C1)** …`, or a named
  condition such as `(EM)` or `H-χ`;
- for a name in the canonical map (below), any paragraph, list item or table row that the occurrence
  register (below) classifies as its canonical definition or as a copy. No typographic form decides
  this: the register does;
- `**Definition …**`, `**Setting …**`, `**Assumption …**` and `**Hypothesis …**` paragraphs;
- a *standing scope sentence*: a sentence opening with `Throughout this (section|chapter|paper|appendix)`
  or `In this (section|chapter), … (is|are) assumed`. Every block in its scope cites it implicitly, so
  it is part of each such block's local hypotheses.

A block cites a node when its statement names the node's label, or the node is a standing scope
sentence over it.

**One corpus-wide dependency index.** Citations are resolved across all surfaces, `papers/*.md`, the
book chapters and `FULL.md`, through a single index built at every run. It has two parts.

**(i) The canonical-definition map.** This is a frozen file, `canonical.json` (§7). For every
*corpus-wide name* it assigns exactly one *canonical definition*, and it lists every other paragraph or
span that has the node form for that name as a *copy*. Corpus-wide names are the AGENTS.md whitelist
((C1)–(C4), (EM), H-χ, H-spin), H-BD, and every further name the enrollment inventory finds cited from
more than one file. Each entry records:
- `name`, with its sub-forms (for example `C2-structural` and `C2-slow` under `(C2)`) and its frozen
  alias phrases (for example "effective-mixing hypothesis" for `(EM)`);
- `canonical`: the file, an *anchor* (the label text that opens it), and the digest of its normalized
  text. For an inline-defined name, the node is the defining span: the run-in bold label and the text it
  governs, up to the next run-in label or the end of its paragraph;
- `copies`: for each copy, its file, anchor, digest and kind. A *mirror* is a chapter↔FULL copy,
  expected to be byte-identical after masking. A *restatement* restates the condition, for example a
  book appendix restating a paper's hypothesis. An *application* uses the label to apply the condition
  in a paper's own setting.

All copies of a name, together with its canonical definition, form one *node group*.
- A citation of the name, in any file, cites the group.
- A change to the canonical definition, or to any copy, makes every member of the group, and every
  citer of any of them, review-set members (R-e, R-b).
- The reviewer answers, for each restatement and application, whether it still agrees with the
  canonical text. This is how a restatement that diverges from the canonical text goes to review.
- At enrollment, every restatement and application is reviewed once against the canonical text, and
  its digest pair is recorded. Afterwards, a change to either digest of a pair is a divergence, and the
  pair goes to review.
- A mirror whose masked text differs from its partner raises rule M.

**(ii) File-local names.** A name outside the map, such as `(F)` or `(H2)`, resolves to the definition in
the citing file. A file-local name cited from another file must name the defining file.

**Ambiguity fails closed, for names outside the map.**
- The enrollment inventory lists every citation by bare name.
- A name outside the map that resolves to two non-mirror definitions fails the inventory (V12), and so
  does a citation that resolves to none.
- A whitelisted name absent from the map fails it.
- For mapped names, the occurrence register below replaces any form-based recognition.

**The occurrence register: fail-closed classification of every mention (c.7065459234).**
Enumerating copy forms has failed twice on the real corpus: first unparenthesised and table forms, then
plain list items (`book/ch18-beyond.md:67–70`) and paragraphs that open "C1 requires …". The design
therefore stops deciding copies by form.
- **Occurrences and their units.** An *occurrence* is a unit that mentions a mapped name in any
  position. The units are:
  - **a paragraph**, including a footnote definition and a display-math paragraph;
  - **a whole list**: every item of the list, together with its lead-in paragraph (the paragraph directly
    before the list, when it ends with `:`), whenever the name appears in the lead-in or in any item.
    Each item still carries its own class within the unit, so items that define a condition without
    naming it under a named lead-in ("The conditions C1–C4 are:") are classified;
  - **a whole table**: header row and every row, whenever the name appears in the header or in any cell,
    with a class per row;
  - **a heading** that mentions a name, together with its section body up to the next heading of the
    same or a higher level. A change anywhere in that section voids the heading unit's classification.
    A body that defines a condition under `### C1 (coupling)` without naming it is therefore classified.
    In the corpus there are 15 such headings, all range citations today (for example
    `papers/Complexity.md:280`, `papers/Medicine.md:146`, `book/ch11-origin-of-life.md:142`), with their
    FULL copies.
- **A mention** may be the name with or without parentheses, bold, italics or a list marker; a sub-form;
  a member of an expanded range or list; or a frozen alias phrase.
- **The matcher's input.** The matcher runs on the unit's raw source after this normalization:
  - #1483's `normalize_text`, with the file text, so that footnotes are expanded, confusable letters are
    folded (Cyrillic `С1` becomes `C1`), NFKC applies (fullwidth `Ｃ１` becomes `C1`), and zero-width and
    discretionary hyphens are removed;
  - FIN-SCOPE's LaTeX pre-normalization (§3.1);
  - an unwrapping of `\mathrm{…}`, `\text{…}` and `\textsf{…}`.

  Code spans, inline and display math, HTML comments and image alt text are matched, not skipped.
- **Over-matching.** The matcher deliberately over-matches: a word-bounded `C1`–`C4` anywhere counts,
  including primed variants such as `C1$'$` and text such as "class C1". Over-matching costs one
  classification. Under-matching would cost an unreviewed dependency.
- **The one stated exclusion.** Subscripted and superscripted symbols, `C_1`, `C_{k}` and `C^1`, are not
  mentions. The corpus uses them for other objects (GR:811, `$C_1, \ldots, C_k$`; GR:653,
  `\Delta C_2`; smoothness classes). This exclusion is frozen with the matcher, and widening it is a
  map change under §7.
- **Classification.** Every occurrence has an entry in `occurrences.json`, keyed by file, the
  occurrence's digest and the name. Its class is one of:
  - **canonical**, exactly one per name;
  - **copy**, with its kind (restatement, application or mirror) and its **fidelity**. It joins the
    name's node group. An occurrence count is not proof of semantic consistency (c.7065520418), so
    each copy's fidelity is one of:
    - **exact**: after the normalization above, masked and whitespace-collapsed, its text equals the
      **whole** canonical text. A copy equal only to a span of it is never exact. It is `equivalent` only
      under an attestation that the omitted part is not relied on by that copy's citers, and `different`
      otherwise (F1, c.7065581514). This is checked mechanically at every run. A
      change to either side that breaks equality voids the class, and the copy blocks until it is
      updated or reclassified. No attestation of equivalence is needed, because identity is checked;
    - **equivalent**: a paraphrase, or an application that is a faithful instance. A reviewer attests in
      the record that it states the same condition as the canonical text, or a correct instance of it,
      and the attestation names the canonical digest it was made against. A change to either side voids
      the attestation, and the copy blocks until it is re-attested. Equivalence is a reviewer's
      judgement, never a mechanical result (§1.1);
    - **different**: a genuinely different formulation. It is a **blocking finding**, routed to
      reconciliation. Its entry in the reconciliation list names both texts, the difference, and the
      citers that resolve to it. This holds at enrollment too, and no baseline tolerance applies. It
      blocks until it is resolved by one of three routes:
      - the copy is aligned with the canonical text and reclassified as exact or equivalent;
      - it is renamed as a distinct condition with its own map entry, as `(C1$'$)` is;
      - an owner decision records that the variant is intended, and names which formulation its local
        citers depend on.

    Every copy carries one of these fidelity classes, with a reason. That covers restatements,
    applications and mirrors alike, not only mirrors;
  - **citation**, a dependency edge to the group;
  - **unrelated**, with a reason: for example GR:629–633, whose `(C1$'$)`–`(C3$'$)` are a different
    condition set.
- **Who classifies: the FIN-SCOPE classifier.** This role is an owner-designated reviewer who is not
  the author of the unit classified, attested under O6. Each classification is a review record made by
  someone in that role. A form-based suggestion from the screen may pre-fill a proposed class, but it
  never classifies. Until O6 is decided, no classification can be attested.
- **Pending is a blocking state, never a class.** An occurrence awaiting classification, such as each
  pending opener of the worked examples, is `pending`.
  - The gate cannot pass while any occurrence in scope is pending.
  - Enrollment cannot complete, and cannot publish `baseline.json`, while any occurrence in the corpus
    is pending or classified `different` and unresolved.
  - The baseline tolerance of §6.3, which lets baseline items stand while their digests stand, never
    covers occurrences.
- **Second classification, against misclassification.** A real copy classified as a citation or as
  unrelated, with its text unchanged, cannot be detected mechanically afterwards. The controls are:
  - **two independent classifiers.** Two distinct people in the classifier role, each attested,
    must agree. That two classifiers are distinct people can be verified only under an O6 option that
    proves distinct identities: (δ), a separate reviewer account; (γ), with separately held keys; or
    (β), where the owner personally designates both people. Under (α) alone, two sessions are not two
    people, and this control is unverified. They must agree for every `citation` or `unrelated` class given to these units: an opening paragraph led
    by a name, a list item or table row led by a name, a heading unit, or a pending opener. A
    disagreement keeps the unit pending;
  - **a recorded second-review sample.** For all other enrollment classifications, a seeded random
    sample of at least one in ten is reviewed again by a second classifier. The seed is frozen before
    the sample is drawn, and the sample is recorded. A misclassification found in the sample triggers a
    second review of every unit of the same name and class;
  - **re-verification on change.** A changed unit voids its classification, so it is classified again
    (above).

  The remaining limit is stated in §9: an unsampled unit, misclassified with its text unchanged and
  not led by a name, stays undetected until its text changes.
- **Ambiguity and incorrect mapping inside the map fail closed.**
  - Entries are keyed per name. A unit that mentions several names needs an entry for every name it
    mentions, so a missing entry fails.
  - Every entry's name must be among the unit's matched mentions, so a copy filed under a name the unit
    does not mention fails.
  - An entry that names a name or anchor absent from the map fails.
  - A second `canonical` entry for one name fails.
  - A mention that could belong to two mapped sets, for example `C1` beside the `(C1$'$)` set, must be
    resolved in its entry to exactly one of them, with a reason. An entry that leaves it open fails.
- **Fail closed.**
  - An occurrence with no classification fails the gate (V26).
  - A new occurrence blocks the gate until it is classified.
  - A changed occurrence voids its classification, because the digest changed, and it blocks until it
    is reclassified.
  - A classification of a deleted occurrence is retired in the same PR.
  - A reclassification from copy or citation to unrelated is itself reviewed, since it removes a node or
    an edge.
- **What follows from a class.**
  - A copy is a node of the group, so its change makes the group and every citer members (R-e, R-b).
  - A citation makes its unit a citer: its block, or the unit itself if it is not in a block. A change
    to the group makes it a member (R-b).
  - An unrelated occurrence carries no dependency.
- **Limit.** The matcher is lexical, so a paraphrase that never names the condition ("the coupling
  condition"), and is not a frozen alias, is not an occurrence (§9). Adding an alias is a map change
  under §7.

**Citation forms recognized.**
- the parenthesised name, `(C1)`, and its sub-forms, `(C2-structural)`;
- ranges, `(C1)–(C4)`, `(C1)-(C4)`, `C1–C4` and `C1--C4`. A range expands to every name between its ends,
  in the order the map records;
- lists, `(C1), (C3)` and `(C1)/(C2)`;
- a bare whitelisted name without parentheses (`C1`, `C2-slow`), counted only inside a range or within
  three words after `condition` or `conditions`, as in "conditions C1–C4 of §1.3". So `class C1` or
  `$C^1$` is not a citation;
- inline forms such as "conditional on (EM)" and "under (EM)", and the map's alias phrases.

**Worked examples: the groups re-derived (c.7065459234).** These come from a read-only `grep` of
`papers/*.md` and `book/*.md` on `main` at `df6da1c6`, which the manuscripts are unchanged since. It
lists every paragraph, list item or table row whose first token, after any marker, bold, italics or
parenthesis, is `C1`–`C4`, `H-BD` or `(EM)`, and every bold run-in containing one. Line numbers are for
orientation only.

The classes below are the **writer's proposed classification**. Enrollment review fixes the actual
classes. Rows marked *pending* are prose openers, which could be restatements or discussion. Mirrors
are listed as pairs, `chapter/FULL`.

| Name | Canonical | Copies (proposed) | Pending openers |
|---|---|---|---|
| `(C1)` | Main:72 | GR:46; Structure:112; Complexity:364; Medicine:27, :150; ch01:251/FULL:584; ch07:24/1889; ch09:112/2527; ch11:152/3115; ch12:42/3228; ch13:50/3471; ch15:59/3936; ch16:196/4341; ch18:67/4798; glossary:25/6516 | ch01:203/FULL:536 ("C1 requires …"); Methodology:162 ("C1 is …") |
| `(C2)` | Main:74 | GR:48; Structure:114; Complexity:366; Medicine:29, :151; ch01:252/585; ch07:26/1891; ch09:114/2529; ch11:154/3117; ch12:44/3230; ch13:52/3473; ch15:61/3938; ch16:198/4343; ch18:68/4799; glossary:27/6518 | ch01:215/548; Methodology:162; SM:1380 ("C2 is *not* established …"); ch15:203/FULL:4080 (`*C2 test.*`) |
| `(C3)` | Main:76 | GR:50; Structure:116; Complexity:368; Medicine:31, :152; ch01:253/586; ch07:28/1893; ch09:116/2531; ch11:156/3119; ch12:46/3232; ch13:54/3475; ch15:63/3940; ch16:210/4355; ch18:69/4800; glossary:29/6520 | ch01:229/562; Methodology:162; SM:1382 ("C3: …") |
| `(C4)` | Main:78 | GR:52; Structure:118; Complexity:370; Medicine:33; ch11:158/3121; ch12:48/3234; ch15:65/3942; ch18:70/4801; glossary:31/6522 | Methodology:162; ch17:168/FULL:4660 ("C4 gives …") |
| `H-BD` | GR:122 | appendix-b:177/FULL:5854 | none |
| `(EM)` | Main:756 (inline run-in) | none | none |

**Recorded as found.** The ch01 definition table (`book/ch01-observation.md:252`, mirrored at
`FULL.md:585`) names C2 "Timescale separation", while the canonical `papers/Main.md:74` reads "(C2)
Memory persistence". Likewise the ch01 table names C3 "Capacity hierarchy" (`:253`/`:586`), against
Main:76's "Sufficient memory capacity". And ch13:52 has "C2: conformational timescale separation". These
are recorded as found, and no correction is made or implied here. Whether each is an equivalent
paraphrase, an application or a different formulation is the classifier's decision at enrollment.
Under §2.5 a `different` class is a blocking finding until it is resolved.

**Group sizes, counting the canonical definition and every copy, with mirrors as two nodes.**

The upper figures are estimates under one assumption: every pending opener is a copy. They are not
maxima, since enrollment review may class any of the roughly 800 other occurrences as a copy, a
mid-paragraph restatement for example.

| Name | Proposed copies only | Estimate if every pending opener is a copy (not a maximum) |
|---|---|---|
| `(C1)` | 26 | 29 |
| `(C2)` | 26 | 32 |
| `(C3)` | 26 | 30 |
| `(C4)` | 15 | 18 |
| `H-BD` | 3 | 3 |
| `(EM)` | 1 | 1 |

**Other name-opening candidates**, proposed as citations or as unrelated:
- range or summary openers, proposed as citations: ch09:84/FULL:2499 ("C1–C4 specify …"), ch18:286/FULL:5017,
  Medicine:88 ("C1–C4 do not …"), and Main:180 (`**Role of (C2)–(C4).**`);
- `(C1$'$)`–`(C3$'$)` at GR:629–633, proposed as unrelated.

**The enrollment workload.** Lines mentioning any of the six names in any position number about 811,
counted approximately with an over-matching `grep`. That is the one-time classification workload.
Afterwards a PR classifies only its new or changed occurrences.

The reviewer's lower bound of 16/16/16/11 (c.7065459234) is contained in these figures. The further
copies found here are the italic run-in forms with their FULL mirrors: 10 for each of C1–C3 (ch09, ch11,
ch12, ch15 and ch16) and 4 for C4 (ch11 and ch15). No form list would have been complete, which is why the register decides.

**Maintenance when a definition moves.**
- A moved node whose digest is unchanged pairs with its old site by digest, as blocks do (§2.4). It is
  not a content change, and the PR must update the map's anchor in the same commit. If it does not, the
  anchor no longer resolves and the gate fails.
- The map update is a `canonical.json` change under §7. It needs its own review record, which states
  that the anchor moved and the text did not.
- If the canonical definition is deleted while copies remain, or edited into what is now a restatement
  of another site, the same PR must designate a new canonical definition. Until it does, the gate fails.
  The designation is a reviewed map change, and the whole group and its citers are members.
- A copy that is deleted is removed from the map in the same PR. It is a member as a deleted node, and
  its citers in its own file are members.
- Line numbers in the map are informational, and are refreshed at each map change.

When a node is new, changed or deleted, the node itself is a review-set member (R-e), and every block
citing it joins the review set by closure (R-b), since its hypothesis digest changed. For example,
editing "(F): $S$ is finite" to "(F): $S$ is a set" makes (F) a member, and every block citing (F) a
member. The screen then recomputes `FS_A` on those blocks, so a finite-use proof raises A. A deleted
node that is still cited also raises rule P on each citing block.

## 3. The decision rule

### 3.1 Term classes

FIN-SCOPE first applies the normalization of §4, then a LaTeX pre-normalization that is applied
identically to both sides: `\mathcal{X}` becomes `\mathcal X`, `\lvert` and `\rvert` become `|`, and
`\left|` and `\right|` become `|`. The exact allowlist is then removed (§4), so the allowlisted
sentences neither trigger an item nor supply scope.

**Carriers.** A carrier is one of:
- the symbols `S`, `\mathcal S`, `\mathcal C_{\ast}`, `\mathcal C`, `\Omega` and `Conf` (as a math
  expression or a Lean term);
- the nouns `configuration space`, `configuration set`, `configurations`, `substratum`, `substrata`,
  `state space`, `system` and `systems`;
- for one block only, every symbol its local hypotheses *declare* as a set, space, group, alphabet or
  carrier (`Let $X$ be a … set`, `$\mathcal H$ a Hilbert space`, `$G$ a group`, `$X \subseteq …$`).

A fixed list cannot name every carrier (R5, §9). A symbol outside the list and undeclared is an
escape class of the screen, and review covers it.

The classes below are counted on the local hypotheses, except `FU` and `IU`, which are also counted on
the proof.

- **`FS_A`, carrier finiteness, counted only on positive predications.** The frozen forms, where `X`
  is a carrier:
  - `$X$ is finite`, `$X$ be finite` (as in `Let $X$ be finite`), with `X` immediately before the verb,
    and the same with `finite-dimensional`;
  - `finite $X$`, `a finite <carrier noun>`, and `a finite(-dimensional)? [<one word>]
    (set|space|group|alphabet)` naming a declared carrier, as in `a finite-dimensional Hilbert space`;
  - `$|X| < \infty$` in any form of `FINITE_TERMS`;
  - `finitely many <carrier noun>`;
  - a Lean finiteness binder: `Fintype`, `Finite`, `Set.Finite`, `FiniteConf`, `Substratum.A1` or
    `Fin n`.

  Any other `finit\w*` occurrence in a sentence that names a carrier does not count. Unless it lies
  inside a `NEG_FINITE` or `GEN` match, it raises the advisory hit `scope-unclear`, which fails closed on the scope side: "Without assuming finiteness of
  $S$", "$S$ is not assumed to be finite" and "finiteness of $S$ is not required" give `FS_A = 0`, so a
  finite-use proof then raises A (R1). The forms are a screen. A negation inside a positive form,
  such as "Let $S$ be finite, though this is not needed", is an escape covered by review (§9).
- **`FS_L`, any finite-scope term.** All `FINITE_TERMS` matches, `bounded` and `compact` included,
  minus those inside a `NEG_FINITE` form. Rule L uses it.
- **`NEG_FINITE`, negated or disjunctive finiteness.** The forms are:
  - `not (necessarily )?finite`, `non-?finite` and `need not be finite`;
  - `finite or (not|infinite)`, `(in)?finite or finite`, `countable or (not|uncountable)` and
    `whether (or not )?finite`.

  These forms are never scope. They count as `GEN`.
- **`IS`, infinite scope.** The terms are:
  - `infinit\w*` outside a `NEG_FINITE` form;
  - `countably infinite`, `uncountabl\w*`, `\aleph`, `\omega` and `of continuum size`;
  - `transfinite` and `|S| = \infty`;
  - `\mathbb N` only where it indexes a carrier: `$X = A^{\mathbb N}$`, `\mathbb N`-indexed
    configurations, `$|X| = |\mathbb N|`. A quantifier `for every $n \in \mathbb N$` is not IS;
  - `\to\infty` applied to a carrier count (`|S|`, `|\mathcal S|`, `N` where `N` is declared in the
    block as the number of configurations), and the Lean terms `Infinite` and `Set.Infinite`.
- **`GEN`, cardinality generality.** Any of:
  - a `NEG_FINITE` form;
  - a *carrier quantifier*: `(for|over|on) (all|every|any|each|arbitrary|unrestricted|unboundedly
    large)` whose quantified object is a carrier. The quantified object is the first math expression
    after the quantifier in the same clause, or, if a noun comes first, that noun. So `for every $S$`,
    `for any $S$ whatsoever`, `for every one of the possible $S$` (first math expression `$S$`) and
    `for every infinite system` (first noun `system`) are carrier quantifiers, and `for every $s \in S$`
    and `for all $n$` are not;
  - a *cardinality phrase*: `of any (size|cardinality|order)`, `(every|all) (size|cardinalit\w*)`,
    `any cardinal`, `regardless of`, `irrespective of`, `independent of`, `whatever` or `no assumption
    on`, where the next words name a carrier or one of `cardinality`, `size`, `finiteness` or `|S|`;
  - `large or small`, `beyond the finite`, `including the infinite`, `also for infinite`, `without (any
    )?finiteness (assumption|hypothesis)` and `uniformly in` followed by a carrier.
- **`PROMO`, status promotion.** On a revised block it is any of `unconditional(ly)`, `without
  exception`, `proved`, `proven`, `established`, `shown`, `derived`, `demonstrated`, `always` or
  `universally`, counted after cross-reference masking. On a new block only `unconditional(ly)` and
  `without exception` count, because the other words occur legitimately in new statements.
- **`FU`, finite use.** The terms are:
  - `pigeonhole`, `counting`, `by counting`, `counting measure`, `summing over`, `sum over`, `average
    over`, `equally likely` and `equiprobable`;
  - `uniform (prior|measure|distribution|weight)`, `1/|S|`, `\frac{1}{|...|}` and `|S|` or `\#S` used as
    a number;
  - `\sum_{...}` with no explicit finite index range, `\log|...|` and `induction on |...|`;
  - `finitely many`, `Poincaré recurrence`, `\max`, `\min`, `\arg\max`, `\arg\min`, `maximum`,
    `minimum`, `attains`, `least element` and `greatest element`;
  - `orbit-stabilizer`, `Lagrange's theorem`, `trace` and `\mathrm{tr}`;
  - `Fintype.card`, `Finset.univ` and `Nat.card`.

  FU also has a transitive clause: a citation in the statement or proof of a block whose `FS_A > 0`
  counts as one `FU`.
- **`IU`, infinite use.** The terms are `countabl\w* additiv\w*`, `\sigma`-additivity, `Kolmogorov
  extension`, `\to\infty` applied to a carrier count, and the Lean terms `Infinite` and `Set.Infinite`.
  The transitive clause is the same: a citation of a block whose `IS > 0` counts as one `IU`. Zorn,
  ultrafilters, general `\lim`, horizon limits `K \to \infty` and compactness arguments are not in IU,
  because they are cardinality-neutral as such (§9).

**The reuse of J10's vocabularies, as an advisory backstop.** J10's `INFINITY_TERMS` and
`PROMOTION_TERMS` serve as a recall set. Its hits are advisory only (R4): they are listed for the
reviewer and never block, so they cannot fail a correct statement.
- Every J10 match in a block's local hypotheses must fall inside a match of one of the classes `IS`,
  `GEN`, `PROMO`, `FS_A`, `FS_L` or `FU`, or inside one of the frozen *neutral* contexts. The neutral
  contexts are:
  - a quantifier whose object is not a carrier. Its span runs from the quantifier word to the end of
    its quantified object, so `for every $n \in \mathbb N$` is one neutral span, and the J10 matches
    inside it (`for every`, `every $`, `\mathbb N`) are all classified;
  - `uniformly continuous`, `independent of the basis`, `universal property` and `in general position`;
  - `\to\infty` applied to a symbol the block declares as a horizon, time, length or index (for
    example `for horizon $K$ … as $K \to \infty$`);
  - on new blocks, the promotion words that `PROMO` omits there (`proved`, `shown`, `derived`,
    `established`, `always`), and `cardinality` used as a noun with a number (`of cardinality $N$`).
- A J10 match outside all of these raises the advisory hit G5 with the note `unclassified`.
  Overlapping J10 matches are merged, and G5 hits are counted per merged span: "in general" is one hit,
  although it matches both `\bin general\b` and `\bgeneral\b`. Since
  every member is reviewed anyway, the backstop's only effect is to point the reviewer at the span.

### 3.2 Per-block counts

For a block `b`, each class name stands for its count in `b`. For a revised block, `b⁻` is its paired
before-version (§2.4), or its reference entry (§6.1) when the reference is newer.

### 3.3 Screen rules and hits

Each screen rule that fires produces a *hit* `(rule, key, digest)`. The screen runs on every member of
the review set (§1.1), and so on the dependency closure as well as the changed blocks. Rule L also
runs on disappeared blocks, and rule P on every parsed block. Hits are *blocking*: each adds
checklist item 5 for its member. The exceptions are G5 and `scope-unclear`, which are *advisory*.

| Rule | Fires when | Guards |
|---|---|---|
| **A**, silent finiteness | `FU(b) > 0` and `FS_A(b) = 0` | (a) |
| **I**, silent infiniteness | `IU(b) > 0` and `IS(b) = 0` and `GEN(b) = 0` | neutrality |
| **L**, lost scope | the block is revised and `FS_L(b) < FS_L(b⁻)` or `IS(b) < IS(b⁻)`; or it has disappeared and `FS_L(b⁻) + IS(b⁻) > 0` | (a); (b) by deletion |
| **G**, generality | see the G-rule below | (b) |
| **M**, mirror | a chapter block and its FULL mirror (§3.4) have different `FS_A`, `FS_L`, `IS` or `GEN` | (a), (b) |
| **K**, kernel scope | the census resolves, in the block's paragraph, a declaration whose type has a finiteness binder (§5.3), and `FS_A(b) = 0` or `GEN(b) > 0` | (a), (b) |
| **E**, escaped generality | in the block's proof or its post-block paragraph, the `GEN` count, or the `IS` count while `FS_A(b) > 0`, rises against `b⁻`; for a new block, is positive. `PROMO` is not read there | (b) |
| **P**, parse | a proof closes at the next label or heading without a closer; or a footnote reference has no definition | recognition |
| `scope-unclear` (advisory) | a `finit\w*` occurrence in a carrier sentence that is not a positive predication and not inside a `NEG_FINITE` or `GEN` match (§3.1) | (a) |

**The G-rule.** It reads only the local hypotheses. Generality in the proof or the post-block paragraph
is rule E's, which reads `GEN` and `IS` only. A promotion word in a proof, such as "By Theorem 3, shown
above", therefore raises nothing. The G clauses are:
- **(G1)** a new block with `GEN > 0` or `PROMO > 0`, using the new-block `PROMO` list;
- **(G2)** a new block with both `FS_A > 0` and `IS > 0`: it claims both scopes;
- **(G3)** a revised block whose `GEN` or `PROMO` count rises;
- **(G4)** a revised block whose `IS` count rises while `FS_A(b) > 0`: an infinite scope has been added
  to a finite one;
- **(G5)** any `unclassified` J10 match (§3.1). This clause is advisory.

A rise in `IS` on a block whose `FS_A` is 0 restricts the block to infinite systems. Such a narrowing
raises no G item. Neither does a rise in `FS_A`, `FS_L` or `FU`, nor any NEUTRAL match. Added
hypotheses therefore pass, whichever cardinality they state.

### 3.4 Mirrors (rule M)

`FULL.md` is segmented at its top-level headings. A `# Chapter N` or `# Appendix X` heading followed
directly by a separate `# <title>` heading (for example lines 334–335) opens one segment, not two. A
top-level heading with no file, such as `# Copyright`, is reported. Segment `# Chapter N` is paired with
`book/chNN-*.md`, `# Appendix X` with `book/appendix-x-*.md`, and `# Introduction`, `# Preface`,
`# Reader's Guide`, `# Acknowledgments`, `# Glossary` and `# Bibliography` with `ch00-introduction.md`,
`preface.md`, `readers-guide.md`, `acknowledgments.md`, `glossary.md` and `bibliography.md`. The pairing table
is frozen at enrollment, and a segment with no chapter file is reported. Inside a pair, blocks are paired
by the three steps of §2.4, applied across the two files. A block that has no mirror in a chapter that
has one raises M.

### 3.5 Review records

Every review-set member is cleared only by an entry in the review registry (§7):

```
{"member": [file, kind, digest-at-introduction], "digests": {<statement>, <proof>, <post-block>},
 "targets": [<resolved citation keys>],
 "checklist": {"finite_used": ..., "infinite_used": ..., "generality": ..., "lost_scope": ...},
 "hits": [{"rule": ..., "outcome": "justified"|"narrowed", "basis": <text>,
           "proof": <citation or null>}],
 "outcome": "accepted"|"rejected", "attestation": <per §3.6>}
```

- The digests and targets must equal the member's current ones, so a later material edit, or a retarget,
  voids the record.
- Each checklist answer is a sentence, not a flag. An empty answer is invalid.
- Every blocking hit on the member appears in `hits`. Hits of rules G, L and E need a `proof`: for G and
  E, one covering the claimed scope; for L, one establishing the result without the removed hypothesis.
  This is J10's R-resolution requirement carried over. Hits of A and I need a `basis` showing that the
  use is stated or not load-bearing, or they are answered by narrowing the statement. Hits of K need a
  `basis` naming the clause that carries the binder's content.
- Advisory hits need no entry.
- A `rejected` outcome leaves the member open.
- A record decides scope only. It does not accept the result scientifically.

### 3.6 Who may review: the attestation (owner decision O6)

Every commit, pull request and comment in this repository is made under one login, so a check that the
reviewer's login differs from the author's can never pass. The reviewer of c.7065126686 assessed what
each candidate attestation can actually verify. The assessment is recorded here for owner decision O6
(§12). The writer makes no choice.

| Option | What the attestation is | What can be verified | Assessment (c.7065126686) |
|---|---|---|---|
| **(α) Session trailer** | the record's commit carries a `Claude-Session` trailer that differs from every author commit's trailer on the member's file | only that two strings differ | Self-asserted. The session that writes the commit writes the trailer, and CI cannot resolve it. A second writer on the author's branch also conflicts with one-writer-per-branch (c.7064767045). On its own, it is resolution by assertion |
| **(β) Owner clearance** | an owner decision record names the member's digests and the record's commit | that the comment exists and names the digests; not who wrote it | Procedural. Owner records are posted from the same login, often relayed by agents. Its strength is the owner's personal confirmation. It is the only listed option that routes through the person |
| **(γ) Signed commits** | the record's commit is signed with a key from a reviewer keyring that only an owner decision changes | the key identity, cryptographically | Verifiable only if custody is separate, for example an owner-held hardware key that author sessions cannot reach. With keys on a shared agent disk it proves no more than (α). An owner-held key is (β) made cryptographic |
| **(δ) Separate reviewer account** | the review is made from a distinct GitHub account (a machine user or an app), optionally with required reviews | a distinct identity, by the host itself | The fix the reviewer proposes. It is the only option the host verifies directly. It needs a new account and its credential custody |

The reviewer's further view, recorded and not adopted: (α) alone should not suffice; (β), or (γ) with an
owner-held key, should be required for every record until (δ) exists. Whatever the owner chooses, the
check is invariant V9 (§11) with its own checkpoint. Until O6 is decided, no record can be attested, and
every pull request with a non-empty review set fails the gate.

### 3.7 Verdict

- **PASS.** Every review-set member has a valid, attested, current review record; every configuration
  control (§7) holds; the controls of §8 pass.
- **FAIL.** A member lacks a valid record; or a blocking hit on a member is unanswered; or a control
  fails; or `vocab.json` or a registry changed outside §7.
- **VOID.** A pinned #1483 blob or commit object is missing or has the wrong digest (§4). A VOID run
  prints no verdicts on members.

Advisory hits never change the verdict. The verdict text is generated from the counts.

## 4. Reuse of #1483: what, how, and its side effects

**What is reused.** From #1483's landed `compare/verdict.py`, FIN-SCOPE reuses:
- `normalize_text`, always called with the block's file text;
- `strip_allowlisted` and `ALLOWLIST`;
- the constants `FINITE_TERMS`, `INFINITY_TERMS` and `PROMOTION_TERMS`;
- the batteries `PARAPHRASES`, `EVASIONS`, `ALLOW_PLUS` and `NCASES`, used as fixtures.

`j10_hits` is not called. It normalizes without file text and so expands no footnote (review B2), and
FIN-SCOPE needs per-match spans rather than counts.

**How it is loaded.**
- FIN-SCOPE's frozen file records the #1483 merge commit, together with the blob ids and SHA-256 digests
  of `compare/verdict.py` and `baseline.py`.
- At run time a subprocess `python3 -I -B` is started in a fresh temporary directory. The directory
  reproduces the layout `compare/verdict.py` plus `baseline.py`, written from the Git objects at that
  commit and never from the working tree. The subprocess checks both digests and imports `verdict.py`.
- It serves only the listed functions and constants, over a JSON pipe. The patterns go across as their
  source strings and flags. Normalized texts go across as strings.
- `release_gate.py` never imports either module. The `sys.path.insert(0, RECORD)` and `import baseline`
  that `verdict.py` performs at import time therefore stay inside the subprocess.

**Side effects at import, as read.** This is a static read of the AST at #1483's head `1287ea60`. It is
an input to review, and it must be re-read at the landed blob.
- The module-level statements of `baseline.py`, apart from definitions and imports, are constant
  assignments and its `__main__` guard.
- `verdict.py` additionally runs `sys.path.insert` and `import baseline`, and its other module-level
  statements are constant and regex assignments.
- Neither module's import-time code reads or writes a file.

FIN-SCOPE's subprocess runs with an empty `HOME`, no network, and a working directory it discards
afterwards. This is a precondition, recorded as invariant V2.

**Precondition.** The gate job checks out with `fetch-depth: 0`, so the pinned commit object is
present. A missing object makes the run VOID.

**Unchanged.** #1483's files stay exactly as landed. A later amendment of #1483 does not move FIN-SCOPE.
Its pin moves only by its own reviewed change.

## 5. Where it runs

### 5.1 Release gate

A new `fin-scope` step in `tools/release_gate.py` runs inside the existing `verify.yml` jobs, on pull
requests and on pushes to `main`. It needs no dispatch and no new workflow. It is ordinary CI, not an
exact-head `check-run` attestation (§A.39, §A.40).

### 5.2 PR review

The tool prints the review set in screen-priority order: each member with its blocking and advisory
hits, the counts that fired them, and the matched spans. Reviewers add the review records (§3.5) with
the attestations of §3.6. A checklist line (§10) asks whether the
statement's scope matches what the proof uses, which no lexical rule can settle.

### 5.3 Lean layer (rule K)

A block *cites* a declaration when `tools/lean_manuscript_census.py`'s per-paragraph resolver, used
read-only, resolves that identifier in a paragraph of the block.

A Lean metaprogram runs in the existing Mathlib bridge job and reads only elaborated declarations. It
reports whether a declaration's type has a *finiteness binder*: an instance or hypothesis of `Finite`,
`Fintype`, `Set.Finite`, `FiniteConf` or `Substratum.A1`, or a carrier `Fin n` or
`FiniteOperationalTheory`.
- A binder supplied by an `axiom`, or by a global `instance` that has no proof, is reported separately.
  The existing `lean-axioms` step fails it.
- Whether rule K comes in the first implementation is owner decision O5.

## 6. Reference record, claim surfaces, baseline

### 6.1 Reference

The reference record is `baseline.json` together with the resolved entries of the registry. For each
block it holds the digest and the counts `FS_A`, `FS_L`, `IS`, `GEN` and `PROMO` at the block's last
enrolled or resolved version.
- A pull request that changes a block replaces the block's reference entry in the same commit.
- The gate recomputes the replaced entry's counts from the merge base's text. A replaced entry whose
  counts differ from the recomputed ones fails the gate, so a before-version cannot be rewritten to hide
  a loss.

### 6.2 Claim surfaces and prose

On claim surfaces (§2.1), a sentence or table row is paired with its before-version as follows:
- by exact masked text;
- otherwise by the highest token-Jaccard similarity of at least 0.6, within the same section and the
  same table;
- a sentence with no partner is new.

A changed sentence or row on a claim surface is a review-set member (R-d). The screen runs rules G
(read as for blocks) and L (`FS_L` and `IS` loss) on it, and their hits are blocking. Changed prose
elsewhere that is neither a proof nor a post-block paragraph is outside the review set. The screen
lists its G and L hits as advisory, unless owner decision O3 brings such prose into the review set.

### 6.3 Baseline enrollment

After D1 and D2, one enrollment commit evaluates every block and claim surface on `main`. It records each
digest and its counts in `baseline.json`, and each item that fires in a published list of *baseline
items*.
- Unchanged blocks are not in any review set, so a baseline item does not fail the gate while its
  digest and targets stand. When its block next changes, the block joins a review set and the hit
  becomes blocking.
- Enrollment records a baseline item. It does not review or accept it.
- How long a baseline item may stand is owner decision O4.

## 7. Files and configuration control

The proposed home is `verification/infrastructure/fin-scope/` (§A.36). It holds:
- `fin_scope.py`, the checker, with `--self-test`;
- `vocab.json`: the classes of §3.1, the carrier and neutral lists, the 0.6 threshold and the #1483 pin;
- `baseline.json`;
- `reviews.json`, the review registry of §3.5;
- `canonical.json`, the canonical-definition map of §2.5.

Each run checks four configuration controls:
- **The allowlist.** It is #1483's, read from the pinned blob, and FIN-SCOPE has none of its own. A new
  allowlisted sentence needs an owner decision and a pin move to a #1483 successor that carries the
  sentence.
- **Narrowing `vocab.json`.** A commit that removes or narrows a pattern, or adds a neutral context,
  fails. It passes only when the same commit adds a case showing that the removed pattern's TESTS cases
  are still caught, or cites an owner decision.
- **The canonical-definition map.** A change to `canonical.json` (a new name, a new copy, a moved anchor
  or a new canonical designation) needs its own review record. A change that leaves a whitelisted name
  without a canonical definition fails.
- **Append-only registries.** `reviews.json` and `baseline.json` are append-only, apart from the
  reference replacement of §6.1. The gate compares each with its blob at the merge base.
- **The fixture inventory.** The `TESTS.md` case list is pinned by digest. A changed expected verdict
  is a reviewed revision made before the run.

## 8. Controls

- **C-R1, load integrity.** This control reproduces the blob's own definitions, so it is not an
  independent control.
  - The subprocess exposes every named object.
  - Each constant equals the literal parsed independently by `ast.literal_eval` from the pinned blob,
    without executing it.
  - Each regex's pattern string and flags match the blob's source.
- **C-R2, pin.** A wrong digest, or a missing commit object, makes the run VOID.
- **C-R3, independent normalization control.** `TESTS.md` §5 fixes, before implementation, the expected
  normalized output of each listed input string. These are written by hand, not derived from the blob.
  The inputs cover a soft hyphen, `\-`, a Cyrillic letter, `ℵ`, an HTML entity, a footnote expanded
  with file text, `\mathcal{S}` and `\lvert S\rvert`. Any mismatch fails the run.
- **C-R4, independent recall control.** Every `PARAPHRASES`, `EVASIONS` and `ALLOW_PLUS` case, inserted
  into FIN-SCOPE's own finite-scoped fixture block (`TESTS.md` §1.3, F1), must raise the screen hit its
  `TESTS.md` §1.4 row states: a blocking G for every row but one, and the advisory G5 for row 42. The expected
  verdicts are FIN-SCOPE's own and are stated per case. The footnote case `[^gen]` carries its
  definition in the fixture file.
- **Mutants.** Each mutant must make the self-test fail on its named target case, and it counts as
  caught only through `tools/mutant_verdict.py`.

  | Mutant | Target case |
  |---|---|
  | rule A off | P-A1 |
  | `FU` emptied | P-A2 |
  | FU's transitive clause off | P-A10 |
  | `NEG_FINITE` exclusion from FS off | P-A12 |
  | allowlist strip after counting | P-A7 |
  | carrier-sentence condition of `FS_A` off | P-A9 |
  | rule L off | P-L1 |
  | the disappearance clause of L off | P-L4b |
  | digest-first matching off | N16 (renumbering) |
  | G1 off | P-G1 |
  | G4 off | P-G2 |
  | G5 output off (advisory list empty) | P-G11 |
  | the NEUTRAL context check off | N14e, N15 |
  | rule I off | P-I1 |
  | rule M off | P-M1 |
  | the record digest check off | P-R2 |
  | the review-set membership check off (screen-clean members pass without a record) | P-S1 |
  | the dependency closure off | P-D2 |
  | the resolved-target comparison off | P-D1 |
  | the proofless extent widened to the next label | P-B3 |
  | rule E off in proofs | P-E1 |
  | rule E off in post-block paragraphs | P-E2 |
  | G5 made blocking | N22, N25 |
  | the hypothesis digest off | P-H1 |
  | standing scope sentences not cited implicitly | P-H2 |
  | the proof-opener search limited to the first paragraph | P-C2 |
  | interposed prose counted in the local hypotheses | P-C3 |
  | cross-file names resolved only within the citing file | P-H4 |
  | deleted scoped blocks not members | P-L4b |
  | the (r1) map limit off | P-R9 |
  | a change to a copy reaching only that copy's own citers | P-H8 |
  | copy recognition limited to the parenthesised form | P-H11, P-H12, P-H15 |
  | copies decided by form instead of by the register | P-H16, P-H17 |
  | unclassified occurrences ignored | P-H18 |
  | classification not voided by a change | P-H19 |
  | headings not occurrence units | P-H20 |
  | lists classified item by item without their lead-in | P-H21 |
  | the matcher run on unnormalized text | P-H22 |
  | the exact-copy identity check off | P-F1, P-F4 |
  | equivalence attestation not voided by a canonical change | P-F2 |
  | a new different formulation not blocking | P-F3 |
  | the glossary not a surface | P-H13 |
  | deleted-block membership filtered by `FS_L + IS > 0` | P-L4c |
  | range citations not expanded | P-H6 |
  | the coverage check (V27) off | P-O3 |
  | the (r2) resolved-target equality off | P-O4 |
  | the attestation check off | P-R1 |
  | the reference-count recomputation off | P-R6 |

  Mutants run only in CI (§A.40), after the live controls and every unmodified check have passed.
- **Negative controls.** Every N-case of `TESTS.md` must produce no blocking hit, and must PASS with a
  plain review record (TESTS conventions).

## 9. How it avoids requiring finiteness

- **No rule fires on absence alone.** Rule A needs finite use. A block with no `FU`, no `IU` and no
  generality produces no item (N3, N4).
- **Symmetry.** Rules A and I mirror each other, and rule L treats a lost infinite restriction as it
  treats a lost finite one.
- **Narrowing is free in both directions.** Adding a hypothesis, finite or infinite, raises no G item.
  That covers `Let $S$ be finite`, `Let $S$ be countably infinite`, `(the finiteness hypothesis)` and a
  uniform prior on a stated finite set (N14a–e). A new theorem restricted to infinite systems produces
  no item, exactly like a finite-only theorem (N6 against N1).
- **G is about widening.** G reads only the local hypotheses, counts only cardinality generality and
  status promotion, and leaves ordinary quantifiers over elements alone (N15). A G item is cleared by a
  covering proof. It is not presumed false.
- **The allowlist.** It is removed before every count, so the owner's sentence neither triggers an item
  nor supplies finite scope (P-A7, N5–N5d).
- **The burden that remains.** Rule I and the `maximum`/`compact` part of rule A raise blocking hits on
  some correct results, for example a maximum on a compact space. These are a review burden, not a
  finiteness requirement: each is answered by a `basis` (§3.5). The J10 backstop is advisory, so it
  cannot fail a correct statement (R4).

### The screen's limits

The screen is lexical and cannot be complete. Its known escape classes are listed here. For a change
inside the review set, they do not weaken the guarantee of §1.1, because every member is reviewed
whether or not the screen fires; they weaken only the prioritisation and the pointing.

**Changes outside the review set do weaken the guarantee.** Such a change alters what a reviewed
statement means, or adds a claim, without any record. The known classes are:
- prose beyond the first post-block paragraph, outside the claim surfaces (X-10), and theorems stated in
  unlabelled prose there (X-3). A generality claim can be made there with no reviewer;
- scope fixed by text that is neither a block, a hypothesis node (§2.5) nor a standing scope sentence,
  for example a notation convention in another chapter ("$S$ denotes a finite set") that statements rely
  on without citing it. Changing that text changes their scope with no reviewer;
- external sources cited by a proof (X-6). A finite-only result outside the corpus is not a node;
- a `**Definition**` used through the term it defines rather than cited by its label. The changed
  definition is a member, and the blocks that use the term are not (X-11);
- Lean declarations that the census does not resolve beside a block (§5.3). A changed binder there
  reaches no reviewer through FIN-SCOPE;
- a block the grammar fails to recognize, until the enrollment inventory check (V12) reports its form;
- baseline items whose blocks never change (§6.3). They stay unreviewed.

Each class is a place where the guarantee holds only through ordinary pull-request review.

- **Negation.** `FS_A` counts only positive predications, which fails closed for most negations (R1).
  A negation outside the form still escapes. Examples are "Let $S$ be finite, though this is not
  needed" and a hypothesis withdrawn in a later sentence of the statement (X-9).
- **Proofs and prose.** Rule E reads `GEN` and `IS` in the proof and the post-block paragraph. It does
  not read `PROMO` there, nor any paragraph after the first. A generality claim made two paragraphs
  later, or in an unlabelled section, is covered only when it sits on a claim surface or in a review-set
  member (X-3, X-10).
- **Symbols and carriers.** A carrier outside the list and undeclared in the local hypotheses, such as a
  lattice configuration set written `$Q^\Lambda$` with no declaration, escapes `FS_A` and the carrier
  quantifier (R5, X-8).
- **Subscripted forms of a condition.** The frozen exclusion of `C_1`, `C_{k}` and `C^1` is right for the
  corpus as read: those symbols are the quadratic Casimir `C_2` and the cyclic group `C_4`. A future
  author who writes a condition as `$C_1$` would escape the register. The screen reports a subscripted
  `C_1`–`C_4` that stands within the same sentence as a condition word (coupling, persistence, capacity,
  readback) as an advisory hit, which only points a reviewer at it.
- **Misclassification with unchanged text.** A real copy classified as a citation or as unrelated, not
  led by a name, outside the second-review sample, and unchanged, stays undetected until its text
  changes (§2.5).
- **Unnamed references to a mapped condition.** A paragraph that relies on a condition without naming
  it, by label or by a frozen alias, is not an occurrence, so it is outside the register (§2.5). An
  example is "the coupling condition". Adding the phrase as an alias brings it in.
- **Wording.** A finite use worded without a listed term escapes rule A, for example "each
  configuration is visited before any repeats" (X-2).
- **Wrong object.** A positive predication about one declared carrier satisfies `FS_A` while the finite
  use ranges over another. An example is "Let $T$ be a finite set of times", with pigeonhole on $S$
  (X-1).
- **Admitted false positives.** These are blocking hits on correct results, answered by a `basis`:
  - `bounded` and `compact` are not in `FS_A`, so a maximum on a compact space raises A (X-5);
  - an `FU` term that ranges over an object whose finiteness is stated outside the local hypotheses
    raises A, for example a trace on a Hilbert space declared finite-dimensional in an earlier
    Setting that the statement does not cite (X-7).
- **Citation chains.** The dependency closure and the transitive clauses follow only parsed blocks. A
  finite-only result cited from outside the corpus is not followed (X-6).
- **Sufficiency.** FIN-SCOPE never decides whether a hypothesis suffices. Under c.7061660930 that is
  the task of independent mathematical review, which checklist items 1–4 carry.

## 10. Proposed governance text

This is a proposal only, and it is not applied before the A1 retirement lands. For a new AGENTS.md
section, numbered at landing:

> **FIN-SCOPE: scope of finiteness claims.** Every theorem states the cardinality scope it uses. A
> result that uses finiteness of a configuration space states that finiteness as a local hypothesis; a
> result claimed for infinite systems, or for systems of every cardinality, cites a proof that covers
> that scope. Neither finiteness nor infiniteness is assumed globally, and adding a hypothesis of either
> kind is always permitted. The release gate's `fin-scope` step checks new and revised statement blocks
> and claim surfaces against these requirements. Every new or revised statement block, every block
> citing one whose scope changed, and every changed proof or post-block paragraph is reviewed against a
> fixed checklist by a reviewer other than its author, attested as the owner has fixed. The step's
> lexical screen prioritises that review and never replaces it. A generality or lost-scope hit is
> answered with the covering proof. Whether a stated hypothesis suffices is decided by that review,
> not by the screen. The vocabularies and the allowlist change only under the step's
> configuration controls.

For the Code Review Rules, under *Claim/evidence boundary*:

> - For each new or revised theorem statement, check that its cardinality scope matches what its proof
>   uses: finiteness the proof needs, directly or through a cited lemma, is stated locally, and a claim
>   for infinite or arbitrary configuration spaces has a proof that covers it (FIN-SCOPE).

## 11. Invariant → checkpoint table (§A.41)

| ID | Invariant asserted | Checkpoint |
|---|---|---|
| V1 | #1483 code is read only from the pinned Git objects, never from the working tree | C-R2 (digest of the bytes actually loaded); P-R7 |
| V2 | importing #1483 has no effect outside the subprocess | the subprocess runs with `-I -B`, an empty `HOME` and a discarded working directory; a self-test case checks that `sys.modules` of the gate process holds no `baseline` or `verdict` after the run |
| V3 | #1483's files are unchanged by FIN-SCOPE | the gate compares the blobs of #1483's record directory at HEAD with the pinned ids, and fails on a difference unless a #1483 amendment that landed separately moved them |
| V4 | the allowlist neither triggers an item nor supplies scope | P-A7, N5–N5d; the strip-after-count mutant |
| V5 | no rule fires on absence alone | N3, N4, N6; rule A's definition requires `FU > 0` |
| V6 | adding a hypothesis of either cardinality raises no G | N14a–e; the NEUTRAL-check mutant |
| V7 | a later material edit, or a retarget, voids a review record | P-R2, P-D1; the digest-check and target mutants |
| V8 | the reference counts cannot be rewritten | P-R6; the recomputation mutant |
| V9 | a review record carries the attestation fixed by O6 | P-R1, P-R3; the attestation-check mutant |
| V10 | the registries are append-only | P-R8 (merge-base blob comparison) |
| V11 | renumbering raises no item | N16; the digest-first mutant |
| V12 | every corpus label form is recognized | the enrollment inventory check (§2.3); P-B1 |
| V13 | J10's recall set is not narrowed silently | G5; P-G11; the `vocab.json` control (§7) |
| V14 | every review-set member has a current, attested record, whatever the screen says | P-S1; the membership mutant |
| V15 | a change of a cited block's scope puts its dependents in the review set | P-D2; the closure mutant |
| V16 | a proofless block is its label paragraph and its continuation paragraphs only | P-B3, N28; the extent mutant |
| V17 | the J10 backstop never blocks | N22, N25; the G5-blocking mutant |
| V18 | generality in a proof or post-block paragraph is screened and reviewed | P-E1, P-E2; the rule-E mutants |
| V19 | a changed hypothesis node puts itself and every citing block in the review set | P-H1, P-H2; the hypothesis-digest mutant |
| V20 | a proof after a multi-paragraph statement is recognized, and interposed prose supplies no scope | P-C2, P-C3, N29; the opener-search and interposed-prose mutants; the enrollment inventory re-derives the 29 cases of c.7065227255 |
| V21 | a batched record (r1) covers only exact instances of a scope-neutral map | P-R9, P-R10, N31; the instance-check and map-limit mutants (if r1 is adopted) |
| V22 | named conditions resolve corpus-wide, and ambiguity fails closed | P-H4, P-H5; the cross-file-resolution mutant |
| V23 | every deleted block is a member, unconditionally, with its scope obligations carried into its record | P-L4b, P-L4c, P-O1; the deleted-member mutant |
| V24 | a reduced (r3) record answers items 1, 2 and 4 | P-R11 (if r3 is adopted) |
| V25 | every mapped name resolves to exactly one node group, and a change to any node of a group, in any form, reaches every citer of the group | P-H4, P-H6–P-H8, P-H11–P-H13, P-H15; the group-closure and form mutants |
| V26 | every occurrence unit (paragraph, whole list, whole table, heading with its section) of a mapped name has a current recorded classification; an unclassified, new or changed occurrence, or an unresolved anchor, fails | P-H9, P-H10, P-H14, P-H18–P-H22 |
| V30 | each copy's fidelity holds: exact copies stay identical (checked mechanically), equivalent copies carry a current attestation, and every different formulation blocks until it is resolved by one of the three routes | P-F1–P-F5, N34 |
| V31 | pending blocks the gate and enrollment, and baseline tolerance never covers occurrences | P-GV1 |
| V32 | ambiguous and incorrectly mapped entries fail closed | P-A1m–P-A5m |
| V33 | name-led citation or unrelated classes need two agreeing classifiers; other enrollment classes are sampled | P-S2, P-S3 |
| V34 | a prose citer outside blocks is a member when its condition changes | P-P1 |
| V27 | no reduction silently excludes a theorem: the union of covered keys equals the review set | P-O1, P-O3; the coverage mutant |
| V28 | a mathematically equivalent but not mechanically identical change is never batched | P-O2, P-O5 |
| V29 | (r2) needs identical text, hypothesis digests and resolved targets | P-O4 |

## 12. Owner decisions needed

- **O1.** Approve this design for independent re-review, and the proposed home (§7). Confirm the
  reading of c.7061660930's "the relevant #1483 checks are reused as a standing release gate": the gate
  is the mandatory review requirement of §1.1, with #1483's normalization and vocabularies reused in the
  screen, and its J10 rule advisory rather than blocking.
- **O2.** What happens if #1483 does not land on `main`. Neither branch has accepted review status for
  the reused code, so both branches need FIN-SCOPE's own review of that code.
  - (i) *Pin the last reviewed #1483 head.* That commit is not on `main`. Under §A.42 item 8 it would
    then be required evidence for the gate's standing claim, to be retained on `main` with a manifest.
  - (ii) *Vendor the reused constants and functions* into FIN-SCOPE, with provenance digests. This
    contradicts §4's "without duplication", and it needs a digest-parity control against the source
    blob for as long as that blob exists.

  The writer's view is that FIN-SCOPE should wait for D2, and that O2 arises only if #1483 is
  withdrawn.
- **O3.** Whether changed prose outside the claim surfaces, proofs and post-block paragraphs joins the
  review set (§6.2).
- **O4.** Whether baseline items may stand indefinitely or must be cleared, and by what process.
- **O5.** Whether rule K is in the first implementation or follows #1482.
- **O6.** The attestation for review records (§3.6): (α) session trailer, (β) owner clearance, (γ)
  signed commits with separately held keys, (δ) a separate reviewer account, or a combination. The
  reviewer's assessment of what each verifies is recorded in §3.6, and the writer proposes no choice.
  Until O6 is decided, no record can be attested.
- **O8.** The owner's longer-term recommendation (c.7065520418): after the A1 retirement, establish one
  canonical definition for each foundational condition, with other locations referring to it wherever
  practical. FIN-SCOPE's reconciliation list (§2.5) is the input to that work. This design does not
  schedule it.
- **O7. Decided by the owner (#1169 c.7065358283).**
  - About 130–250 review items a week is approved *provisionally*, as a design target. It is not a
    guarantee about staffing or throughput.
  - The actual cost is reviewed after deployment.
  - The reductions are approved only under the owner's conditions, which §12.1 carries.
  - No reduction may silently exclude a theorem from review.
  - Three items are blocking before acceptance, each with adversarial regression tests (TESTS §2.3) and
    independent confirmation:
    - corpus-wide named-condition dependencies (§2.5);
    - deleted theorems keeping their scope obligations (§1.1, R-a);
    - individual review of any transformation that affects finiteness, infinite-system assumptions,
      mathematical carriers or theorem scope (§12.1, r1).
  - The checker is not implemented, `AGENTS.md` is not modified, and FIN-SCOPE is not merged, until the
    A1 retirement is complete.

### 12.1 The cost of O7

**Counting conventions.** A revised block can be counted in two ways:
- **paired**: each revised block counts once, as one member. This is the convention of this
  specification, because §2.4's pairing makes a revised block a single member;
- **split**: each revision counts as one disappearance plus one new block, roughly doubling the count.

**Measurements.** All are approximate R-a counts of changed labelled blocks in the first-parent history
of `main` touching `papers/` or `book/`, from 2026-11-11 to 2026-11-21. Each used an ad hoc paragraph
parser approximating §2.2. They are design inputs, not FIN-SCOPE measurements.

| Count | Convention | Block changes | Largest PR (the #1475 propagation sweep) |
|---|---|---|---|
| reviewer, two independent parsers (c.7065227255, c.7065296420) | paired | about 170, in 28 commits | 63–64 |
| reviewer, same window | split | 338 | 127 |
| writer (c.7065264934) | mixed: pairs some revisions, splits others | 242 | 77 |

The paired figure, **about 170 in eleven days**, is the one that matches this specification. All counts
already include `FULL.md` and the chapter files, so mirrors are not multiplied again. The window was
the A1-EXIT propagation period, busier than usual, and the counts are re-measured at enrollment.

**Expected load, paired.**
- **R-a alone:** about 110 members a week.
- **With the closure (R-b), hypothesis nodes (R-e), proofs and post-block paragraphs (R-c), claim
  surfaces (R-d) and deleted scoped blocks:** about **130–250 members a week**.
- **Per PR:** a typical PR has a handful. One PR in five has 10–20. A propagation sweep or a renaming
  like #1482's has about 60–130.

Each member needs a record with sentence answers and an attestation: an owner clearance per member or
per batch under (β), or a separate reviewer identity under (δ).

**Reductions, under the owner's O7 conditions (c.7065358283).** Every reduction is bound by one
coverage rule: **no reduction may silently exclude a theorem from review**. Each reduced record lists
every member it covers by key and digest. The gate checks that the union of the keys covered by records,
reduced or not, equals the review set. A member that no record names fails (V27).

- **(r1) Batched records, only for substitutions that are mechanically identical and independently
  verified not to change mathematical scope.**
  - The PR declares a frozen substitution map. The tool checks that each member's diff is exactly an
    instance of the map, token for token. This is mechanical identity.
  - **Limit.** Neither side of any map entry may contain a token of a screen class (`FINITE_TERMS`,
    `FS_A` forms, `NEG_FINITE`, `IS`, `GEN`, `PROMO`, `FU`, `IU`, J10's vocabularies), a carrier symbol
    or a carrier noun. No member's screen counts, hypothesis digest or resolved targets may change under
    the map. A map that fails the limit is refused for batching, and every member needs its own record.
    So any transformation that touches finiteness, infinite-system assumptions, carriers or theorem scope
    is reviewed member by member.
  - **Independent verification of scope neutrality.** The batched record is a review record by a
    non-author, with an attestation under O6. It answers one question for the map itself: can this
    substitution change the mathematical scope of any statement at any of its sites? The answer is
    recorded per map entry. The mechanical checks of the limit are necessary for batching, and this
    record is required as well.
  - The record lists every covered member. A member whose diff is not an exact instance falls back to its
    own record.
- **(r2) One record per mirror pair, only when the text and the resolved hypothesis dependencies are both
  identical.** The masked texts must be byte-identical. The hypothesis digests and the resolved citation
  targets must be equal, since `FULL.md` and the chapter may resolve different nodes. The control is
  equality of all three. Otherwise two records are needed.
- **(r3) A reduced checklist for closure members whose own text is unchanged**, only if it still checks
  three things, against the changed lemma or node:
  - finite assumptions: item 1;
  - infinite assumptions: item 2;
  - the effect of the changed dependency: whether this block relies on what changed, and whether its own
    scope is lost, widened or narrowed by it. This is item 4, extended for dependents.

  Item 2 is needed because a cited lemma narrowed to infinite systems changes what its dependents rely
  on.
- **(r4) One owner attestation per PR under (β), covering an explicit, individually reviewable set of
  findings.**
  - The attestation names every member's key, digests and record, and every blocking hit with its
    answer.
  - It attests records that already exist and that each answer their checklist. It replaces none of
    them, and it is never automatic acceptance.
  - A member, record or finding that the attestation omits is not attested, and the gate fails on it.
  - Its risk is stated plainly: a single action over a hundred findings invites approval without
    reading. It keeps the guarantee only as well as the owner reads.

**Reductions that would weaken the guarantee.** These are listed for completeness and not proposed:
- exempting screen-clean members;
- sampling;
- exempting punctuation-only or "editorial" changes. A deleted qualifier or a flipped operator is a
  scope change (#1483 NCASES).

**Trade-off.** The guarantee costs one attested review record per member, about 130–250 a week on the
measured window. With (r1)–(r4), a typical PR needs a handful of records. A sweep needs one per member
whose change carries scope, plus one per scope-neutral map. Making it cheaper still means reviewing
less, which reopens the escapes R1–R5 for the unreviewed changes. The owner has accepted the load
provisionally, with the reductions under the conditions above, and the actual cost is to be reviewed
after deployment (O7).

## 13. Result classification

This record proves no theorem, so it holds no result of class (N), proved from OI's native assumptions,
and none of class (I), conditional on imported quantum or operational assumptions. It adopts no physical
assumption. FIN-SCOPE checks the stated scope of a result; it does not classify results on that axis, and
a FIN-SCOPE pass is not evidence for either class.

## 14. Response to review c.7064941939

| Finding | Where addressed |
|---|---|
| B1 | §3.1 (classes, carriers, NEUTRAL, J10 as recall set), §3.3 G-rule (G1–G5; local hypotheses only, proof not read), §9; TESTS N14a–e, P-G2 |
| B2 | §4 (`j10_hits` not called; file text always passed), §8 C-R1 relabelled as load integrity, C-R3 and C-R4 added |
| B3 | TESTS N6, N2b, P-A5, N12, N13 rewritten; each expected verdict is derived from §3 in the case's "why" column |
| B4 | `NEG_FINITE` (§3.1) excluded from FS and counted in GEN; carrier quantifier replaces bare quantifiers; TESTS P-A12, N15 |
| B5 | `FU` widened, transitive clause, `FS_A` without bounded/compact and with the carrier-sentence condition; §9 Known limits; TESTS P-A9–P-A11, X-1, X-5, X-6 |
| B6 | §2.2 grammar, §2.3 inventory, §2.4 masked digests and content matching; TESTS P-B1, N16–N18 |
| B7 | §3.6 options (α)–(δ), O6, V9 |
| N-a | IU narrowed (§3.1); TESTS N19–N21 |
| N-b | §9 |
| N-c | §4 subprocess, side-effect read, `fetch-depth: 0` precondition; V2 |
| N-d | §12 O2 |
| N-e | Remark and Prediction in the grammar; claim surfaces gating (§6.2) |
| N-f | §3.4 |
| N-g | §5.3 |
| N-h | §11 |
| N-i | §3.1 LaTeX pre-normalization; TESTS N5d |
| N-j | `'` in the grammar's `ID`; TESTS P-L4 |

**Delta review c.7065126686.**

| Finding | Where addressed |
|---|---|
| Structure | §1.1: the guarantee is mandatory, attested review of the review set; the lexical rules are a screen |
| R1 | §3.1 `FS_A` counts positive predications only, with the advisory `scope-unclear`; §9 limit; TESTS P-N1–P-N4, X-9 |
| R2 | §2.2 statement extent (label paragraph plus continuation paragraphs), post-block paragraph, bold proof openers; TESTS P-B3, N28 |
| R3 | §2.4 resolved citation targets; §1.1 (R-b) dependency closure; §3.3 screen runs on the closure; TESTS P-D1, P-D2 |
| R4 | §3.1 the J10 backstop is advisory; `#ref` masking without the kind word; new-block promotion words and `cardinality` with a number are neutral; `\mathbb N` is IS only where it indexes a carrier; TESTS N22–N25 |
| R5 | §3.1 declared-symbol carriers and `finite-dimensional`; §9 admitted classes; TESTS N26, N27, X-7, X-8 |
| Proof and post-proof escapes | §3.3 rule E; §1.1 (R-c); TESTS P-E1, P-E2 |
| O6 | §3.6 options (α)–(δ) with the reviewer's assessment; §12 O6 |
| TESTS | row 39 by the first-math-expression definition; row 43 G3 with an advisory G5; N7 rewritten with correct hypotheses |

**Delta review c.7065227255.**

| Finding | Where addressed |
|---|---|
| C1 | §2.5 hypothesis nodes; §2.4 hypothesis digest; §1.1 (R-e) and (R-b); TESTS P-H1–P-H3 |
| C2 | §2.2 extent for blocks with a proof, interposed prose, clause-marker continuations; V20; TESTS P-C2, P-C3, N29 |
| C3 | §12.1 measurements, expected load, reductions (r1)–(r4), the trade-off; TESTS P-D3, P-R9 |
| §9 overstatement | §9 "Changes outside the review set do weaken the guarantee" |
| O1 reading | §12 O1 |
| §14 nit | B7 row |
| TESTS nits | N24 (neutral span, §3.1), N25 (merged spans, §3.1) |

**Delta review c.7065296420.**

| Finding | Where addressed |
|---|---|
| C1 across files | §2.5 corpus-wide dependency index, mirror nodes, fail-closed ambiguity; V22; TESTS P-H4, P-H5 |
| Definitions cited by term | §9 limit; TESTS X-11 |
| R1, deleted blocks | §1.1 (R-a); V23; TESTS P-L4b |
| C3 cost | §12.1 conventions (paired, split), reconciled counts, about 130–250 a week with no second mirror factor, the busy-window caveat |
| (r1) limit | §12.1; V21; TESTS P-R9 (refused for batching), P-R10, N31 |
| (r2) hypothesis digests | §12.1 |
| (r3) item 2 | §12.1; V24; TESTS P-R11 |
| (r4) risk | §12.1 |

**Delta review c.7065333755.**

| Finding | Where addressed |
|---|---|
| Canonical-definition map | §2.5 (i): one canonical definition per name; copies (mirror, restatement, application) form one node group; divergence goes to review |
| Range and inline citations | §2.5, citation forms |
| Worked examples | §2.5 table: (C1), (C2), H-BD and (EM), with file:line, read-only at `df6da1c6`; each resolves to one group |
| Maintenance | §2.5, maintenance when a definition moves; §7 map control; V26 |
| TESTS | P-H4 rebased; P-H6–P-H10 and N32 added; P-H5 kept for names outside the map |

**Owner decision O7 (c.7065358283).**

| Point | Where carried |
|---|---|
| Provisional load, cost reviewed after deployment | §12 O7; §12.1 trade-off |
| r1–r4 conditions | §12.1 |
| No silent exclusion | §12.1 coverage rule; V27 |
| Blocking items with adversarial tests | §12 O7; TESTS §2.3 |
| Clean lexical result is not review; mechanical identity is not equivalence | §1.1 |

**Delta review c.7065410306.**

| Finding | Where addressed |
|---|---|
| Copy recognition | §2.5 node forms keyed to the name: unparenthesised, bold, list-item, table-row and run-in forms; V26 |
| Glossary and other mirrored book files | §2.1 surfaces; §3.4 segment pairing |
| Full copy groups | §2.5 worked groups: (C1) 14, (C2) 14, (C3) 14, (C4) 9, H-BD 3, (EM) 1, with file:line |
| Deleted theorems | §1.1 (R-a): every deleted block is a member, with its scope obligations carried; V23 |
| TESTS | P-H11–P-H15, P-L4c |

**Delta review c.7065459234.**

| Finding | Where addressed |
|---|---|
| Plain list items and prose openers | §2.5 occurrence register: every mention classified (canonical, copy, citation, unrelated) by a recorded review; unclassified, new or changed occurrences fail (V26) |
| Groups re-derived | §2.5: proposed groups (C1) 26–29, (C2) 26–32, (C3) 26–30, (C4) 15–18, H-BD 3, (EM) 1, including ch18:67–70/FULL:4798–4801 |
| FULL segmentation | §3.4 |
| TESTS | P-H16–P-H19, N33 |

**Review c.7065519776 (CONFIRMED WITH NITS) and owner criterion 5 (c.7065520418).**

| Point | Where addressed |
|---|---|
| Nit 1, headings (the condition on owner item 1) | §2.5 units: a heading with its section; V26; TESTS P-H20 |
| Nit 2, whole lists and tables | §2.5 units; TESTS P-H21 |
| Nit 3, matcher input and exclusion | §2.5 matcher's input (#1483 normalization, LaTeX pre-normalization, unwrapping); the subscript exclusion with its reason; TESTS P-H22, N35 |
| Nit 4, upper ends | §2.5: estimates, not maxima |
| O6 dependency of enrollment | §2.5 who classifies |
| Owner criterion 5: exact, equivalent, different | §2.5 fidelity; V30; TESTS P-F1–P-F4, N34 |
| Designated reviewer for pending openers | §2.5 who classifies |
| Longer-term recommendation (one canonical definition, others referring) | recorded in §12, O8 |

**Addendum c.7065535973 (the owner's five criteria).**

| Criterion | Where addressed |
|---|---|
| 1 Coverage | §2.5 units (headings, whole lists and tables with a named lead-in or header), the matcher's input, the subscript exclusion with its reason |
| 2 Governance | §2.5 the FIN-SCOPE classifier role; pending blocks the gate and enrollment; no baseline tolerance for occurrences; V31; TESTS P-GV1 |
| 3 Controls | §2.5 ambiguity and mapping checks, two classifiers for name-led citation or unrelated classes, the second-review sample; V32, V33; §9 limit; TESTS P-A1m–P-A5m, P-S2, P-S3 |
| 4 Propagation | §1.1 (R-b): prose citers anywhere; V34; TESTS P-P1 |
| F1 (c.7065581514), exact means the whole canonical text | §2.5 exact; TESTS P-F6 |
| Nits C1-a, C2-a (c.7065581514) | §9 subscripted forms; §2.5 two classifiers verifiable only under (δ), (γ) with separate keys, or (β) with owner designation |
| 5 Semantic consistency | §2.5 fidelity for every copy; `different` blocking, with three resolution routes; the ch01-table finding recorded as found; V30; TESTS P-F5 |
