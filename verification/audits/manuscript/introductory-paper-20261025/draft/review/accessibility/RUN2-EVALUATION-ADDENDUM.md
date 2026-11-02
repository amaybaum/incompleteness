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