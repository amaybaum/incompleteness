## Gate 2 at `10c629ea`: comprehension test run 2 — not met

The reader now explains Q1–Q4 and Q6 correctly, and most of Q5. Q5 is still PARTIAL on the two concepts the owner singled out. On why the hidden odds must be shared, the reader only restates the hypothesis, and Q7 confirms they guessed. On memory beyond the accessible windows, the reader states the conclusion correctly but not why it happens. Both gaps trace to explanation passages in §2.5 (L134 and L144). Two explanation changes are required before run 3; neither alters a theorem.

I read `RUN2-ANSWERS-10c629ea.md`, `QUESTION-SHEET.md` and `RUN1-EVALUATION.md` at `c89aa61e`, read-only. Line numbers below are the paper at `10c629ea`.

### Q1–Q6 verdicts

**Q1, the basic idea: PASS.**
- "out of reach in principle, not just not yet measured" is correct (L33).
- "any observer inside a closed system who can only read some of its variables" is a correct example of the situation.

**Q2, randomness from hidden information: PASS.**
- The mechanism is correct: "Two complete states can look the same to you and still differ in their hidden parts, and those two can lead to different things you see next" (L29).
- So is the conclusion: "The uncertainty is the player's own ignorance, not something in the rules."

**Q3, the main result: PASS.**
- The three collections coinciding "over any fixed, finite number of steps", in both directions, is correct (Theorem 1).
- "The match is exact only over a chosen stretch of time. A pattern that never repeats can't be reproduced forever by one fixed finite world" is correct (L91; Main §3.4).
- The reader also restates the clock-and-sequence construction correctly (L73).

**Q4, what the result does not show: PASS.**
- Every element of the evaluator note is present:
  - "only … possible";
  - "picks out nothing specific";
  - squaring "put in by hand";
  - the evolution between two times not fixed;
  - one fixed measurement only;
  - "a representation of the statistics, not a physical mechanism";
  - five independent conditions not implied by OI, with the substrate question open.
- The reader's gloss of the five conditions matches L214.
- **One side remark is too broad:** "Bell correlations need one lab's hidden response to depend on the other lab's setting". The paper allows either that, or settings correlated with the hidden state (L250, and §6 L300, "With measurement independence retained"). This is a compression of a peripheral clause, not a failure of the Q4 concept.

**Q5, memory: PARTIAL.**

What the reader got right:
- the forward direction ("must store that memory … big enough to hold it");
- the converse ("if any one such world keeps a trace … the record has memory");
- keeping the past versus memory ("memory is only the part of that store that affects what you see next");
- the capacity bound, the exact minimum hidden predictive memory, and the floor from two pasts;
- the recurrence result with its hypothesis ("If the hidden part starts with the same odds whatever is visible …"), the full-support equivalence, and "That memory might lie beyond any window an observer can actually access".

The evaluator note's "coupling and capacity without readback allow zero memory" is not mentioned. That is an omission, not a scope error.

The two concepts the owner singled out (question 1):

- **Shared odds: the answer only restates the term.** "If the hidden part starts with the same odds whatever is visible" copies the hypothesis and gives no reason for it. Q7 confirms this: "why 'a hidden prior shared by every root and drawn independently of it' matters … I mostly guessed".
- **Hidden memory against visible memorylessness on a window: the conclusion is right, but the reason is missing.**
  - "That memory might lie beyond any window an observer can actually access" is correct.
  - The answer does not say that the record can look memoryless on every accessible window, or why: the hidden part can hold a trace that changes what is seen only later.
  - The reader reproduces L144's conclusion without its mechanism. L144 states the mechanism only abstractly and gives no example.

**Q6, the two applications: PASS.**
- The cosmological-constant answer is correct on both sides:
  - established: two levels, the invisible offset;
  - proposed, and conditional on field equations not yet derived;
  - the observed value taken as an input.
- The black-hole answer is correct:
  - conservation is automatic, recovery is not;
  - the |𝒰| ≥ |ℳ| floor; irreversible worlds can still reveal a message;
  - the Page curve rests on conditions not established.
- "fails for the simple type of dynamics considered" is looser than L292, which says for every bijection on a definite configuration with the split aligned to the configuration coordinates. This is still not a scope error.

### Q7 as evidence (question 2)

**Yes: L134 is a gate-2 defect, even though most of Q5 is correct.** The owner's standard is understanding, and the reader reports guessing at both of L134's points. L134 gives correct reasons, but in abstract terms ("one preparation defines all the rows", "the step … rests on this independence") with no example. It also does not say what keeping the never-occurring rows costs: the failure of chaining can then sit only in forecasts no observer will see. That cost is why the Corollary's equivalence with memory needs full support.

| # | Q7 point | Passage | Classification |
|---|---|---|---|
| 1 | Why the shared prior drawn independently of the root matters, and why never-occurring rows are kept ("mostly guessed") | L134 | **Required** (change 1) |
| 2 | §3.1 is dense; the Hadamard and Pauli-twirl examples assume background | L184–L194 | Recommended (gate 3 covers §3.1) |
| 3 | The five conditions read as a list; unclear which a real world might fail | L214, L216, L218 | Recommended (change 3) |
| 4 | The cosmological-constant "proposed resolution" feels like a restatement | L262–L274 | No change: the reader correctly sees it is conditional, which is the intended reading |
| 5 | Bell terms (ontic parameter dependence, H-Bell, coupling graph) point to other papers | L244, L248, L250 | Recommended (change 4) |
| 6 | The abstract is very compressed and readable only after the body | L17 | Recommended, after F1 |

### Gate verdict: NOT MET

**Changes required before run 3 with a fresh reader.** Both keep every theorem at full strength.

**1. L134: the reasons for the shared odds and for the never-occurring rows.** Keep the first two sentences unchanged ("In words, … (§2.6). Each row of Γ_t … its *root*."). Replace the rest of L134, from "The hidden part is prepared the same way …" to its end, with:

> "The hidden part is prepared the same way whatever is visible at the start, and independently of it: this is the hidden prior shared by every root. It matters because the table $\Gamma_t$ is then a property of one physical setup, the same hidden preparation run forward from each visible start, so every row is the forecast the process actually gives from that start, and a row exists even for a start that never happens. If the hidden preparation depended on the visible start, the rows would describe different setups, and a start that never happens would have no preparation to define its row; the step from two observed histories with a common endpoint to two overlapping rows uses that every row comes from the same preparation [Main §2.3]. Rows for starts that never happen are kept because the argument compares the whole square table with its return to certainty at the recurrence, and the table may fail to be a permutation only through such a row [Main §2.3]. The price is that the failure of chaining can then lie only in forecasts that no observer will see; when every start has positive probability, every row is one that occurs, and the failure is equivalent to memory in the record (the Corollary)."

This incorporates gate-1 F2: "may fail to be a permutation only through such a row" replaces "can sit in such a row alone". It matches Main §2.3's proof: "possibly only through a row of a root of visible probability zero; the lemma applies to the square matrix, which is why every row is kept".

**2. L144: a worked example of memorylessness on a window while the hidden part keeps memory.** Insert after "An observer confined to accessible windows sees neither.":

> "For example, let $X_0,X_1,X_2$ be independent fair bits and $X_3=X_0$. On the window up to time 2 each next observation is independent of the past, so $M_1=I(X_0;X_2\mid X_1)=0$ and the record there is memoryless; yet every hidden deterministic world that reproduces the law must hold $X_0$ at time 2, and at time 3 the past predicts the next observation exactly, $M_2=1$ bit [Main §3.4, Remark (a variational question)]."

The rest of L144, including the "Precisely: …" sentence, stays as it is. I checked the numbers:
- On the window {0,1,2}: M₁ = I(X₀;X₂|X₁) = 0, because X₂ is independent of (X₀,X₁).
- At time 2: M₂ = I(X₀X₁;X₃|X₂) = H(X₀) = 1 bit.
- In every deterministic completion, I(X_{<2};H₂|X₂) ≥ I(X_{<2};X_{>2}|X₂) = 1 bit (L120; `c3_necessity_via_hidden`).

Main uses this example in the same remark.

**Recommended (not blocking):**

3. **L214 or L218: say which conditions are substantive.** Add: "Conditions (i) and (ii) are basic consistency requirements that any operational theory meets; the substantive ones are (iii)–(v), and which of these a physical substratum supplies is the open question." This is GR §3.3: "(i) and (ii) are well-formedness requirements … (iii)–(v) are the substantive selection principles". It is consistent with L216 and with F1.

4. **L250: gloss the Bell terms in plain words.** Add before "whether a coupling graph …": "(the coupling graph records which parts of the substratum directly affect which, and H-Bell is the named hypothesis that suitable extra links can be added for a Bell preparation)". Also consider opening L250 with "Given determinism and an outcome in every run," so that the either/or is not compressed, as the Q4 side remark was.

5. **§3.1 (L184–L194).** Leave this to gate 3's findings for that section.

6. **Abstract (L17).** After applying F1, keep the plain bridging sentence second. Consider moving the formal recurrence sentence's qualifiers after a short plain clause, for example "(in plain terms: hidden odds that do not depend on the visible start)". The scope wording must stay unchanged.

All six proposals are consistent with gate-1 F1–F4 and with gate 3's L230 must-fix; none touches L230.