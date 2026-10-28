# Introduction r23: the two r22 confirmations (`40935ccf`), on base `a3b49057`

r23 is a small corrective revision. It applies the two r22 confirmations, both ACCEPT WITH CHANGES:
`scientific/GATE1-papers-40935ccf.md` (R1, R2, O1–O3) and `editorial/GATE3-papers-40935ccf.md` (findings 1–7 and the
p. 5 gap), together with the owner's note on the raw spacing hint.

**Unchanged:**
- No theorem or corollary statement changed.
- The §2.4 Corollary (L116) is byte-identical.
- Every census fingerprint is unchanged. Only the ledger `line` fields moved (65, 101, 116, 136, 142, 214).
- No ID was retired, and main was not merged.

Line numbers below are r22 → r23.

## 1. Finding → change

| # | Finding | r22 → r23 | Change |
|---|---|---|---|
| 1 | R1 = G3 #1: the definition of hidden predictive memory | L99 → L99 | Now reads: "The *hidden predictive memory* I(X_<t;H_t\|X_t) is the information the hidden state holds about the observed past beyond what the observed present tells; it is at least the conditional memory (Theorem 2(c)), and only part of it need affect what is seen next." Theorem 2(c) in the paper reads M_t ≤ I(X_<t;H_t\|X_t) ≤ log₂\|𝒞_H\|, so the cited lower bound holds as stated. The owner's gloss ("the part … that supports the observed process's dependence on history") now sits only at the readout-relevant memory: "readout-relevant hidden memory, the part of the hidden memory that supports the observed process's dependence on history" (L118, after the Corollary). The other uses are re-checked in §2 |
| 2 | R2, and G3 #5 (moved) | L148 → L146 | Now reads: "Accessible windows are, by definition, short compared with the world's recurrence time L [Main §2.3, Scope], and the gap between them leaves room for conditional memory that no accessible window detects: a trace held in the hidden part can first affect what is seen at an order beyond every accessible window, though still before the return." The sentence now comes before "An observer confined to accessible windows sees neither." |
| 3 | G3 #3, G1 O1: the name for L | L49, L142 → L49, L140 | L49 now adds "and L is the world's *recurrence time*, the least time after which the whole world returns to its starting configuration". L140 now reads: "…for the order L of φ, the recurrence time. A *return horizon* is a time n with Γ_n=I, at which only the forecasts from the start return to certainty; L is one, and there may be earlier ones." "Least return time" no longer appears. "Recurrence time" is used for L at L17, L49, L122, L140, L146, L298 and L307. "Order L of φ" is kept where the statement texts use it |
| 4 | G3 #2, G1 O3: the abstract's "So" | L17 | The sentence moves to follow the memory sentence and now reads "Stochastic, quantum-like records can therefore arise exactly from deterministic dynamics, and any memory they show must be stored in the hidden part." It follows from the two results before it |
| 5 | G3 #4: repeated clause | L167 → L165 | "…because its visible steps are not fully predictable; that failure need not lie on an accessible window." |
| 6 | G3 #6 | L220 → L218 | "Conditions (i) and (ii) only make the theory well formed; (iii)–(v) are the substantive requirements, which [GR §3.3] calls selection principles." |
| 7 | G1 O2, G3 #7 | L17 | "whenever some table of forecasts from the start is not a permutation, in particular whenever a visible step is not fully predictable from the current observation". The scope is unchanged: the table of forecasts from the start is the rooted transition matrix, and the abstract already carries its rows for every start |
| 8 | p. 5 gap and the raw spacing hint (owner note) | L101 | The raw `\vspace … \penalty` hint is removed, along with a trial `\nopagebreak` before (c). Three source-level trims above Theorem 2 were tried and did not keep it whole, so they were reverted. Per the owner's note, the page break is accepted: Theorem 2's header, (a) and (b) sit on p. 5, and (c) on p. 6. There is no gap at the foot of p. 5, and the Markdown carries no raw spacing command |

## 2. "Hidden predictive memory" re-checked against the corrected definition

| Line | Use | Consistent? |
|---|---|---|
| L99 | the definition | — |
| L101 | Theorem 2's title, "unavoidable hidden predictive memory" | yes: (c) bounds it below by M_t and above by capacity |
| L120 | "the least hidden predictive memory I(X_<t;H_t\|X_t) is exactly I(X_<t;X_>t\|X_t) … while bijective realizations run from time 0 carry H(X_<t\|X_t), Markov laws included"; "the exact minimum of the hidden predictive memory a deterministic completion must carry" | yes: the same quantity, minimized over completions; the bijective value H(X_<t\|X_t) is all that the hidden state holds about the past |
| L126 | the Main remark title in Proofs and sources | yes |
| L298 | "the least hidden predictive memory" | yes |
| L116, L118 | the Corollary's "readout-relevant hidden memory" and its plain reading | these are the readout-relevant part, which is where the owner's gloss now sits |

## 3. Terminology occurrence list (§§1–6, r23 lines)

- **conditional memory (M_t):** L17, L99 (definition), L120, L122, L124, L146, L165, L190, L307.
- **hidden predictive memory:** L99 (definition), L101, L120, L126, L298. The bare phrase "predictive memory" occurs nowhere.
- **readout-relevant (hidden memory):** L116, L118.
- **accessible memory:** L146, L192.
- **memory in the record:** L124, L165, L194.
- **P-divisibility / P-divisible:** L130 (plain definition), L132 (formal), L134, L136, L142, L148, L152, L165, L192, L200.
- **P-indivisible:** L17, L163, L176, L190, L192, L196, L298.
- **recurrence time (L):** L17, L49 (definition), L122, L140, L146, L298, L307.
- **return horizon:** L140 (definition), L154.
- **recurrence cycle:** L17, L140 (definition), L146, L190.

## 4. Not applied

None. The p. 5 spacing hint was removed rather than kept, and the resulting Theorem 2 page break is accepted as the
owner's note allows.

## 5. Build and checks

- **Build:** `sh ./build.sh Introduction` gives 21 pages, and §1 starts on p. 1.
- **Typesetting:** a direct compile has 0 overfull and 0 underfull boxes and no missing characters.
- **Release gate:** every step passes except `lean-axioms`, which cannot run locally because `lake` is not installed (it passes in CI).
- **Other checks:**
  - `duplicate`, `voice`, `claims`, `coverage` (134), `staleness` and `mirror` all pass.
  - `edge_rigidity_probe`: ALL CHECKS PASS.
- **Added-lines scans:** no hits for the §A.32/§A.33 phrase families, caps emphasis, markers, secrets, scratch paths or model identifiers.
