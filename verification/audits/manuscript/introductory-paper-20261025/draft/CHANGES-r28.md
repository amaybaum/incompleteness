# Introduction r28: the run-4 comprehension evaluation, on base `08e4d757`

r28 applies `review/accessibility/RUN4-EVALUATION.md` (gate 2, NOT MET; Q5 (a) PARTIAL, (b) FAIL, (c) PARTIAL; Q7 a
legitimate objection the paper did not answer). It adds the three required explanation changes G1–G3, with the
coordinator's correction to G3, and the recommended plain reading of conditions (i)–(v). All are insertions; no
existing sentence of L130, L132 or L150–L152 is reworded.

**Unchanged:**
- No theorem or corollary statement changed.
- The §2.4 Corollary (L116) is byte-identical.
- The "Stated precisely" scope (L156) is unchanged.
- Every census fingerprint is unchanged, and the census lines equal r27's (65, 101, 116, 142, 148, 222), because every
  insertion sits inside an existing paragraph or list item. The ledger `line` fields therefore need no change.
- The six terms are unchanged.
- No ID was retired, and main was not merged.

Line numbers are r27's, which r28 keeps.

## 1. Finding → change

| # | Finding | Line | Change |
|---|---|---|---|
| G1 | Q5(a): the shared preparation restated, not explained | L130 | Inserted verbatim after "…not one rule started in two ways.": "A forecast from a start is a forecast of what the rule does only if the hidden part is set up by the same procedure every time; if the procedure changed with the start, a difference between two forecasts could come from the setup rather than from the dynamics." It restates the hidden prior shared by every root and drawn independently of it, and adds no claim |
| G2 | Q5(b): no plain reason for keeping never-occurring starts | L140 | The brief allows a merge if the mechanism sentence becomes redundant, and it does: "the evidence … may come only from such a start" and "the only rows keeping the table from being a permutation belong to starts that never happen" say the same thing. The two are merged with the reason first: "Rows for starts that never happen are kept because a result about a rule has to cover every start the rule can be given, not only the starts a particular sample contains. The argument compares the whole square table with its return to certainty at the recurrence, and it can happen that the only rows keeping the table from being a permutation belong to starts that never happen [Main §2.3], as in the different-deck example; dropping those rows would then describe the sample rather than the rule." The required clause is kept word for word. The merge also resolves the referent of G2's "such a start". The different-deck example qualifies: Γ₁ = [[1, 0], [½, ½]], so the red row is a point mass and only the never-dealt black row is not (checked exactly at r25) |
| G3 | Q5(c) and Q7: what the cycle-wide result means | L152 | Inserted after "…but neither appears in any accessible record.": "Such a failure is a property of the world's rule, its dynamics with its hidden preparation, rather than of any record: in a finite reversible world whose hidden part starts with the same odds whatever is visible at the start, and with a visible step that is not fully predictable from the current observation, no single step-by-step chain of forecasts from every start describes the visible sector over the whole cycle, although one may hold on every accessible window, as in the example below. It is a constraint on how such a world can be described, not a prediction for accessible data [Main §2.3, Scope]." This is the coordinator's text with two adjustments. "At the start" is added so the hypothesis matches L134 and L150 word for word (§2 below). The brief's closing clause, "and since it needs so little it does not tell one law from another; what an observer can test is memory at an accessible order, which (C4) asserts", is dropped: L158 states both points ("needs only finite reversibility and one non-deterministic visible step … does not separate them from memory-bearing laws at accessible orders; what an observer can discriminate is memory at an accessible order, which (C4) asserts [Main §2.3, Scope]"), so keeping the clause would say them twice within three paragraphs. The (C4) clause the brief places at L156 is this L158 clause; L156 carries none. The citation moves to the end of the kept sentence |
| R | Recommended: the physical demand of each condition (i)–(v) | L216–L220 | Each condition is prefixed with the name GR §3.3 gives it, which is GR's own plain reading: *valid probabilities*, *trivial-ancilla consistency*, *inert spectators*, *full reversible control*, *iterated composition*. (v) also gains GR's description: "…gives an available operation, so that a composite can itself serve as the working system of a larger experiment." The condition text after each colon is unchanged word for word. GR gives no plain description of (i)–(iv) beyond the name and the condition itself, so no further clause was invented for them. The plain summary of all five already follows Theorem 4 (L224) |

## 2. The G3 hypothesis check

| Hypothesis | Corollary (L148) | Abstract (L17) | L150 | G3 (L152) |
|---|---|---|---|---|
| Finite reversible | "Let φ have order L" (φ a bijection of the finite configuration set) | "In a finite reversible world" | "in a finite reversible world" | "in a finite reversible world" |
| Shared, start-independent hidden odds | "one hidden prior shared by every root and drawn independently of it" | "whose hidden odds are shared by every visible start and drawn independently of it" | "whose hidden part starts with the same odds whatever is visible at the start" | "whose hidden part starts with the same odds whatever is visible at the start" |
| Non-deterministic visible step | "every non-deterministic visible step" supplies a non-permutation Γ_s | "whenever a visible step is not fully predictable from the current observation" | "whenever a visible step is not fully predictable from the current observation" | "with a visible step that is not fully predictable from the current observation" |
| All roots kept | "let Γ_t keep a row for every root, roots of visible probability zero included" | "the forecasts from every start, starts of probability zero included" | "the forecasts from two different starting points" | "forecasts from every start" |

The hidden-odds wording is that of L134 and L150. Equal odds whatever the visible start is the plain form of a prior
that is shared by every root and independent of it. The conclusion, that no single step-by-step chain describes the
cycle, is the Corollary's failure of P-divisibility on {0,…,L}. "Although one may hold on every accessible window" is
the Corollary's "also when the law is Markov on every accessible window". The example that follows at L154 shows it:
"its forecasts from the start chain step by step there." Nothing claims that chaining fails inside a window.

## 3. GR §3.3, quoted (`papers/GR.md` L216, §3.3)

> (i) *Valid probabilities*: every available family sends positive states to positive states and its outcomes' traces
> sum to the input trace. (ii) *Trivial-ancilla consistency*: an operation available on the system is available on the
> system with a one-state ancilla adjoined. (iii) *Inert spectators*: an untouched independent system can be adjoined
> without changing an intervention. (iv) *Full reversible control*: every finite unitary on every composite is
> available. (v) *Iterated composition*: a composite may itself serve as the working system of a larger experiment — an
> operation obtained by attaching a fresh uniformly prepared ancilla to a composite, acting on the enlarged carrier, and
> discarding the ancilla is available on the composite.

(v)'s clause uses GR's "may itself serve" as "can itself serve", the evaluator's wording. Both mean the composite is
admissible as a working system.

## 4. Not applied

- The brief's G3 closing clause, for the reason in §1.
- Gate 3's §3.1 items, which RUN4-EVALUATION also recommends, are outside this brief.

## 5. Build and checks

- **Build:** `sh ./build.sh Introduction` gives 22 pages, the same as r27; median 3,206 non-space characters per page.
- **Typesetting:** a direct compile shows 0 overfull, 0 underfull and 0 missing characters.
- **Release gate:** every step passes except `lean-axioms`, which needs `lake` and runs in CI.
- **Other checks:** `coverage` (134), `duplicate`, `voice`, `claims`, `staleness` and `architecture_check` pass.
  `edge_rigidity_probe`: ALL CHECKS PASS.
- **Added-lines scans:** no hits for the §A.32/§A.33 phrase families, caps emphasis, history voice, markers, secrets,
  scratch paths or model identifiers.
