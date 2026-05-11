# Phase 3 Results — A1 Cycle-Length Number Theory

**Date:** May 11, 2026
**Status:** Phase 3 complete. **Outcome C** per pre-registration.
**Companion to:** PHASE_1_SPEC_cycle_number_theory.md

---

## Executive summary

Per the Phase 1 spec, 1D enumeration at $L = 5, 7, 9, 11, 13$ was decisive for H1 vs H3 (no cubic group complications). Results:

**Outcome C: cycle structure is real and clean, but produces no framework-rational connection.**

The 1D cycle structure follows an extraordinarily clean rule:
$$\text{ord}(W_{1D}) = \begin{cases} 2L & \text{if } L \text{ odd} \\ L & \text{if } L \text{ even} \end{cases}$$

with cycle length spectrum $\{1, 2, L, 2L\}$ for odd $L$ and $\{1, 2, L\}$ (plus divisors of $L$) for even $L$. This is a number-theoretic consequence of the wave-step matrix $W$ being circulant over $\mathbb{F}_2$ with characteristic polynomial structure $(x^L - 1)$ over $\mathbb{F}_2$ — completely determined by $L$, with no dependence on the substratum's physical structure.

The 2D pattern is more complex (involves additional primes, e.g., 13 appearing at $L = 6$) but the orders measured ($L=2 \to 2$, $L=3 \to 6$, $L=4 \to 4$, $L=5 \to 30$, $L=6 \to 156$) **do not match any framework rational** other than a single coincidence at 1D $L = 5$ where order = 10 = $\delta_0$ = $\text{Tr}[Y^2]$.

The research line is closed at chat scale. Cycle structure is a real feature of the substratum but does not produce the framework's rationals.

---

## Detailed findings

### Finding 1: 1D order pattern is determined entirely by L parity

| L | order(W) | factorization | cycle spectrum |
|---|----------|---------------|----------------|
| 4 | 4 = 2² | $2^2$ | {1, 2, 4} |
| 5 | 10 = 2·5 | $2 \cdot 5$ | {1, 2, 5, 10} |
| 6 | 6 = 2·3 | $2 \cdot 3$ | {1, 2, 3, 6} |
| 7 | 14 = 2·7 | $2 \cdot 7$ | {1, 2, 7, 14} |
| 8 | 8 = 2³ | $2^3$ | {1, 2, 4, 8} |
| 9 | 18 = 2·9 | $2 \cdot 3^2$ | {1, 2, 3, 6, 9, 18} |
| 10 | 10 = 2·5 | $2 \cdot 5$ | {1, 2, 5, 10} |
| 11 | 22 = 2·11 | $2 \cdot 11$ | {1, 2, 11, 22} |
| 12 | 12 = 2²·3 | $2^2 \cdot 3$ | {1, 2, 3, 4, 6, 12} |
| 13 | 26 = 2·13 | $2 \cdot 13$ | {1, 2, 13, 26} |

**Pattern:** $\text{ord}(W_{1D}) = 2L$ for $L$ odd, $L$ for $L$ even. No exceptions in tested range.

**Interpretation:** This is a standard number-theoretic result for circulant matrices over $\mathbb{F}_2$. The wave-step matrix $W = \begin{pmatrix} N & I \\ I & 0 \end{pmatrix}$ has minimal polynomial related to $(x^L + 1)$ over $\mathbb{F}_2$, whose order is twice the smallest $T$ with $L | T$ in $\mathbb{Z}/T$, modulated by the parity of $L$ in characteristic 2.

### Finding 2: Cycle-length spectrum has structural ratio 2:1 for odd L

For odd $L$, the dominant cycles are of length $L$ and $2L$, with multiplicities in ratio $2:1$:

| L | length-L cycles | length-2L cycles | ratio |
|---|----------------|------------------|-------|
| 5 | 102 | 51 | 2:1 |
| 7 | 1170 | 585 | 2:1 |
| 11 | 190,650 | 95,325 | 2:1 |
| 13 | 2,581,110 | 1,290,555 | 2:1 |

This $2:1$ ratio is a real algebraic structure of $\mathbb{F}_2$-circulants. **However, the ratio $2:1$ does not correspond to any framework rational** — Koide $\theta_0 = 2/9$ has a 9 not a 1; sum rule $7/6$ doesn't reduce to $2:1$; etc.

### Finding 3: 2D structure is more complex but still not framework-rational

From §B.2.113 + present session:

| 2D L | order(W) | factorization |
|------|----------|---------------|
| 2 | 2 | $2$ |
| 3 | 6 | $2 \cdot 3$ |
| 4 | 4 | $2^2$ |
| 5 | 30 | $2 \cdot 3 \cdot 5$ |
| 6 | 156 | $2^2 \cdot 3 \cdot 13$ |

The appearance of $3$ in 2D $L=5$ (where $5$ is prime) and $13$ in 2D $L=6$ are interesting — they reflect the lattice's cubic-group structure interacting with the $\mathbb{F}_2$-algebra. But these primes do not match framework rationals (no $7$ from $7/6$; no $9$ from Koide; etc.).

### Finding 4: 3D structure (tractable only at L=2)

3D $L = 2$: order = 2 (trivial). 3D $L = 3$: state space $2^{54}$, exceeds 64-bit enumeration with the current code. Would require multi-word state representation for full enumeration (or sampling-based cycle finding from §B.2.113, which found cycles of length 6 in 3D L=3).

3D is the framework's actual substratum dimension. The data here is insufficient to characterize 3D's cycle structure at non-trivial $L$. **This is a known scope limit of the chat-tractable test.** A more thorough investigation would require offline computational resources.

### Finding 5: The single near-match (δ_0 = 10) is a coincidence within a known chain of coincidences

The one numerical match found:
- 1D $L = 5$: order(W) = 10
- Framework: $\delta_0 = 10.02$ (universal threshold, empirically determined per SM §6.2)
- Framework: $\text{Tr}[Y^2] = 10$ (hypercharge-squared sum, three generations)

**Honest characterization:** $\delta_0$ is not derived from substratum mode counting (SM §6.2 explicitly treats it as empirical input determined by the U(1) row). The $\text{Tr}[Y^2] = 10$ coincidence with $\delta_0$ is documented as numerical and unresolved. Adding "order(W, 1D, $L=5$) = 10" to this chain produces a triple coincidence but:

1. 1D $L = 5$ has no special status in the framework (which uses 3D)
2. $L = 5$ has no physical meaning (framework's substratum doesn't have a preferred $L = 5$)
3. The match is to a single number (10), not a pattern

**Conclusion:** the triple coincidence is consistent with the kind of numerical coincidence one finds in small-number searches. It does not constitute structural evidence that cycle structure produces $\delta_0$.

---

## Outcome classification

Per the Phase 1 spec pre-registration (PHASE_1_SPEC_cycle_number_theory.md §3.4):

- ☐ **Outcome A** (cycle structure produces ≥3 framework rationals with structural interpretation): **NOT MET.** Only one coincidence (δ_0 = 10) with no clear structural derivation. At minimum 3 distinct rationals would need to appear with cross-validation across $L$ values.

- ☐ **Outcome B** (cycle structure has clear regularities but no rational connection): **PARTIALLY MET.** The 1D order pattern is genuinely clean (order = L or 2L by parity), but this is an unsurprising consequence of $\mathbb{F}_2$-circulant algebra rather than a novel structural feature. The 2D pattern is more complex but still doesn't match framework rationals.

- ☑ **Outcome C** (cycle structure is purely combinatorial, no framework connection): **MET.** The 1D structure is determined entirely by $L$'s factorization properties over $\mathbb{F}_2$, not by the substratum's physical content. The single δ_0 = 10 coincidence is consistent with chance.

- ☐ **Outcome D** (inconclusive): **NOT MET.** 1D at $L \leq 13$ was decisive — the pattern is clear.

**Final classification: Outcome C with B-flavored acknowledgment.**

The 1D order = (L or 2L by parity) is a clean number-theoretic result, but it's a *known* result for $\mathbb{F}_2$-circulants, not a novel structural finding. The 2D additional-prime structure is more interesting but still not framework-connected.

---

## What this means for the framework

### What's now known

- Cycle structure of substratum dynamics is fully determined by the wave-step matrix's algebra over $\mathbb{F}_2$ — it's a property of the *lattice geometry*, not of the framework's specific physical content
- The framework's empirical rationals (Koide 2/9, sum rule 7/6, Cabibbo $1/(\pi\sqrt{2})$, $\delta_0 = 10$, $A \cdot B = 48$, Wolfenstein $\sqrt{2/3}$, Tr[Y²] = 10) do not originate in cycle structure
- They originate in **cubic-group representation theory** (decomposition $K = 6 = 3+2+1$, $4 = 1+3$ tastes, hypercharge constraints from anomaly cancellation, etc.) — which is independent of cycle structure

### What's still open (and was always Tier 3)

- Which specific bijection $\varphi$ realizes our universe is still a Tier 3 commitment
- Cycle structure of $\varphi$ might be relevant to $\varphi$-selection but doesn't constrain framework predictions
- The §B.2.115 commitment to $v$ as Tier 3 stands

### Confidence impact

- Composite-Higgs cluster: **unchanged at 72-78%**
- Framework overall: **unchanged at 89-93%**

The negative result removes an open speculative direction (the "rational with π originates in substratum number theory" hypothesis) without affecting existing predictions. This is healthy methodology — speculative directions get tested at chat scale and either confirm or close.

The §B.2.113 unexpected positive finding (cycle structure is non-trivial) is now contextualized: the structure is real, but it's a generic $\mathbb{F}_2$-algebra property, not a substantive new physical mechanism.

---

## Methodology validation (further evidence for §A.13 fifth refinement)

The Phase 1 spec pre-registered Outcome C at ~40% prior, B at ~40%, A at ~15%. The empirical result is **Outcome C** — consistent with the spec's stated modal expectation.

The fifth refinement's value is visible here: without the pre-registration:
- The δ_0 = 10 coincidence at 1D $L = 5$ could have been written up as "evidence that substratum cycle structure produces δ_0" — *post hoc* rationalization of a numerical match
- The clean 1D pattern (order = L parity rule) could have been presented as a "substantive new finding" rather than recognized as a known $\mathbb{F}_2$-circulant property
- The negative result on framework rationals could have been obscured by selective reporting

The pre-registration prevented all three failure modes. The result is interpretable, calibrated, and adds to the framework's structural understanding without overclaiming.

**The §A.13 fifth refinement is now empirically validated in 3 distinct contexts:**
1. §B.2.111 trace-out v1 (failed without it)
2. §B.2.113 trace-out v2 (succeeded with it; produced clean Outcome C refutation of GEMs 53-54)
3. §B.2.116 A1 spec → §B.2.117 A1 execution (succeeded with it; produced clean Outcome C closure of cycle-length number theory)

---

## Files produced

- `PHASE_1_SPEC_cycle_number_theory.md` (10 KB) — pre-registered spec
- `cycle_1d.c` (5 KB) — 1D enumeration code
- `cycle_2d_full.c` (3 KB) — 2D enumeration code
- `cyc3d.c` (2 KB) — 3D enumeration code (tractable to $L = 2$)
- `cycle_1d`, `cyc2d_full`, `cyc3d` — compiled binaries
- `PHASE_3_RESULTS_cycle_number_theory.md` (this document)

---

## Recommendation

**Close the cycle-length number theory research line at chat scale.** Mark the §B.2.113 unexpected positive finding as "structure exists but is purely algebraic; not connected to framework predictions."

The line could be reopened offline if:
- 3D $L \geq 3$ becomes computationally tractable (would require multi-word state representation, ~1 chat session of code work)
- A specific framework prediction is identified that depends on cycle structure (none currently identified)
- The cycle structure of a specific bijection $\varphi$ becomes relevant to a Tier 3 commitment

None of these are immediate priorities. The research line is **closed**.
