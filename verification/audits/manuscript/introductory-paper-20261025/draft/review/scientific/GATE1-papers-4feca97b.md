# Gate 1 (scientific accuracy): focused confirmation of PR #918 r28 at `4feca97b`

**Verdict: ACCEPT.** All four edits check out against Main §2.3 and GR §3.3, nothing in the exact statements changed, and nothing is overstated or weakened.

The review was read-only. I compared `08e4d757` (the same paper as r27 `59622f0e`) with `4feca97b` in a detached worktree, now removed. Line numbers are at `4feca97b`.

## 1. G1 (L130): confirmed
- The inserted text is verbatim: "A forecast from a start is a forecast of what the rule does only if the hidden part is set up by the same procedure every time; if the procedure changed with the start, a difference between two forecasts could come from the setup rather than from the dynamics."
- It restates the shared hidden prior drawn independently of the root (Main §2.3, Theorem; `RootedRealization`, `CausalReadback.lean:178`).
- It adds no claim.

## 2. G2 (L140): confirmed
- The reason comes first: "a result about a rule has to cover every start the rule can be given, not only the starts a particular sample contains."
- The mechanism sentence follows, with "it can happen that the only rows keeping the table from being a permutation belong to starts that never happen [Main §2.3]" kept verbatim.
- It continues "…, as in the different-deck example; dropping those rows would then describe the sample rather than the rule."
- "It can happen … then" keeps Main §2.3's sense, "possibly only through a row of a root of visible probability zero". It does not restrict the general case.

## 3. G3 (L152): confirmed
**The hypotheses match the Corollary at L148:**

| Corollary (L148) | G3 sentence |
|---|---|
| φ has order L | "a finite reversible world" |
| one hidden prior shared by every root and drawn independently of it | "whose hidden part starts with the same odds whatever is visible at the start" |
| a non-permutation Γ_s, which every non-deterministic visible step supplies | "a visible step that is not fully predictable from the current observation" |
| rows for every root | "forecasts from every start" |

- **The claim is exactly the rooted family failing to be P-divisible on {0,…,L}.** "No single step-by-step chain of forecasts from every start describes the visible sector over the whole cycle" means that no stochastic Δ_{s,t} satisfies Γ_t = Γ_s Δ_{s,t} for all s < t ≤ L.
- **"Although one may hold on every accessible window, as in the example below" is correct.** In the four-bit example at L154, Γ₁ = Γ₂ = ½J, so the forecasts chain on {0,1,2}. The example also has a non-deterministic visible step, so chaining still fails over its full cycle. "May" is the right modality.
- **Nothing implies the property is absent from the dynamics.** The sentence calls it "a property of the world's rule".
- **Nothing implies chaining fails inside a window.**
- **The ending stays at the right scope.** "a constraint on how such a world can be described, not a prediction for accessible data [Main §2.3, Scope]" is anchored to Main §2.3 Scope: "a global recurrence-cycle result … an observer's statistics are its restriction to accessible windows".
- **Your correction was right.** My earlier proposal omitted the shared-prior hypothesis, and the r28 text restores it.

## 4. R (L216–L220): confirmed
- Each condition now opens with GR §3.3's own name: valid probabilities, trivial-ancilla consistency, inert spectators, full reversible control, iterated composition.
- (v) gains "so that a composite can itself serve as the working system of a larger experiment". That is GR §3.3's gloss for iterated composition: "a composite may itself serve as the working system of a larger experiment".
- Apart from the labels and that clause, the text of each condition is unchanged from r27.

## 5. Unchanged material: confirmed
- Every exact statement is word for word as in r27. I checked:
  - Theorems 1–4;
  - both corollaries;
  - the Γ_t definition;
  - the "Stated precisely" scope (L156);
  - the labelled paragraphs of §§4–6;
  - the Bell paragraph.
- The §2.4 Corollary is byte-identical.
- The ledger has no change in this commit, so no ID is retired. `coverage_check` reports OK (134 statements).
- Nothing is weakened.

## 6. The owner's two final questions
- **Is every substantive claim supported by its evidence and assumptions?** Yes.
- **Does the paper communicate the strongest results without unnecessary weakening?** Yes. The recurrence Corollary is stated at full strength with all its hypotheses. The new L152 sentence says what the cycle-wide result means physically, a constraint on descriptions rather than an accessible prediction, without narrowing it and without over-reading it.