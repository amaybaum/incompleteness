# FIN-SCOPE: adversarial test designs

**Status.** Writer's test plan, revision 9, WIP / UNVERIFIED, for `SPEC.md` revision 9. These are
designs: no case has been run. Every "expected" entry is the verdict the rule as written in SPEC §3 must
produce, fixed before any implementation exists, and the "why" column derives it from the counts.
Revision 2 answered review c.7064941939, revision 3 the delta review
c.7065126686, revision 4 c.7065227255, revision 5 c.7065296420, revision 6 c.7065333755,
revision 7 c.7065410306, revision 8 c.7065459234,
and revision 9 answers c.7065519776 and owner criterion 5 of c.7065520418.

**Conventions.**
- Every case is synthetic text in a fixture file and never an edit of the manuscript. Where a case is
  modelled on a real site or review finding, the source is named for provenance only. The case makes no
  claim about the current text of that site.
- "Before" is the paired before-version (SPEC §2.4). "(new)" means there is no before-version.
- "Items" is the exact set of *blocking* screen hits (SPEC §3.3) the case must produce. An extra hit
  fails the case as surely as a missing one. Advisory hits (G5, `scope-unclear`) are listed separately
  where a case produces them. Otherwise it produces none.
- Every case's block is a review-set member (SPEC §1.1) unless the case says otherwise. With no review
  record, every member FAILS; P-S1 tests this. "Verdict" is therefore the gate verdict with a *plain
  record*: an attested, current record that answers checklist items 1–4 and answers no screen hit. A
  positive FAILS with a plain record, because a blocking hit is unanswered. A negative PASSES with one.
  A case that states a fuller record gives the verdict for that record.
- The cases not in any review set are N5–N5d (setup and definition paragraphs that are neither blocks,
  claim surfaces, nor post-block paragraphs), N9 (digest unchanged), N11 (unchanged), and the
  renumbered blocks of N16. These PASS with no record.
- Wherever an older row says "resolution", read "review record" (SPEC §3.5).
- Proofs end with `$\square$` unless stated. Counts use SPEC §3.1's names, with `FS` meaning `FS_A`
  unless written `FS_L`.

## 1. Positives: cases FIN-SCOPE must catch

### 1.1 Unstated finiteness (rule A)

| ID | Before | After (statement / proof) | Why | Items | Verdict |
|---|---|---|---|---|---|
| P-A1 | (new) | *Every bijection $\pi$ of $S$ has a periodic orbit.* / By pigeonhole, $\pi^n(s)$ repeats. | FU=1 (pigeonhole), FS=0. "Every bijection" is not a carrier quantifier | {A} | FAIL |
| P-A2 | (new) | *The equilibrium weight of each configuration is $1/|S|$.* / Invariance and normalization of the uniform prior. | FU≥2 (`1/|S|`, uniform prior), FS=0. J10's `|S|` match falls in FU, so it is classified | {A} | FAIL |
| P-A3 | (new) | *Every orbit of $\pi$ on $S$ returns to its start.* / Poincaré recurrence. | FU=1, FS=0 | {A} | FAIL |
| P-A4 | (new) | *Under the uniform prior on $\mathcal C_H$, the visible law is $\mu$.* / Counting preimages. Modelled on the Theorem 24(i) finding, c.7062144714 | FU=2, FS=0 | {A} | FAIL |
| P-A5 | (new) | the statement cites `(H2)`, defined in the fixture as "$\pi$ commutes with $\tau$" / summing over $s \in S$ | FU=1 (`summing over`); (H2) carries no finite term, so FS=0 | {A} | FAIL |
| P-A7 | (new) | The allowlisted sentence ($S$ rendering), then *Every orbit is periodic.* / Pigeonhole on $S$. | The sentence is stripped before counting, so FS=0, GEN=0 and FU=1. Under the strip-after-count mutant, its "finite or infinite" counts as GEN and adds G | {A} | FAIL |
| P-A9 | (new) | *For a finite time $t$, the visible law of $\pi^t$ is the push-forward of the uniform prior.* / Counting. | "finite" stands in a sentence with no carrier, so FS=0; FU=2 | {A} | FAIL |
| P-A10 | (new) | *Every orbit of $\pi$ on $S$ is periodic.* / By Lemma 12. (Lemma 12 is N1, with FS=1) | The transitive clause gives FU=1; FS=0 | {A} | FAIL |
| P-A11 | (new) | *The observable $f$ attains its maximum on $S$.* / Take $s^\ast$ with $f(s^\ast) = \max_{s\in S} f(s)$. | FU≥2 (`attains`, `maximum`, `\max`); FS=0 | {A} | FAIL |
| P-A12 | (new) | *Let $S$ be a set, not necessarily finite. Every bijection of $S$ has a periodic orbit.* / Pigeonhole. (review B4) | `not necessarily finite` is NEG_FINITE: excluded from FS and counted in GEN. FS=0, FU=1, GEN=1 | {A, G} | FAIL |
| P-A13 | (new) | *The entropy of the equilibrium law is $\log|S|$.* / All configurations are equally likely. | FU≥2 (`\log|...|`, `equally likely`); FS=0 | {A} | FAIL |

### 1.2 Lost scope (rule L)

| ID | Before | After | Why | Items | Verdict |
|---|---|---|---|---|---|
| P-L1 | *On a finite configuration space $S$, conserved quantities are orbit-constant.* (modelled on #1483 C9 (f)) | `finite` deleted | FS_L 1→0; FU=0 | {L} | FAIL |
| P-L2 | *Each conserved quantity of $S$ is a function of finitely many components.* (NCASES N3) | `finitely many` deleted | FS_L 1→0. FU also falls to 0, so no A | {L} | FAIL |
| P-L3 | *A substratum of $N < \infty$ ontic configurations has …* (NCASES N4i) | `$N < \infty$` deleted | FS_L 1→0 | {L} | FAIL |
| P-L4 | `**Lemma 9.**` *Let $S$ be finite. Every orbit of $\pi$ is periodic.* / Pigeonhole. | `**Lemma 9'.**` *Every orbit of $\pi$ is periodic.* / Pigeonhole. | The kinds match and the Jaccard similarity is at least 0.6, so the block pairs as revised. FS_L 1→0 gives L; FU=1 with FS=0 gives A | {L, A} | FAIL |
| P-L4b | Lemma 9 as in P-L4 | the block deleted, with nothing similar added | Every disappeared block is a member (R-a), reviewed against extended item 4. This one also has FS_L+IS=1, so it raises the L hit as a pointer | {L} | FAIL with a plain record; PASS with a record answering the L hit with a `proof` that no surviving result needs the deleted lemma |
| P-L4c | `**Lemma 10.**` *Every bijection of the configuration set has a cycle through each configuration it visits twice.* / Each configuration is visited before any repeats, so the walk closes. (No scope wording: FS_L=IS=0, and the finite use is worded with no listed term, as in X-2) | the block deleted, with nothing similar added | Every deleted block is a member, unconditionally. No L hit, because FS_L+IS=0. The record must answer extended item 4: whether any surviving result relies on it, and whether the finite use it silently carried is carried elsewhere | ∅ hits | membership (deletion) | FAIL with no record; PASS with a record answering extended item 4. Under the mutant that filters deletions by `FS_L + IS > 0`, it is not a member and passes with no record |
| P-L5 | *Let $S$ be finite. Then every orbit is periodic.* / Pigeonhole. | "Let $S$ be finite." moved into the paragraph before the label, and not cited | Revised: FS_L 1→0 gives L; FU=1 with FS=0 gives A | {L, A} | FAIL |
| P-L6 | N6's statement | "Let $S$ be countably infinite." deleted | IS 1→0; FU=IU=0 | {L} | FAIL |
| P-L7 | *… for a Hamiltonian flow on compact energy surfaces* (NCASES N4j) | `compact` deleted | FS_L counts `compact`, and it falls 1→0 | {L} | FAIL |
| P-L8 | P-L1, with a resolution: `justified`, `proof: null`, valid attestation | unchanged | An L resolution needs `proof` | {L} | FAIL |
| P-L9 | P-L1, with a resolution: `justified`, `proof` cited, valid attestation, current digest | unchanged | The resolution has the right form. Whether the proof suffices is the reviewer's call | {L}, resolved | PASS |

### 1.3 Unsupported generality (rule G)

**Fixture F1**, a finite-scoped block used by the battery cases:

> `**Lemma F1.**` *Let $S$ be a finite configuration space and $\pi$ a bijection of $S$. A function
> conserved by $\pi$ takes one value on each orbit and on all its members.* / $g\circ\pi = g$ gives
> $g(\pi^n s) = g(s)$.

Its counts are FS=1, FS_L=1 and IS=GEN=PROMO=FU=IU=0.

| ID | Before | After | Why | Items | Verdict |
|---|---|---|---|---|---|
| P-G1 | (new) | *For every $S$, finite or infinite, the conserved quantities are the orbit-constant functions.* | carrier quantifier plus NEG_FINITE: GEN=2 (G1) | {G} | FAIL |
| P-G2 | F1 | each battery case of §1.4, inserted after "members" | the per-case clause in §1.4 | {G} for each case | FAIL for each |
| P-G5 | F1 | `, and this is proved` (#1483 C9 (d)) | PROMO 0→1 (G3) | {G} | FAIL |
| P-G6 | F1 | `; the identity holds unconditionally` | PROMO 0→1 (G3) | {G} | FAIL |
| P-G7 | *On a finite configuration space $S$, the near-return condition holds for $\pi$.* | *For every infinite system, the near-return condition holds for $\pi$.* (modelled on #1483 C9 (a)) | FS_L 1→0 gives L; the carrier quantifier "for every … system" gives GEN 0→1 (G3) | {L, G} | FAIL |
| P-G8 | P-G1, with a resolution: `justified`, `proof: null`, valid attestation | unchanged | A G resolution needs `proof` | {G} | FAIL |
| P-G9 | (new) | *For every substratum, conserved quantities are orbit-constant.*, with the census resolving an anchor whose type has `FiniteConf` | GEN=1 (G1). The anchor binder with GEN>0 gives K | {G, K} | FAIL |
| P-G10 | (claim surface: abstract) | the added sentence "OI's conservation laws hold for configuration spaces of any size." | a new sentence with `of any size` (G1); the abstract is gating | {G} | FAIL |
| P-G11 | (new) | *The visible law converges as $N \to \infty$.*, where the block does not declare $N$ | J10's `\to\infty` matches, falls in no class and in no neutral context. G5 is advisory | ∅; advisory {G5} | PASS with a plain record. It is a positive for the advisory output only: the G5-output mutant must fail it |

### 1.4 The #1483 battery on F1 (control C-R4)

Each string is inserted into F1 after "members". Clause G3 is a rise in GEN or PROMO, G4 a rise in IS
while FS>0, and G5 an unclassified J10 match.

| # | Inserted text (from #1483) | Clause |
|---|---|---|
| 1 | for arbitrary $S$ | G3 (carrier quantifier) |
| 2 | regardless of cardinality | G3 |
| 3 | in the infinite case | G4 |
| 4 | for infinite $S$ | G4 |
| 5 | when $|S| = \infty$ | G4 |
| 6 | for $S$ of any size | G3 |
| 7 | for countable or uncountable $S$ | G3 (NEG_FINITE), G4 |
| 8 | for every $S$, finite or not | G3 |
| 9 | without any finiteness assumption | G3 |
| 10 | whatever the cardinality of $S$ | G3 |
| 11 | including the infinite case | G3, G4 |
| 12 | for all $S$ | G3 |
| 13 | also for infinite $S$ | G3, G4 |
| 14 | regardless of the cardinality of the configuration space | G3 |
| 15 | and $S$ may be finite or infinite; the result holds in either case | G3 (NEG_FINITE; this is not the whole allowlisted sentence) |
| 16 | the configuration space $S$ may be finite or infinite, and the statement holds in both cases | G3 |
| 17 | , for unrestricted $S$ | G3 |
| 18 | , for non-finite $S$ | G3 |
| 19 | , for $S$ not finite | G3 |
| 20 | ; $S$ need not be finite | G3 |
| 21 | (also when $S$ is not finite) | G3 |
| 22 | (including non-finite $S$) | G3 |
| 23 | , for unboundedly large $S$ | G3 |
| 24 | , irrespective of $|S|$ | G3 |
| 25 | , for $S$ large or small | G3 |
| 26 | ; no assumption on $|S|$ is made | G3 |
| 27 | , holding uniformly in $S$ | G3 |
| 28 | . This extends beyond the finite setting | G3 |
| 29 | , for $|S|\geq\omega$ | G4 |
| 30 | , for $S$ of continuum size | G4 |
| 31 | , in the transfinite case | G4 |
| 32 | , for $\mathbb{N}$-indexed configuration sets | G4 |
| 33 | , for in\-finite $S$ | G4 (after normalization) |
| 34 | , for in(soft hyphen)finite $S$ | G4 (after normalization) |
| 35 | , for inf(Cyrillic і)nite $S$ | G4 (after normalization) |
| 36 | [^gen], where the fixture file defines `[^gen]: The identity holds for every infinite system.` | G3, G4 (after footnote expansion with file text) |
| 37 | , for $|S| = 2^{\aleph_0}$ | G4 |
| 38 | , for every size of $S$ | G3 |
| 39 | , for every one of the possible $S$ | G3 (the first math expression after "every" is `$S$`) |
| 40 | , for any $S$ whatsoever | G3 |
| 41 | , for $|S|=\aleph_0$ | G4 |
| 42 | , as $N\to\infty$ | none blocking; advisory G5 (F1 does not declare $N$) |
| 43 | , for $\kappa$ any cardinal | G3, with an advisory G5 for `\kappa` |
| 44 | , for $S$ countable or not | G3 |
| 45 | the allowlisted sentence + "This identity is independent of $|S|$" (ALLOW_PLUS) | G3 |
| 46 | the allowlisted sentence + "It holds for each such $S$" (ALLOW_PLUS) | G3 |

Every row except 42 must produce exactly {G} as its blocking hits, and in particular no L: no row
removes a finite-scope term, because NEG_FINITE matches are excluded from FS_L both before and after.
Row 42 produces no blocking hit and the advisory G5. It remains in the review set, where checklist
item 3 covers it.

### 1.5 Silent infiniteness, mirrors, kernel, parsing (rules I, M, K, P)

| ID | Before | After | Why | Items | Verdict |
|---|---|---|---|---|---|
| P-I1 | (new) | *The law $\mu$ on $S$ is determined by its values on cylinder sets.* / By countable additivity of $\mu$. | IU=1; IS=GEN=0 | {I} | FAIL |
| P-I2 | (new) | *The horizon laws $\mu_K$ have a common extension $\mu$ on $S$.* / Kolmogorov extension. | IU=1; IS=GEN=0 | {I} | FAIL |
| P-M1 | ch02 and its FULL mirror both: *Under the uniform prior on a finite $\mathcal C_H$, the visible law is $\mu$.* | FULL only: `a finite` → `the` | On the FULL block, FS_L 1→0 gives L, and FU=1 with FS=0 gives A. The mirror counts now differ, giving M | {L, A, M} on FULL | FAIL |
| P-M2 | a mirror pair, both F1 | FULL only gains `, for arbitrary $S$` | G3 on FULL; GEN differs, giving M | {G, M} on FULL | FAIL |
| P-K1 | (new) | *Every bijection of the configuration space has a nontrivial conserved quantity.*, with the census resolving an anchor whose type carries the finiteness predicate | the anchor has a binder and FS=0; FU=0 | {K} | FAIL |
| P-K2 | — | a Lean module adds `instance : Fintype Conf := sorry` | the existing `lean-axioms` step fails it; the Lean layer reports an unproved binder | the lean-axioms failure | FAIL (cross-check) |
| P-B1 | (new) | a `**Lemma.**` block whose `*Proof.*` reaches the next label without a closer | rule P | {P} | FAIL |
| P-B2 | — | a label form outside the grammar, for example `**Main Theorem.**`, at enrollment | the inventory check (SPEC §2.3, V12) reports an unrecognized form | the inventory failure | FAIL |

### 1.6 Resolution and configuration abuse

| ID | Case | Expected |
|---|---|---|
| P-R1 | P-A1 with a record whose attestation fails the O6 standard (SPEC §3.6): the reviewer's role is the writer's role, or the conflict disclosure is missing | unresolved, {A}, FAIL |
| P-R2 | P-A1 resolved, then one proof token edited | the digest no longer matches; unresolved, FAIL |
| P-R3 | a record whose exact-head identification names a different commit or digest than the member's current ones | the offline form check fails; FAIL. A record on a different PR, or evidence not separate from the writer's, is caught by PR review against the host |
| P-R4 | a commit adds an allowlist entry to FIN-SCOPE's own configuration | FAIL (FIN-SCOPE has no allowlist of its own) |
| P-R5 | a commit deletes `pigeonhole` from FU, with no case and no owner decision | FAIL |
| P-R6 | a commit raises a block's recorded FS_L in `baseline.json` and lowers it in the manuscript | the recomputation from the merge base differs; FAIL |
| P-R7 | the pinned `verdict.py` blob replaced by a copy with an empty `INFINITY_TERMS` | VOID, with no item verdicts |
| P-R8 | a commit deletes an entry from `resolutions.json` | the append-only check fails; FAIL |

## 2. Negatives: cases FIN-SCOPE must pass

| ID | Before | After (statement / proof) | Why | Items | Verdict |
|---|---|---|---|---|---|
| N1 | (new) | *Let $S$ be finite and $\pi$ a bijection of $S$. Then every orbit of $\pi$ is periodic.* / Pigeonhole. | FS=1, FU=1; GEN=0 | ∅ | PASS |
| N2 | (new) | the statement cites `(F)`, defined in the fixture as "$S$ is finite" / uniform prior | the local hypotheses include (F), so FS=1 | ∅ | PASS |
| N2b | (new) | *Assume `[Fintype Conf]`. Every orbit of `π : Conf ≃ Conf` has at most `Fintype.card Conf` elements.* / `Fintype.card` bound. | the Lean binder gives FS=1; FU=1 | ∅ | PASS |
| N2c | (new) | *Under the uniform prior on a finite $\mathcal C_H$, the visible law is $\mu$.* / Counting preimages. | "finite" stands with the carrier $\mathcal C_H$, so FS=1; FU=2 | ∅ | PASS |
| N3 | (new) | *A function $g$ is conserved by $\pi$ iff it is constant on the orbits of $\pi$.* / $g\circ\pi = g$ iff $g(\pi^n s) = g(s)$ for every $n$. | FU=IU=0. G does not read the proof | ∅ | PASS (cardinality-neutral) |
| N4 | (new) | *Every bijection of $S$ has an inverse bijection.* / Neutral. | no class is counted | ∅ | PASS |
| N5 | — | the owner's sentence, verbatim with $\mathcal S$, in a setup paragraph of Main (not a block and not a claim surface) | allowlisted; the advisory layer sees no gain | ∅ | PASS |
| N5b | — | the same sentence with $S$, in a Definition paragraph of ch01 | the same | ∅ | PASS |
| N5c | — | the sentence followed by an unrelated next paragraph | it is matched as a whole sentence | ∅ | PASS |
| N5d | — | the sentence written `$\mathcal{S}$`, with braces | pre-normalization maps it to `\mathcal S` before allowlist stripping | ∅ | PASS |
| N5e | (new) | the allowlisted sentence, then *Let $S$ be finite. Every orbit is periodic.* / Pigeonhole. | stripping leaves FS=1, FU=1 and GEN=0 | ∅ | PASS |
| N6 | (new) | *Let $S$ be countably infinite. Then $S$ admits a bijection $\pi$ with $\pi^n(s) \neq s$ for every $s \in S$ and every $n \geq 1$.* / Identify $S$ with $\mathbb Z$ and set $\pi(n) = n + 1$. | IS=1, FS=0 (so no G2), GEN=0 (the quantifiers' objects are $s \in S$ and $n$, not carriers), FU=IU=0 | ∅ | PASS; the symmetric counterpart of N1 |
| N7 | (new) | *Let $A$ be a countable alphabet and $S = A^{\mathbb N}$. Every consistent family of laws on the finite products $A^{\{1,\dots,K\}}$ extends uniquely to a law on $S$.* / Kolmogorov extension, $A$ being standard Borel. | IU=1; IS=1 (`\mathbb N` indexes the carrier $S$), so no I. "the finite products" stands in a sentence with the carrier $S$, but it is not a positive predication about a carrier, so FS_A=0 and no G2. That occurrence raises `scope-unclear` | ∅; advisory {scope-unclear} | PASS |
| N8 | P-G1 | a resolution: `justified`, `proof` citing a proof that covers arbitrary $S$, an attestation valid under the O6 option, current digest | the right form | {G}, resolved | PASS |
| N9 | N1 | whitespace reflowed only | the digest is unchanged | ∅ | PASS |
| N10 | N1 | `and $\pi$ a bijection of $S$` → `and $\pi$ an involution of $S$` | revised; FS_L kept; no rise in GEN, PROMO or IS | ∅ | PASS |
| N11 | a baseline block containing "for all $S$" | unchanged | its digest is in the baseline, so it is a baseline item | ∅ open; one baseline item | PASS |
| N12 | the ch02 block and its FULL mirror, both: *Let $S$ be finite. Every orbit of $\pi$ is periodic.* / Pigeonhole. | both changed identically to *Let $S$ be finite and $\pi$ a bijection of $S$. Every orbit of $\pi$ is periodic.* | each is revised with FS_L kept and FS=1, FU=1; the mirror counts are equal | ∅ | PASS |
| N13 | (new) | *Let $\mathcal C_H$ be finite. The horizon-$K$ visible law is the push-forward of the uniform prior on $\mathcal C_H$.* / Counting preimages. | FS=1 ("finite" with the carrier $\mathcal C_H$); FU=2 | ∅ | PASS |
| N14a | N1 | `Let $S$ be finite` → `Let $S$ be finite (the finiteness hypothesis)` | FS_L rises. J10's `finiteness` match falls in FS_L, so it is classified. No G. "finiteness" is not a positive predication, so it raises `scope-unclear` | ∅; advisory {scope-unclear} | PASS |
| N14b | N3 | `Let $S$ be countably infinite.` prepended | IS 0→1 with FS=0: a narrowing, so no G4. GEN=0 | ∅ | PASS |
| N14c | N1 | `under the uniform prior` added to the statement | FU rises with FS=1. J10's `uniform` match falls in FU | ∅ | PASS |
| N14d | N1 | `with weight $1/|S|$` added | the same, for `|S|` | ∅ | PASS |
| N14e | N1 | `for every $n \geq 1$` added | J10's quantifier matches fall in the neutral context (the object is not a carrier) | ∅ | PASS |
| N15 | (new) | *Let $S$ be finite. For every $s \in S$, the orbit of $s$ is periodic.* / Pigeonhole. | FS=1, FU=1. The object of "for every" is $s \in S$, so GEN=0 | ∅ | PASS |
| N16 | Lemmas 3–5 of a fixture file, citing each other | a new N1-style lemma inserted before Lemma 3; Lemmas 3–5 become 4–6 and their citations are retargeted | the masked digests are unchanged, so they pair in step 1. The new block has no item | ∅ | PASS |
| N17 | (new) | N1 with its proof closed by `$\blacksquare$` | the closer is recognized, so no P | ∅ | PASS |
| N18 | two `**Corollary.**` blocks in one FULL segment | the second narrowed as in N10 | the first pairs by digest, the second by content (revised); nothing fires | ∅ | PASS |
| N19 | (new) | *Every partial order on $S$ in which every chain has an upper bound has a maximal element.* / Zorn's lemma. | Zorn is not IU; `maximal` is not FU; GEN=0 | ∅ | PASS |
| N20 | (new) | *Let $X$ be a compact metric space and $f$ continuous on $X$. Then $f$ is bounded.* / The finite subcover of the preimages of open intervals. | FU=0, so no A. Compact and bounded count only for FS_L | ∅ | PASS |
| N21 | (new) | *For horizon $K$, the visible laws $\mu_K$ converge as $K \to \infty$.* | `\to\infty` applies to a declared horizon, which is a neutral context; no IS, no IU | ∅ | PASS |

### 2.1 Cases added in revision 3 (delta review c.7065126686)

"Route" says how the case reaches review: through a blocking screen hit, through an advisory hit, or
through review-set membership alone.

| ID | Before | After (statement / proof, or change) | Why | Items | Route | Verdict |
|---|---|---|---|---|---|---|
| P-S1 | (new) | N3's block, with no review record | It is a review-set member (R-a) with no record, although the screen is clean | ∅ | membership | FAIL with no record; PASS with a plain record |
| P-N1 | (new) | *Without assuming finiteness of $S$, every bijection of $S$ has a periodic orbit.* / Pigeonhole. (R1) | "finiteness of $S$" is not a positive predication, so FS_A=0; FU=1. GEN=0. J10's `finiteness` falls in FS_L | {A}; advisory {scope-unclear} | screen | FAIL |
| P-N2 | (new) | *$S$ is not assumed finite. Every bijection of $S$ has a periodic orbit.* / Pigeonhole. (R1) | `$S$ is finite` does not match; FS_A=0 | {A}; advisory {scope-unclear} | screen | FAIL |
| P-N3 | (new) | *$S$ is not assumed to be finite. …* as P-N2 (R1) | `be finite` is not preceded directly by `$S$`; FS_A=0 | {A}; advisory {scope-unclear} | screen | FAIL |
| P-N4 | (new) | *Finiteness of $S$ is not required. …* as P-N2 (R1) | FS_A=0 | {A}; advisory {scope-unclear} | screen | FAIL |
| P-B3 | (new) | `**Proposition 2.**` *The equilibrium weight of each configuration is $1/|S|$.* (no proof), followed by the ordinary paragraph "Here $S$ is finite." (R2) | The extent is the label paragraph, so the next paragraph supplies nothing: FS_A=0, FU=2. The next paragraph is the post-block paragraph, with GEN=IS=0, so no E | {A} | screen | FAIL |
| P-B4 | (new) | *Every orbit of $\pi$ on $S$ is periodic.* / `**Proof.**` Pigeonhole. $\square$ | The bold opener is recognized, so the proof's FU=1 counts; FS_A=0 | {A} | screen | FAIL |
| P-D1 | the block *Every orbit of $\pi$ on $S$ is periodic.* / By Lemma 3. (Lemma 3 is N3, neutral) | the citation retargeted to Lemma 7 (Lemma 7 is N1, FS_A=1) (R3) | The masked digest is unchanged, but the resolved targets changed, so the block is revised. The transitive clause gives FU=1; FS_A=0 | {A} | screen | FAIL |
| P-D2 | Lemma 12 is N3 (neutral), and block C reads *Every orbit of $\pi$ on $S$ is periodic.* / By Lemma 12. | Lemma 12 narrowed to N1's form, *Let $S$ be finite. …*; C unchanged (R3) | Lemma 12's change is free (N10-type, no hit), but its FS_A changed, so C joins the review set by closure (R-b). On C, the transitive clause gives FU=1; FS_A=0 | {A} on C | screen (on a dependent) | FAIL |
| P-E1 | (new) | N1, with the proof "Pigeonhole; hence the identity holds for every $S$, finite or infinite." | Rule E: GEN=2 in the proof (carrier quantifier, NEG_FINITE). The statement keeps FS_A=1 and FU=1 | {E} | screen | FAIL |
| P-E2 | N1, unchanged | the post-block paragraph "It follows that the result holds for all $S$." added after N1's proof | The changed post-block paragraph puts N1 in the review set (R-c). Rule E: GEN=1 there | {E} on N1 | screen | FAIL |
| N22 | (new) | *Under the hypotheses of Theorem 3, let $S$ be finite. Every orbit of $\pi$ is periodic.* / Pigeonhole. (R4) | The citation masks to `#ref`, so no `theorem` reaches J10. FS_A=1, FU=1 | ∅ | membership | PASS |
| N23 | (new) | *Let $S$ be finite. The orbit decomposition derived in §2 is unique.* / Neutral. (R4) | On a new block, `derived` is a neutral context | ∅ | membership | PASS |
| N24 | (new) | *Let $S$ be finite. For every $n \in \mathbb N$, $\pi^{n\,|S|!} = \mathrm{id}$.* / Orbit lengths divide $|S|!$. (R4) | `\mathbb N` does not index a carrier, so IS=0 and there is no G2. `for every $n \in \mathbb N$` is one neutral quantifier span (SPEC §3.1), so J10's `for every`, `every $` and `\mathbb N` matches inside it are classified, and no G5 is raised. FS_A=1, FU=1 (`|S|` as a number) | ∅ | membership | PASS |
| N25 | (new) | *Let $S$ be finite, of cardinality $N$. The bound holds uniformly in $t$, is independent of the initial state, holds in general, and the horizon is unlimited.* (R4) | `of cardinality $N$` is neutral. The rest are unclassified J10 matches, which are advisory only, counted per merged span (SPEC §3.1): `uniformly`, `independent of`, `in general` (one span, although two J10 patterns match it) and `unlimited`. GEN=0 | ∅; advisory {G5 ×4 spans} | membership | PASS |
| N26 | (new) | *Let $X$ be a finite set and $\pi$ a bijection of $X$. Every orbit of $\pi$ is periodic.* / Pigeonhole. (R5) | $X$ is declared, so it is a carrier for this block, and `a finite set` is a positive predication: FS_A=1 | ∅ | membership | PASS |
| N27 | (new) | *Let $\mathcal H$ be a finite-dimensional Hilbert space and $\rho$ a density operator on $\mathcal H$. Then $\mathrm{tr}\,\rho^2 \le 1$.* / The eigenvalues of $\rho$ lie in $[0,1]$ and sum to 1. (R5) | `a finite-dimensional Hilbert space` is a positive predication about a declared carrier: FS_A=1; FU=1 (`\mathrm{tr}`) | ∅ | membership | PASS |
| N28 | (new) | `**Proposition 3.**` *Let $S$ be finite. Every orbit of $\pi$ is periodic.* (no proof), followed by the paragraph "The next section treats the gauge group." (R2) | The extent is the label paragraph. FU=0. The post-block paragraph has no GEN or IS | ∅ | membership | PASS |

### 2.2 Cases added in revision 4 (c.7065227255)

| ID | Before | After (statement / proof, or change) | Why | Items | Route | Verdict |
|---|---|---|---|---|---|---|
| P-H1 | the node "(F): $S$ is finite." and block N2, which cites (F) and has a uniform-prior proof | (F) edited to "(F): $S$ is a set." N2 unchanged (C1) | (F) is a changed node, so it is a member (R-e). N2's hypothesis digest changed, so N2 is a member (R-a, R-b). On N2, FS_A=0 and FU=1 | {A} on N2; ∅ on (F) | screen, on a dependent of a node | FAIL |
| P-H2 | the standing sentence "Throughout this section, $S$ is finite." and, in that section, P-A1's block | the standing sentence deleted (C1) | The node is a deleted member. The block cites it implicitly, so its hypothesis digest changed. FS_A=0 and FU=1 | {A} on the block | screen, on a dependent of a node | FAIL |
| N30 | the node "(H3): $\pi$ is an involution." with no citing block | reworded to "(H3): $\pi^2 = \mathrm{id}$." | The node is a member, with no dependents and no hits | ∅ | membership | PASS |
| P-C2 | (new) | the label paragraph `**Theorem B.9.** *Let $\pi$ be a bijection of $S$. Then:*`, then `*(i) every orbit is periodic;*`, `*(ii) …*`, `$$\pi^{N} = \mathrm{id}$$`, `*so that …*`, then `*Proof.* Pigeonhole. $\square$` (modelled on appendix B's Theorem B.3.2 form) (C2) | A proof opener occurs before the next label, so the statement runs to it and the proof is recognized. FU=1; FS_A=0 | {A} | screen | FAIL. Under the first-paragraph-only mutant the proof is missed, FU=0, and the case gives ∅ |
| P-C3 | (new) | as P-C2, with an interposed ordinary paragraph "For finite $S$ this is classical." between the clauses and the proof (C2) | Interposed prose is not local hypotheses, so FS_A=0. FU=1 | {A} | screen | FAIL. Under the interposed-prose mutant it would give ∅ |
| N29 | (new) | P-C2 with clause `*(i)*` reading `*(i) if $S$ is finite, every orbit is periodic;*` | `$S$ is finite` is a positive predication in a statement paragraph: FS_A=1; FU=1 | ∅ | membership | PASS |
| P-D3 | Lemma L is N3 (neutral). B1–B5 cite L; C1–C4 cite B1; D1–D3 cite C1. None of B, C, D states finiteness; B1–B5 have neutral proofs | L narrowed to N1's form; nothing else changes | The review set is L plus its transitive dependents: 1 + 5 + 4 + 3 = 13 members, or 26 if all are book blocks with FULL mirrors. The transitive clause gives FU=1 on B1–B5, whose cited L now has FS_A=1. C and D cite blocks with FS_A=0, so they get no transitive FU | {A} on each of B1–B5; ∅ on L, C1–C4 and D1–D3 | screen on 5; membership on 8 | FAIL; the expected review-set size is 13 |
| P-R9 | a PR renaming `$\mathcal C_H$` to `$\mathcal H_c$` in 20 blocks under one batched record (r1) | — | `\mathcal C_*` is a carrier symbol, so the map fails the (r1) limit and is refused for batching. Every member needs its own record. On each block whose finite predication was `finite $\mathcal C_H$`, FS_A falls to 0: A fires where there is finite use, and the block's dependents join by closure | refused batch; {A} on each such block with finite use | membership, plus the screen | FAIL with only the batched record |
| P-R10 | a map deleting the word `finite` at 40 sites, under one batched record | — | `finite` is a `FINITE_TERMS` token, so the map is refused for batching. Every member needs its own record, and each raises L | refused batch; {L} on each of 40 | membership, plus the screen | FAIL with only the batched record |
| N31 | a map renaming the non-carrier symbol `$\tau$` to `$\sigma_1$` in 12 blocks, under one batched record | — | Neither side holds a screen token or a carrier, and no member's counts or hypothesis digest change. All 12 diffs are exact instances | ∅ | membership (one batched record) | PASS with the batched record |
| P-R11 | Lemma M is N3; block D cites M and is unchanged | M narrowed with "Let $S$ be countably infinite." D's reduced (r3) record answers items 1 and 4 only | M's IS changed, so D joins by closure. A reduced record must answer items 1, 2 and 4, and this one lacks item 2 | ∅ hits on D | membership (closure) | FAIL; PASS once item 2 is answered |
| P-H4 | a fixture in the corpus's shape: the canonical `**(C1) Non-zero coupling.** … the configuration space is finite …` in a Main-like file; a restatement copy `(C1) **Coupling.** …` in a Structure-like file; and a block in a GR-like file citing `(C1)` by bare name, with a pigeonhole proof and FS_A drawn from (C1)'s text | "is finite" dropped from the canonical definition (C1, cross-file) | (C1) is mapped, so the GR citer resolves to its group. The canonical definition changed, so the group (canonical and restatement) and every citer are members. On the GR block, FS_A=0 and FU=1. The restatement's agreement with the canonical text is a checklist answer on it | {A} on the GR block; ∅ on the group's nodes | screen, on a cross-file dependent; membership for the group | FAIL. Under the mutant that resolves names only within the citing file, the GR block is not a member and the case gives ∅ |
| P-H6 | the P-H4 fixture with (C3) mapped, and a block citing `(C1)–(C4)` | (C3)'s canonical text edited | The range expands to (C1), (C2), (C3) and (C4), so the block cites (C3)'s group and is a member | ∅ hits unless its counts change | membership (range) | FAIL with no record; PASS with a plain record. Under the no-expansion mutant the block is not a member |
| P-H7 | `(EM)` canonical as an inline run-in span inside a `**Setup.**` paragraph (the Main:756 shape); one block citing "conditional on (EM)"; one using the alias "the effective-mixing hypothesis" | the italic statement inside the run-in span edited | The inline span is the node, so it is a member. Both citers are members, the second through the alias | ∅ hits unless counts change | membership (inline node, alias) | FAIL with no record; PASS with plain records |
| P-H8 | the P-H4 fixture | only the restatement copy in the Structure-like file edited | A change to any node of the group makes the canonical definition, every copy and every citer, in every file, members. The reviewer answers whether the restatement still agrees with the canonical text | ∅ hits | membership (group) | FAIL with no record. Under the mutant where a copy change reaches only the copy's own citers, the GR citer and the canonical definition are missed |
| P-H9 | the P-H4 fixture | a new paragraph `**(C1)** In the lattice setting …` added to a fourth file, with `canonical.json` unchanged | A node-form paragraph for a mapped name that the map does not list | gate failure (V26) | configuration | FAIL until the same PR adds it to the map as a copy, with its kind and a review record |
| P-H10 | the P-H4 fixture | the canonical paragraph moved unchanged to another section of its file, with `canonical.json` unchanged | It pairs by digest, so its content is unchanged, but the map's anchor no longer resolves at its recorded site | gate failure (V26) | configuration | FAIL. PASS when the same PR updates the anchor with a review record stating that the anchor moved and the text did not |
| N32 | (new) | *Let $f$ be of class C1 on a compact interval.* | A bare `C1` counts as a citation only inside a range or after `condition(s)`, so this is not a citation of (C1) | ∅ | membership (new block) | PASS |
| P-H5 | (a name outside the canonical map) `(F)` defined in both `papers/SM.md` and `papers/GR.md`, not as mirrors; a block in `papers/Structure.md` cites `(F)` by bare name | — | the name is ambiguous, so the enrollment inventory fails (V12, V22) | inventory failure | inventory | FAIL |

### 2.2a Copy forms (c.7065410306)

These cases use fixtures in the corpus's real shapes. The canonical definition in each is
`**(C1) Non-zero coupling.** … the configuration space is finite …`, in a Main-like file.

| ID | Before | Change | Why | Items | Route | Verdict |
|---|---|---|---|---|---|---|
| P-H11 | a Medicine-like file with the unparenthesised copy `**C1 (Coupling).** …`; a block in an SM-like file citing `(C1)` by bare name, with a pigeonhole proof and FS_A drawn from the group's text | only the Medicine-like copy edited | The unparenthesised form is a node form for a mapped name, so the copy is in (C1)'s group. A change to any node makes the canonical definition, every copy and every citer, in any file, members. The reviewer answers whether the copy still agrees with the canonical text | ∅ hits | membership (group) | FAIL with no record. Under the parenthesised-only mutant the copy is not a node, and nothing becomes a member |
| P-H12 | a ch01-like table `\| C1 \| Coupling \| … \|` and its FULL mirror row | the chapter's row edited, and the FULL row not | The table row is a copy, so the group and its citers are members. The two mirror rows differ, which raises M | {M} | screen (M), membership (group) | FAIL |
| P-H13 | the glossary-like copy `**C1 (Coupling).** …` in `book/glossary.md`, and its FULL `# Glossary` copy | both edited identically | The glossary is a surface, and its FULL segment pairs with it (§3.4). Both copies are in the group, so the group and every citer are members. The mirror texts are equal, so there is no M | ∅ hits | membership (group) | FAIL with no record. Under the glossary-not-a-surface mutant only the FULL copy is seen |
| P-H14 | the P-H11 fixture | a new paragraph `**C2 (Memory).** …` added to a new paper, with `canonical.json` unchanged | An unparenthesised copy of a mapped name, not in the map (V26) | gate failure | configuration | FAIL until the same PR adds it to the map as a copy, with its kind and a review record |
| P-H15 | a Medicine-like list `- **C1:** The kinase domain is coupled …` | the list item edited | The list-item form is a node form, so the item is an application copy, and its edit makes the group and its citers members | ∅ hits | membership (group) | FAIL with no record |

### 2.2b The occurrence register (c.7065459234)

Under revision 8, every occurrence of a mapped name is classified in `occurrences.json` by a recorded
review. P-H11–P-H15 hold with their copies classified as copies.

| ID | Before | Change | Why | Items | Route | Verdict |
|---|---|---|---|---|---|---|
| P-H16 | a ch18-form plain list item `- C1 (coupling): the subsystem must interact non-trivially …`, classified as a copy (restatement), with its FULL mirror; a block in a GR-like file citing `(C1)` | the chapter's list item edited | The edited item is a copy of (C1), as the register records, so the group and every citer in any file are members. Its digest changed, so its classification is voided and must be renewed. The FULL mirror now differs, which raises M | {M} | membership (group), screen (M) | FAIL with no records; PASS once the item is reclassified, the mirror is updated or answered, and the members have records |
| P-H17 | a ch01-form opening paragraph `C1 requires non-trivial coupling between visible and hidden …`, classified as a copy (restatement) | its text edited | The same as P-H16: the register, not the form, makes it a node. The group and its citers are members, and it needs reclassification | ∅ hits | membership (group) | FAIL with no records |
| P-H18 | the P-H16 fixture | a new paragraph `C1 requires that the subsystem be finite …` added to a new paper, with no `occurrences.json` entry | An unclassified occurrence of a mapped name | gate failure (V26) | configuration | FAIL until it is classified by a recorded review. As a copy, its group and citers are then members |
| P-H19 | a paragraph citing `(C2)`, classified as a citation | its text edited so that it now restates (C2) | Its digest changed, which voids the classification, so it blocks until it is reclassified. The reviewer reclassifies it as a copy, and it then joins the group | gate failure until reclassified | configuration | FAIL until reclassified |
| N33 | GR:629-form `(C1$'$) *Emergent action scale.* …`, classified as unrelated with its reason | unchanged | It is classified, and nothing depends on it | ∅ | none | PASS |

### 2.2c Units, normalization and fidelity (c.7065519776, c.7065520418)

| ID | Before | Change | Why | Items | Route | Verdict |
|---|---|---|---|---|---|---|
| P-H20 | a heading `### C1 (coupling)` over a body that defines the condition without naming it, the heading unit classified as a copy | one body sentence edited | The heading unit spans its section, so the edit voids its classification. As a copy, its group and the citers are members | gate failure until reclassified | configuration, membership (group) | FAIL until reclassified |
| P-H21 | the lead-in "The conditions C1–C4 are:" and four unnamed list items defining them, classified as one list unit with a class per item | the third item edited | The list is one unit, because its lead-in names the conditions. The edit voids the unit's classification, and the item's class (a copy of (C3)) makes (C3)'s group members | gate failure until reclassified | configuration, membership (group) | FAIL until reclassified |
| P-H22 | — | a new paragraph `С1 requires …` with a Cyrillic `С` (U+0421), unclassified | After #1483's normalization it reads `C1`, so it is an occurrence, and it is unclassified | gate failure (V26) | configuration | FAIL. Under the unnormalized-matcher mutant it is not an occurrence |
| N35 | — | a paragraph with `$C_1, \ldots, C_k$` and no other mention | Subscripted symbols are the stated exclusion, so this is not an occurrence | ∅ | none | PASS |
| P-F1 | an exact copy (a mirror restatement identical to the canonical text after normalization) | the canonical text edited, and the copy not | The exact class is checked mechanically, and the identity now fails, so the class is void | gate failure until the copy is updated or reclassified | configuration, membership (group) | FAIL |
| N34 | the exact copy of P-F1 | unchanged, with the canonical text unchanged | The identity holds, and no equivalence attestation is needed | ∅ | none | PASS |
| P-F2 | an equivalent paraphrase (the Medicine:27 shape), attested against canonical digest d₀ | the canonical text edited, giving digest d₁ | The attestation names d₀, so it is void, and the copy blocks until it is re-attested against d₁ | gate failure until re-attested | configuration, membership (group) | FAIL |
| P-F3 | — | a new restatement of (C2) reading "C2 (timescale separation): the hidden sector relaxes much faster than the visible sector", classified as different | A different formulation is a blocking finding, routed to reconciliation | gate failure until resolved by one of the three routes | configuration | FAIL |
| P-F5 | the corpus finding, as found: the ch01-table row `\| C2 \| Timescale separation \| …` (ch01:252, FULL:585) against the canonical Main:74 "(C2) Memory persistence" | at enrollment, the classifier classes the row as `different` | A different formulation blocks enrollment and the gate until it is aligned, renamed as a distinct condition, or accepted by an owner decision naming the formulation its citers depend on. No baseline tolerance applies | enrollment failure | configuration | FAIL until resolved. If the classifier instead attests the row as an equivalent paraphrase, with a reason, it passes. That judgement is the classifier's, and this test fixes only the consequence of each class |
| P-F6 | the canonical `(C2)` (the Main:74 shape) defines both `C2-structural` and `C2-slow`; a copy reproduces only the `C2-structural` form, verbatim; a block citing the copy relies on `C2-slow` | the copy classed `exact` | It equals only a span of the canonical text, so it is not exact (F1). With its citer relying on the omitted `C2-slow`, no equivalence attestation can say the omission is not relied on, so it is `different` | gate failure | configuration | FAIL as exact. It stays blocking as `different` until it is resolved by one of the three routes |
| P-F4 | an occurrence classified as an exact copy whose text differs from the canonical text by one word | — | The mechanical identity check fails, so a paraphrase cannot be passed off as an exact copy | gate failure | configuration | FAIL until reclassified as equivalent (with an attestation) or different |

### 2.2d Governance and controls (addendum c.7065535973)

| ID | Before | Change | Why | Items | Route | Verdict |
|---|---|---|---|---|---|---|
| P-GV1 | enrollment over a corpus fixture in which one name-led opener (the ch01:203 shape) is `pending` | enrollment attempts to publish `baseline.json` | Pending is a blocking state, and baseline tolerance never covers occurrences | enrollment failure | configuration | FAIL |
| P-A1m | a paragraph mentioning `C1` and `C2`, with an entry for `C1` only | — | Entries are per name, so the `C2` entry is missing | gate failure | configuration | FAIL |
| P-A2m | in a GR:629-like file, a `C1` mention next to the `(C1$'$)` set, with an entry that does not say which set it belongs to | — | A mention that could belong to two mapped sets must be resolved to exactly one, with a reason | gate failure | configuration | FAIL |
| P-A3m | an entry naming `(C5)` or an anchor that the map lacks | — | an incorrect mapping | gate failure | configuration | FAIL |
| P-A4m | a second `canonical` entry for `(C2)` | — | one canonical definition per name | gate failure | configuration | FAIL |
| P-A5m | a unit mentioning only `C2`, filed as a copy of `(C3)` | — | the entry's name is not among the unit's mentions | gate failure | configuration | FAIL |
| P-S2 | a name-led opening paragraph classified `citation` by one classifier | — | Name-led units classed as citation or unrelated need two agreeing classifiers, so the unit stays pending | gate failure | configuration | FAIL until a second classifier agrees, or the unit is reclassified |
| P-S3 | a seeded 1-in-10 second-review sample that finds a mid-paragraph copy misclassified as a citation | — | The finding triggers a second review of every unit of the same name and class. The misclassified unit is reclassified as a copy and joins its group | second review triggered; the group's citers become members | configuration, membership | FAIL until the triggered second review completes |
| P-P1 | a Methodology-like prose paragraph outside any block and outside a claim surface, classified as a citation of `(C1)` | (C1)'s canonical text edited | The prose citer is a member (R-b), reviewed against items 1, 2 and 4 | ∅ hits | membership (prose citer) | FAIL with no record; PASS with a record |

### 2.3 Regression tests for the owner's blocking items (O7, c.7065358283)

Each blocking item has adversarial regression tests. Independent confirmation of each is a separate
review step.

| Blocking item | Regression tests |
|---|---|
| Corpus-wide named-condition dependencies, papers and book | P-GV1 (pending blocks enrollment), P-A1m–P-A5m (ambiguous and incorrect mappings), P-S2, P-S3 (misclassification controls), P-P1 (a prose citer), P-F5 (the ch01-table finding), P-H20 (a heading unit), P-H21 (a list unit with a named lead-in), P-H22 (a confusable, normalized), P-F1–P-F4, P-F6 and N34 (exact, equivalent, different and span-only copies), P-H16 (a plain list-item copy), P-H17 (an opening-paragraph copy), P-H18 (an unclassified new occurrence: the gate fails), P-H19 (a voided classification), P-H11 (an unparenthesised copy), P-H12 (a table row), P-H13 (a glossary copy with its FULL mirror), P-H14 (map drift, unparenthesised), P-H15 (a list item), P-H4 (a cross-file citer), P-H6 (a range), P-H7 (an inline node and an alias), P-H8 (a copy edit reaching every citer), P-H9, P-H10 (map drift), P-H5 (ambiguity outside the map) |
| Deleted theorems keep their scope obligations | P-L4b (a deleted scoped block), P-L4c (a deleted block with no scope wording at all), P-O1 (a deletion inside a batched PR) |
| Individual review of transformations affecting finiteness, infinite-system assumptions, carriers or scope | P-R9 (a carrier rename), P-R10 (deleting `finite`), P-O2 (a mathematically equivalent rewrite), P-O5 (a substitution into a carrier) |
| No reduction silently excludes a theorem | P-O3 (r4), P-O1 (r1), P-O4 (r2), P-R11 (r3) |

| ID | Before | Change | Why | Items | Route | Verdict |
|---|---|---|---|---|---|---|
| P-O1 | 20 blocks; Lemma 9 (FS_L=1) among them | a PR applies N31's scope-neutral rename at 19 sites under one batched record, and deletes Lemma 9 | The rename members are covered by the batch. The deleted Lemma 9 is a member (R-a) that the batch does not name, so it needs its own record answering its L hit | {L} on Lemma 9 | membership, plus the screen | FAIL with only the batched record |
| P-O2 | 10 blocks with "Let $S$ be finite" | rewritten everywhere as "Let $|S| < \infty$", declared as one map | Mechanically identical, but both sides carry `FINITE_TERMS`/`FS_A` tokens, so the map is refused for batching. A claimed mathematical equivalence does not license batching | refused batch; each of 10 needs its own record | membership | FAIL with only the batched record; PASS with 10 records |
| P-O3 | a PR with 10 members, each with its record | one (r4) owner attestation listing 9 of them | The 10th member is not attested, and the coverage check finds it uncovered | coverage failure (V27) | configuration | FAIL |
| P-O4 | a chapter block and its FULL mirror, byte-identical, both citing `(F)`; the chapter's `(F)` and FULL's `(F)` are file-local nodes with different texts | both edited identically, under one (r2) record | The texts are identical, but the resolved hypothesis dependencies differ, so (r2) does not apply | two records required | membership | FAIL with one record |
| P-O5 | 12 blocks using `$\tau$` | a map renaming `$\tau$` to `$S$` | The right side is a carrier symbol, so the map fails the (r1) limit, and each member's FS_A, carriers and quantifier objects may change | refused batch | membership | FAIL with only the batched record |

## 3. Documented limits (X-cases)

The tool's expected verdict is recorded, and the safeguard named.

| ID | Case | Tool's expected verdict | Why, and what catches it |
|---|---|---|---|
| X-1 | *Let $T$ be a finite set of times. For every $t \in T$, every orbit of $\pi$ on $S$ is periodic.* / Pigeonhole on $S$. | no blocking hit (screen escape) | `a finite set` is a positive predication about the declared carrier $T$, so FS_A=1, although the pigeonhole step needs $S$ finite. Caught by checklist item 1. (Revision 2's "for a finite time $t$" now raises A: it is not a positive predication about a carrier.) |
| X-2 | finite use with no listed term ("each configuration is visited before any repeats, so the walk closes") | no blocking hit (screen escape); caught by checklist item 1 | Lexical classes. Caught by review; the wording is then added to FU under SPEC §7, with its own case |
| X-3 | a theorem in unlabelled prose outside the claim surfaces | advisory item only | Caught by the advisory PR layer and owner decision O3 |
| X-4 | a non-cardinality change: an operator flip or a dropped qualifier such as "on the visible sector" (the other NCASES) | not FIN-SCOPE's object | Caught by general claim review; #1483 covers the A1 transformation itself |
| X-5 | *Let $X$ be compact and $f$ continuous. Then $f$ attains its maximum on $X$.* / The image is compact. | {A}, FAIL until resolved (false positive) | FU=2 and FS=0 (compact is not in FS_A). Cleared by a resolution with a `basis` |
| X-6 | *Every orbit of $\pi$ on $S$ is periodic.* / By [external reference, Thm 2]. | no blocking hit (screen escape) | The transitive clause follows only parsed blocks. Caught by checklist item 1, since the block is a member |
| X-7 | *For every density operator $\rho$ on $\mathcal H$, $\mathrm{tr}\,\rho^2 \le 1$.*, where $\mathcal H$ is declared finite-dimensional in an earlier Setting that the statement does not cite | {A}, an admitted false positive | FU=1; the finiteness lies outside the local hypotheses. Answered by a `basis`, or by citing the Setting |
| X-8 | *For every lattice $\Lambda$, the conserved quantities of a bijection of $Q^\Lambda$ are orbit-constant.* | no blocking hit (screen escape) | "lattice" is not a carrier noun, and `$Q^\Lambda$` is undeclared. The generality over infinite lattices is caught by checklist item 3 (R5) |
| X-9 | *Let $S$ be finite, though this is not needed. Every bijection of $S$ has a periodic orbit.* / Pigeonhole. | no blocking hit (screen escape) | The positive predication satisfies FS_A. Caught by checklist items 1 and 3 (R1) |
| X-11 | a `**Definition (orbit space).**` edited, and blocks that use the phrase "orbit space" without citing the Definition's label | the Definition is a member; the using blocks are not (escape) | Definitions used by their term are outside the index. They reach review only through ordinary PR review (SPEC §9) |
| X-10 | "The same holds for all $S$." two paragraphs after a block, outside a claim surface | not in the review set (screen escape) | Beyond the post-block paragraph. Advisory only, unless owner decision O3 brings such prose in |

## 4. Coverage

| Rule or control | Positives | Negatives | Mutant targets |
|---|---|---|---|
| A | P-A1–P-A5, P-A7, P-A9–P-A13, P-N1–P-N4, P-B3, P-B4, P-D1, P-D2 | N1, N2, N2b, N2c, N5e, N13, N15, N20, N22–N24, N26–N28 | P-A1, P-A2, P-A7, P-A9, P-A10, P-A12, P-B3, P-D1, P-D2 |
| L | P-L1–P-L9, P-G7, P-M1 | N9, N10, N12, N14a | P-L1, P-L4b |
| G (G1–G5) | P-A12, P-G1–P-G11, the 46 rows of §1.4 | N3, N5–N5e, N6, N8, N11, N14a–e, N15, N21 | P-G1, P-G2, P-G11, N14e, N15 |
| I | P-I1, P-I2 | N6, N7, N19, N21 | P-I1 |
| M | P-M1, P-M2 | N12 | P-M1 |
| K | P-G9, P-K1, P-K2 | N2b | defined with the Lean layer (O5) |
| P and grammar | P-B1–P-B4 | N16, N17, N18, N28 | N16, P-B3 |
| E | P-E1, P-E2 | N28 | P-E1, P-E2 |
| membership and closure (§1.1) | P-S1, P-D2, P-D3, P-H1, P-H2 | N30, the non-member cases in the conventions | P-S1, P-D2, P-H1, P-H2 |
| block extent with a proof (C2) | P-C2, P-C3 | N29 | P-C2, P-C3 |
| batched records (r1), (r3) | P-R9, P-R10, P-R11 | N31 | P-R9 |
| corpus-wide names, the canonical map and the occurrence register | P-H4–P-H22, P-F1–P-F5, P-GV1, P-A1m–P-A5m, P-S2, P-S3, P-P1 | N32–N35 | P-H4, P-H6, P-H8, P-H11, P-H13, P-H16–P-H19 |
| reductions under O7 | P-O1–P-O5, P-R9–P-R11 | N31 | P-O3, P-O4 |
| deleted blocks | P-L4b, P-L4c | — | P-L4c |
| advisory backstop | P-G11, row 42 | N25 | N22, N25 (G5 made blocking) |
| resolutions and configuration | P-L8, P-G8, P-R1–P-R8 | N8, P-L9 | P-R1, P-R2, P-R6 |
| #1483 reuse | §1.4 (C-R4), P-R7 | N5–N5d | C-R1, C-R2 |

## 5. Independent normalization control (C-R3)

These expected outputs were written by hand from SPEC §3.1 and §4. Each is the input after #1483's
normalization with file text and FIN-SCOPE's LaTeX pre-normalization, with whitespace collapsed. They
were not produced by running the blob.

| # | Input | Expected output |
|---|---|---|
| 1 | `in` + U+00AD + `finite` | `infinite` |
| 2 | `in\-finite` | `infinite` |
| 3 | `inf` + U+0456 + `nite` | `infinite` |
| 4 | `ℵ_0` | `\aleph_0` |
| 5 | `ℕ` | `\mathbb{N}` |
| 6 | `&lt; \infty` | `< \infty` |
| 7 | `holds[^g]`, with file text containing `[^g]: for every $S$` | `holds [^g] (for every $S$)` |
| 8 | `$\mathcal{S}$` | `$\mathcal S$` |
| 9 | `$\lvert S\rvert$` | `$| S|$` |
| 10 | fullwidth `Ｓ` (U+FF33) | `S` |

A case is catalogued here once. An expected verdict changes only through a reviewed revision of this
file made before implementation, never after a run.
