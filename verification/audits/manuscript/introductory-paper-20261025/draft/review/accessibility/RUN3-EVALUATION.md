## Gate 2 at `e64b2a4c`: comprehension test run 3 — not met

The reader explains Q1–Q4 and Q6 correctly, and Q5's main memory results are right. Q5 is still PARTIAL on the owner's three criteria:
- **(a) why the hidden preparation is shared** is only restated;
- **(b) why never-occurring starts are kept** is absent from the answer;
- **(c) hidden memory** is explained, but the two cases are run together: memory at a later step an observer still sees, and memory beyond every accessible window, which no observer detects.

Q7 confirms that (a) and (b) still take "several passes", and that the reader does not see why a failure "somewhere in the cycle" matters physically. Two short explanation changes are required, at L130 and L146. Neither touches a theorem.

I read `RUN3-ANSWERS-e64b2a4c.md`, `QUESTION-SHEET.md` and the run-2 reports at `f27c4e21`, read-only. The paper there is identical to `e64b2a4c`. Line numbers below are the paper at `e64b2a4c`.

### Q1–Q6 verdicts

**Q1, the basic idea: PASS.**
- "out of reach in principle, not just not yet measured" is correct (L33).
- "The hypothesis is that every physical observer is in that player's position" is correct.

**Q2, randomness from hidden information: PASS.**
- "many hidden states fit the same visible state, and the deterministic rule sends them to different visible futures" is correct (L29).
- So is the stored-sequence construction (L73).

**Q3, the main result: PASS.**
- The three collections coincide over a fixed finite horizon, in both directions (Theorem 1).
- "no record of one repeated measurement can by itself rule out a hidden deterministic explanation" is correct (L93).
- "A pattern that never repeats cannot be reproduced exactly for all time by one fixed finite world" is correct (L91; Main §3.4).

**Q4, what the result does not show: PASS.**
- Every element of the evaluator note is present:
  - "possibility, not fact";
  - one fixed measurement;
  - the Born exponent not selected, with the correct reason ("permutations with entries 0 and 1");
  - the evolution between two times not fixed;
  - representation without mechanism;
  - the five conditions, not implied by OI, with the non-coherent qubit theory;
  - (iii)–(v) open.
- One side remark is wrong in scope; see "The Q4 side remark" below.

**Q5, memory: PARTIAL.**

What the reader got right:
- the forward and converse memory results;
- storage versus memory ("A reversible world always stores its whole past … Memory … is only the part of that store that affects what is seen next");
- the capacity bound, the exact minimum and the Pinsker floor;
- the recurrence result with its shared-odds hypothesis.

The owner's three criteria:

- **(a) Shared hidden preparation: restatement only.** "Suppose the hidden part starts with the same odds whatever is visible at the start" repeats the hypothesis. The answer does not say that the comparison is about one hidden preparation rule tried from different starts, nor that changing the hidden odds start by start would compare different rules.
- **(b) Never-occurring starts: absent.** Q5 does not mention them. Q7 says their role "took several passes".
- **(c) Hidden memory against a memoryless window: partly understood, with the two cases conflated.**
  - The answer says the failure "can happen beyond any window the observer can actually access, so the memory might first show up only at very long time scales", and gives the four-bit example as an instance.
  - "might first show up" implies the observer eventually sees it, which is true only when a window reaches the later step, as in the four-bit case with a window through time 3.
  - When the memory lies beyond every accessible window, no observer ever detects it.
  - The answer also links P-indivisibility to the memory showing up. The paper does not say this.

**Q6, the two applications: PASS.**
- **Cosmological constant.** Correct on all three levels:
  - established: the two levels, the invisible offset;
  - proposed: under the targeted field equations;
  - open: those field equations, and the observed value taken as an input.
- **Black holes.** The toy-model numbers and the floor are correct. Two phrasings are slightly loose:
  - "The scrambling condition fails for these permutation dynamics" is looser than L288, which says it fails on a definite configuration with a configuration-aligned split.
  - "the same-energy condition does not hold" matches L288's proper-shell case.
  - Neither is a scope error.

### The Q4 side remark

**What the reader wrote:** "Bell correlations need one lab's hidden response to depend on the other lab's setting, which is the open hypothesis 'H-Bell'".

**What is wrong.**
- It drops the alternative of settings correlated with the hidden state.
- It identifies ontic parameter dependence with H-Bell. H-Bell is the narrower open question of whether a preparation-indexed coupling graph can supply that dependence without signalling and while keeping the continuum limit.

**Where it comes from.**
- L246 states both options correctly: "only if one laboratory's hidden response depends on the other laboratory's choice, or if the choices are correlated in advance with the hidden state".
- The compression matches §6 L296 almost word for word: "With measurement independence retained, quantum Bell correlations then require ontic parameter dependence, subject to H-Bell". A reader remembering L296 loses the condition.

**Does it matter for the gate?** No. It is peripheral to Q4's concept and is not one of the owner's Q5 criteria. It has now recurred twice, though, so a change is recommended (R2 below).

### Q7 as evidence

**1. Never-occurring rows and the shared prior ("took several passes"): a remaining gate-2 defect. Passages responsible: L130 and L134.**
- The card example at L130 shows hidden-preparation dependence, but only as a contrast ("would describe two different deals").
- It does not say the conclusion: the comparison is about the rule, not the sample.
- For never-occurring starts it says only that "the black start belongs to that comparison", not why it must.
- L134 gives the reason abstractly: "the only rows keeping the table from being a permutation belong to starts that never happen". There is no picture.
- The card example cannot supply that picture, because in the swap game both rows overlap.

**2. Why a failure "somewhere in the cycle" matters physically if it can sit outside every window: a remaining gate-2 defect. Passage responsible: L146.**
- L146 says the observer "sees neither", and L146's closing sentence says the result "does not separate them from memory-bearing laws at accessible orders".
- It never says plainly what the cycle-wide failure is: a structural consequence of finite reversibility and partial access, which no accessible window records. Its observable counterpart is memory at an accessible order.
- The same passage presents the four-bit example ("For example …") straight after "conditional memory that no accessible window detects". This invites the case conflation seen in Q5(c).

**Other Q7 points:**

| Point | Passage | Classification |
|---|---|---|
| §3.1 dense, Pauli-twirl "still classical" | L184–L194 | Recommended (gate 3's §3.1 scope) |
| Five-condition structure terms ("spectator-independent readout", "outcome-conditioned composition") | L202 | Recommended: R3 |
| What Theorem 1 says physically ("close to … a lookup table") | L71, L93 | None. This is the correct reading; L93 makes memory the content |
| Bell "preparation-indexed coupling graph", and how it avoids signalling | L244–L246 | Recommended: R2. How it avoids signalling is the open part of H-Bell, and the paper should say so plainly |
| Cosmological constant reads as a reinterpretation pending field equations | L254–L274 | None. This is the intended conditional reading |
| Reliance on companion papers | throughout | None. Proofs are cited by design; every result carries its evidence class |

### Gate verdict: NOT MET

**Required explanation changes.** Both keep every theorem and definition at full strength.

**Change D: L130, the rule rather than the sample, with a never-occurring start.**

Insert after "…not one rule started in two ways.":

> "So the comparison is about one fixed rule, the same hidden preparation tried from every visible start the world could have, not about the starts a sample happens to contain; letting the hidden odds change with the start would compare different rules. A start that never occurs stays in the comparison for the same reason. A rule could, for instance, make a red start always show red after the first shuffle while a black start may show either colour: a dealer who always deals red then never sees uncertainty, yet under that rule the forecasts from the two starts overlap, and they overlap only because of the start that is never dealt [Main §2.3]."

- **It matches the formal construction.** There is one shared hidden prior, independent of the root. The zero-probability root keeps its row. The overlap is "only because of" that row, which matches Main §2.3's "possibly only through a row of a root of visible probability zero". It does not say the overlap lies in one row, so the F2 misreading is avoided.
- **The rule is realizable**, with a shared prior that need not be uniform. Take visible {R, B}, hidden {0, 1, 2}, and μ_H uniform on {0, 1}.
  - The bijection is φ(R,0)=(R,0), φ(R,1)=(R,1), φ(R,2)=(B,2), φ(B,0)=(R,2), φ(B,1)=(B,1), φ(B,2)=(B,0).
  - The red row is a point mass at R. The black row is (½, ½). The rows overlap at R.
  - By Theorem 3 the family is not P-divisible on {0,…,L}.
- **It does not read as a proof.** It is placed before the formal statements.

**Change E: L146, the two cases kept apart, and what the cycle-wide failure is.**

Insert after "…therefore sees neither the late dependence nor the failure of chaining.", and before "For example,":

> "Two cases should be kept apart. If the memory first affects a later step that some accessible window still reaches, an observer who watches that long detects it, as in the example below. If it first affects what is seen only beyond every accessible window, no observer detects it; the failure of chaining across the cycle is then a structural consequence of finite reversibility and partial access, not something any accessible window records, and what an observer can test is memory at an accessible order, which (C4) asserts."

Then change "The example shows memory beyond the window; it shows no failure of chaining inside it." to:

> "Here the window ends at time 2: an observer whose window reaches time 3 detects the memory, while one whose windows all end at time 2 never does. The example shows memory beyond the window; it shows no failure of chaining inside it."

- **Anchors.** Main §2.3, Scope: "an observer's statistics are its restriction to accessible windows, and on them the memory is witnessed only by a gap at an accessible order". Also the (C4) requirement "kτ_S ≪ t_R".
- **Scope of the claim.** The sentence claims nothing about chaining inside a window beyond what the four-bit example already shows (Γ₁ = Γ₂ = ½J). The structural reading is stated only for the case beyond every window.

**Recommended:**
- **R2 (L296, and optionally L246).** Make the either/or explicit where it is summarized: "Bell's theorem, given determinism and an outcome in every run, leaves two options; with measurement independence retained, quantum Bell correlations then require ontic parameter dependence, whose realization on the substratum without usable signalling and with the gravitational continuum limit is the open hypothesis H-Bell (§3.5)."
- **R3 (L202).** Add one plain gloss of the structure: "in plain terms, the experimenter can do nothing, combine operations and lump outcomes together, prepare an evenly mixed helper, read the helper without disturbing the system, and discard it."
- **§3.1.** Leave this to gate 3's findings.

Changes D and E are consistent with gate-1 F1–F4, with the r22–r24 terminology and with gate 3's earlier findings. Every theorem, the rooted-family definition and the shared-prior assumptions remain exactly as stated.