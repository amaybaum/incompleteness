# Confirmation of Addendum 2 to change map A1C r6-min

**Reviewer.** The independent reviewer of PR #1313 (REVIEW-PR1313-r1), who did not draft the addendum. Paper-only: no repository file edited, nothing committed, pushed or posted. Checks are read-only, and every replacement was simulated in memory; nothing was written to disk.

**Base.** Worktree `wt-2a` at the PR head `8bf6ecf99`.

## Verdict

**CONFIRMED WITH NITS.**

- The nine drafted pairs are exact.
- Each fixes its finding fully and minimally.
- Each adds no claim and keeps A1 open.
- None leaves a fragment.

The nits:

- **F9.** One pair should be drafted for ch18:190; ch14:106 should stay unedited.
- **ch14:90 end and ch14:268 lead.** Each deserves a pair. Take them together with F10, or take none of the three.
- **Line correction.** My review placed the F9 bijectivity site at "ch18:188"; the addendum's ch18:190 is correct.

## 1. Mechanics

Each old string was checked on its stated line at `8bf6ecf99`. All twelve pairs were then applied in sequence to in-memory copies, and the chapter line and its FULL twin were compared again after each pair.

| Pair | Site | Occurrences on the line | FULL twin byte-identical (before and after) | Other occurrences in `papers/`, `book/` |
|---|---|---|---|---|
| F1 | ch01:85 / FULL:420 | 1 | yes | none |
| F2 | ch03:84 / FULL:949 | 1 | yes | none |
| F3 | SM:308 | 1 | — | none |
| F4 | ch14:278 / FULL:3944 | 1 | yes | none |
| F5 | ch18:162 / FULL:4968 | 1 | yes | none |
| F6a | Computation:176 | 1 | — | none |
| F6b | ch14:184 / FULL:3850 | 1 | yes | none |
| F7 | Main:728 | 1 | — | none |
| F10 | ch14:92 / FULL:3758 | 1 | yes | none |
| F9-a (added below) | ch18:190 / FULL:4996 | 1 | yes | none |
| F10-b (added below) | ch14:90 / FULL:3756 | 1 | yes | none |
| F10-c (added below) | ch14:268 / FULL:3934 | 1 | yes | none |

No pair adds or removes a line. I did not re-run `coverage_check`; the addendum's dry run reports no STALE entry. Re-run it at application.

## 2. Content of the nine drafted pairs

| Pair | Fixes the finding fully | Minimal | New claim? | A1 status | Reads cleanly |
|---|---|---|---|---|---|
| F1 | yes: the nature-uses-the-counting-measure clause goes, as at Main:58 and GR:20 | deletes four words | no | n/a | yes |
| F2 | yes: same wording as N-K02-136 | one word plus "(finite under A1)" | no | open | yes |
| F3 | yes: same scope as N-K05-95, the book mirror | one inserted clause | no | n/a (finite representatives) | yes |
| F4 | yes: same scope as N-P04 at Computation:120 | one inserted phrase | no | n/a | yes |
| F5 | yes: recurrence leaves the forward-prediction list (Q10 (c)), with no conditional restated | deletes one list item | no | open | yes |
| F6a, F6b | yes: "always finite at any moment" is A1 by Computation:180's own definition, now conditioned | "under A1" inserted | no | open | yes |
| F7 | yes: the doubled dash is gone and the status phrase is unchanged | one punctuation change | no | open | yes |
| F10 | yes: only the infinite-time route takes the condition, matching ch14:90 | one inserted clause | no | open | yes |

## 3. The F6 and F7 choices

**F6: leaving "finiteness-per-moment" unchanged is correct.**

- The list at Computation:174 and ch14:184 is "finiteness-per-moment, bijectivity, the proper-part decomposition $V \subsetneq S$, the C1–C4 partition conditions". That is the methodology paper's rung list.
- Methodology:166 names rung 7 "(finiteness-per-moment)" and identifies it as "the finite-capacity clause of the Definition".
- Methodology:253 says "Finiteness-per-moment of the visible configuration space is the finite-capacity clause of the observer's definition".
- Main:36 and Main:728 say the same of Lemma 1.

So the corpus uses the term for visible finiteness, not for A1. Once F6a/F6b condition the following sentence, the passage presents total finiteness as adopted nowhere. The fallback pair should not be applied.

**F7: the parentheses are better than my comma form.**

- With commas, "of the status Remark of §1.2, an open hypothesis, not adopted —" could attach the status to the Remark.
- The parentheses attach it to the head noun of item (ii), total finiteness.
- The words of the status phrase are unchanged, and the item's own dash pair is kept.
- Main already writes status asides in parentheses ("(finite under A1)", "(item (ii))").

## 4. F9

**Scope.** Both sites state bijectivity of nature's dynamics as a commitment. That is the Q5 (a) qualified question, which the reviewed map already decides and applies: Main:64 (N-M11) now says "reversibility of nature's dynamics is not adopted as a postulate", and the bijectivity-premise sites read "of the framework's models" (N-K07-12, N-K09-129, N-K18-122, N-K19-22). It is also tied to A1, since bijectivity follows from injectivity only on a finite set (N-M10c). A pair here propagates an existing decision (§A.25); it does not open a new question.

### ch18:190: draft a pair

- **Why.** The same sentence now calls finiteness "the hypothesis A1" (N-K18-192) and bijectivity "the framework's commitment", which contradicts Main:64.
- **Wording.** The pair reuses the map's reviewed phrase, as at N-K09-129 and N-K18-122.

**F9-a.** Location `book/ch18-beyond.md:190`; FULL `book/The-Incompleteness-of-Observation-FULL.md:4996`.

Old:

```text
(the framework's commitment to $\varphi$ as a bijection)
```

New:

```text
(the bijectivity premise of the framework's models)
```

The line then reads "… substratum finiteness (the hypothesis A1, $|S| < \infty$), bijection dynamics (the bijectivity premise of the framework's models), and P-indivisibility at the recurrence scale." The guard phrase "Recurrence together with C1" later on the line is untouched.

### ch14:106: no pair

- **Where the line sits.** It is an item under "**Proof outline.**" (ch14:102–104), in the list "The proof relies on the framework's structural commitments at multiple points" of the Conditional BQP Characterization Theorem.
- **The theorem's hypothesis.** "Let $\mathcal{S} = (S, \varphi)$ be a finite deterministic system" (ch14:100). In that proof, $\varphi$ is the theorem's bijection.
- **The map's classing.** The reviewed check table classes the neighbouring item ch14:105 MOD (K-ch14-100/105). That classing applies equally to :106.
- **The policy.** Proofs stay unchanged.

The sentence is therefore a statement about the theorem's object, not about nature, and editing it would change a proof outline. My F9 suggestion for ch14:106 is withdrawn.

## 5. The ch14:90 observation, and the same pattern at ch14:268

**ch14:90: yes, a pair.**

- Within one paragraph, ch14:90 now says the infinite-time exclusion is "a structural exclusion conditional on A1" (N-K14-90).
- It then ends "Hypercomputation is therefore excluded structurally in its infinite-resource forms …", which states that exclusion as unconditional.
- That is an assertion and its qualification in the same paragraph (§A.30).
- F10 conditions the same route two lines later, so the three summaries should agree.

**ch14:268: the same pattern.** The italic lead "*Hypercomputation is excluded — structurally in its infinite-resource forms, by the model in its oracle form.*" is followed by "The framework's finite substratum (under A1) … preclude infinite-time … computation".

**Recommendation.** Both are recommended, and should be taken or declined together with F10, so that the chapter states the condition consistently.

**F10-b.** Location `book/ch14-quantum-computing.md:90`; FULL `book/The-Incompleteness-of-Observation-FULL.md:3756`.

Old:

```text
Hypercomputation is therefore excluded structurally in its infinite-resource forms and by the model in its oracle form.
```

New:

```text
Hypercomputation is therefore excluded structurally in its infinite-resource forms (the infinite-time form under A1) and by the model in its oracle form.
```

**F10-c.** Location `book/ch14-quantum-computing.md:268`; FULL `book/The-Incompleteness-of-Observation-FULL.md:3934`.

Old:

```text
*Hypercomputation is excluded — structurally in its infinite-resource forms, by the model in its oracle form.*
```

New:

```text
*Hypercomputation is excluded — structurally in its infinite-resource forms (the infinite-time form under A1), by the model in its oracle form.*
```

On both lines the arbitrary-precision route stays structural: it rests on the lattice's discreteness, not on A1, as F10's note says.

## 6. What survives after application

With F1–F7 and F10 applied, together with F9-a, F10-b and F10-c, none of the unsupported physical assertions of REVIEW-PR1313-r1 survives:

- **F1–F6.** Corrected.
- **F7.** Repaired.
- **F8.** No edit, agreed: the pointer lands on Main:64's "the emergence results of §3.4 do not use it".
- **F9.** Corrected at ch18:190. ch14:106 is a proof-outline statement about the theorem's finite object.
- **F10.** Corrected at all three hypercomputation summaries.
- **F11 and F12.** No text issue.

**If the owner declines F10, F10-b and F10-c together**, the residue is the unconditional "structurally" at ch14:90, :92 and :268. ch14:90 and ch14:268 carry the A1 condition in their own text, so this is a consistency nit, not an unsupported claim about nature.

**If the owner declines F9-a**, ch18:190 keeps "the framework's commitment to $\varphi$ as a bijection", which contradicts Main:64.

## Final apply list

Each book pair is applied byte-identically to its FULL twin.

| # | Pair | Site | Severity |
|---|---|---|---|
| 1 | F1 | ch01:85 / FULL:420 | blocking |
| 2 | F2 | ch03:84 / FULL:949 | blocking |
| 3 | F3 | SM:308 | required |
| 4 | F4 | ch14:278 / FULL:3944 | required |
| 5 | F5 | ch18:162 / FULL:4968 | required |
| 6 | F6a | Computation:176 | required |
| 7 | F6b | ch14:184 / FULL:3850 | required |
| 8 | F7 (parenthesis form) | Main:728 | required |
| 9 | F9-a (this file) | ch18:190 / FULL:4996 | recommended; the owner's Q5 (a) propagation |
| 10 | F10 | ch14:92 / FULL:3758 | recommended; take with 11–12 |
| 11 | F10-b (this file) | ch14:90 / FULL:3756 | recommended; take with 10, 12 |
| 12 | F10-c (this file) | ch14:268 / FULL:3934 | recommended; take with 10–11 |

**Do not apply:**

- the F6 fallback ("finiteness-per-moment under A1");
- any edit at ch14:106;
- any edit for F8, F11 or F12.

**After application:**

1. Re-run `coverage_check`, `claims_check`, `voice_check` and the mirror check.
2. Rebuild Main, SM, Computation and the book.
3. Regenerate the SC-42 receipt, since chapter lines mirrored in FULL change.
4. Put the F11 sentence in the PR description.
