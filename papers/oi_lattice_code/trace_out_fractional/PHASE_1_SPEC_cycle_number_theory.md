# Phase 1 Spec — Cycle-Length Number Theory

**Date:** May 11, 2026
**Methodology:** §A.13 fifth refinement (Phase 1 deliverables 1–4)
**Companion to:** PHASE_1_RESULTS_v2.md (which surfaced the unexpected positive finding)

---

## 1. Background and the question

§B.2.113 Phase 1 v2 trace-out calculation produced an unexpected positive finding: the OI substratum's wave-step matrix $W$ acting on the state space $\{0,1\}^{2L^d}$ has orbits whose lengths depend on $L$ in number-theoretic ways. The 2D cycle lengths measured at $L = 3, 4, 5, 6$ were $6, 4, 30, 156$ — determined by the order of $W$ in $GL(2L^d, \mathbb{F}_2)$, which depends on whether the characteristic polynomial of $W$ over $\mathbb{F}_2$ factors nicely.

This is a genuine structural feature of the OI substratum that wasn't previously characterized. The question is whether it has any connection to the framework's existing structural predictions.

## 2. The hypothesis to test

**Hypothesis H1 — Cycle structure produces framework rationals.** The framework's empirical rational/algebraic predictions originate in the cycle-length number theory of $\phi$:
- Koide $\theta_0 = 2/9$
- PMNS sum rule $2\sin^2\theta_{12} + \sin^2\theta_{23} = 7/6$
- Cabibbo $\lambda = 1/(\pi\sqrt{2})$
- Wolfenstein $A = \sqrt{2/3}$
- $1/\alpha_0 = 23.25 = ?$
- $\delta_0 = 10.02$
- $A \cdot B = 48$
- $\text{Tr}[Y^2] = 10$ (three generations)

If H1 holds, the numerators and denominators of these rationals should appear as quantities in the cycle structure (cycle lengths, factor orders, character sums) of $W$.

**Hypothesis H2 — Cycle structure constrains $\varphi$ selection but doesn't produce existing rationals.** The cycle structure is a real feature of the substratum but only relevant to *which bijection* is physically realized (Tier 3), not to the framework's structural predictions (Tier 1/2). If H2 holds, the framework's rationals come from representation theory + integer counting (which they manifestly do at the level of derivation), and cycle structure is a separate research line about $\varphi$ selection.

**Hypothesis H3 — Cycle structure is purely combinatorial, no framework connection.** The cycle structure reflects only the algebraic properties of the wave-step matrix over $\mathbb{F}_2$, with no special relationship to physical predictions. If H3 holds, the line is closed cleanly.

## 3. The four Phase 1 deliverables (per §A.13 fifth refinement)

### 3.1 Computational scoping

**Lattice sizes and dimensions to test.**
- 2D: $L = 3, 4, 5, 6, 7, 8$ (state space $2^{2L^2}$ ranges from $2^{18}$ to $2^{128}$)
- 3D: $L = 2, 3$ (state space $2^{16}$ and $2^{54}$); $L = 4$ needs multi-word state (128 bits)
- 1D: $L = 5, 7, 11, 13$ to study odd-$L$ vs even-$L$ pattern

**Quantities to compute.**
For each $L, d$:
1. Cycle length distribution (sample $N_s = 100$ random initial states, find orbit length)
2. Minimal polynomial of $W$ over $\mathbb{F}_2$ (degree $\leq 2L^d$; this determines the order of $W$ as LCM of orders of irreducible factors)
3. Order of $W$: smallest $T$ such that $W^T = I$ over $\mathbb{F}_2$
4. Character of $W$ under the cubic group $O$ acting on the lattice

**Resource estimates.**
- 1D $L = 13$: state space $2^{26} \approx 6.7 \times 10^7$. Direct enumeration of cycle types possible in chat.
- 2D $L = 7$: state space $2^{98}$. Cycle-finding via Floyd's algorithm on random initial states — chat-tractable, ~minutes each.
- 2D $L = 8$: state space $2^{128}$. Cycle-finding feasible if cycles are short; may not be.
- 3D $L = 4$: state space $2^{128}$. Same comment.
- Minimal polynomial computation: $2L^d \times 2L^d$ matrix over $\mathbb{F}_2$; for $L^d = 64$ this is $128 \times 128$ matrix, tractable; for $L^d = 100$ this is $200 \times 200$, still tractable.

### 3.2 Decomposition

**Smallest informative version.** Test in 1D first (no cubic group complications):
- $L = 5$: state space $2^{10}$, cycle structure fully enumerable
- $L = 7$: state space $2^{14}$, fully enumerable
- $L = 11$: state space $2^{22}$, fully enumerable
- $L = 13$: state space $2^{26}$, fully enumerable

For each, compute the full cycle structure (multiplicities of each cycle length), the order of $W$, and compare to predictions from $\mathbb{F}_2$ algebra.

The 1D test is decisive for H1 vs H3 because 1D has no cubic group representation theory to confound — if the framework's rationals come from cycle structure, they should already be visible (in some encoded form) in 1D.

### 3.3 Measurement procedure (the new requirement from §A.13 fifth refinement)

**The precise quantities computed:**

(a) **Cycle length spectrum.** For each $L, d$: $\{\lambda_i: i \in I_{L,d}\}$ where $\lambda_i$ is a cycle length and $I_{L,d}$ indexes distinct cycles. With multiplicities (number of orbits of each length).

(b) **Order of $W$.** $\text{ord}(W) = \text{lcm}(\{\lambda_i\}) = $ smallest $T$ with $W^T = I$.

(c) **Minimal polynomial of $W$ over $\mathbb{F}_2$.** Factor as product of irreducibles $m_W(x) = \prod_j p_j(x)^{e_j}$. The order of $W$ equals $\text{lcm}(\{\text{ord}(p_j)\})$ where $\text{ord}(p_j) = 2^{\deg p_j} - 1$ if $p_j$ is primitive over $\mathbb{F}_2$.

(d) **Character of $W$ under cubic group $O$.** $\chi_W(g) = \text{Tr}(g \cdot W)$ where $g \in O$ acts on the lattice.

**How these connect to framework rationals.**

(a) → Cabibbo $\lambda$? If $\text{ord}(W)$ involves $\pi$ via some lattice momentum analog, the $\pi\sqrt{2}$ structure could emerge. *But this is a stretch:* cycle lengths are integers, not transcendentals involving $\pi$. So Cabibbo connection requires identifying $1/(\pi\sqrt{2})$ as a ratio of integer-counted quantities, which is unlikely.

(b) → Koide $2/9$? Look for cycle lengths in ratio $2:9$ at any $L$. Or $\text{ord}(W)$ being divisible by 9 with quotient 2.

(c) → Sum rule $7/6$? Look for the integer ratio $7/6$ in cycle structure of irreducible factors of $m_W(x)$.

(d) → Tr$[Y^2] = 10$? Look for $\chi_W$ values that produce 10 at the cubic-group representation level.

**Measurement specifics.**
- Cycle length via Floyd's algorithm with `max_iter = 10^9` (sufficient for chat-time at $L \leq 7$ 2D)
- Minimal polynomial via Berlekamp-Massey on the orbit of a generic vector under $W$
- Cubic-group character via direct evaluation of $\text{Tr}(g \cdot W)$ for representative $g \in O$

### 3.4 Outcome pre-registration

**Outcome A — H1 confirmed (cycle structure produces framework rationals):** At least 3 of {2/9, 7/6, 23.25, 10, 48} appear in cycle structure quantities at small $L$ with structural interpretation (not numerical coincidence). Specifically:
- "Structural interpretation" means: the appearance is consistent across multiple $L$ values, with the rational/integer reproduced as a specific function of $L$ that equals the empirical value at the framework's working $L$.
- Cycle confidence upgrade: substantial framework restructuring; new cluster "Substratum number theory derivations" worth $\sim 75$-$85\%$ confidence.

**Outcome B — H2 (cycle structure constrains $\varphi$ but not rationals):** Cycle structure has clear regularities (e.g., $\text{ord}(W)$ has a closed-form expression in $L$, or specific cycle multiplicities recur) but the framework's rationals do not appear in the cycle structure. The cycle structure is real and characterizable but separate from existing framework content.
- Confidence impact: opens a new research direction with $\sim 60$-$75\%$ confidence; doesn't affect existing predictions.

**Outcome C — H3 (purely combinatorial, no framework connection):** Cycle structure has no closed-form regularity and no relationship to framework rationals. The structure is determined by chance factorizations of polynomials over $\mathbb{F}_2$.
- Confidence impact: research line closed cleanly. Cycle structure is documented as a feature of the substratum that doesn't connect to physics predictions.
- Composite-Higgs / Framework overall confidence: unchanged.

**Outcome D — Inconclusive:** $L$-scaling not clean enough at chat-tractable sizes to distinguish A/B/C. Phase 2 (offline) would extend to larger $L$.
- Confidence impact: hold the line open; document the chat-scale findings; defer.

### 3.5 Falsification of the speculative direction

H1 is **refuted** if 1D $L = 5, 7, 11, 13$ cycle structures show no integers/rationals corresponding to framework predictions. This is a falsifiable test at chat scale.

H1 is **confirmed** only if specific integers (9, 6, 7, 10, 48, 23) appear in the cycle structure with $L$-scaling that reproduces the framework's working values.

The middle ground (Outcome B) is also informative — it would establish cycle structure as a real but separate research direction, not the source of the existing rationals.

---

## 4. Honest pre-execution assessment

**Prior probability of Outcome A (H1 confirmed):** Low (~15%).

Reason: the framework's rationals come from cubic-group representation theory ($K = 2d = 6$, $4 = 1 + 3$, hypercharge assignment 1/6, 2/3, -1/3, -1/2, -1) and from integer counting (three generations, six anomaly conditions). These don't obviously connect to cycle structure of $W$ over $\mathbb{F}_2$, which depends on a different mathematical structure (Galois theory of $\mathbb{F}_2$-polynomials).

**Prior probability of Outcome B (cycle structure separate but real):** Moderate (~40%).

Reason: §B.2.113 already showed that cycle structure exists and is non-trivial. With proper measurement, regularities are likely to be visible. Whether those regularities have framework connections is the question.

**Prior probability of Outcome C (no connection, close line):** High (~40%).

Reason: cycle structure is determined by $\mathbb{F}_2$-algebra of $W$, which is essentially unrelated to the cubic-group representation theory that produces the framework's rationals. The two mathematical structures live in different categories.

**Prior probability of Outcome D (inconclusive):** Low (~5%).

Reason: 1D enumerable at $L = 13$ should be decisive.

**Total: ~100%, with C the modal outcome.**

This is a **research line where the negative result is most likely**. That's not a reason to skip the work — Outcome C is also informative, and Outcome A would be substantively important if it occurred. But the expected value is modest.

## 5. Resource estimates and execution plan

**Phase 1 (this spec):** Complete. Chat-tractable.

**Phase 2 (execution, chat or offline):**
- 1D $L = 5, 7, 11, 13$ enumeration: chat-tractable, ~minutes total
- 2D $L = 5, 6, 7$ random sampling: chat-tractable, ~minutes each
- 2D $L = 8, 3D L = 4$ with multi-word state: requires implementing 128-bit state representation; ~1 chat session of additional code work
- Minimal polynomial computation via Berlekamp-Massey: chat-tractable

**Phase 3 (analysis):** Match measured quantities to framework rationals; classify outcome A/B/C/D; propagate to OI_MASTER §B.2; update confidence assessments if applicable.

**Total Phase 1 + 2 + 3 estimate:** 1-2 chat sessions assuming straightforward execution. Could extend if Outcome B regularities are rich enough to warrant deeper structural investigation.

## 6. Recommendation

**Execute Phase 2 in the next chat session, focusing on 1D first.**

The 1D test is decisive for H1 vs H3 (no cubic group complications). If 1D shows no framework rationals in cycle structure, H1 is refuted and the work can be closed at chat scale without 2D/3D extension. If 1D shows interesting patterns, extend to 2D/3D to confirm the connection.

Expected outcome: Outcome C closure at 1D scale, with modest documentation of the cycle structure as a substratum feature unrelated to existing framework predictions.

This spec is Phase 1 complete per §A.13 fifth refinement deliverables 1-4. Phase 2 is chat-tractable and awaits user direction.
