# FIN-SCOPE: design specification

**Status.** Writer's design, WIP / UNVERIFIED. This is a plan only. No checker exists, nothing has
been run, and no verdict below is a measurement. Independent non-author review is required before any
implementation is proposed, and implementation, the governance change and any merge each need a
separate owner decision.

**Authority.**
- #1169 c.7061660930 (owner decision, 2026-11-21), item 1. FIN-SCOPE is the permanent name; `A1` stays
  retired and its identifier is not reused; "the relevant #1483 checks are reused as a standing release
  gate for new or materially revised theorem statements. Wherever automation cannot decide whether a
  hypothesis is sufficient, independent mathematical review is required"; `FiniteConf` (#1482) stays as
  the explicit Lean predicate for finite-configuration results; "FIN-SCOPE verifies the scope of
  claims; it does not require finiteness. A theorem may apply only to infinite systems, only to finite
  systems, or to both, provided its assumptions and proof justify that scope." Its governance PR is
  prepared after the A1-retirement edits land.
- #1169 c.7063843557, stream 5: "Design specification and adversarial tests only. No change to
  `AGENTS.md` until the A1 retirement lands."
- #1169 c.7064767045: research, planning and preregistration authorized; no computational experiments,
  CI dispatches, manuscript changes or merges.
- Background: c.7057297534 ("Add a regression check against new global infinity assumptions";
  cardinality neutrality), c.7058446475 (the configuration-space sentence; "Finiteness stays explicit
  wherever an individual theorem requires it"), c.7058783437 (safeguard: removing the global finiteness
  assumption is not proof that the theory works for every infinite system), c.7061062574 item 6 (the
  #1483 criterion: finite-only theorems keep their hypotheses; no unsupported infinite-system
  generalization).

**Dependencies, none treated as established.**
- D1. The A1 retirement (#1477) has landed. FIN-SCOPE's baseline is enrolled only on a `main` that
  contains it.
- D2. #1483 has landed on `main` with its frozen `compare/verdict.py` and `baseline.py`. FIN-SCOPE
  reuses their J10 machinery from those landed blobs (§4). If #1483 does not land, §4's reuse route is
  unavailable and an owner decision is needed (§12, decision O2).
- D3. #1482 has renamed `Substratum.A1` to `FiniteConf`. Until it lands, the Lean layer (§5.3) reads the
  current name; both names are in its binder list, so the design does not depend on the rename.

This design does not modify, and does not require changes to, #1477's frozen material, #1483's tools or
inputs, or any manuscript line under the #1477 ledger.

## 1. Purpose

A permanent safeguard for the A1 retirement. With no global cardinality assumption, every result
carries its own scope. FIN-SCOPE checks that the scope a statement claims is the scope its hypotheses
state. It guards against two failures:

- **(a) Silent finiteness.** A new or revised theorem uses finiteness (counting, a uniform prior,
  pigeonhole, finite recurrence, `Fintype`) without stating it as a local hypothesis.
- **(b) Unsupported generality.** A new or revised claim asserts validity for infinite systems, or for
  every system, without a proof that covers that generality.

It also catches the mirror image of (a), silent infiniteness (§3, rule I), so that the check is
cardinality-neutral rather than a preference for finite statements.

## 2. Scope

### 2.1 Surfaces

| Surface | Units | Mode |
|---|---|---|
| `papers/*.md` | statement blocks (§2.2) | gate (§6.1) |
| `book/ch*.md`, `book/appendix-*.md`, `book/The-Incompleteness-of-Observation-FULL.md` | statement blocks; mirror pairs compared | gate |
| Lean modules governed by `verification/lean-manuscript-census.json` | declarations named as census anchors | gate (§5.3) |
| added prose lines in the same manuscript files, outside statement blocks | sentences | PR layer (§6.2) |

Out of scope: `verification/` records (they narrate history and are kept by `G13` and the
`legacy-records` step), Git history, frozen records of any round, and generated `.tex`/`.pdf` (their
consistency with source is the build's business).

### 2.2 Statement blocks

A *statement block* is a paragraph that opens with a bold label of the form `**Theorem N**`,
`**Lemma N**`, `**Proposition N**`, `**Corollary N**` or `**Claim N**` (optional parenthetical title),
in any of the surfaces above. It has three parts:

- **statement**: from the label to the start of the proof, or to the end of the paragraph when no proof
  follows;
- **local hypotheses**: the statement itself, plus the text of every hypothesis or setting the statement
  cites by label (for example `(F)`, `(H2)`, `Setting 3`) when that label is defined in the same file;
  a label defined elsewhere counts only when the statement cites it with file and label;
- **proof**: from `*Proof.*` (or `Proof.`) to the first `∎`, `$\square$` or `\qed`.

The block's *key* is `(file, label)`. Its *digest* is the SHA-256 of the normalized (§4), whitespace-
collapsed text of statement and proof together. A block is *revised* when its key exists in the
reference record (§6.1) with a different digest, and *new* when its key does not.

"Materially revised" (c.7061660930) is read as: the digest changes. Whitespace-only reflow does not
change it; any token change does. This is deliberately wider than "the mathematics changed", because a
lexical tool cannot decide that.

## 3. What is checked: the decision rule

All counts are taken on normalized text with the allowlisted sentences removed (§4), so the allowlist
can neither trigger a hit nor supply a scope term.

### 3.1 Vocabularies

Reused unchanged from #1483 `compare/verdict.py` (§4):
- `FINITE_TERMS`: finite-scope terms (`finit*`, `< \infty` in any form, `bounded`, `compact`).
- `PROMOTION_TERMS` and `INFINITY_TERMS`: J10's layer-2 vocabularies.

Added by FIN-SCOPE, frozen in its own file (`vocab.json`, §7), each list with its own countercontrols:
- `FINITE_USE`: reasoning that is valid only for finite carriers, or that needs finiteness to be stated:
  `pigeonhole`; `counting` (`counting measure`, `by counting`); `uniform (prior|measure|distribution|
  weight)`; `1/|S|`, `\frac{1}{|S|}`, `\frac{1}{N}` over configurations; `|S|`, `|\mathcal C_*|` as a
  number; `\sum_{s \in S}` over a whole configuration space; `finitely many`; `Poincaré recurrence` and
  `recurrence` of a permutation; `period(ic)` of an orbit of a bijection; `permutation of a finite`;
  `Fintype`, `Fintype.card`, `Finset.univ`, `Nat.card`, `Finite.`; `maximum over` a configuration space.
- `INFINITE_USE`: reasoning that needs an infinite carrier, or a measure or limit structure the
  statement must state: `countabl* additiv*`; `\sigma`-additivity; `Kolmogorov extension`;
  `ultrafilter`; `Zorn`; `compactness argument`; `\lim`, `\to \infty` over the configuration count;
  `ergodic theorem`; `Haar measure` on an infinite group; `Infinite`, `Set.Infinite`, `Cardinal`.
- `INFINITE_SCOPE`: restricting hypotheses of infinite cardinality: `infinite`, `countably infinite`,
  `uncountable`, `\aleph_0`, `of continuum size`, `Infinite`, `Set.Infinite`.
- `GENERALITY`: the widening subset of `INFINITY_TERMS` and `PROMOTION_TERMS` that asserts a scope
  rather than restricting one: `arbitrar*`; `for|over all|every|any|each`; `regardless`; `irrespective`;
  `whatever`; `whatsoever`; `unrestricted`; `finite or not`; `finite or infinite`; `in (either|both|
  all) cases`; `independent of`; `uniformly in`; `of any size`; `any number of`; `no assumption`;
  `no restriction`; `beyond the finite`; `including the infinite`; `also for`; `without (any) finit*`;
  `unconditional*`; `universal*`; `in general`; `without exception`.

`uniform` followed by `prior`, `measure`, `distribution` or `weight` is `FINITE_USE` and not
`GENERALITY`; every other `uniform(ly)` is `GENERALITY`.

### 3.2 Per-block predicates

For a block `b`, with `stmt` its local hypotheses and `pf` its proof:
- `FS(b)` = count of `FINITE_TERMS` in `stmt`;
- `IS(b)` = count of `INFINITE_SCOPE` in `stmt`;
- `GEN(b)` = count of `GENERALITY` in `stmt`;
- `FU(b)` = count of `FINITE_USE` in `stmt` and `pf`;
- `IU(b)` = count of `INFINITE_USE` in `stmt` and `pf`.

For a revised block, `b⁻` is its reference version (§6.1).

### 3.3 Items

Each rule that fires produces an *item* `(rule, key, digest)`. Rules are evaluated on every new or
revised block, and rule L also on every block that disappears.

| Rule | Fires when | Guards |
|---|---|---|
| **A**, silent finiteness | `FU(b) > 0` and `FS(b) = 0` | (a) |
| **I**, silent infiniteness | `IU(b) > 0` and `IS(b) = 0` and `GEN(b) = 0` | neutrality |
| **L**, lost scope | revised, and `FS(b) < FS(b⁻)` or `IS(b) < IS(b⁻)`; or a block with `FS(b⁻) + IS(b⁻) > 0` whose key disappears | (a), and (b) by deletion |
| **G**, generality | new, and `GEN(b) > 0`; or revised, and J10's `j10_hits(b⁻, b)` reports a promotion or infinity gain | (b) |
| **M**, mirror | a book chapter block and its `FULL.md` mirror (same label, same chapter) differ in `FS`, `IS` or `GEN` | (a), (b) |
| **K**, kernel scope | the block cites a census anchor whose type has a finiteness binder (§5.3), and `FS(b) = 0`; or the anchor has such a binder and `GEN(b) > 0` | (a), (b) |

Rule G on a revised block is exactly J10's layer 2, read from the landed #1483 function (§4); on a new
block, where no before-text exists, it is the `GENERALITY` count, so that a new theorem restricted to
infinite systems ("Let $S$ be countably infinite") is treated like a new theorem restricted to finite
ones: neither produces an item.

### 3.4 Resolutions

An item is *resolved* only by an entry in the resolution registry (§7):

```
{"rule": "A"|"I"|"L"|"G"|"M"|"K", "key": [file, label], "digest": <sha256>,
 "outcome": "justified"|"unjustified", "review": <URL>, "reviewer": <login>,
 "author": <login>, "basis": <text>, "proof": <citation or null>}
```

- `review` is a comment or review URL on the pull request that introduced the digest;
- `reviewer` differs from `author`, case-insensitively, and from every author of that pull request's
  commits (checked by PR review against the host; the tool checks the form offline, as #1483 does);
- `digest` equals the block's current digest; any later edit to the block voids the resolution;
- rules G and L need `proof`: the citation of the proof that covers the scope the after-text states
  (G), or that establishes the result without the removed hypothesis (L). This is J10's R-resolution
  requirement carried over;
- rule A is resolved either by narrowing the statement (the item then disappears) or by `basis`
  showing that the finite-use term is not load-bearing; rule I likewise;
- rule K needs a reviewer who checks the kernel statement, and `basis` naming the clause of the
  statement that carries the binder's content.

An `unjustified` outcome leaves the item open. A resolution decides scope only; it is not a scientific
acceptance of the result.

### 3.5 Verdict

- **PASS**: every item in scope is resolved, the configuration controls (§7) hold, and every
  countercontrol (§8) is caught.
- **FAIL**: any unresolved item, any failed control, any unparsable block in a surface (a block whose
  label opens but whose proof does not close), or any change to `vocab.json` or the allowlist not made
  under §7.
- **VOID**: a pinned #1483 blob is missing or has the wrong digest (§4). A VOID run prints no item
  verdicts.

The verdict text is generated from the counts; no wording is fixed in advance.

## 4. Reuse of #1483, without duplication or modification

FIN-SCOPE reuses, from #1483's landed blobs, the normalization (`normalize_text`: HTML entities,
`ℕ`/`ℤ`/`ℝ`/`ℵ`, NFKC, zero-width and discretionary hyphens, confusable letters, footnote expansion),
the exact allowlist and `strip_allowlisted`, the vocabularies `FINITE_TERMS`, `PROMOTION_TERMS`,
`INFINITY_TERMS`, and `j10_hits`, plus the batteries `PARAPHRASES`, `EVASIONS`, `ALLOW_PLUS` and
`NCASES` as standing regression fixtures.

Mechanism:
- FIN-SCOPE pins the Git blob ids and SHA-256 digests of `compare/verdict.py` and `baseline.py` as
  landed on `main` by #1483 (the merge commit is recorded in FIN-SCOPE's own frozen file);
- at run time it reads both blobs from that commit's Git objects (never the working tree), writes them
  to a private temporary directory, checks the digests, and loads `verdict.py` there as a module;
- it calls only the pure functions and constants listed above. It never calls `collect`, `verdict`,
  `c0` or any function that reads #1483's inputs or writes;
- a parity control (§8, C-R1) confirms that the loaded `j10_hits` reproduces #1483's T13 battery
  outcome: every `PARAPHRASES` and `EVASIONS` case inserted into a fixture block is a hit.

#1483's files stay exactly as landed. A later amendment of #1483 does not move FIN-SCOPE; FIN-SCOPE's
pin moves only by its own reviewed change. What FIN-SCOPE adds (§3.1's four lists, block parsing, rules
A, I, L, M, K, the registry) is new and lives in its own directory.

## 5. Where it runs

### 5.1 Release gate

A new step `fin-scope` in `tools/release_gate.py`, run by the existing `verify.yml` jobs on every pull
request and every push to `main`. It needs no dispatch and no new workflow. Its run is ordinary CI and
is not an exact-head `check-run` attestation (§A.39, §A.40).

### 5.2 PR review

The tool prints, for the pull request's diff, each item with its rule, key, the counts that fired it and
the matched terms. Reviewers check the items and add the resolutions. A reviewer checklist line (§10)
asks, for each new or revised statement block, whether the statement's scope matches what the proof
uses, which no lexical check can settle.

### 5.3 Lean layer

For a census anchor cited beside a statement block, a Lean metaprogram (run in the existing Mathlib
bridge job, reading only elaborated declarations) reports whether the declaration's type has a
*finiteness binder*: an instance or hypothesis of `Finite`, `Fintype`, `Set.Finite`, `FiniteConf`,
`Substratum.A1` (until #1482 lands), or a carrier of the form `Fin n` or `FiniteOperationalTheory`. Rule
K compares that report with the manuscript block. A finiteness binder supplied by an `axiom` or a
global `instance` without a proof is reported separately, and the existing `lean-axioms` step fails it.

## 6. Reference record and baseline

### 6.1 Reference

The *reference record* is `baseline.json` (§7) together with the resolved entries of the registry:
for each key, the digest and the counts `FS`, `IS`, `GEN` at the last enrolled or resolved version.
A pull request that changes a block replaces its reference entry in the same commit, and the gate
checks that the replaced entry's counts are the ones the reference held (so the before-version cannot
be rewritten to hide a loss).

### 6.2 PR layer for prose

Added manuscript lines outside statement blocks, compared with the merge base: a `GENERALITY` or J10
gain in an added sentence is a PR-layer item with the same resolution form (rule G). Whether these
items block the gate or are advisory is an owner decision (§12, O3).

### 6.3 Baseline enrollment

After D1 and D2, one enrollment commit evaluates every statement block on `main` and records each
block's digest and counts in `baseline.json`, and each item that fires in a published list of
*baseline items*. Baseline items do not fail the gate while their digests stand, and they are not
resolved by enrollment: enrollment records them, it does not accept them. They are the input for later
review. Whether baseline items may stand indefinitely or must be cleared by a date is an owner decision
(§12, O4).

## 7. Files and configuration control

Proposed home: `verification/infrastructure/fin-scope/` (§A.36), containing:
- `fin_scope.py`: the checker, with `--self-test`;
- `vocab.json`: §3.1's four added lists and the #1483 pin;
- `baseline.json`: §6.3;
- `resolutions.json`: §3.4.

Configuration controls, checked at every run:
- the allowlist is #1483's, read from the pinned blob; FIN-SCOPE has no allowlist of its own. A
  further allowlisted sentence needs an owner decision and a change to FIN-SCOPE's pin to a #1483
  successor that carries it;
- a change to `vocab.json` that removes or narrows a pattern fails unless the same commit adds a
  countercontrol showing the removed pattern's cases are still caught, or an owner decision is cited;
- `resolutions.json` and `baseline.json` entries are append-only apart from the reference replacement of
  §6.1.

## 8. Controls

- **C-R1, reuse parity.** §4's parity control on the loaded #1483 functions.
- **C-R2, pin.** A wrong digest for either #1483 blob makes the run VOID.
- **Mutants**, each of which must make the self-test fail on the named case: rule A disabled (TESTS
  P-A1); `FINITE_USE` emptied (P-A2); rule L disabled (P-L1); the disappearance clause of L removed
  (P-L4); rule G for new blocks disabled (P-G1); `j10_hits` replaced by a function returning no hits
  (P-G3); allowlist stripping applied before counting scope removed, so the owner sentence supplies
  `FS` (P-A7); rule I disabled (P-I1); rule M disabled (P-M1); the digest check on resolutions removed
  (P-R2); the reviewer-differs check removed (P-R1). Each mutant names its target case and counts as
  caught only when the self-test fails cleanly on that case (`tools/mutant_verdict.py`).
- **Negative controls**: every TESTS negative (N-cases) must PASS, with the item counts stated there.

Mutants run in CI only (§A.40), after the live controls and every unmodified check have passed.

## 9. How it avoids requiring finiteness

- No rule fires on the absence of a finite-scope term alone. Rule A needs finite-use reasoning; a
  statement with neither finite-use nor infinite-use terms produces no item (N-cases N3, N4).
- Rules A and I are symmetric: silent finiteness and silent infiniteness are both items. Rule L treats a
  lost infinite restriction as it treats a lost finite one.
- A new theorem restricted to infinite systems by a local hypothesis produces no item, exactly as a
  finite-only theorem does (N6 against N1).
- Generality items (G) are cleared by a covering proof, as J10's are; they are not presumed false.
- The allowlist is removed before every count, so the owner's sentence neither triggers an item nor
  supplies finite scope to a theorem that lacks it.

### Known limits

- The vocabularies are lexical, so the guarantee is relative to them: a finiteness use worded with no
  listed term escapes rule A, and a finite-scope term used in another sense ("finite time",
  "finite-dimensional") satisfies `FS` without restricting the configuration space (TESTS X-cases).
  The PR review checklist (§10) is the safeguard there; FIN-SCOPE does not claim to decide sufficiency
  of a hypothesis, which c.7061660930 assigns to independent mathematical review.
- Statement blocks are recognized by their bold labels. A theorem stated in unlabelled prose is seen only
  by the PR layer (§6.2).
- Rule K covers only declarations named as census anchors.

## 10. Proposed governance text (proposal only; not to be applied before the A1 retirement lands)

For a new AGENTS.md section, number assigned at landing:

> **FIN-SCOPE: scope of finiteness claims.** Every theorem states the cardinality scope it uses. A
> result that uses finiteness of a configuration space states that finiteness as a local hypothesis; a
> result claimed for infinite systems, or for every system, cites a proof that covers that scope. Neither
> finiteness nor infiniteness is assumed globally. The release gate's `fin-scope` step checks new and
> revised statement blocks against these requirements. An item it raises is resolved only by narrowing
> the statement or by a resolution recorded on the pull request by a reviewer who is not its author;
> a generality or lost-scope resolution cites the covering proof. Whether a stated hypothesis suffices is
> decided by independent mathematical review, not by the step. The allowlist and vocabularies change only
> under the step's configuration controls.

For the Code Review Rules, one line under *Claim/evidence boundary*:

> - For each new or revised theorem statement, check that its cardinality scope matches what its proof
>   uses: finiteness the proof needs is stated locally, and a claim for infinite or arbitrary
>   configuration spaces has a proof that covers it (FIN-SCOPE).

## 11. Result classification

This record proves no theorem, so it carries no result of class (N), proved from OI's native
assumptions, or (I), conditional on imported quantum or operational assumptions. It adopts no physical
assumption. FIN-SCOPE, once implemented, checks the stated scope of results; it does not classify them
on that axis, and a FIN-SCOPE pass is not evidence for either class.

## 12. Owner decisions needed

- **O1.** Approve this design for independent review, and the proposed home (§7).
- **O2.** If #1483 does not land, choose between pinning its blob from its last reviewed head (a
  non-`main` commit, which §A.42 would then require retaining) and vendoring the constants with
  provenance digests.
- **O3.** Whether PR-layer prose items (§6.2) block the gate or are advisory.
- **O4.** Whether baseline items (§6.3) may stand indefinitely or must be cleared, and by what process.
- **O5.** Whether rule K is part of the first implementation or a follow-up after #1482.
