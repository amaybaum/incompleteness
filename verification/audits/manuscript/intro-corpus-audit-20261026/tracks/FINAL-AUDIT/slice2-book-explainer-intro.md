# Final consolidated audit, slice 2: book, FULL, Explainer and Introduction (main `55e3217b`; Introduction at `4a260ca9`)

This is an independent, read-only check. Book and Explainer line numbers are chapter lines; FULL mirror lines appear in
brackets where they were computed.

## A. Mirror integrity
- The release gate's mirror step finds 0 chapter lines absent from FULL. That check is one-way.
- An exact two-way line-count comparison also finds no chapter line missing and no FULL duplicate.
- FULL has 37 extra nonblank lines. All are front matter (title page, copyright, dedication, `\clearpage`, `***`).
- One cosmetic difference: ch05 :5–6 has a double blank line where FULL has one.

## B. Regression sweep
| Unit | Result |
|---|---|
| SC-1 | Clean. glossary :107, README :17 and ch19 :126 use Main's own summary wording (optional tightening, E17). |
| SC-2 | Clean. |
| SC-4 | Clean. The graph-cone speed is never identified with c. |
| SC-18 | Clean. |
| SC-3 | Regressions at preface :3, README :76 and ch03 :36/:102/:114 (E5, E7, E8). |
| SC-16 | "(C1) and finiteness" has 0 hits, and the backflow terminology is consistent in ch01, appendix-b, glossary and Explainer. Residuals: the ch15 cluster and ch13 :80 (E3, E4, E6); unscoped "coupling ⇒ P-indivisibility" at ch01 :93, ch18 :193 and Explainer :135/:1005 (E11). |
| SC-20 | The two-form statement is present throughout. The glossary :27 heading is stale (E14). |
| SC-21 | Scoped everywhere except ch04 :178 (a known item) and ch04 :36 (E15). |
| C3 | Unconditional everywhere. |

## C. Known open items, all confirmed still present
- **SC-22:** ch13 :20/:68/:134–144; ch15 :20/:142–154/:168/:208/:212; ch18 :16/:74–92; glossary :29/:115; ch09 :285.
- **SC-23:**
  - glossary :27 (last sentence) and :31;
  - ch03 :58;
  - ch04 :178;
  - Explainer :361, :926 and :1018–1019;
  - ch01 :223, which still carries two different "coarse-grained description" phrases;
  - appendix-c :102 "is lost".
- **SC-17:** ch00 :55; ch01 :16/:169/:183; ch02 :188; ch03 :162/:164/:180; ch04 :90/:92; ch18 :110; appendix-c :32/:34;
  glossary :19; Explainer :58/:300/:338/:563/:665/:1017.
- **SC-19:** ch00 :37; ch01 :133/:155/:201/:259; ch07 :30; Explainer :64/:88.
- **ch04 :178:** the rate condition is absent. The same paragraph also says "requires C1–C4" (C2 sits outside the
  equivalence) and asserts the exclusion before the (EM) scope is introduced.
- **Explainer :767:** the selectors are still there.
- **Explainer :826 and ch05 :95:** they still contradict SM :236/:306.
- **Explainer:** the "§3.3" section numbering is still there.

## D. Introduction alignment (at `4a260ca9`; also present after the pinned-main merge `edac91c9`)
| Item | Line | Topic | Current | Source | Proposed |
|---|---|---|---|---|---|
| D1 | L12 | abstract, SC-3 | "finite recurrence turns history readback into stochastic indivisibility somewhere in the recurrence cycle" | Main :20, :82(2), :141 | "…whenever some rooted visible map is not a permutation, which every non-deterministic visible step supplies, Markov laws included; with a full-support visible prior this indivisibility is equivalent to memory at some order below the recurrence time…" |
| D2 | L56 | SC-2 | "For a law with rational probabilities, a realization whose hidden prior is independent of x₀ also exists" | Main :512–514 | the rational class is the conditional kernels at positive-probability histories; the visible initial law may be irrational; the response-table extension covers arbitrary kernels |
| D3 | L86 | SC-20 | "(C2) is a physical-regime premise" | Main :76 | C2-structural holds by reversibility in every bijective realization and constrains coarse-grained descriptions; C2-slow is one mechanism |
| D4 | L96 | SC-3 | "history readback forces indivisibility somewhere in the recurrence cycle" | Main :137–141 | any non-permutation rooted map does so; a (C4) gap supplies one, and so does every non-deterministic visible step. The machine-check sentence stays: `routed_forces_indivisible_somewhere` (`PhysicalC4Discharge.lean:122`) |
| D5 | L185 (4) | SC-20 | C2 necessity stated as conditional | Main :76, :630 | the slow-bath form is conditional on the mixing hypothesis; the persistence form needs none |
| D6 | L136 | SC-4, **stronger than the source** | "keeps pointwise causal cones and a setting-independent pre-setting ensemble is Bell-local … must give up one of the two" | Main :361–398 | state Main's hypotheses (ii), (iii), (iv) and "an outcome in every run", and the conclusion "gives up at least one of ontic parameter independence and measurement independence" |
| D7 | — | no change needed | SC-1, SC-21 and SC-18 (L68), and the backflow terminology (L106) | — | — |

## E. New findings
1. **Medium-high: appendix-c :14 [6260].** "the specific Bell-violating mechanism (P-indivisibility producing
   factorizability violation)" contradicts appendix-c :42, ch01 :219, ch04 :98 and Main §3.3. Proposed: name the adopted
   branch (ontic parameter dependence, measurement independence retained, operational no-signaling preserved). Hidden
   memory and indivisibility are not the mechanism.
2. **Medium: README :100.** It describes appendix-c as "outcome-dependence-without-parameter-dependence", which is the
   opposite of the adopted branch.
3. **Medium: ch15 revival stated as a prediction.**
   - Sites: ch15 :18, :99, :116, :122, :128, :130, :132 [3979, 4060, 4077, 4083, 4089, 4091, 4093].
   - The "backflow-aware" naming at ch15 :136, :138, :226, :244, :256 and appendix-a :172 has the same problem.
   - Proposed: make each conditional ("where the bath's return also revives distinguishability"), as SC-16 did at
     ch15 :101.
4. **Medium: ch15 :75 [4036] and :85 [4046].**
   - :75 says higher-order correlations are "uniquely diagnostic of P-indivisible" dynamics.
   - :85 says "predicted P-indivisible noise".
   - The same section has two errors next to SC-22: §15.8 :197 [4158] and :210 [4171] treat autocorrelation revival as a
     P-indivisibility witness.
5. **Medium: ch03 :36, :102, :114 [912, 978, 990] and ch03 :240.** They list P-indivisibility among the features "any
   partial-trace observation must produce … no embedded observer can avoid". Proposed: "recurrence-cycle P-indivisibility
   of the marginal process wherever a rooted visible map is not a permutation".
6. **Medium: ch13 :80 [3579].** "non-Markovian dynamics — specifically, information backflow". Proposed: memory-bearing
   where the record is read back; backflow is a further property.
7. **Medium-low: preface :3 [74].** This is an SC-3 regression: recurrence indivisibility is listed as readback content.
8. **Low-medium: README :76.** "evolution as a P-indivisible process" → "memory-bearing (non-Markovian) process".
9. **Low: ch01 :207 [551].** "P-indivisibility cannot arise", given as the reason the Bell route is closed, contradicts
   ch01 :219.
10. **Low: ch12 :232 [3484].** The table row conflates P-indivisibility with the memory witness.
11. **Low: ch01 :93 [437], ch18 :193 [5011], Explainer :135, :1005.** Each says coupling ⇒ P-indivisibility without the
    uniform-prior and recurrence-cycle scope.
12. **Low: ch01 :123 vs :125 [467/469].** One says the decay rate is set by a spectral gap Δ; the other says no gap
    exists.
13. **Low: glossary :25 [6625].** It cites [Main §3.3] for the delayed-revival family; the correct reference is §3.4.
14. **Low: glossary :27 [6627].** The heading "C2 (Slow-bath memory persistence)" → "C2 (Memory persistence)".
15. **Low: ch04 :36.** It points to the observer-selection theorem with no (EM) scope.
16. **Cosmetic: ch05 :5–6.** The double blank line.
17. **Optional (SC-1): glossary :107, README :17, ch19 :126.** These could add the exact-arithmetic qualifier.
