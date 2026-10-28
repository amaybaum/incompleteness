# Gate 1 (scientific accuracy): PR #918 r24 at `e64b2a4c`

**Verdict: ACCEPT.** Each of the four edits is accurate against Main §2.3 and §3.4, the definition of L is unchanged in substance, and "whether or not the whole world has returned" is correct.

I compared `git diff edfc863d e64b2a4c -- papers/Introduction.md` with CHANGES-r24.md, read-only. The parent `edfc863d` has the same paper as r23 `e87b9e27`, and only the four sentences at L49, L118, L140 and L146 changed.

1. **L49: L is still both the order and the recurrence time.** The sentence now reads "its *order* $L$, the world's *recurrence time*, is the least number of steps after which every configuration has returned to itself". That is the least $n$ with $\varphi^n=\mathrm{id}$. This is the same quantity r23 called "the least time after which the whole world returns to its starting configuration", which is Main §2.3's "order $L$" with $\Gamma_L=I$.

2. **L118: "readout-relevant hidden memory, the part of the hidden predictive memory that supports the observed process's dependence on history".** This is accurate.
   - Readout-relevant memory, meaning posteriors with different pushforwards, is the part of $I(X_{<t};H_t\mid X_t)$ that changes the next-step law. That follows from Theorem 2(a) and the §2.4 Corollary (Main §1.5).
   - The rest can be pure storage. Every bijective completion carries $H(X_{<t}\mid X_t)$, Markov laws included (Main §3.4, Remark (a variational question)).

3. **L140: "at which the forecasts from the start return to certainty, whether or not the whole world has returned; $L$ is one, and there may be earlier ones".** This is correct and applies my O2.
   - $\Gamma_n=I$ requires only that, from every root, the visible state is back at the root, μ_H-almost surely. The hidden state need not be back.
   - At $n=L$ the whole world has returned.
   - This matches Main §2.3, Theorem: "for every $n>s$ with $\Gamma_n=I$, $n=L$ among them".

4. **L146: "An observer confined to accessible windows therefore sees neither the late dependence nor the failure of chaining".** This is accurate and applies my O1.
   - The failure of chaining is located on {0,…,L}.
   - Accessible windows are short compared with $L$ (Main §2.3, Scope, $k\tau_S\ll t_R$).
   - "therefore" follows from the preceding sentence about memory that no accessible window detects.

None of the four sentences is an exact statement. Theorems 1–4, both corollaries and the §2.4 Corollary are untouched, and the ledger is unchanged in this commit. Nothing is weakened.