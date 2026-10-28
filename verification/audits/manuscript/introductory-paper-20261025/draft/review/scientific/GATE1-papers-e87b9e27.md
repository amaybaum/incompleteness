# Gate 1 (scientific accuracy): focused confirmation of PR #918 r23 at `e87b9e27`

**Verdict: ACCEPT.** R1 and R2 from r22 are fixed exactly, and every other item checks out against Main. I have two optional wording suggestions (O1, O2) and nothing required.

This was a read-only review against r22 `40935ccf`; the parent `a3b49057` has the same paper. I used a detached worktree at `e87b9e27`, now removed, and did not commit, push or comment. Line numbers refer to `e87b9e27`.

## 1. R1 (L99): fixed
- **New definition.** "The *hidden predictive memory* $I(X_{<t};H_t\mid X_t)$ is the information the hidden state holds about the observed past beyond what the observed present tells; it is at least the conditional memory (Theorem 2(c)), and only part of it need affect what is seen next." This is the wording I proposed.
- **Theorem 2(c).** As stated at L110, (c) gives $M_t\le I(X_{<t};H_t\mid X_t)$. So "at least the conditional memory" is right (Main §3.4, Theorem (unavoidable hidden predictive memory)(c)).
- **"Only part of it need affect what is seen next."** This matches Main §3.4, Remark (a variational question): every bijective completion carries $H(X_{<t}\mid X_t)$, Markov laws included.
- **Every other use is consistent.** I checked each occurrence in CHANGES-r23 §3 against the text:
  - L101, the Theorem 2 title;
  - L120, the least hidden predictive memory, and the bijective $H(X_{<t}\mid X_t)$;
  - L126, the Main remark title;
  - L298;
  - the bare phrase "predictive memory" appears nowhere.
- **The owner's gloss at L118 is accurate.** It now reads "readout-relevant hidden memory, the part of the hidden memory that supports the observed process's dependence on history". By Theorem 2(a), readout-relevant memory is exactly what makes histories ending at the same state give different next-step laws (Main §1.5; the §2.4 Corollary). The gloss now describes the readout-relevant part, not the whole of $I(X_{<t};H_t\mid X_t)$.

## 2. R2 (L146): fixed
- **New wording.** "the gap between them leaves room for conditional memory that no accessible window detects". This is consistent with Main §2.3, Scope: "on them the memory is witnessed only by a gap at an accessible order".
- **New position.** "An observer confined to accessible windows sees neither" now comes after that sentence, so it no longer collides with the misreading "becomes detectable". Its antecedents are now further away; see O1.

## 3. Recurrence time and return horizon: consistent
- **L49.** $L$ is "the world's *recurrence time*, the least time after which the whole world returns to its starting configuration". That is the order of φ.
- **L140.** "the order $L$ of $\varphi$, the recurrence time. A *return horizon* is a time $n$ with $\Gamma_n=I$ … $L$ is one, and there may be earlier ones." This matches Main §2.3, Theorem: "for every $n>s$ with $\Gamma_n=I$, $n=L$ among them".
- **Every other use agrees:** L17, L122 (accessible orders short compared with the recurrence time, which is Main's $k\tau_S\ll t_R$), L146, L154 ("indivisibility at some return horizon", matching `routed_forces_indivisible_somewhere`), L298 and L307.
- **Statement texts.** "order $L$ of $\varphi$" is kept: the Corollary still reads "Let $\varphi$ have order $L$", unchanged.

## 4. Abstract (L17): confirmed
- **Reordered consequence sentence.** "Stochastic, quantum-like records can therefore arise exactly from deterministic dynamics, and any memory they show must be stored in the hidden part." It now follows the equality and memory sentences it draws on.
- **"some table of forecasts from the start is not a permutation".** This has the same scope as "rooted transition matrix": both refer to Γ_s, with rows for every start.
- **Hypotheses and equivalence, all present:**
  - a finite reversible world;
  - hidden odds shared by every visible start and drawn independently of it;
  - starts of probability zero included;
  - failure somewhere in the recurrence cycle;
  - "in particular whenever a visible step is not fully predictable from the current observation";
  - the full-support equivalence with conditional memory below the recurrence time.
- **Theorem 4.** All its hypotheses are unchanged.

## 5. L165 and L218: confirmed
- **L165.** "that failure need not lie on an accessible window" is correct. The Corollary places the failure on {0,…,L} without locating it.
- **L218.** "Conditions (i) and (ii) only make the theory well formed; (iii)–(v) are the substantive requirements, which [GR §3.3] calls selection principles." This is accurate against GR §3.3: "(i) and (ii) are well-formedness requirements of any operational theory; (iii)–(v) are the substantive selection principles".

## 6. Unchanged material: confirmed
- **Exact statements.** Every exact statement is word for word as in r22. That covers:
  - Theorems 1–4 with (a)–(c);
  - both corollaries, including the §2.4 Corollary, which is byte-identical;
  - the Γ_t definition and the plain P-divisibility paragraph;
  - every labelled paragraph in §§2.2, 4, 5 and 6, including the Summary;
  - the Bell paragraph and the "Proofs and sources" blocks.
- **Ledger.** Only `line` fields changed; no ID is retired. `coverage_check` reports OK, with 134 statements.
- **Nothing is weakened.** The only removed text is the raw TeX spacing hint, which carried no content.

## Optional findings
- **O1 (L146).** "An observer confined to accessible windows sees neither" now has distant antecedents. Suggested: "An observer confined to accessible windows sees neither the late conditional memory nor the failure of chaining." Anchor: Main §2.3, Scope.
- **O2 (L140).** "at which only the forecasts from the start return to certainty" could be read as excluding $L$, where the whole world also returns. Suggested: "at which the forecasts from the start return to certainty, whether or not the whole world has returned". Anchor: Main §2.3, Theorem ("$n=L$ among them").

## 7. The owner's two final questions
- **Is every substantive claim supported by its evidence and assumptions?** Yes.
- **Does the paper communicate the strongest results without unnecessary weakening?** Yes. Every established result, including Theorem 4 with all its hypotheses and the recurrence Corollary with its full-support equivalence, is stated at proved strength. The new definitions keep conditional memory, hidden predictive memory, readout-relevant hidden memory, accessible memory and P-divisibility distinct, as Main does.