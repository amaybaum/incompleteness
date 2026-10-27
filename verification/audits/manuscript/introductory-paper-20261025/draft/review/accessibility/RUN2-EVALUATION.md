The scientific reviewer's three reports on run 2, each verbatim and in the order received: the evaluation, its revision after the owner's addendum, and the addendum on the owner's refinement.

***

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

***

## Gate 2 at `10c629ea`: comprehension test run 2 — not met (with the owner's addendum)

The reader now explains Q1–Q4 and Q6 correctly, and most of Q5. Q5 is still PARTIAL on the concepts the owner singled out:
- **The shared hidden starting odds** are only restated, and Q7 says they were guessed.
- **Starting states that never occur** are not explained, and Q7 says they were guessed.
- **Memory beyond the accessible windows** is stated correctly, but not why it happens.
- **Memory against P-divisibility on a finite window** does not appear in the answer at all.

Each gap traces to a passage in §2.5 or §2.6. The fixes below are short additions: one concrete example after the weather analogy, one worked example in L144, and one plain sentence after the parity (XOR) example. No theorem changes.

While checking addendum point 3, I also found one statement that is stronger than its source (L188). It is a gate-1 item and is reported at the end.

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

**Q4, what the result does not show: PASS.**
- Every element of the evaluator note is present:
  - "only … possible";
  - "picks out nothing specific";
  - squaring "put in by hand";
  - the evolution between two times not fixed;
  - one fixed measurement only;
  - "a representation of the statistics, not a physical mechanism";
  - five independent conditions not implied by OI, with the substrate question open.
- **One side remark is too broad:** "Bell correlations need one lab's hidden response to depend on the other lab's setting". The paper allows either that, or settings correlated with the hidden state (L250; §6 L300, "With measurement independence retained"). This is a compression of a peripheral clause, not a failure of the Q4 concept. It is actionable at L250 (recommended change R2).

**Q5, memory: PARTIAL.**

What the reader got right:
- the forward direction ("must store that memory … big enough to hold it");
- the converse ("if any one such world keeps a trace … the record has memory");
- keeping the past versus memory ("memory is only the part of that store that affects what you see next");
- the capacity bound, the exact minimum predictive memory, and the floor from two pasts;
- the recurrence result with its hypothesis, the full-support equivalence, and "That memory might lie beyond any window an observer can actually access".

The evaluator note's "coupling and capacity without readback allow zero memory" is not mentioned. That is an omission; the paper states it at L124.

The concepts the owner singled out:

1. **Shared odds: the answer only restates the term.** "If the hidden part starts with the same odds whatever is visible" copies the hypothesis. Q7: "why 'a hidden prior shared by every root and drawn independently of it' matters … I mostly guessed".
2. **Never-occurring starting states: not covered.** Q7: "why rows for starting states that never occur must be included … I mostly guessed".
3. **Hidden memory against visible memorylessness on a window: the conclusion is right, the reason is missing.** The answer does not say that the record can look memoryless on every accessible window, nor that this is because the hidden part can hold a trace that changes what is seen only later.
4. **Memory against P-divisibility on a finite window (addendum point 3): not present.** The answer does not say that a record can have memory while its forecasts still chain on a window.

**Q6, the two applications: PASS.**
- The cosmological-constant answer is correct on both sides:
  - established: two levels, the invisible offset;
  - proposed, and conditional on field equations not yet derived;
  - the observed value taken as an input.
- The black-hole answer is correct:
  - conservation is automatic, recovery is not;
  - the |𝒰| ≥ |ℳ| floor;
  - irreversible worlds can still reveal a message;
  - the Page curve rests on conditions not established.
- "fails for the simple type of dynamics considered" is looser than L292 but is not a scope error.

### Addendum 1: the two Q7 uncertainties, assessed against the owner's bar

The bar: a non-specialist should understand that the theorem compares hypothetical starting states under one common rule, including starting states that never arise in the sample, and why that comparison is needed. They should get this without knowing what a stochastic matrix is.

**(a) One hidden distribution shared by every starting state: confirmed comprehension defect. Responsible passages: L130 and L134.**
- What is true:
  - The rooted transition matrix Γ_t is defined from one hidden prior μ_H applied to every visible start (Main §2.3 Theorem; `RootedRealization`, `CausalReadback.lean:178`).
  - The proof then uses that the actual process draws the hidden state from μ_H independently of the root. Its step "if Γ_1,…,Γ_min(k,L−1) were all permutations … the visible configuration at each time t ≤ k would be σ_t of the root, μ_H-almost surely" needs this.
  - So every row is "the same hidden mechanism, run from this visible start".
- What the paper gives: L134 states the reason correctly but only abstractly ("one preparation defines all the rows"). L130 has the hypothesis but no picture of what fails without it.
- The defect: a non-specialist cannot see from the text why changing the hidden odds per starting state would spoil the comparison.

**(b) Starting states that never occur: confirmed comprehension defect. Responsible passages: L134 and L142.**
- What is true (Main §2.3 proof): "possibly only through a row of a root of visible probability zero; the lemma applies to the square matrix, which is why every row is kept".
- The consequence: the cycle-wide failure of chaining is a property of the dynamics from every start, and may show up only in a forecast from a start the sample never contains. That is why the equivalence with memory in the record needs every start to be possible (full support).
- What the paper gives:
  - L134 says the overlap "can sit in such a row alone", which is imprecise; gate-1 F2 already corrects it.
  - L142 says the forecasts include "starting points that never occur".
  - Neither says that an absent start still belongs to the comparison, nor what keeping it costs.

### Addendum 2: concrete example right after the weather-forecast analogy (required, change A)

Insert after L130's sentence "…so the chain breaks." and before "The property that fails is called P-divisibility.":

> "The comparison is between starting conditions under one fixed rule. Suppose the dealer always deals red face up, so that a black start never appears in the player's sample. The question is still what the same shuffle, with the face-down card dealt the same way, at even odds, does from a red start and from a black start, and the black start belongs to that comparison although it never occurs. The comparison means something only because the face-down card is dealt the same way whichever card is face up: if the dealer put the opposite colour face down, as in the deal at the end of §2.6, the forecast from red and the forecast from black would describe two different deals, not one rule started in two ways."

Checks:
- **No new technical terms.** The example uses only face-up and face-down cards, deal, shuffle, forecast and start.
- **Definitions untouched.** The rooted-family definition (L132) and the shared-prior assumption are unchanged. The example illustrates them:
  - "the face-down card dealt the same way, at even odds" is the hidden prior shared by every root and drawn independently of it;
  - "a black start never appears … belongs to that comparison" is a row for a root of visible probability zero;
  - the anticorrelated deal is §2.6's own (L174, "With anticorrelated cards (b=1−x), Γ₁ is a permutation and the game is divisible"), so the paper already shows that a root-dependent hidden deal changes the forecasts.
- **L134, minimal companion (recommended, change R1).** Apply gate-1 F2 ("the table may fail to be a permutation only through such a row"), and add one sentence at the end of L134: "The price is that the failure of chaining can then lie only in forecasts that no observer will see; when every start has positive probability, every row is one that occurs, and the failure is equivalent to memory in the record (the Corollary)."

### Hidden memory against visible memorylessness on a window (required, change B)

**Responsible passage: L144.** It states the mechanism abstractly and gives no example.

Insert after "An observer confined to accessible windows sees neither.":

> "For example, let $X_0,X_1,X_2$ be independent fair bits and $X_3=X_0$. On the window up to time 2 each next observation is independent of the past, so $M_1=I(X_0;X_2\mid X_1)=0$ and the record there is memoryless; yet every hidden deterministic world that reproduces the law must hold $X_0$ at time 2, and at time 3 the past predicts the next observation exactly, $M_2=1$ bit [Main §3.4, Remark (a variational question)]."

Checks:
- M₁ = 0, because X₂ is independent of (X₀,X₁).
- M₂ = I(X₀X₁;X₃|X₂) = H(X₀) = 1 bit.
- In every deterministic completion, I(X_{<2};H₂|X₂) ≥ I(X_{<2};X_{>2}|X₂) = 1 bit (L120; `c3_necessity_via_hidden`).
- Main uses this example in the same remark. The "Precisely: …" sentence of L144 stays as it is.

### Addendum 3: memory against P-divisibility on a finite window

**What is true (verified against Main; the four notions are kept apart as in Scheme A).**
- **The proved instance.** A law can have conditional memory M_t>0 while its family of forecasts from the start is P-divisible on a finite window.
  - Then, by the Corollary at L116, every faithful realization carries readout-relevant hidden memory at t.
  - The XOR law (X₀, X₁ independent fair bits, X₂ = X₀⊕X₁) has M₁ = I(X₀;X₂|X₁) = 1 bit. Every two-time matrix is ½J, so the family factors through Δ = I and is P-divisible on {0,1,2}.
  - Sources: Main §2.3, Scope ("It does **not** say that C4 forces P-indivisibility on every accessible short-time window; the XOR control remains a counterexample"); Main §3.4, Remark (the XOR family "has T^{(k)}=T^k exactly with one full bit of it"); paper §2.6, L161.
- **Memory is not Markov factorization.** M_t = 0 at every t is the Markov factorization (L99). XOR fails it at t = 1, yet is P-divisible on the window.
- **Distinguishability backflow is different again.** A revival of distinguishability within a window makes the family P-indivisible on that window (Main §2.3; paper L186), and C1–C4 do not supply it.
- **What is not proved, so the paper must not say it:**
  - That memory and window P-divisibility are independent in both directions in general.
  - Window P-indivisibility without any memory occurs only through rows of roots that never occur (Main §2.3 Scope: "otherwise a non-permutation row may belong to a root of visible probability zero while the realized law has no gap").
  - Under full support, Main proves the link between memory and P-divisibility only at the recurrence horizon {0,…,L}.
  - "Memory and P-divisibility are unrelated" would overstate.
- **One more scope caveat.** XOR's P-divisibility is on the window only. Any reversible world that reproduces XOR with hidden odds that do not depend on the visible start still fails to chain somewhere in its full cycle (the Corollary), because its visible steps are not fully predictable.

**Does the paper convey it?** Correctly, but only in technical form, and away from the §2.5 reconciliation:
- L161's plain gloss explains parity ("neither earlier bit alone predicts it, and both together determine it") but does not say what the example shows.
- L186 says "conditional memory does not force short-window indivisibility (§2.6)".
- L144's reconciliation is about Markov on every accessible window against memory before the return, which is a different statement.

**Does Q5 show it was understood?** No; the reader does not mention it.

**Proposed wording (required, change C, at proved strength).** Add after L161 ("…[Dou26, App. A]."):

> "So on this window the forecasts from the start chain step by step, and yet the record has memory, and every hidden world that reproduces it carries that memory in its hidden part: memory in the record and the chaining of forecasts are different properties. A reversible world that reproduces this law, with the face-down odds independent of the visible start, still fails to chain somewhere in its full cycle (§2.5), because its visible steps are not fully predictable."

This states only the proved instance and its scope. It does not claim that the two properties are independent in both directions.

### Q7 as evidence, and where each point is addressed

**Yes: L130 and L134 are gate-2 defects, even though most of Q5 is correct.** The reader reports guessing at both conditions, and the owner's bar asks for understanding without the formalism. Changes A and R1 address it.

| # | Q7 point | Responsible passage | Classification |
|---|---|---|---|
| 1 | Why the shared prior drawn independently of the root matters | L130, L134 | **Required:** change A |
| 2 | Why never-occurring rows are kept | L134, L142 | **Required:** change A; recommended: R1 |
| 3 | §3.1 dense; Hadamard and Pauli-twirl assume background | L184–L194 | Recommended (gate 3 covers §3.1) |
| 4 | The five conditions read as a list; unclear which a real world might fail | L214, L216, L218 | Recommended: R3 |
| 5 | The cosmological-constant "proposed resolution" feels like a restatement | L262–L274 | No change: the reader correctly sees it is conditional, which is the intended reading |
| 6 | Bell terms (ontic parameter dependence, H-Bell, coupling graph) | L244, L248, L250 | Recommended: R2 |
| 7 | The abstract is very compressed | L17 | Recommended: R4, after F1 |

### Addendum 4: every shortfall mapped to its passage

| Shortfall | Responsible passage | Action |
|---|---|---|
| Q5 concept 1 (shared odds restated, not understood) | L130, L134 | Change A (required) |
| Q5 concept 2 (never-occurring starts not explained) | L134, L142 | Change A (required); R1 with F2 (recommended) |
| Q5 concept 3 (memoryless window: conclusion without reason) | L144 | Change B (required) |
| Q5 concept 4 (memory against window P-divisibility absent) | L161, L186 | Change C (required) |
| Q4 Bell side remark (one alternative dropped) | L250 | R2 (recommended) |
| Q5 omits coupling without readback | L124 (states it correctly) | None; omission only |
| Q6 "simple type of dynamics" | L292 (states it precisely) | None; reader compression |

### Gate verdict: NOT MET

**Required before run 3 with a fresh reader:** changes A, B and C above. All three keep every theorem and definition at full strength.

**Recommended:**
- **R1 (L134).** Apply F2 and add the "price" sentence quoted under addendum 2.
- **R2 (L250).** Open with "Given determinism and an outcome in every run," and add "(the coupling graph records which parts of the substratum directly affect which, and H-Bell is the named hypothesis that suitable extra links can be added for a Bell preparation)".
- **R3 (L214 or L218).** Add "Conditions (i) and (ii) are basic consistency requirements that any operational theory meets; the substantive ones are (iii)–(v), and which of these a physical substratum supplies is the open question" (GR §3.3).
- **R4 (L17).** After applying F1, keep the plain bridging sentence second, and consider a plain gloss of the recurrence qualifiers. The scope wording must stay unchanged.
- **§3.1.** Leave this to gate 3's findings.

All proposals are consistent with gate-1 F1–F4 and with gate 3's L230 must-fix; none touches L230.

### One more finding (gate 1, required): L188 is stronger than its source

- **Current text (L188):** "Three notions are distinct, and no unconditional implication holds among them [Main §3.2, Remark (three notions, kept apart)]".
- **The source says:** "No unconditional implication among the three is asserted here" (Main §3.2, unchanged at `4449b0d9`).
- **Problem:** "holds" turns "not asserted" into "proved to fail", and Main does not prove that for every ordered pair.
- **What is proved:**
  - (1) does not imply (2) on a window (XOR, L161);
  - (2) does not imply (3) outside the diagonal-preserving class (Hadamard, L188);
  - (2) implies CP-indivisibility for the permutation-dilation family (L188).
- **Proposed replacement:** "Three notions are distinct, and no unconditional implication among them is asserted [Main §3.2, Remark (three notions, kept apart)]: … ; accessible memory does not force P-indivisibility on a window (§2.6), and outside the diagonal-preserving class P-indivisibility does not force CP-indivisibility (below)."

***

## Addendum to the run-2 evaluation (owner's refinement of item 3)

**Results:** both owner questions are answered yes, with the exact formulation Main supports. The L144 four-bit example serves question (B) and, as reworded below, meets the owner's scope condition. L134, L144 and the Summary keep the three terms apart, with one small tightening proposed for L144. The shared-prior rewrite matches the formal construction after one correction: rows for starts that never occur are not forecasts the process "actually gives". Final wording for all three changes is at the end.

Every claim below is checked against Main at `4449b0d9`, where §2.3 is unchanged since `55e3217b`. Line numbers are the paper at `10c629ea`.

### (A) Can a process have predictive memory and still be P-divisible on the specified window?

**Yes, and Main supports one exact formulation.**
- The XOR law: X₀ and X₁ are independent fair bits and X₂ = X₀ ⊕ X₁.
- It has predictive memory: M₁ = I(X₀;X₂|X₁) = 1 bit.
- Its rooted family Γ₁ = P(X₁|X₀) = ½J and Γ₂ = P(X₂|X₀) = ½J is P-divisible on {0,1,2}, since Γ₂ = Γ₁·I.
- By the Corollary at L116, every faithful realization carries readout-relevant hidden memory at t = 1.
- Anchors:
  - Main §2.3, Scope: "It does **not** say that C4 forces P-indivisibility on every accessible short-time window; the XOR control remains a counterexample to that stronger statement."
  - Main §3.4, the Remark after the physical-memory theorem: the XOR family "has T^{(k)}=T^k exactly with one full bit of it".
  - The paper states it at L161 and L186.

**Scope of what is proved:**
- This is one law on one window. It shows that predictive memory, even accessible memory, does not force P-indivisibility on that window.
- Main does **not** prove that the two properties are independent in both directions in general.
- Any reversible world that reproduces XOR with hidden odds independent of the visible start is still P-indivisible somewhere in its full recurrence cycle (the Corollary), because its visible steps are not fully predictable.

**Would stating it improve comprehension? Yes.**
- The paper already has the result (L161, L186), but L161's plain gloss explains parity, not what the example shows.
- Run 1's reader asked "how this kind of indivisibility differs from memory".
- Run 2's reader does not mention the distinction at all.
- One plain sentence after L161 targets exactly that gap.

Both conditions hold, so I keep the addition (change C below), shortened to the proved instance. The recurrence-cycle caveat is optional.

### (B) Can a finite reversible system look memoryless on every accessible window yet show memory at a later order before the return?

**Yes. This is the point L144 makes, and the four-bit example serves it.**
- The law: X₀, X₁, X₂ are independent fair bits and X₃ = X₀.
- **Memoryless on the window {0,1,2}.** M₁ = I(X₀;X₂|X₁) = 0, because X₂ is independent of (X₀, X₁).
- **Predictive memory at the later order 2, seen at time 3.** M₂ = I(X₀X₁;X₃|X₂) = H(X₀) = 1 bit.
- **Every faithful deterministic completion must keep X₀ at time 2.**
  - In a deterministic completion, X₃ is a function of (X₂, H₂), and X₃ = X₀.
  - So, given X₂, the hidden state H₂ determines X₀.
  - Equivalently, I(X_{<2};H₂|X₂) ≥ I(X_{<2};X_{>2}|X₂) = 1 bit (L120; `c3_necessity_via_hidden`; Main §3.4, Remark "a variational question", which uses this very example).
- **The owner's scope condition holds.**
  - On {0,1,2} the rooted family is Γ₁ = Γ₂ = ½J, which is P-divisible.
  - The example establishes no P-indivisibility on any accessible window.
  - Chaining fails only on a horizon that includes the later time: on {0,…,3}, Γ₃ = I while Γ₁ = ½J.
- The sentence below states this explicitly, so it cannot be read the other way.

### The three terms in L134, L144 and the Summary

| Passage | Predictive memory | P-divisibility | Accessible memory | Verdict |
|---|---|---|---|---|
| L134 | not mentioned (the proposed price sentence adds "memory in the record at some step before the return") | rooted-family chaining | not mentioned | Kept apart |
| L144 | "memoryless on a window … M_t = 0 there"; "conditional dependence … at some order beyond the window" | "failure of chaining" across the recurrence cycle | "An observer confined to accessible windows sees neither" | Kept apart |
| L296 (Summary) | "memory … conversely …" | "forecasts … that cannot be chained step by step" | not mentioned | Kept apart |

**Proposed tightening at L144 (recommended).**
- The phrase "Hidden memory can exist all the same" blurs hidden storage with predictive memory in the record.
- Proposed: "Predictive memory can exist all the same, at a later order, because the hidden part can hold a trace of the past that changes what is seen only later:".
- L146 already keeps accessible memory separate ("what an observer can discriminate is memory at an accessible order").

### Final check of the shared-prior rewrite and the card example

**Against the formal construction:**

| Requirement | Status |
|---|---|
| One hidden preparation rule, with no change per starting condition | Met: "the same hidden preparation run forward from each visible start"; "the face-down card dealt the same way, at even odds, whichever card is face up" |
| Rows for roots of visible probability zero are kept | Met: "a start that never happens still has a row, computed from the same preparation"; "the black start belongs to that comparison" |
| The two-row overlap argument is preserved | Met: Theorem 3 and the Corollary are untouched; the rewrite names the step "from two observed histories with a common endpoint to two overlapping rows" and cites Main §2.3, whose proof uses the shared, independent prior (μ_H-almost surely) |

**One correction.** My earlier wording said every row is "the forecast the process actually gives from that start". That is false for starts that never occur. Fixed below.

### Final wording

**Change A (required).** Insert in L130 after "…so the chain breaks." and before "The property that fails is called P-divisibility.". Unchanged from the main report.

> "The comparison is between starting conditions under one fixed rule. Suppose the dealer always deals red face up, so that a black start never appears in the player's sample. The question is still what the same shuffle, with the face-down card dealt the same way, at even odds, does from a red start and from a black start, and the black start belongs to that comparison although it never occurs. The comparison means something only because the face-down card is dealt the same way whichever card is face up: if the dealer put the opposite colour face down, as in the deal at the end of §2.6, the forecast from red and the forecast from black would describe two different deals, not one rule started in two ways."

**Change 1, L134 (approved subject to this check).** Keep the first two sentences unchanged. Replace from "The hidden part is prepared the same way …" to the end with:

> "The hidden part is prepared the same way whatever is visible at the start, and independently of it: this is the hidden prior shared by every root. It matters because the table $\Gamma_t$ is then a property of one physical setup, the same hidden preparation run forward from each visible start: the row for a start that occurs is the forecast the process gives from it, and a start that never happens still has a row, computed from the same preparation. If the hidden preparation depended on the visible start, the rows would describe different setups, and a start that never happens would have no preparation to define its row; the step from two observed histories with a common endpoint to two overlapping rows uses that every row comes from the same preparation [Main §2.3]. Rows for starts that never happen are kept because the argument compares the whole square table with its return to certainty at the recurrence, and the table may fail to be a permutation only through such a row [Main §2.3]. The price is that the failure of chaining can then lie only in forecasts that no observer will see; when every start has positive probability, every row is one that occurs, and the failure is equivalent to predictive memory in the record at some step before the return (the Corollary)."

This includes gate-1 F2. If the owner prefers a minimal L134, apply only F2 and the final "price" sentence (R1); change A then carries the intuition.

**Change B, L144 (required; adjusted to the owner's scope condition).** Insert after "An observer confined to accessible windows sees neither.":

> "For example, let $X_0,X_1,X_2$ be independent fair bits and $X_3=X_0$. Up to time 2 each next observation is independent of the past, so $M_1=I(X_0;X_2\mid X_1)=0$: the record has no accessible memory on that window, and its forecasts from the start chain step by step there. Yet every deterministic world that reproduces the law, reversible or not, must keep $X_0$ in its hidden part at time 2, and at time 3 the past predicts the next observation exactly, $M_2=1$ bit [Main §3.4, Remark (a variational question)]. The example shows memory beyond the window; it shows no failure of chaining inside it."

**Change C, after L161 (required; kept because both (A) conditions hold).**

> "So on this window the forecasts from the start chain step by step, yet the record has predictive memory, and every reversible world that reproduces it carries that memory in its hidden part: predictive memory and P-divisibility are different properties."

Optional second sentence: "A reversible world that reproduces this law, with the face-down odds independent of the visible start, still fails to chain somewhere in its full cycle (§2.5)."

All of these keep every theorem, the rooted-family definition and the shared-prior assumptions exactly as stated. They are consistent with gate-1 F1–F4, with the L188 finding and with gate 3's L230 must-fix.
