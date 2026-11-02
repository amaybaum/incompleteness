# Gate 1 (scientific accuracy): PR #918 r30 at `cc986a5b`

**Verdict: ACCEPT WITH CHANGES.** One correction is required, at L300, and the error is in my own R-Page wording that was applied verbatim. H1, H2 and the L152 trim are accurate, and nothing else in the paper changed.

I checked `git diff 72014a79 cc986a5b -- papers/Introduction.md` against CHANGES-r30.md. There are four hunks (L132, L152, L156, L300) and no ledger change.

1. **H1 (L132) is exactly supported.** "Such a start is not impossible: the world can be started there, and this dealer's preparation simply never does so." In Main §2.3 these starts are roots of visible probability zero under the chosen visible prior. The rooted map has a row for every $a\in\mathcal C_V$, so the dynamics does not exclude them.

2. **H2 (L156) is exactly supported.** "…the order $k$ of the Corollary can lie anywhere on it, so a memory that first appears late on the line is real in the dynamics but outside every window." This matches Main §2.3 Scope: "the gap it is equivalent to may lie at any order below the recurrence time; (C4) … require an accessible order, $k\tau_S\ll t_R$".

3. **The L152 trim loses nothing and overstates nothing.** "The failure of chaining is a property of the world's rule, its dynamics with its hidden preparation: it constrains how such a world can be described, not what accessible data will show [Main §2.3, Scope]."
   - The "accessible" contrast is carried by the previous sentence: "neither appears in any accessible record".
   - "A property of the world's rule" is true: the rooted family is fixed by the dynamics and the shared hidden preparation.
   - The sentence no longer contrasts the property with records at all. So it no longer conflicts with the full-support case, where the failure is equivalent to memory in the full-cycle law.

4. **R-Page (L300): the quotation is faithful, but the sentence states too little of the hypothesis. Required.**
   - **The quotation.** "which requires an initial superposition of configurations or a split not aligned with them, and which of these the substratum supplies is open [GR App. A.7]" faithfully renders GR's "it requires an initial superposition of configurations or a bipartition not aligned with them, and which of these the substratum supplies is open". The only change is "split" for "bipartition".
   - **The overstatement.** "the cycle-averaged Page value follows once H-scramble holds" makes H-scramble sound sufficient on its own. In GR, Theorem A.9 is "conditional on A.8, hence on H-scramble, and on H-decouple", and Theorem A.8 also requires the whole of $\mathcal C_B\times\mathcal C_R$ to be a single energy shell. The paper itself lists all three conditions at L298 and in §6 L308. This was my own wording's error.
   - **Replacement:** "What survives is the conditional statement: the cycle-averaged Page value follows if H-scramble, isolation and constant energy all hold; H-scramble requires an initial superposition of configurations or a split not aligned with them, and which of these the substratum supplies is open [GR App. A.7]; the separation of conservation from recovery above does not depend on any of them."

5. **Nothing else changed.** All exact statements, the §2.4 Corollary and the ledger are untouched.