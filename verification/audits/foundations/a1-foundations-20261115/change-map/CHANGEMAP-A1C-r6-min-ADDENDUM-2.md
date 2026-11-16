# CHANGEMAP-A1C-r6-min — Addendum 2: exact edit pairs for the sites found by the review of PR #1313

Base: the PR head `8bf6ecf9` (branch `paper/a1-min-correction-20261116`, worktree `wt-2a`). Source: REVIEW-PR1313-r1, findings F1–F12. These sites lie outside the owner's Stage 2a authorization, so **nothing is applied**; each pair needs owner authorization and independent review first.

## Conventions

- Each pair is one replacement on the named line at `8bf6ecf9`. Its old string occurs exactly once on that line and once in its file (checked). No other `papers/` or `book/` file carries it, apart from the FULL twin named.
- A book pair is applied byte-identically to its FULL twin (§A.14). The twin was located by byte-identical content, and the line numbers are the PR head's. No pair adds or removes a line, so no line number moves.
- Each pair narrows wording only. It adds no claim, premise or prediction. A1 stays an open hypothesis and is nowhere presented as adopted or as refuted. No fragment is left.
- Dry run on a throwaway copy of `wt-2a` with all nine pairs applied: `coverage_check` OK (133 canonical statements; no STALE, so SM:308, Computation:176 and Main:728 lie outside any census statement body); `lean_manuscript_census` OK; `claims_check` OK; `voice_check` OK; V1 guard ALL CHECKS PASS; the six chapter lines and their FULL twins byte-identical. The copy was then deleted.
- After application: rebuild Main, SM, Computation and the book, and regenerate the SC-42 receipt (F1, F2, F4, F5, F6b and F10 change chapter lines mirrored in FULL).

## Pairs

### F1 (blocking)

Location: `book/ch01-observation.md:85`; FULL `book/The-Incompleteness-of-Observation-FULL.md:420`

Old:

```text
and the framework's baseline transition matrices and its physical realization use the canonical one.
```

New:

```text
and the framework's baseline transition matrices use the canonical one.
```

Note: Book mirror of the clause N-M09 deletes at Main:58 and N-G01b deletes at GR:20. After the pair ch01:85 agrees with Main:58 ("the framework's baseline transition matrices (§2.3) use it"). No other occurrence of the old string in `papers/` or `book/`.

### F2 (blocking)

Location: `book/ch03-structural-realism.md:84`; FULL `book/The-Incompleteness-of-Observation-FULL.md:949`

Old:

```text
the substratum is a finite set with a bijection on it, governed
```

New:

```text
the substratum is a set (finite under A1) with a bijection on it, governed
```

Note: Same wording as N-K02-136 at ch02:136 ("the substratum is a set (finite under A1) with a bijection on it"), so the two chapters state the same clause the same way.

### F3 (required)

Location: `papers/SM.md:308`

Old:

```text
and its recurrence-cycle theorem the P-indivisibility content
```

New:

```text
and, on finite reversible representatives, its recurrence-cycle theorem the P-indivisibility content
```

Note: Same scope as N-K05-95 at ch05:95, which cites SM §4.3 for this sentence ("and, on finite reversible representatives, its recurrence-cycle theorem the P-indivisibility").

### F4 (required)

Location: `book/ch14-quantum-computing.md:278`; FULL `book/The-Incompleteness-of-Observation-FULL.md:3944`

Old:

```text
(the maximal-entropy measure, the gauge status of the microstate)
```

New:

```text
(the maximal-entropy measure of a finite representative, the gauge status of the microstate)
```

Note: Same scope as N-P04 at Computation:120 ("the substratum measure of a finite representative is the unique $\varphi$-invariant maximal-entropy measure …, which excludes a planted-measure escape").

### F5 (required)

Location: `book/ch18-beyond.md:162`; FULL `book/The-Incompleteness-of-Observation-FULL.md:4968`

Old:

```text
finite information under A1, recurrence, the arrow of time
```

New:

```text
finite information under A1, the arrow of time
```

Note: Q10 (c) residue: recurrence is removed from the list of substratum commitments that test the framework, as at ch18:20, :28 and :328. No conditional is restated. The §18.7 heading and the recurrence mathematics stay.

### F6 (required), Computation

Location: `papers/Computation.md:176`

Old:

```text
The framework's axiomatic content concerns finite physical structures
```

New:

```text
The framework's axiomatic content concerns, under A1, finite physical structures
```

Note: Computation:180 (N-P06) defines A1 as "that the substratum has finitely many tokens at any moment", so "always finite at any moment" in this sentence is A1. The pair conditions it. The passage's conclusion (no bridge from finite-structure axioms to asymptotic complexity classes) is unchanged.

### F6 (required), book

Location: `book/ch14-quantum-computing.md:184`; FULL `book/The-Incompleteness-of-Observation-FULL.md:3850`

Old:

```text
the framework's axiomatic content concerns finite physical structures
```

New:

```text
the framework's axiomatic content concerns, under A1, finite physical structures
```

Note: Book mirror of F6a, lowercase as on the line.

### F7 (required)

Location: `papers/Main.md:728`

Old:

```text
of the status Remark of §1.2 — an open hypothesis, not adopted — — Lemma 1 delivers
```

New:

```text
of the status Remark of §1.2 (an open hypothesis, not adopted) — Lemma 1 delivers
```

Note: Repairs the doubled dash that N-M44's map text produced. It uses parentheses rather than the reviewer's comma form ("of §1.2, an open hypothesis, not adopted —"): with commas the status phrase could be read as attached to "the status Remark of §1.2" instead of to total finiteness. The status phrase is unchanged, and the item's existing dash pair ("— Lemma 1 delivers … — consumed here by …") is kept.

### F10 (recommended)

Location: `book/ch14-quantum-computing.md:92`; FULL `book/The-Incompleteness-of-Observation-FULL.md:3758`

Old:

```text
The infinite-resource routes are closed by the framework's structural commitments;
```

New:

```text
The infinite-resource routes are closed by the framework's structural commitments, the infinite-time route only under A1;
```

Note: **Recommended.** ch14:90 (N-K14-90) makes the infinite-time exclusion conditional on A1, and this sentence summarizes the infinite-resource exclusions. The CTC and naked-singularity responses on this line rest on deterministic dynamics and bounded coupling degree, not on A1, so only the infinite-time route takes the condition.

### F6, the commitment list (no pair)

"finiteness-per-moment" in the commitment lists at Computation:174 and ch14:184 is left unchanged. Main:728 separates the two finiteness statements: "visible finiteness is stipulated per moment rather than derived" (Lemma 1, from the Definition's finite-capacity clause) is distinct from item (ii), total finiteness (A1). A list of what the axioms' commitments characterize ("the boundary structure between substratum and embedded observer") naturally reads in the first sense, and after F6a/F6b the passage no longer presents total finiteness as adopted. If the owner reads the item as A1, the pair at both lines (and FULL:3850) would be `finiteness-per-moment` → `finiteness-per-moment under A1`; the old string occurs once on each line.

## Notes (no pairs drafted)

### F8 (Main:728 (iii) pointer)

No edit needed. The parenthetical ("a reader who declines the recovery may instead adopt reversibility as the standard information-conservation postulate … at no cost to the downstream results — see the remark following Lemma 3") stays true. The remark after Lemma 3 (Main:64) now says that the emergence results of §3.4 do not use reversibility, which is the "no cost" the parenthetical claims, so the pointer still lands on support. I agree with the reviewer's preference to leave it, under the minimum-change policy.

### F9 (bijectivity of nature stated as a commitment)

**The sites, with line numbers corrected:**

- **ch18:190 / FULL:4996** (the reviewer's "ch18:188" is off by two): "bijection dynamics (the framework's commitment to $\varphi$ as a bijection)".

- **ch14:106 / FULL:3772**: "The framework's deterministic bijection $\varphi$ guarantees unitarity at the substratum level."

**Where the decision already sits.** Total finiteness (A1) is not the issue here; bijectivity of nature is. But that question is already inside the reviewed map. Q5 (a) qualified is one of the map's standing decisions ("Decisions not revised by the policy"), and the map applies it at the analogous sites: N-M11 at Main:64 (bijectivity "of the constructed realizations"; reversibility of nature not adopted as a postulate); N-K07-12 ("a premise of the framework's models"); and N-K07-118, whose ch07:118 sentence "bijectivity is the framework's structural commitment to unitarity at the substratum level" becomes "… in those models". That last one is close kin to ch14:106.

**What taking them would and would not be.** Taking them would propagate an existing map decision to two missed restatements (§A.25), not extend the scope to a new question. There is also a direct A1 link: injectivity yields surjectivity only on a finite set.

**Inconsistency left if they are not taken.** At ch18:190 the same sentence now labels finiteness "the hypothesis A1" (N-K18-192) while calling bijectivity "the framework's commitment".

**Recommendation.** I recommend the owner take both, with the reviewer's wording or the map's "in the framework's models" form. Pairs are not drafted, as instructed.

### F10 companion (observation, no pair drafted)

ch14:90 / FULL:3756, already edited by N-K14-90, still ends "Hypercomputation is therefore excluded structurally in its infinite-resource forms and by the model in its oracle form." Its infinite-resource forms include infinite-time computation, which the same line now excludes only under A1. If F10 is taken, the owner may want the same condition here; the minimal form would be "excluded structurally in its infinite-resource forms (infinite-time computation under A1)". This is not a site the review named, so it is recorded here only.

### F11 (PR-description note)

No text edit. Suggested sentence for the PR description: "N-M51 edits the last sentence of the Main:760 corollary paragraph (\"Corollary (observer-selection rule, with its rate condition)\"), removing the interpretive gloss that the rule replaces the past hypothesis; the selection rule and its rate condition are unchanged. The edit moves the `MAIN:C-observer-selection-rule-rate-condition` fingerprint (N-D2d)."

### F12 (nits)

Neither needs an edit. N-U27's `$(S,\varphi)$` is the map's own text and renders identically to `$(S, \varphi)$`. N-K19-80's lowercase "reciprocity" is the necessary consequence of the sentence-initial insertion.

## Counts

9 pairs: F1, F2 (blocking); F3, F4, F5, F6 (two pairs), F7 (required); F10 (recommended). F6's commitment list: no pair, with the reason above. F8, F11 and F12: no edit. F9: note for the owner, pairs not drafted. One observation (ch14:90) is recorded and not drafted.
