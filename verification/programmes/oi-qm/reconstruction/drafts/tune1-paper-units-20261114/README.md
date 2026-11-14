# TUNE-1 paper-only units of 2026-11-14 (#1236)

Work in progress, published under AGENTS.md §A.43. Research drafts: paper-only, model-reviewed, not
independently verified, not adopted. They change no manuscript claim and no scientific status.

**Authorization.** The owner authorized two paper-only units on #1236 (comment 6874529744,
`amaybaum`, 2026-11-14): "I authorize steps 2 and 4 as paper-only work". Step 2 is a derivation on
gap L5.4; step 4 is the specification of one non-linear candidate. Paper-only means hand reasoning
and the repository's check scripts: no computation on OI rules was run.

## `nlcand/`: one non-linear candidate (step 4)

The candidate is the ring rule of `papers/SM.md` §3.1 as written, completed with a law, an observer,
labels and setting generators, and analysed by hand against three requirements: control, Bell
parameter dependence without signalling, and supply of known-value cells. The hypothesis that the
world's rule is this ring rule is written H-ring in r3 and is unadopted. It is not TUNE-1's H-nl,
which names the rounded rule of `papers/SM.md`:294.

| File | What it is |
| --- | --- |
| `SUMMARY-r3.md` | Plain-language summary of r3 |
| `NLCAND-r3.md` | The final text |
| `NLCAND-r2.md` | The revision the confirmation review read |
| `NLCAND-r1.md` | The first draft, which the review read |
| `NOTES-r1.md` | The writer's reading list and what was not checked |
| `REVIEW-r1.md` | Non-author review of r1: REVISE |
| `RESPONSE-r1.md` | Dispositions of the review's findings and of the confirmation review's edits |
| `CONFIRM-r2.md` | Confirmation review of r2: ACCEPT WITH CHANGES |

**Review status, exactly.**

- `REVIEW-r1.md` re-derived the rule quotation, bijectivity and the inverse, the directed cone and
  the signalling computations by hand and returned REVISE on verdict strength and scope. r2 applies
  its findings (`RESPONSE-r1.md`).
- `CONFIRM-r2.md` confirmed r2 and asked for five wording edits, N1–N5, with exact text and no
  change to any verdict.
- r3 applies all five edits as written; the verdicts of r2 are unchanged. Beyond N1–N5, r3 differs
  from r2 in the title and status paragraph, the review row of the reference table, one sentence in
  §8 and a closing "Not included" line. `diff NLCAND-r2.md NLCAND-r3.md` shows every change (13
  hunks).
- r3 itself has not been reviewed. Neither review is independent verification, a human review or an
  owner decision.

**Scope.** Every verdict is for the one candidate analysed. Nothing here is a statement about the
non-linear class, about H-ring or H-nl as hypotheses, or about H-Bell. Several results depend on the record convention
(complete-history records against the single-time readout of `papers/Main.md`:369–372); r3 states
which hold under which.

## `l54/`: gap L5.4 (step 2)

The question (TUNE-1 Step 3): for the linear rule under a coset-uniform law, can a family whose
Q6′ witnesses are heralded meet Q3′, Q5′ and Q6′ together at every ε?

**Headline of r3.** Classes A, B and C fail Q5′ under its specified target and record conventions.
That gives L5.4, L5.5 and L5.6 a definite answer within that scope, and no answer outside it. The
theorem's hypotheses are an additive rule, complete-history records and the Lüders product-form
target as the source record defines it; the full list is in r3. Class D is untouched, the gate
question stays open, and nothing follows for a non-additive rule. Relative to `main` the result is
an elaboration of a mechanism already recorded there; r3 states what it adds.

| File | What it is |
| --- | --- |
| `SUMMARY-r3.md` | Plain-language summary of r3 |
| `L54-r3.md` | The final text |
| `L54-r2.md` | The revision the confirmation review read |
| `L54-r1.md` | The first draft, which the review read |
| `NOTES-r1.md` | The writer's reading list and what was not checked |
| `REVIEW-r1.md` | Non-author review of r1: ACCEPT WITH CHANGES (findings F1–F9) |
| `RESPONSE-r1.md` | Dispositions of the review's findings and of the confirmation review's changes |
| `CONFIRM-r2.md` | Confirmation review of r2: ACCEPT WITH CHANGES (changes C1–C5), with the reviewer's own section 6 |
| `CHECK-RULEFREE.md` | Independent check of section 6 of `CONFIRM-r2.md` |

**Review status, exactly.**

- `REVIEW-r1.md` re-derived the lemmas, Theorem 1, Corollary 1a, Proposition 2 and the constants by
  hand, found no counterexample, and asked for changes to controls, scope and wording. r2 applies
  them (`RESPONSE-r1.md`).
- `CONFIRM-r2.md` confirmed r2 and asked for five wording and scope changes, C1–C5, with exact text;
  no proof is touched.
- r3 applies C1, C3, C4 and C5 as given and C2 with one modification (its closing pointer goes to
  r3's §9), adds that closing section and the scoped headline, and has no review of its own.
  `diff L54-r2.md L54-r3.md` shows every change.
- Neither review is independent verification, a human review or an owner decision.

**Reviewer-authored results and their independent check.** Section 6 of `CONFIRM-r2.md` is the
reviewer's own derivation on whether the obstruction belongs to the rule or to the record
convention. `CHECK-RULEFREE.md` is an independent check of that section by a second non-author,
by hand, with these verdicts:

| Claim of `CONFIRM-r2.md` §6 | Verdict of the check |
| --- | --- |
| Q5′ compares complete records; the class only states the target | confirmed |
| Consecutive round records share a slice of the observer's state | confirmed with correction: it is a copy present in both records, already stated on `main` |
| Rule-free lemma: the shared slice must sit on one configuration with probability at least 1 − 17ε; in initial-condition mode with τ = 1 this fails every rule (ε ≥ 1/288) | confirmed, constants included; it holds for every pair-form rule and law and survives heralds and adaptivity; a definitional corner of the schema, not evidence about dynamics |
| A non-additive rule meets Q5′ at ε = 0 under complete-history records (exchange mode, under H-write, τ = 4) | confirmed by independent hand time-stepping, for Q5′ only; the example fails Q3′, Q6′ and Q2, is not in class D, and has no bearing on the linear or ring rule beyond showing that the interface alone does not force failure |
| Theorem 1 depends on the target having no persistent memory | corrected: Theorem 1's failure comes from the dynamics (additivity) under a comparison with no decoder, not from the shared slice or from a lack of memory |
| A memory-tolerant target readmits post-hoc selection | corrected: unrestricted memory tolerance does; memory can be admitted with the selection requirement kept, by a label-independent split of each record into a retained part and an outcome part, and Theorem 1 then holds unchanged |

Headline supported by the check, after it re-derived Theorem 1 and Corollary 1a: classes A, B and C
fail Q5′ under its specified target and record conventions, answering L5.4–L5.6 within that scope
and no wider. A universal interface obstruction is refuted; the question stays open for the rounded
non-linear rule.

Status of these results: the reviewer's section 6 has one author and this one independent check.
The check's own additions (its Proposition M, an initial-condition-mode construction at τ = 14 and
the others listed in its §8) have one derivation each and no check. Its §9 proposes eight
replacement texts; they are not applied to r3. None of this is independent verification in the
sense of AGENTS.md §A.46, and r3's theorem does not rest on it.

## Names used in the files

The files name the checkouts they read. They resolve as follows.

| Name in the files | Content |
| --- | --- |
| `wt-mainread` | `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153` |
| `wt-3a` | branch `research/tune1-step3a-1236-20261113` at `8228b3c24e17a17f324b6779b53b04ad296b4308` (off `main`; written `8228b3c2` in `l54/`) |
| `wt-tune1plan` | branch `records/tune1-landing-plan-1236-20261114` at `ea9bff9c2f2f0f238db66690073868e281e43501` (off `main`) |
| `wt-bell` | branch `research/bell-ladder-868-20261113` at `d8e4f80e71b64972ee3e87a874544c8bd358d5c2` (off `main`) |
