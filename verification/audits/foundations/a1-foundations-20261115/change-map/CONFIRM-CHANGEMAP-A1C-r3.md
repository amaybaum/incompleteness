# Confirmation of change map A1C r3

**Reviewer.** The independent reviewer of r1 and r2. Paper-only: no repository file was edited and no tool beyond read-only text search and small read-only scripts was run. The base is the worktree of `main` at `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`.

## Verdict

**CONFIRMED.** R1–R3 and nits N1–N5 are applied correctly. The extra change at ch01:41 is correct and needed, and it adds no claim. The r2 → r3 diff introduces no new error, and the counts are right.

## 1. R1–R3 and the nits

| Item | r3 row(s) | Check |
|---|---|---|
| R1 | M-11 | Fixed. "imported here rather than invented" is deleted, and the opening now reads "mirrors the orthodox assumption of mainstream physics rather than an exotic commitment". The title becomes "(reversibility and the orthodox assumption)"; I found no census, ledger or guard pin on the old title. The remark no longer asserts the assumption and then disclaims it. |
| R1 | K-ch01-41 | Fixed. The book mirror carries the same treatment. Its last sentence now reads "The framework's realizations are bijective by construction, and reversibility of nature's dynamics is not adopted as a postulate". |
| R2 | K-ch14-92 | Fixed. The row is now no-change, with the right reason: the paragraph's closed routes rest on determinism and bounded coupling degree. K-ch14-90/268 is unchanged. |
| R3 | G-03, OQ-2, K-ch09-14/42/61/84/118 | Fixed. Under option (b), Tier 1's horizon-temperature item keeps "for a finite total system or under the shell-counting condition", and the results built on it take GR:669's "additional condition" wording. The held ch09:118 sentence matches, and option (a) is unchanged. |
| N1 | I-02 to I-08 | Fixed. Each row now quotes its sentence, and every quote is at its stated line at the base. |
| N2 | S-16 | Fixed. The row now points to S-20. |
| N3 | M-59 | Fixed. The text now reads "By the continuum form of Lemma 3's maximal-entropy selection (the proof's own parenthesis)". |
| N4 | OQ-6 | Fixed. Under (a), Structure:134, :741 and SM:14, :20 are read as statements about the finite model, and rows T-06, T-10, S-01 and S-02 are read the same way. |
| N5 | K-ch01-41 | Fixed. The text uses "the record requirement just stated", as M-10 (7) does. |

## 2. The extra change at ch01:41

At the base, ch01:41 reads: "The bijection requirement is structural: non-injective dynamics would merge distinct total states, erasing the observer's records of past outcomes". r3 changes this to "The injectivity requirement is structural: dynamics that merged states differing in registered content would erase the observer's records of past outcomes".

- **Correct.** The argument supports only the record prong. Merging two states that differ only in the hidden sector erases no record. Main's own statement is narrower: Main:36 says injectivity "on states differing in registered content" follows as a lemma, and Main:60 says "For states differing in registered content, injectivity is the requirement that the dynamics preserve the observer's records". For the hidden sector, Main uses a separate, two-pronged argument, which holds only on a finite realization. The base sentence therefore claims more than its argument and more than Main.
- **Needed.** Under Q5 (a) qualified, only injectivity on registered content is asserted of nature. "The bijection requirement is structural" asserts bijectivity of nature's dynamics, which is the reading the unit removes. Left in place, the sentence would contradict K-ch01-38 (book Lemma 3, narrowed to finite realizations) and the rest of the rewritten ch01:41.
- **No added or changed claim.** The new sentence states the record prong as Main does. The rest of the line (injectivity implies surjectivity only on a finite realization; the hidden sector and surjectivity open for nature) repeats M-10 (7). It is a narrowing in 2a, and the FULL mirror is the same line.

## 3. Diff r2 → r3

Hunks were found at the header, M-11, M-59, I-02 to I-08, G-03, S-16, K-ch01-41, K-ch09-14/42/61/84/118, K-ch14-90/268 together with the split-out K-ch14-92, OQ-2, OQ-6, the F6 and F15 rows of Part H, and the new recheck table. Every hunk corresponds to R1–R3 or N1–N5. None introduces a new claim, a register violation, or a reading that asserts or implies infiniteness.

The quotations in every changed row match the base text. One fragment of G-03 is a paraphrase of a locator; it was carried unchanged from r1, does not misquote, and needs no action.

## 4. Recount

| Part | Rows | Stage 2a | Stage 2b |
|---|---|---|---|
| A | 319 | 310 | 9 |
| B | 21 | 20 | 1 |
| C | 11 | 11 | 0 |
| D | 17 | 17 | 0 |
| **Total** | **368** | **358** | **10** |

No row ID is duplicated. The 137-site reconciliation is unchanged from r2 (95 / 6 / 4 / 32).

## What I could not check

- The guard, census and coverage tools were not run. The absence of a pin on the Main:64 title comes from a text search of `verification/lean/*.py` and `tools/*.py`.
