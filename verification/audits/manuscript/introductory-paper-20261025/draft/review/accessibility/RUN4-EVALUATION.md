## Gate 2 at `59622f0e`: comprehension test run 4 — not met

The reader explains Q1–Q4 and Q6 correctly, and most of Q5. Q5 still falls short on all three owner-specified parts:
- **(a)** the shared hidden preparation is restated, not explained;
- **(b)** the reason for keeping starts that never occur is absent;
- **(c)** improves on run 3: the conflation of the two cases is gone, and the reader states correctly that the effect "can sit beyond any time window an observer can actually reach". But the answer gives no reason why such an effect is established yet unobservable.

Q7 raises, for the fourth time, why a cycle-wide failure matters physically. This is a **legitimate objection that the paper leaves unanswered**, not a misunderstanding. Three short additions are required, at L130, L140 and L152. None changes a theorem.

I read `RUN4-ANSWERS-59622f0e.md`, `QUESTION-SHEET.md` and `RUN3-EVALUATION.md` at `9daa17b3`, read-only. The paper there is identical to `59622f0e`, and line numbers below are the paper at that commit.

### Q1–Q6 verdicts

**Q1, the basic idea: PASS.**
- Correct: "The rest is not just unknown so far. It is out of reach in principle" (L33).
- Correct: "this is not the usual quantum 'you can't measure both' kind of limit. It applies even when you only ever look at one fixed thing" (L33).

**Q2, randomness from hidden information: PASS.**
- Correct mechanism: "When the hidden part of a world differs, the same visible state can lead to different futures" (L29).
- Correct own example: the secretly ordered deck.
- The stored-sequence construction is also correct (L73).

**Q3, the main result: PASS.**
- The three sets coincide over a fixed number of steps, in both directions (Theorem 1).
- "no statistical fingerprint that a hidden deterministic world couldn't copy" is correct (L71, L93).
- "A pattern that never repeats can't be reproduced exactly for all time by one fixed finite world" is correct (L91).

**Q4, what the result does not show: PASS.**
- Every element of the evaluator note is present, including "the construction works the same for any power" and the qubit theory that never creates superpositions.
- **Side remark:** "would need one lab's hidden response to depend on the distant lab's setting" again drops the measurement-dependence alternative.
  - L246 and L306 now both state the either/or explicitly, so this is reader compression, not a gap in the paper.
  - No change is required.

**Q5, memory: PARTIAL.**
- Correct throughout:
  - the forward direction and the converse ("a trace that actually affects what you see next");
  - the capacity bound, the minimum hidden memory and the floor;
  - the recurrence result with its hypothesis;
  - "Memory and chaining failure are also not the same thing, and the paper gives examples of each without the other". Memory without chaining failure is L161's parity example. Chaining failure without memory is L132's never-dealt start.
- The three owner-specified parts:

| Part | Verdict | From the answer's wording | Passage that enabled or failed |
|---|---|---|---|
| (a) why one hidden preparation across hypothetical starts | **PARTIAL: restatement** | "Suppose the hidden part starts the same way whatever you see at the start." The hypothesis is correct but no reason is given. | L130: "The comparison is about one fixed rule … it means something only because the face-down card is dealt the same way …". The reason is there, but as a contrast ("two different deals"). It never says plainly that differences between rows would otherwise come from the setup rather than from the dynamics. |
| (b) why never-occurring starts stay in the rooted family | **FAIL: absent** | Not mentioned in Q5. Q7: the rooted family "keeps forecast rows for starting states that never actually happen", and the card discussion "helped a little but stayed confusing". | L132, the different-deck example, which is mathematically exact. L140: "kept because the argument compares the whole square table … it can happen that the only rows keeping the table from being a permutation belong to starts that never happen". Both give the mechanism but not a plain reason a non-specialist can carry: a result about a rule must cover every start the rule can be given. |
| (c) why an effect beyond every accessible window is established but cannot be observed | **PARTIAL: correct conclusion, no reason** | "that failure, and some of the memory, can sit beyond any time window an observer can actually reach". This is correct, and no longer conflated with the case where a later step is reached. But "why" is missing, and Q7 asks whether it is "physically meaningful rather than a feature of the bookkeeping". | L152: "both remain established in the dynamics under the theorem's hypotheses, but neither appears in any accessible record". This says that it is unobservable, but not what an established-but-unobservable property means physically. L158 says only that it "does not separate them from memory-bearing laws at accessible orders". |

**How each part changed from run 3 to run 4:**
- **(a): unchanged; restated both times.** The r25–r26 fixed-rule sentence at L130 and the r27 merge did not move the reader from restatement to explanation.
- **(b): unchanged; absent from Q5 both times.** Change D's different-deck example (L132) helped the reader see what is kept ("keeps forecast rows for starting states that never actually happen"), but not why.
- **(c): improved.** Change E's two-case wording (L152) removed run 3's conflation ("might first show up only at very long time scales"). The reader now places the effect beyond every reachable window correctly. The remaining gap is the physical meaning (below).

**Q6, the two applications: PASS.**
- **Cosmological constant.**
  - Established: the two levels, and the invisible offset that lets a gravitational source be "define[d] … separately".
  - Open: the field equations, with "two versions … fit everything visible equally well".
  - The observed value is taken as an input.
- **Black holes.**
  - Conservation and recovery are separated.
  - The floor |𝒰| ≥ |ℳ| and the non-injective recovery are correct.
  - The three Page-curve conditions are given with their status.
  - "the scrambling one fails for the simple reversible maps it has in mind" is looser than L288's definite configuration with aligned split, but it is not a scope error.

### Q7 as evidence

**The cycle-wide failure: legitimate objection.** The reader asks why a failure seen only in forecasts no observer will see, or only beyond every reachable window, is "physically meaningful rather than a feature of the bookkeeping".
- **Not a misunderstanding.** The reader has everything the paper says right: the effect is established and unobservable (L152), and it does not discriminate laws (L158).
- **A fair question the paper leaves unanswered.** The paper states what the result is and that it cannot be seen, but never what it means physically or what it does not mean.
- **Not mainly a presentation problem.** Four runs with different wordings have raised the same question.
- **The shortest correct answer at proved strength** (anchor: Main §2.3, Scope: "This is a global recurrence-cycle result … The equivalence is a property of the representative's rooted law over its whole recurrence cycle; an observer's statistics are its restriction to accessible windows"):
  - The result is a property of the world's rule, its dynamics together with its hidden preparation, not of any record.
  - Its physical content is a constraint on descriptions: in any finite reversible world with a non-deterministic visible step, no single step-by-step chain of forecasts from every start can describe the visible sector over the whole cycle, although one may hold on every accessible window.
  - It is not an experimental prediction for accessible data, and because it needs so little it cannot by itself tell one law from another.
  - What an observer can test is memory at an accessible order (C4).
- **Every claim in that answer is proved.**
  - The first part is the Corollary.
  - "may hold on every accessible window" is the four-bit example (Γ₁ = Γ₂ = ½J).
  - "cannot by itself tell" is L158 and Main §2.3, Scope.

**Other Q7 points:**

| Point | Passage | Classification |
|---|---|---|
| §3.1 dense (Hadamard, Pauli twirl) | L190–L200 | Recommended (gate 3's §3.1 scope) |
| (v) and the five conditions, "what physical demand each one makes" | L216–L224 | Recommended: one plain clause per condition, for example for (v): "a composite can itself serve as the working system of a larger experiment" (GR §3.3, "Iterated composition") |
| Bell coupling graph and H-Bell "beyond the gist" | L244–L246 | None: the R2 glosses are in place, and the gist is what the paper can say while H-Bell is open |
| "its strength comes from matching everything … says little about physics" | L71, L93 | None: this is the paper's own correct reading; L93 locates the content in memory |
| Applications "read more like reframings" | §§4–5 | None: this is the intended conditional reading (G3; the Page-curve conditions) |
| Reliance on companion papers | throughout | None: proofs are cited by design, and each result carries its evidence class |

### Gate verdict: NOT MET

**Required explanation changes.** Each keeps every theorem, the rooted-family definition and the shared-prior assumptions exactly as stated.

**G1 (L130), for part (a): give the reason plainly.** Insert after "…not one rule started in two ways.":

> "A forecast from a start is a forecast of what the rule does only if the hidden part is set up by the same procedure every time; if the procedure changed with the start, a difference between two forecasts could come from the setup rather than from the dynamics."

This is a restatement of the shared prior drawn independently of the root (Main §2.3, Theorem; `RootedRealization`, `CausalReadback.lean:178`). It adds no claim.

**G2 (L140), for part (b): the plain reason for keeping never-occurring starts.** Insert before "Rows for starts that never happen are kept because …":

> "A result about a rule has to cover every start the rule can be given, not only the starts a particular sample contains: here the evidence that the forecasts cannot be chained may come only from such a start, as in the different-deck example, and dropping it would describe the sample rather than the rule."

The anchor is Main §2.3's proof ("possibly only through a row of a root of visible probability zero"). The existing mechanism sentence stays.

**G3 (L152), for part (c) and the Q7 objection: what the cycle-wide result means physically.** Insert after "…but neither appears in any accessible record.":

> "Such a failure is a property of the world's rule, its dynamics with its hidden preparation, rather than of any record: in any finite reversible world with a visible step that is not fully predictable, no single step-by-step chain of forecasts from every start describes the visible sector over the whole cycle, although one may hold on every accessible window, as in the example below. It is a constraint on how such a world can be described, not a prediction for accessible data, and since it needs so little it does not tell one law from another; what an observer can test is memory at an accessible order, which (C4) asserts [Main §2.3, Scope]."

- The failure statement is the Corollary.
- "may hold on every accessible window" is the four-bit example at L154 (Γ₁ = Γ₂ = ½J).
- The closing clause repeats L158 and Main §2.3's Scope.
- Nothing claims that chaining fails inside a window, and nothing claims the property is absent from the dynamics.

**Recommended:** the five-conditions clause above, and gate 3's §3.1 items.

These changes are consistent with gate 1's accepted r21–r27 text and with the owner's causal safeguard at L132.