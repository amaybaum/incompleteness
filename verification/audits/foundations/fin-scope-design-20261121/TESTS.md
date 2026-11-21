# FIN-SCOPE: adversarial test designs

**Status.** Writer's test plan, WIP / UNVERIFIED, for the design in `SPEC.md`. These are designs: no
case has been run, and every "expected" entry is the verdict the specified rule must produce, fixed
before any implementation exists. Rule letters and predicates are those of SPEC §3.

**Conventions.**
- Every case is synthetic text in a fixture file, never an edit of the manuscript. Where a case is
  modelled on a real site or review finding, the source is named for provenance only; the case makes no
  claim about the current text of that site.
- *Before* is the reference version (SPEC §6.1); a case with no before is a new block.
- `$\square$` closes each proof. The fixture's local hypothesis labels are defined in the same fixture
  file unless stated.
- "Items" lists the items the case must produce; "Verdict" is the gate verdict with no resolutions
  present, then, where relevant, with the stated resolution.
- Each positive case is also the target of at least one mutant (SPEC §8) where a mutant is named.

## 1. Positives: cases FIN-SCOPE must catch

### 1.1 Unstated finiteness (rule A)

| ID | Before | After | Items | Verdict |
|---|---|---|---|---|
| P-A1 | (new) | `**Lemma 1.** *Every bijection $\pi$ of $S$ has a periodic orbit.* *Proof.* By pigeonhole, the sequence $\pi^n(s)$ repeats. $\square$` | A | FAIL; target of the rule-A mutant |
| P-A2 | (new) | `**Proposition 2.** *The equilibrium weight of each configuration is $1/|S|$.* *Proof.* Invariance under $\pi$ and normalization of the uniform prior. $\square$` | A | FAIL; target of the emptied-`FINITE_USE` mutant |
| P-A3 | (new) | `**Theorem 3.** *Every orbit of $\pi$ returns to its start.* *Proof.* Poincaré recurrence for the permutation $\pi$. $\square$` | A | FAIL |
| P-A4 | (new) | `**Theorem 4** (Prior). *Under the uniform prior on $\mathcal C_H$, the visible law is $\mu$.* *Proof.* Counting preimages. $\square$` (modelled on the Theorem 24(i) finding of #1169 c.7062144714) | A | FAIL |
| P-A5 | (new) | statement cites `(H2)`, where the fixture defines `(H2)`: "$\pi$ commutes with $\tau$"; proof: "summing over $s \in S$" | A (the cited label carries no finite-scope term) | FAIL |
| P-A7 | (new) | `**Lemma 7.** The substratum has a configuration space $S$. No restriction is imposed on its cardinality; $S$ may be finite or infinite. *Every orbit is periodic.* *Proof.* Pigeonhole on $S$. $\square$` | A: the allowlisted sentence is removed before counting, so its "finite" does not count toward `FS` | FAIL; target of the strip-before-count mutant |

The case where a finite-scope term in the statement concerns another object than $S$ is not a
positive: the tool passes it, and it is recorded as the documented limit X-1 (§3).

### 1.2 Lost finite scope (rule L)

| ID | Before | After | Items | Verdict |
|---|---|---|---|---|
| P-L1 | `... on a finite configuration space ...` in a statement (modelled on #1483 C9 (f), appB:42) | `... on a configuration space ...` | L | FAIL; target of the rule-L mutant |
| P-L2 | `a function of finitely many components` (modelled on #1483 NCASES N3, appB:194) | `a function of components` | L | FAIL |
| P-L3 | `a substratum of $N < \infty$ ontic configurations` (NCASES N4i) | `a substratum of ontic configurations` | L | FAIL |
| P-L4 | block `**Lemma 9**` with `FS = 1` | block deleted and its statement restated without the hypothesis as `**Lemma 9'**` | L (key disappears) and A if the proof uses pigeonhole | FAIL; target of the disappearance-clause mutant |
| P-L5 | `*Let $S$ be finite. Then ...*` | `Let $S$ be finite.` moved into the paragraph before the label, not cited by the statement | L (`FS` drops from 1 to 0); A as well when the proof is finite-use | FAIL |
| P-L6 | `*Let $S$ be countably infinite. Then the shift has no periodic point.*` | `*Then the shift has no periodic point.*` | L (`IS` drops) | FAIL |
| P-L7 | `for a Hamiltonian flow on compact energy surfaces` (NCASES N4j) | `for a Hamiltonian flow on energy surfaces` | L (`compact` is a finite-scope term) | FAIL |
| P-L8 | Resolution of P-L1 recorded with `outcome: justified`, reviewer ≠ author, `proof: null` | unchanged | L | FAIL: an L resolution needs `proof` |
| P-L9 | Resolution of P-L1 with `proof` citing a proof that does not use finiteness | unchanged | L, resolved | PASS. Expected only as a form check: whether the cited proof suffices is the reviewer's decision |

### 1.3 Unsupported generality (rule G)

| ID | Before | After | Items | Verdict |
|---|---|---|---|---|
| P-G1 | (new) | `**Theorem 10.** *For every $S$, finite or infinite, the conserved quantities are the orbit-constant functions.*` | G | FAIL; target of the new-block rule-G mutant |
| P-G2 | GR:134-style statement ending `on all its members. $\square$` (the #1483 battery site) | each of #1483's 16 `PARAPHRASES`, inserted after "members" | G, once per case (16) | FAIL for each |
| P-G3 | same | each of #1483's 28 `EVASIONS` (soft hyphen, discretionary hyphen, Cyrillic `і`, footnote `[^gen]` with a generality definition, `\aleph_0`, `\kappa`, `\to\infty`, ...) | G, once per case (28) | FAIL for each; target of the empty-`j10_hits` mutant |
| P-G4 | same | the allowlisted sentence followed by each `ALLOW_PLUS` claim ("This identity is independent of $|S|$", "It holds for each such $S$") | G | FAIL |
| P-G5 | same | `, and this is proved` (#1483 C9 (d)) | G (promotion gain) | FAIL |
| P-G6 | same | `; the identity holds unconditionally` | G | FAIL |
| P-G7 | `Without A1, the near-return condition ...` style statement (modelled on #1483 C9 (a)) | `For every infinite system, the near-return condition ...` | G | FAIL |
| P-G8 | P-G1 with a resolution: `justified`, reviewer ≠ author, `proof: null` | unchanged | G | FAIL: a G resolution needs `proof` |
| P-G9 | (new) Lean-anchored statement `*For every substratum, ...*` citing an anchor whose type has `[FiniteConf 𝒮]` | — | K (binder, `FS = 0`) and G | FAIL |
| P-G10 | (prose, PR layer) an added abstract sentence: "OI's conservation laws hold for configuration spaces of any size." | — | PR-layer G | FAIL or advisory, per owner decision O3 |

### 1.4 Silent infiniteness, mirrors, kernel (rules I, M, K)

| ID | Before | After | Items | Verdict |
|---|---|---|---|---|
| P-I1 | (new) | `**Lemma 11.** *The time average of $f$ along $\pi$ exists.* *Proof.* By the ergodic theorem and countable additivity. $\square$` | I | FAIL; target of the rule-I mutant |
| P-I2 | (new) | `*The visible law is the limit of the horizon laws.* *Proof.* Kolmogorov extension. $\square$` | I | FAIL |
| P-M1 | ch02 block `**Theorem 24**` and its FULL.md mirror, both with "finite $\mathcal C_H$" | the chapter keeps it; the FULL mirror loses it | M, and L on the FULL block | FAIL; target of the rule-M mutant |
| P-M2 | mirror pair with equal counts | the FULL mirror gains ", for arbitrary $S$" | M and G on the FULL block | FAIL |
| P-K1 | (new) block citing anchor `cx3b_complex_not_A1` (or its #1482 successor), whose type carries the finiteness predicate | statement says nothing about finiteness | K | FAIL |
| P-K2 | — | a new Lean module declares `instance : Fintype Conf := sorry` or an axiom supplying it | the `lean-axioms` step fails; FIN-SCOPE's Lean layer reports the binder as unproved | FAIL (cross-check of an existing step) |

### 1.5 Resolution and configuration abuse

| ID | Case | Expected |
|---|---|---|
| P-R1 | P-A1 resolved with `reviewer` equal to `author`, differing only in case | unresolved; FAIL; target of the reviewer-differs mutant |
| P-R2 | P-A1 resolved, then one token of the proof edited | resolution's digest no longer matches; item open; FAIL; target of the digest-check mutant |
| P-R3 | resolution with `review` pointing at a different pull request | unresolved by PR review (host check); the offline form check passes; recorded as a PR-review obligation |
| P-R4 | a commit adds a third sentence to FIN-SCOPE's own configuration as an allowlist entry | FAIL: FIN-SCOPE has no allowlist of its own (SPEC §7) |
| P-R5 | a commit deletes `\bpigeonhole\b` from `FINITE_USE` without a countercontrol or owner decision | FAIL |
| P-R6 | a commit edits `baseline.json` to raise a block's recorded `FS`, then lowers the block's `FS` in the manuscript | FAIL: the reference replacement must carry the counts the reference held (SPEC §6.1) |
| P-R7 | the pinned #1483 `verdict.py` blob replaced by a copy with an emptied `INFINITY_TERMS` | VOID (digest), no item verdicts printed |

## 2. Negatives: cases FIN-SCOPE must pass

| ID | Before | After | Items | Verdict |
|---|---|---|---|---|
| N1 | (new) | `**Lemma 12.** *Let $S$ be finite and $\pi$ a bijection of $S$. Then every orbit of $\pi$ is periodic.* *Proof.* Pigeonhole. $\square$` | none (`FU = 1`, `FS = 1`) | PASS |
| N2 | (new) | statement cites `(F)`, defined in the fixture as "$S$ is finite"; proof uses the uniform prior | none | PASS |
| N2b | (new) | `*For [Fintype Conf], card (orbit s) ∣ card Conf.*`, proof `Fintype.card` | none | PASS |
| N2c | (new) | Theorem 24(i)-style statement "*Under the uniform prior on a finite $\mathcal C_H$, ...*" (the corrected form of P-A4) | none | PASS |
| N3 | (new) | `**Proposition 13.** *A function $g$ is conserved by $\pi$ iff it is constant on the orbits of $\pi$.* *Proof.* $g \circ \pi = g$ iff $g(\pi^n s) = g(s)$ for every $n$. $\square$` | none | PASS (cardinality-neutral) |
| N4 | (new) | `*Every bijection has an inverse bijection.*`, proof neutral | none | PASS |
| N5 | — | the owner's configuration-space sentence, verbatim with $\mathcal S$, in a setup paragraph of Main | none (allowlisted; prose layer sees no gain) | PASS |
| N5b | — | the same sentence with $S$ (the #1477 rendering) in the book's ch01 Definition | none | PASS |
| N5c | — | the sentence followed by the next paragraph's unrelated text | none (whole-sentence match holds) | PASS |
| N6 | (new) | `**Theorem 14.** *Let $S$ be countably infinite and $\sigma$ the shift. Then $\sigma$ has no periodic point of period 1 outside the fixed sequences.* *Proof.* ... $\square$` | none (`IS = 1`, `GEN = 0`) | PASS; the symmetric counterpart of N1 |
| N7 | (new) | an infinite-only theorem whose proof uses Kolmogorov extension and whose statement says "Let $S$ be uncountable" | none (`IU > 0`, `IS = 1`) | PASS |
| N8 | P-G1 with a resolution: `justified`, reviewer ≠ author, `proof` citing a proof covering arbitrary $S$, current digest | unchanged | G, resolved | PASS |
| N9 | a finite-only theorem | whitespace reflowed only | none (digest unchanged) | PASS |
| N10 | `*Let $S$ be finite.*` | `*Let $S$ be finite and $\pi$ an involution.*` (narrowed) | none (`FS` kept) | PASS |
| N11 | a baseline block containing "for all $S$" | unchanged | baseline item, not an open item | PASS; listed in the baseline report |
| N12 | a finite-only theorem in ch02 and its FULL mirror, both edited identically | — | none | PASS |
| N13 | a new block whose proof cites "the finite-horizon law" and whose statement says "for a finite horizon $K$" | none (`FS = 1`) | PASS. The same text is also X-1's mechanism: `FS` counted without checking which object is finite |

## 3. Documented limits (X-cases): the tool's expected verdict is recorded, and the safeguard is review

| ID | Case | Tool's expected verdict | Why, and what catches it |
|---|---|---|---|
| X-1 | `*Each conserved quantity takes finitely many values.*` with a pigeonhole proof on $S$: a finite-scope term about another object ("finitely many values", "finite time", "finite-dimensional") satisfies `FS` while the proof uses finiteness of $S$ | PASS | `FS` is lexical. The PR review checklist line (SPEC §10) |
| X-2 | finiteness used with no listed term ("each configuration is visited before any repeats, so the walk closes") | PASS | Vocabulary incompleteness. Review; a found wording is added to `FINITE_USE` under SPEC §7 with its own case |
| X-3 | a theorem stated in unlabelled prose, using finiteness | PR layer only (SPEC §6.2) | Block recognition is by label |
| X-4 | a generality claim made by deleting a qualifier that is not a vocabulary term ("on the visible sector" removed) | PASS for rule G; any digest change re-runs A and I | Not a cardinality term; outside FIN-SCOPE's object. General claim review |

## 4. Coverage table (SPEC rule → cases)

| Rule or control | Positives | Negatives | Mutant target |
|---|---|---|---|
| A | P-A1–P-A5, P-A7 | N1, N2, N2b, N2c, N13 | P-A1, P-A2, P-A7 |
| L | P-L1–P-L9 | N9, N10 | P-L1, P-L4 |
| G | P-G1–P-G10 | N3, N5–N5c, N6, N8, N11 | P-G1, P-G3 |
| I | P-I1, P-I2 | N6, N7 | P-I1 |
| M | P-M1, P-M2 | N12 | P-M1 |
| K | P-G9, P-K1, P-K2 | N2b | — (rule K's mutant is defined with the Lean layer, owner decision O5) |
| resolutions, configuration | P-R1–P-R7 | N8 | P-R1, P-R2 |
| #1483 reuse | P-G2, P-G3, P-G4, P-R7 | N5, N5b | C-R1 |

A case is catalogued here once. A change to any expected verdict above is made before implementation
by a reviewed revision of this file, never after a run.
