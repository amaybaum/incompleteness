# Gate 1 (scientific accuracy): focused confirmation of PR #918 r22 at `40935ccf`

**Verdict: ACCEPT WITH CHANGES.** Two new explanatory sentences say more than their sources and must be corrected before merge (R1 at L99, R2 at L148). Everything else is confirmed.

The review was read-only, against r21 `d3790019`; the parent `683c45de` has the same paper. I used a detached worktree at `40935ccf`, which is now removed. Line numbers are at `40935ccf`.

## 1. L134, starts that never happen: confirmed
- The new wording is "it can happen that the only rows keeping the table from being a permutation belong to starts that never happen [Main §2.3]".
- It carries the sense of Main §2.3's proof, "possibly only through a row of a root of visible probability zero": it states a possibility and does not restrict the general case.
- It speaks of the rows that keep the table from being a permutation, not of an overlap sitting in one row, so the F2 misreading is gone.
- Also correct in L134:
  - "a preparation that depended on the start would give rows for different setups, as in the card comparison above";
  - the overlap definition "two rows that are both positive in a common column (Theorem 3)", which applies O1;
  - "(see the Corollary)", which points to where the full-support equivalence is stated.

## 2. The abstract (L17): confirmed
I checked every row of CHANGES-r22 §2 against the r21 text.

**Theorem 4.** The sentence is unchanged from r21 and carries every hypothesis:
- an operational theory with a stated minimal structure;
- a nonempty finite system, on the system and with every finite ancilla;
- exactly the normalized finite Kraus instruments, if and only if the five conditions hold;
- not implied by OI.

**The recurrence sentence carries every hypothesis:**
- a finite reversible world;
- hidden odds "shared by every visible start and drawn independently of it";
- "the forecasts from every start, starts of probability zero included", which is the rooted family;
- "P-indivisible somewhere in the recurrence cycle whenever some rooted transition matrix is not a permutation";
- "in particular whenever a visible step is not fully predictable from the current observation", which also applies r21's O5;
- "with every start of positive probability, this is equivalent to conditional memory at some order below the recurrence time", which is the full-support equivalence.

**The rest is preserved:**
- the three-class equality;
- the machine-checked attribution;
- "every faithful realization carries the law's conditional memory in its hidden state";
- "any memory they show must be stored in the hidden part";
- the two applications at their status, and the three open items.

Nothing is dropped, weakened or strengthened. Two optional wording points are O2 and O3.

## 3. Definitions at L142 and the accessible-window sentence
- **"Return horizon": a time n with Γ_n = I.** Confirmed. It matches Main §2.3's Theorem ("for every n > s with Γ_n = I, n = L among them") and Appendix A's "indivisibility at some return horizon" (`rootedMap R n = 1`, PhysicalC4Discharge:122).
- **"Recurrence cycle": {0,…,L}.** Confirmed; it matches Main §2.3 ("not P-divisible on {0,…,L}").
- **"The order L of φ, the least return time".** Correct if "return" means the whole world. It can be misread as the least return horizon, which can come earlier (see O1).
- **"Accessible windows are, by definition, short compared with the world's least return time L [Main §2.3, Scope]".** Confirmed. Main's Scope says (C4) and condition (ii) "require an accessible order, kτ_S ≪ t_R".
- **The clause that follows it is overstated (R2).**

## 4. Terminology (CHANGES-r22 §4)
- **Conditional memory, for M_t.** Correct everywhere:
  - the abstract;
  - L99, "the information about the next observation that the observed past carries beyond what the observed present already tells", which matches the owner's definition;
  - L122, L124, L126, L148, L167, L192 and L309.
- **Memory in the record.** Correct at L126 and L167.
- **Accessible memory.** Correct at L148 and L194 ("(1) accessible memory, M_t > 0"), matching Main §3.2's "accessible finite-horizon memory".
- **P-divisibility, for the rooted family.** Correct at L130, L132 and L134.
- **Bare "predictive memory".** None remains.
- **Hidden predictive memory.** Correct as used at L122 and L300; the new definition at L99 is not (R1).

## 5. The other edits: confirmed
- **§2.5 reordering (L130).** "The property that fails is called *P-divisibility*: whether the forecasts from the start admit step-by-step intermediate forecasts over the interval in question". This is the owner's definition, and it matches L132. The card comparison follows, and the back-reference from L134 resolves.
- **L148, the three-way split.** "Conditional memory can exist all the same, at a later order" and "the record has no accessible memory on that window" keep the three notions apart. The four-bit example is unchanged in substance.
- **L214.** Reordered to GR §3.3's own claim: "(i) and (ii) are well-formedness requirements of any operational theory; (iii)–(v) are the substantive selection principles". The open step now follows it, and "OI alone does not imply quantum mechanics" remains.
- **L167.** "memory in the record and P-divisibility are different properties", and "that failure lies somewhere in its full cycle, not necessarily on an accessible window". No general claim of independence.
- **L250.** "[Wei89, §III]", and the sentence no longer uses "mismatch" before L252 defines it.
- **O4 (L194).** "Among what is proved:".
- **L138.** "A step-by-step forecast can never move two forecasts further apart" is the contraction criterion.
- **L19.** A raw TeX page-break hint; layout only.

## 6. Unchanged statements: confirmed
- Every exact statement is word for word as in r21. I checked:
  - Theorems 1–4 with (a)–(c), and conditions (i)–(v);
  - both corollaries;
  - the Γ_t definition;
  - every labelled paragraph in §§2.2, 4, 5 and 6, including the Summary;
  - the Bell theorem paragraph;
  - the "Proofs and sources" blocks;
  - the open-problem lists.
- The §2.4 Corollary is byte-identical.
- The ledger has only `line` changes. No ID is retired, and `coverage_check` reports OK (134 statements).
- Nothing is weakened.

## Findings

**R1 — L99. Required.**
- *Current text:* "The *hidden predictive memory* I(X<t;H_t|X_t) is the information retained in the hidden state that supports the observed process's dependence on history."
- *Problem:* I(X<t;H_t|X_t) is all the information the hidden state holds about the past beyond the present, not only the part that produces history dependence. In every bijective realization run from time 0 it equals H(X<t|X_t), Markov laws included. The paper says so itself at L118 ("Keeping the past is not the same as memory") and L122.
- *Anchor:* Main §3.4, Theorem (unavoidable hidden predictive memory)(c); Main §3.4, Remark (a variational question), which states that every bijective completion has I(X<t;H_t|X_t) = H(X<t|X_t).
- *Replace with:* "The *hidden predictive memory* $I(X_{<t};H_t\mid X_t)$ is the information the hidden state holds about the observed past beyond what the observed present tells; it is at least the conditional memory (Theorem 2(c)), and only part of it need affect what is seen next."

**R2 — L148. Required.**
- *Current text:* "…and the gap between the two is why memory can become detectable only later: a trace held in the hidden part can first affect what is seen at an order beyond every accessible window, though still before the return."
- *Problem:* "can become detectable only later" implies that the late memory becomes detectable to the observer. That contradicts "An observer confined to accessible windows sees neither" and blurs conditional memory with accessible memory. The gap also leaves room for this; it does not cause it.
- *Anchor:* Main §2.3, Scope: "an observer's statistics are its restriction to accessible windows, and on them the memory is witnessed only by a gap at an accessible order".
- *Replace with:* "…and the gap between them leaves room for conditional memory that no accessible window detects: a trace held in the hidden part can first affect what is seen at an order beyond every accessible window, though still before the return."

**O1 — L142. Optional.**
- *Current text:* "the order $L$ of $\varphi$, the least return time".
- *Suggest:* "the order $L$ of $\varphi$, the least time after which the whole world returns to its starting configuration". A return horizon, at which only the forecasts return to certainty, can come earlier.
- *Anchor:* Main §2.3, Theorem ("every $n>s$ with $\Gamma_n=I$, $n=L$ among them").

**O2 — L17. Optional.** The abstract no longer defines "rooted", but uses "some rooted transition matrix is not a permutation". Consider "whenever some table of forecasts from the start is not a permutation", so that the scope stays the same.

**O3 — L17. Optional.** "So stochastic, quantum-like records can arise exactly from deterministic dynamics, and any memory they show must be stored in the hidden part" now follows the Theorem 4 sentence, so "So" reads as if it followed from Theorem 4. Use "Together," or move the sentence to follow the memory sentence.

## 7. The owner's two final questions
- **Is every substantive claim supported by its evidence and assumptions?** Yes, once R1 and R2 are applied. Both are explanatory sentences; no statement or theorem is affected.
- **Does the paper communicate the strongest results without unnecessary weakening?** Yes. The restructured abstract keeps every established result at proved strength, with all of Theorem 4's hypotheses and the recurrence sentence's hypotheses and full-support equivalence.