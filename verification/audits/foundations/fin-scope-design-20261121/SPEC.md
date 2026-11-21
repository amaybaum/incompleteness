# FIN-SCOPE: design specification

**Status.** Writer's design, revision 2, WIP / UNVERIFIED. This is a plan only. No checker exists and
nothing has been run, so no verdict below is a measurement. The corpus inventory in §2.3 is a read-only
`grep` count. Independent non-author review is required before any implementation is proposed.
Implementation, the governance change and any merge each need a separate owner decision. Revision 2
answers review c.7064941939 (B1–B7, N-a–N-j). The map from findings to sections is in §14.

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
sufficiency. Every item it raises goes to a review, and only a review clears it (§3.5).

## 2. Scope and block recognition

### 2.1 Surfaces

| Surface | Units | Mode |
|---|---|---|
| `papers/*.md` | statement blocks (§2.2) | gate (§5.1) |
| `book/ch*.md`, `book/appendix-*.md`, `book/The-Incompleteness-of-Observation-FULL.md` | statement blocks; mirror pairs (§3.4, rule M) | gate |
| Lean declarations that the census resolves in a block's paragraph (§5.3) | declarations | gate |
| *Claim surfaces* outside blocks: abstracts, sections titled Conclusion(s) or Summary, and Markdown table rows | sentences and table rows | gate (§6.2) |
| other manuscript prose outside blocks | sentences | PR layer, advisory (§6.2; §12, O3) |

The following are out of scope:
- `verification/` records, which are kept by `G13` and by the `legacy-records` step;
- Git history and frozen records;
- generated `.tex` and `.pdf` files.

### 2.2 Block grammar

A *statement block* starts at a *label* and ends at the next label, at a heading of the same or a higher
level, or at the end of its proof, whichever comes first. A label is any of:

- a bold opener at the start of a paragraph: `**K[ ID][ (TITLE)][.|:]**`, where:
  - `K` is one of `Theorem`, `Lemma`, `Proposition`, `Corollary`, `Claim`, `Remark` or `Prediction`;
  - `ID` matches `[A-Z]?\.?\d+(\.\d+)*[a-z]?'*` (for example `24`, `A.3`, `B.2.1`, `5b`, `9'`), or is
    absent;
  - `TITLE` is any parenthetical. The closing `.` or `:` may stand inside or outside the parenthesis;
- `**Theorem statement.**`;
- a heading `#{2,4} K[ ID][ (TITLE)]`, with `K` and `ID` as above.

A block has three parts:
- **Statement.** From the label to the proof opener, or to the block's end if it has no proof.
- **Local hypotheses.** The statement, together with the text of each hypothesis or setting label the
  statement cites, for example `(F)`, `(H2)` or `Setting 3`, defined in the same file. A label defined in
  another file counts only when the statement cites it with its file.
- **Proof.** It opens with `*Proof*`, or with `*Proof` followed by any words or a parenthetical and then
  `.*`; this covers *Proof sketch.*, *Proof outline.*, *Proof structure.*, *Proof setup.*, *Proof of X.*
  and *Proof (construction).*. It closes at the first `$\square$`, `∎`, `\qed` or `$\blacksquare$`.
  A proof that reaches the block's end without a closer is closed there, and the run records a *parse
  note* (§3.3, rule P).

Remarks and Predictions have no proof part. The rules read only their statement.

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
  Definition|§|Eq\.?|Equation|Section|Chapter|Appendix) ID` is replaced by `K #`;
- whitespace is collapsed.

The *digest* of a block is the SHA-256 of its masked text. Renumbering a block, or retargeting one of its
cross-references, therefore leaves its digest unchanged. Citation targets are still read for rule A's
transitive clause (§3.2), which uses the actual labels.

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
  `state space`, `system` and `systems`.

The classes below are counted on the local hypotheses, except `FU` and `IU`, which are also counted on
the proof.

- **`FS_A`, carrier finiteness.** Either of:
  - a `FINITE_TERMS` match (#1483), other than `bounded` and `compact` and other than a match inside a
    `NEG_FINITE` form, standing in a sentence that also names a carrier;
  - a Lean finiteness binder, that is `Fintype`, `Finite`, `Set.Finite`, `FiniteConf`, `Substratum.A1`
    or `Fin n`.
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
  - `transfinite`, `\mathbb N`-indexed and `|S| = \infty`;
  - `\to\infty` applied to a carrier count (`|S|`, `|\mathcal S|`, `N` where `N` is declared in the
    block as the number of configurations), and the Lean terms `Infinite` and `Set.Infinite`.
- **`GEN`, cardinality generality.** Any of:
  - a `NEG_FINITE` form;
  - a *carrier quantifier*: `(for|over|on) (all|every|any|each|arbitrary|unrestricted|unboundedly
    large)` followed, within three words, by a carrier as the quantified object. "Quantified object"
    means the first math expression after the quantifier is exactly a carrier symbol, or the first noun
    is a carrier noun. So `for every $S$`, `for any $S$ whatsoever` and `for every one of the possible
    $S$` are carrier quantifiers, and `for every $s \in S$` and `for all $n$` are not;
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

**The reuse of J10's vocabularies.** J10's `INFINITY_TERMS` and `PROMOTION_TERMS` serve as the recall
set.
- Every J10 match in a block's local hypotheses must fall inside a match of one of the classes `IS`,
  `GEN`, `PROMO`, `FS_A`, `FS_L` or `FU`, or inside one of the frozen *neutral* contexts. The neutral
  contexts are:
  - a quantifier whose object is not a carrier;
  - `uniformly continuous`, `independent of the basis`, `universal property` and `in general position`;
  - `\to\infty` applied to a symbol the block declares as a horizon, time, length or index (for
    example `for horizon $K$ … as $K \to \infty$`).
- A J10 match outside all of these raises rule G with the note `unclassified`. So the class lists can
  narrow J10's hits only by naming a neutral context, and they fail closed when they do not.

### 3.2 Per-block counts

For a block `b`, each class name stands for its count in `b`. For a revised block, `b⁻` is its paired
before-version (§2.4), or its reference entry (§6.1) when the reference is newer.

### 3.3 Rules and items

Each rule that fires produces an item `(rule, key, digest)`. A rule is evaluated on new and revised
blocks. Rule L is also evaluated on disappeared blocks, and rule P on every block that is parsed.

| Rule | Fires when | Guards |
|---|---|---|
| **A**, silent finiteness | `FU(b) > 0` and `FS_A(b) = 0` | (a) |
| **I**, silent infiniteness | `IU(b) > 0` and `IS(b) = 0` and `GEN(b) = 0` | neutrality |
| **L**, lost scope | the block is revised and `FS_L(b) < FS_L(b⁻)` or `IS(b) < IS(b⁻)`; or it has disappeared and `FS_L(b⁻) + IS(b⁻) > 0` | (a); (b) by deletion |
| **G**, generality | see the G-rule below | (b) |
| **M**, mirror | a chapter block and its FULL mirror (§3.4) have different `FS_A`, `FS_L`, `IS` or `GEN` | (a), (b) |
| **K**, kernel scope | the census resolves, in the block's paragraph, a declaration whose type has a finiteness binder (§5.3), and `FS_A(b) = 0` or `GEN(b) > 0` | (a), (b) |
| **P**, parse | a proof closes at the block's end without a closer; or a footnote reference has no definition | recognition |

**The G-rule.** It reads only the local hypotheses, never the proof. A promotion word in a proof, such as
"By Theorem 3, shown above", therefore raises nothing. Its clauses are:
- **(G1)** a new block with `GEN > 0` or `PROMO > 0`, using the new-block `PROMO` list;
- **(G2)** a new block with both `FS_A > 0` and `IS > 0`: it claims both scopes;
- **(G3)** a revised block whose `GEN` or `PROMO` count rises;
- **(G4)** a revised block whose `IS` count rises while `FS_A(b) > 0`: an infinite scope has been added
  to a finite one;
- **(G5)** any `unclassified` J10 match (§3.1).

A rise in `IS` on a block whose `FS_A` is 0 restricts the block to infinite systems. Such a narrowing
raises no G item. Neither does a rise in `FS_A`, `FS_L` or `FU`, nor any NEUTRAL match. Added
hypotheses therefore pass, whichever cardinality they state.

### 3.4 Mirrors (rule M)

`FULL.md` is segmented at its top-level `# Chapter N` headings and at its appendix headings. Segment `N`
is paired with `book/chNN-*.md`, and appendix segment `X` with `book/appendix-x-*.md`. The pairing table
is frozen at enrollment, and a segment with no chapter file is reported. Inside a pair, blocks are paired
by the three steps of §2.4, applied across the two files. A block that has no mirror in a chapter that
has one raises M.

### 3.5 Resolutions

An item is resolved only by an entry in the resolution registry (§7):

```
{"rule": ..., "key": [file, kind, digest-at-introduction], "digest": <current digest>,
 "outcome": "justified"|"unjustified", "basis": <text>, "proof": <citation or null>,
 "attestation": <per §3.6>}
```

- The `digest` must equal the block's current digest, so a later material edit voids the resolution.
- Rules G and L need a `proof`. For G, the cited proof must cover the scope the statement states. For L,
  it must establish the result without the removed hypothesis. This is J10's R-resolution requirement
  carried over.
- Rules A and I are resolved either by narrowing the statement, which makes the item disappear, or by a
  `basis` showing that the use is not load-bearing. An example is a compactness argument on a compact
  space that has a maximum.
- Rule K needs a `basis` naming the clause of the statement that carries the binder's content, and an
  attestation from a reviewer who has checked the kernel statement.
- An `unjustified` outcome leaves the item open.
- A resolution decides scope only. It does not accept the result scientifically.

### 3.6 Who may resolve: the attestation

Every commit, pull request and comment in this repository is made under a single login. A check that the
reviewer's login differs from the author's would therefore always fail, and a self-declared reviewer
string would be resolution by assertion alone. Owner decision O6 (§12) chooses the attestation. The
options, from weakest to strongest:

- **(α) Session-bound.** The attestation is `{session, commit}`.
  - `commit` is a commit that adds the resolution and changes nothing else.
  - `session` is that commit's `Claude-Session` trailer.
  - The tool checks offline that the trailer differs from the `Claude-Session` trailer of every commit
    since the merge base that touched the block's file.
  - Weakness: the trailer is written by its writer, so this is evidence of separation and not proof of
    it.
- **(β) Owner clearance.** The attestation is `{owner_record, commit}`. `owner_record` is the URL of an
  owner decision record that names the item's digest and the resolution commit.
  - The tool checks the form.
  - Pull-request review checks the record against the host.
  - This matches how owner decisions are recorded on #1169 today.
- **(γ) Signed.** The resolution commit is signed with a key listed in a reviewer keyring file. That
  file is changed only by owner decision.
  - The tool runs `git verify-commit` and checks that the signing key is not the key of any commit
    touching the block's file.
  - This needs key infrastructure the repository does not have.

The writer's recommendation is (α) for every item, and (β) in addition for items of rules G, L and K.
Whatever the choice, the check is invariant V9 (§11) with its own checkpoint.

### 3.7 Verdict

- **PASS.** Every in-scope item is resolved, every configuration control (§7) holds, and the controls of
  §8 pass.
- **FAIL.** An item is unresolved, or a control fails, or `vocab.json` or `resolutions.json` changed
  outside §7.
- **VOID.** A pinned #1483 blob or commit object is missing or has the wrong digest (§4). A VOID run
  prints no item verdicts.

The verdict text is generated from the counts.

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

The tool prints each item with its rule, key, the counts that fired it, and the matched spans.
Reviewers add the resolutions with the attestations of §3.6. A checklist line (§10) asks whether the
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

Rules G (G1–G5, read as for blocks) and L (`FS_L` and `IS` loss) apply to the paired sentences and are
gating. The same rules on other prose are advisory unless owner decision O3 makes them gating.

### 6.3 Baseline enrollment

After D1 and D2, one enrollment commit evaluates every block and claim surface on `main`. It records each
digest and its counts in `baseline.json`, and each item that fires in a published list of *baseline
items*.
- A baseline item does not fail the gate while its digest stands.
- Enrollment records a baseline item. It does not resolve or accept it.
- How long a baseline item may stand is owner decision O4.

## 7. Files and configuration control

The proposed home is `verification/infrastructure/fin-scope/` (§A.36). It holds:
- `fin_scope.py`, the checker, with `--self-test`;
- `vocab.json`: the classes of §3.1, the carrier and neutral lists, the 0.6 threshold and the #1483 pin;
- `baseline.json`;
- `resolutions.json`.

Each run checks four configuration controls:
- **The allowlist.** It is #1483's, read from the pinned blob, and FIN-SCOPE has none of its own. A new
  allowlisted sentence needs an owner decision and a pin move to a #1483 successor that carries the
  sentence.
- **Narrowing `vocab.json`.** A commit that removes or narrows a pattern, or adds a neutral context,
  fails. It passes only when the same commit adds a case showing that the removed pattern's TESTS cases
  are still caught, or cites an owner decision.
- **Append-only registries.** `resolutions.json` and `baseline.json` are append-only, apart from the
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
  into FIN-SCOPE's own finite-scoped fixture block (`TESTS.md` §1.3, F1), must raise G. The expected
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
  | G5 off | P-G11 |
  | the NEUTRAL context check off | N14e, N15 |
  | rule I off | P-I1 |
  | rule M off | P-M1 |
  | the resolution digest check off | P-R2 |
  | the attestation check off | P-R1 |
  | the reference-count recomputation off | P-R6 |

  Mutants run only in CI (§A.40), after the live controls and every unmodified check have passed.
- **Negative controls.** Every N-case of `TESTS.md` must PASS, with the item counts stated there.

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
- **The burden that remains.** Rule I and the `maximum`/`compact` part of rule A raise items on some
  correct results, for example a maximum on a compact space. These are a review burden, not a
  finiteness requirement: each is cleared by a `basis` (§3.5).

### Known limits, each routed to review

- **Lexical classes.** The guarantee holds relative to the classes. A finiteness use worded without a
  listed term escapes rule A, for example "each configuration is visited before any repeats" (X-2).
- **Carrier sentences.** A finiteness term about another object passes `FS_A` when it stands in a
  sentence that also names a carrier, for example "for a finite time $t$ and every $s \in S$" (X-1).
- **Bounded and compact.** They count for `FS_L` and not for `FS_A`. A compact-space theorem whose proof
  takes a maximum raises A, and a review clears it (X-5).
- **Citation chains.** The transitive clauses follow citations only within the parsed corpus. A
  finite-only result cited from outside it, or by an unparsed wording, is not followed (X-6).
- **Unlabelled theorems.** A theorem stated in unlabelled prose outside the claim surfaces is seen only by
  the advisory PR layer (X-3).
- **Sufficiency.** FIN-SCOPE never decides whether a hypothesis suffices. Under c.7061660930 that is the
  task of independent mathematical review, and the checklist line of §10 carries it.

## 10. Proposed governance text

This is a proposal only, and it is not applied before the A1 retirement lands. For a new AGENTS.md
section, numbered at landing:

> **FIN-SCOPE: scope of finiteness claims.** Every theorem states the cardinality scope it uses. A
> result that uses finiteness of a configuration space states that finiteness as a local hypothesis; a
> result claimed for infinite systems, or for systems of every cardinality, cites a proof that covers
> that scope. Neither finiteness nor infiniteness is assumed globally, and adding a hypothesis of either
> kind is always permitted. The release gate's `fin-scope` step checks new and revised statement blocks
> and claim surfaces against these requirements. An item it raises is resolved only by narrowing the
> statement or by a resolution carrying the attestation the owner has fixed; a generality or lost-scope
> resolution cites the covering proof. Whether a stated hypothesis suffices is decided by independent
> mathematical review, not by the step. The vocabularies and the allowlist change only under the step's
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
| V7 | a later material edit voids a resolution | P-R2; the digest-check mutant |
| V8 | the reference counts cannot be rewritten | P-R6; the recomputation mutant |
| V9 | a resolution carries the attestation fixed by O6 | P-R1, P-R3; the attestation-check mutant |
| V10 | the registries are append-only | P-R8 (merge-base blob comparison) |
| V11 | renumbering raises no item | N16; the digest-first mutant |
| V12 | every corpus label form is recognized | the enrollment inventory check (§2.3); P-B1 |
| V13 | J10's recall set is not narrowed silently | G5; P-G11; the `vocab.json` control (§7) |

## 12. Owner decisions needed

- **O1.** Approve this design for independent re-review, and the proposed home (§7).
- **O2.** What happens if #1483 does not land on `main`. Neither branch has accepted review status for
  the reused code, so both branches need FIN-SCOPE's own review of that code.
  - (i) *Pin the last reviewed #1483 head.* That commit is not on `main`. Under §A.42 item 8 it would
    then be required evidence for the gate's standing claim, to be retained on `main` with a manifest.
  - (ii) *Vendor the reused constants and functions* into FIN-SCOPE, with provenance digests. This
    contradicts §4's "without duplication", and it needs a digest-parity control against the source
    blob for as long as that blob exists.

  The writer's view is that FIN-SCOPE should wait for D2, and that O2 arises only if #1483 is
  withdrawn.
- **O3.** Whether advisory prose items outside the claim surfaces (§6.2) become gating.
- **O4.** Whether baseline items may stand indefinitely or must be cleared, and by what process.
- **O5.** Whether rule K is in the first implementation or follows #1482.
- **O6.** The attestation for resolutions (§3.6): (α), (β), (γ) or a combination. Without O6, no item
  can be resolved except by narrowing.

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
| B7 | §3.6 options (α)–(γ), O6, V9 |
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
