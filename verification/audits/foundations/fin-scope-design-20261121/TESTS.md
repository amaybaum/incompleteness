# FIN-SCOPE: adversarial test designs

**Status.** Writer's test plan, revision 2, WIP / UNVERIFIED, for `SPEC.md` revision 2. These are
designs: no case has been run. Every "expected" entry is the verdict the rule as written in SPEC §3 must
produce, fixed before any implementation exists, and the "why" column derives it from the counts.
Revision 2 answers review c.7064941939.

**Conventions.**
- Every case is synthetic text in a fixture file and never an edit of the manuscript. Where a case is
  modelled on a real site or review finding, the source is named for provenance only. The case makes no
  claim about the current text of that site.
- "Before" is the paired before-version (SPEC §2.4). "(new)" means there is no before-version.
- "Items" is the exact set of items the case must produce. An extra item fails the case as surely as a
  missing one.
- "Verdict" is the gate verdict with no resolutions, unless the case states a resolution.
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
| P-L4b | Lemma 9 as in P-L4 | the block deleted, with nothing similar added | It disappeared with FS_L+IS=1 | {L} | FAIL |
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
| P-G11 | (new) | *The visible law converges as $N \to \infty$.*, where the block does not declare $N$ | J10's `\to\infty` matches, falls in no class and in no neutral context (G5) | {G} | FAIL |

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
| 39 | , for every one of the possible $S$ | G3 |
| 40 | , for any $S$ whatsoever | G3 |
| 41 | , for $|S|=\aleph_0$ | G4 |
| 42 | , as $N\to\infty$ | G5 (F1 does not declare $N$) |
| 43 | , for $\kappa$ any cardinal | G3 |
| 44 | , for $S$ countable or not | G3 |
| 45 | the allowlisted sentence + "This identity is independent of $|S|$" (ALLOW_PLUS) | G3 |
| 46 | the allowlisted sentence + "It holds for each such $S$" (ALLOW_PLUS) | G3 |

Every row must produce exactly {G}, and in particular no L: no row removes a finite-scope term,
because NEG_FINITE matches are excluded from FS_L both before and after.

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
| P-R1 | P-A1 with a resolution whose attestation fails the O6 check: under (α), the session equals an author commit's session; under (β), there is no owner record | unresolved, {A}, FAIL |
| P-R2 | P-A1 resolved, then one proof token edited | the digest no longer matches; unresolved, FAIL |
| P-R3 | under (β), the owner record names a different digest | the offline form check fails; FAIL. A record that names the right digest on a different PR is caught by PR review against the host |
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
| N7 | (new) | *Let $S$ be uncountable and $(\mu_K)$ a projective family on $S$. It has a unique extension.* / Kolmogorov extension. | IU=1 and IS=1, so no I | ∅ | PASS |
| N8 | P-G1 | a resolution: `justified`, `proof` citing a proof that covers arbitrary $S$, an attestation valid under the O6 option, current digest | the right form | {G}, resolved | PASS |
| N9 | N1 | whitespace reflowed only | the digest is unchanged | ∅ | PASS |
| N10 | N1 | `and $\pi$ a bijection of $S$` → `and $\pi$ an involution of $S$` | revised; FS_L kept; no rise in GEN, PROMO or IS | ∅ | PASS |
| N11 | a baseline block containing "for all $S$" | unchanged | its digest is in the baseline, so it is a baseline item | ∅ open; one baseline item | PASS |
| N12 | the ch02 block and its FULL mirror, both: *Let $S$ be finite. Every orbit of $\pi$ is periodic.* / Pigeonhole. | both changed identically to *Let $S$ be finite and $\pi$ a bijection of $S$. Every orbit of $\pi$ is periodic.* | each is revised with FS_L kept and FS=1, FU=1; the mirror counts are equal | ∅ | PASS |
| N13 | (new) | *Let $\mathcal C_H$ be finite. The horizon-$K$ visible law is the push-forward of the uniform prior on $\mathcal C_H$.* / Counting preimages. | FS=1 ("finite" with the carrier $\mathcal C_H$); FU=2 | ∅ | PASS |
| N14a | N1 | `Let $S$ be finite` → `Let $S$ be finite (the finiteness hypothesis)` | FS and FS_L rise. J10's `finiteness` match falls in FS_L, so it is classified. No G | ∅ | PASS |
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

## 3. Documented limits (X-cases)

The tool's expected verdict is recorded, and the safeguard named.

| ID | Case | Tool's expected verdict | Why, and what catches it |
|---|---|---|---|
| X-1 | *For a finite time $t$ and every $s \in S$, the orbit of $s$ is periodic.* / Pigeonhole. | PASS (escape) | "finite" stands in a sentence with a carrier, so FS=1. Caught by the checklist line (SPEC §10) |
| X-2 | finite use with no listed term ("each configuration is visited before any repeats, so the walk closes") | PASS (escape) | Lexical classes. Caught by review; the wording is then added to FU under SPEC §7, with its own case |
| X-3 | a theorem in unlabelled prose outside the claim surfaces | advisory item only | Caught by the advisory PR layer and owner decision O3 |
| X-4 | a non-cardinality change: an operator flip or a dropped qualifier such as "on the visible sector" (the other NCASES) | not FIN-SCOPE's object | Caught by general claim review; #1483 covers the A1 transformation itself |
| X-5 | *Let $X$ be compact and $f$ continuous. Then $f$ attains its maximum on $X$.* / The image is compact. | {A}, FAIL until resolved (false positive) | FU=2 and FS=0 (compact is not in FS_A). Cleared by a resolution with a `basis` |
| X-6 | *Every orbit of $\pi$ on $S$ is periodic.* / By [external reference, Thm 2]. | PASS (escape) | The transitive clause follows only parsed blocks. Caught by the checklist line |

## 4. Coverage

| Rule or control | Positives | Negatives | Mutant targets |
|---|---|---|---|
| A | P-A1–P-A5, P-A7, P-A9–P-A13 | N1, N2, N2b, N2c, N5e, N13, N15, N20 | P-A1, P-A2, P-A7, P-A9, P-A10, P-A12 |
| L | P-L1–P-L9, P-G7, P-M1 | N9, N10, N12, N14a | P-L1, P-L4b |
| G (G1–G5) | P-A12, P-G1–P-G11, the 46 rows of §1.4 | N3, N5–N5e, N6, N8, N11, N14a–e, N15, N21 | P-G1, P-G2, P-G11, N14e, N15 |
| I | P-I1, P-I2 | N6, N7, N19, N21 | P-I1 |
| M | P-M1, P-M2 | N12 | P-M1 |
| K | P-G9, P-K1, P-K2 | N2b | defined with the Lean layer (O5) |
| P and grammar | P-B1, P-B2 | N16, N17, N18 | N16 |
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
