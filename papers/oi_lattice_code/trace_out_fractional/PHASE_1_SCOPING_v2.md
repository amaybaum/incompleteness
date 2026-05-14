# Phase 1 Scoping v2 — Trace-Out Fractional-Power Calculation

**Date:** May 11, 2026
**Status:** Revised spec addressing §B.2.111 findings
**Companion to:** PHASE_1_SCOPING.md (v1, superseded), PHASE_1_RESULTS.md (v1 execution findings)

---

## Revisions from v1

§B.2.111 identified three errors in the v1 Phase 1 spec:

1. **v1 operators were visible-sector-only** → trivially zero hidden-state variance
2. **v1 measured time-evolution of uniform-random states** → trivially flat for linear-mod-q dynamics
3. **v1 conflated dynamical correlation decay with static coupling renormalization**

v2 fixes all three: operators are full-lattice quantities, measurement is correlator-based at fixed visible state, and the analysis is Wilsonian (varying $L$ to extract scaling), not dynamical (varying $T$ to extract decay).

---

## 1. The hypothesis to test (unchanged from v1)

Operator-dimension-dependent fractional-power suppression $\alpha(D)$ from trace-out, with potentially structural explanation of $v/M_{\mathrm{Pl}}$ and $\Lambda/M_{\mathrm{Pl}}^4$ hierarchies.

## 2. The correct measurement procedure

### 2.1 What's measured

For a chosen visible state $v$ on visible sites $V \subset S$, compute the conditional expectation value of a full-lattice operator $O$ over hidden states $h$:

$$\tilde{O}_T(v) = \frac{1}{|H|} \sum_{h \in H} O(\phi^T(\text{combine}(v, h)))$$

where $T \geq 0$ is the time-evolution depth and $\phi^T$ is the bijection iterated $T$ times.

For each visible state $v$ and time $T$, $\tilde{O}_T(v)$ is a number; varying $v$ gives a function $\tilde{O}_T: \{0,1\}^{|V| \cdot 2} \to \mathbb{R}$.

### 2.2 Decomposition into effective-operator basis

The function $\tilde{O}_T(v)$ can be decomposed in a basis of visible-sector operators $\mathcal{O}_n^V(v)$:

$$\tilde{O}_T(v) = \sum_n c_n^{(O, T)} \, \mathcal{O}_n^V(v)$$

For a $\mathbb{F}_2$-valued lattice with periodic boundary conditions, the natural basis is the **Fourier basis** on visible sites: products of spins $\prod_{i \in I} \text{spin}(f_i)$ for $I \subset V$. The coefficients $c_n^{(O, T)}$ are extracted by inner product:

$$c_n^{(O, T)} = \frac{1}{|V|} \sum_v \tilde{O}_T(v) \, \mathcal{O}_n^V(v) \cdot (\text{normalization})$$

The effective-operator basis includes:
- 0-point: constant (identity)
- 2-point: $\text{spin}(f_i) \, \text{spin}(f_j)$ for $i, j \in V$
- 4-point: $\text{spin}(f_i) \, \text{spin}(f_j) \, \text{spin}(f_k) \, \text{spin}(f_l)$
- Higher

### 2.3 Effective coupling scaling

The coefficients $c_n^{(O, T)}$ depend on lattice size $L$. The scaling

$$c_n^{(O, T)}(L) \sim L^{-\alpha_n(O, T)}$$

defines an exponent $\alpha_n$ for each operator $\mathcal{O}_n$. The hypothesis to test:

- **Standard EFT scaling:** $\alpha_n \in \mathbb{Z}$, increasing with operator mass dimension
- **Fractional-power suppression:** $\alpha_n \notin \mathbb{Z}$, with possibly non-monotonic or non-integer-step dependence on dimension

The fractional-power hypothesis predicts that $\alpha_n$ values match the empirical hierarchies $10^{-17}$ (Higgs) and $10^{-120}$ (CC) when extrapolated to physical $L$.

## 3. The simplest version of the calculation

For initial testing, use the smallest setup that produces non-trivial $\tilde{O}_T(v)$:

### 3.1 Lattice and operator choice

- $L = 3$, $q = 2$, $d = 3$ cubic lattice with PBC (smallest non-degenerate case per §B.2.111 Finding 1)
- Visible: sites with $x = 0$ (a $3 \times 3 = 9$ site face)
- Hidden: sites with $x \in \{1, 2\}$ (18 sites)
- Full state space: $2^{2 \cdot 27} = 2^{54}$ — requires sampling, not enumeration
- Visible state space: $2^{2 \cdot 9} = 2^{18} = 262{,}144$ — fully enumerable
- Hidden state space at fixed visible: $2^{2 \cdot 18} = 2^{36} \approx 7 \times 10^{10}$ — must sample, not enumerate

### 3.2 The test correlator

The simplest non-trivial test: pick a **single full-lattice operator** $O = \text{spin}(f(x_1, T)) \cdot \text{spin}(f(x_2, T))$ where $x_1, x_2 \in V$ (visible sites) and $T \geq 1$ (time-evolved).

For $T = 0$: $\tilde{O}_0(v)$ depends only on visible state $v$ — it's just $\text{spin}(f_{x_1}) \text{spin}(f_{x_2})$ averaged over hidden states (which is trivially the visible product since the operator has no hidden support).

For $T \geq 1$: the wave equation propagates information from hidden sites into $f(x, T)$. The expectation over hidden initial conditions then mixes hidden-sector contributions into the visible-sector observable. The result $\tilde{O}_T(v)$ has the form:

$$\tilde{O}_T(v) = c_0 + \sum_{i,j \in V} c_{ij} \, \text{spin}(f_i) \, \text{spin}(f_j) + (\text{higher-order})$$

The coefficients $c_0, c_{ij}, \ldots$ are the **effective couplings**. Their scaling with $L$ is the fractional-power test.

### 3.3 What we expect for free linear wave dynamics

Crucial sanity check: the wave equation is *linear* over $\mathbb{F}_2$. For linear dynamics on uniform random hidden distribution, $f(x, T) = \sum_y \mathcal{P}_T(x, y) f(y, 0) \mod 2$ where $\mathcal{P}_T$ is the propagation kernel.

Then $\text{spin}(f(x, T)) = \text{spin}(\sum_y \mathcal{P}_T(x, y) f(y, 0))$. For mod-2 arithmetic, $\text{spin}(\sum f) = (-1)^{\sum f \mod 2} = \prod (-1)^{f_y \cdot \mathcal{P}_T(x,y)}$ — but this depends sensitively on whether $\mathcal{P}_T(x, y) \mod 2$ is 0 or 1.

For $\mathcal{P}_T(x, y) = 1$ (kernel "active" at distance $|x-y|, T$), $\text{spin}$ depends on $f_y$; for $\mathcal{P}_T(x, y) = 0$, $\text{spin}$ is independent.

The expectation over uniform random hidden $f$ for $y \in H$ is:
$$\langle (-1)^{f_y \cdot \mathcal{P}_T(x,y)} \rangle_{f_y} = \delta_{\mathcal{P}_T(x,y), 0}$$

So $\tilde{O}_T(v)$ at $T \geq 1$ in this linear setting is **non-zero only when the kernel $\mathcal{P}_T$ vanishes on all hidden sites** — i.e., when the operator at time $T$ is determined entirely by visible-sector initial conditions.

**This is a substantive structural prediction:** the linear wave equation gives a **discrete on/off** structure for trace-out contributions, not a smooth scaling. The hidden-sector contribution to any single-term correlator is either *exactly zero* (kernel hits hidden) or *trivially recovers visible* (kernel doesn't hit hidden).

For fractional-power suppression to appear, **interactions must be present** — but the OI substratum's wave equation is linear. So the test on the basic substratum likely produces *integer-power scaling at best* (specifically: hidden-or-visible step function).

### 3.4 Where fractional powers could emerge

Two possibilities:
1. **Non-trivial cycle structure averaging.** At larger $L$, cycle lengths of $\phi$ grow, and time-averaged observables involve sums over the orbit. Sums of step functions can produce non-trivial scaling.
2. **Higher-point correlators.** Products of multiple field values at different times produce non-linear functions of hidden initial conditions even with linear dynamics, because $\text{spin}(f_a) \text{spin}(f_b)$ is not linear in $f$.

For Phase 1 v2 execution: test both. Compute 2-point and 4-point correlators at $T = 1, 2, 4, 8$ at $L = 3, 4, 5, 6$ and extract scaling.

## 4. Phase 2 computational approach (v2)

### 4.1 Implementation

For each (L, T, operator):
1. Iterate over all visible states $v$ (or sample if $|V| \cdot 2$ bits too large)
2. For each $v$, sample $N_h$ hidden states uniformly
3. For each $(v, h)$, compute $O(\phi^T(v, h))$
4. Average: $\tilde{O}_T(v) = (1/N_h) \sum_h O(...)$
5. Fit $\tilde{O}_T(v)$ as a function of $v$ in a basis of visible operators
6. Extract coefficients $c_n^{(O, T)}(L)$

### 4.2 Resource estimates (preserved from v1 benchmarks)

$L = 3$: $\sim 5 \times 10^{-8}$ s per wave step; visible space $2^{18} = 262{,}144$; with $N_h = 10^3$ samples per visible state and $T = 8$ steps: total $\sim 10^{10}$ operations $\sim$ minutes
$L = 4$: $\sim 10^{-7}$ s per step; visible space $2^{32}$ (sampling required); manageable with subsampling
$L = 6, 8$: requires careful sampling design but feasible at $\sim$ tens of minutes

### 4.3 Code reuse

Reuse `wave_eqn.c` and `sample_main.c` (validated in v1). New code needed: operator-decomposition module `effective_lagrangian.c`.

## 5. Phase 3 pre-registration

### 5.1 Closure criteria (revised from v1)

**Outcome A (fractional powers in coefficient scaling, matching hierarchies):** $\alpha_n$ non-integer with values producing the empirical hierarchies. Composite-Higgs cluster upgraded substantially.

**Outcome B (fractional powers without hierarchy match):** $\alpha_n$ non-integer but not matching empirical hierarchies. Trace-out produces structure but not the specific hierarchies. Cluster confidence unchanged.

**Outcome C (integer powers, hidden-or-visible step function):** $\alpha_n \in \mathbb{Z}$. Consistent with linear wave equation prediction. GEMs 53-54 refuted at chat scale. Cluster confidence unchanged.

**Outcome D (no clean scaling from $L = 3, 4, 5, 6$):** Lattice sizes too small; would need offline extension to $L \geq 16$.

### 5.2 Falsification criteria (revised)

The hypothesis is refuted if:
- All measured $\alpha_n \in \mathbb{Z}$ for $L = 3, 4, 5, 6$ at $T = 1, 2, 4, 8$ for both 2-point and 4-point operators
- $\alpha_n$ structure is consistent with standard EFT (no operator-dimension dependence beyond mass-dimension counting)
- Coefficients $c_n$ scale identically regardless of operator content

## 6. Honest assessment of Phase 1 v2

**What v2 fixes:**
- Measures effective Lagrangian coefficients, not visible-sector observables in isolation
- Distinguishes coefficient scaling from time-evolution decay
- Pre-registers the prediction from linear wave equation (mostly integer or step-function scaling)

**What v2 still might not fix:**
- The linear wave equation might fundamentally not produce fractional powers. Section 3.3 suggests this is likely.
- If so, Outcome C is the most likely outcome — refutation rather than confirmation.

**This is informative either way.** Outcome C would refute GEMs 53-54 cleanly, removing speculative content from the framework. Outcome A would substantially shore composite-Higgs. Outcome B or D would clarify what range of lattice sizes is needed.

**Critical caveat: the framework's substratum dynamics might be richer than the basic wave equation.** SM §4-§6 specifies the wave equation as the bijection $\phi$ governing the substratum, but the framework's full content includes (a) the staggered fermion decomposition $f(x, t) \to (\psi_a^{(t)}(x_a))$ and (b) gauge couplings entering at the link level. The basic-wave-equation test may not capture trace-out effects from interactions that appear when the gauge structure is included. A negative result on basic wave equation would not exhaustively refute the hypothesis; it would refute it for the basic substratum, leaving open whether interaction-level trace-out produces fractional powers.

## 7. Next steps

Phase 1 v2 deliverables:

- **Deliverable 2v2:** Implement effective-Lagrangian extraction at $L = 3$, $T = 1, 2, 4$ for 2-point operators. Validate against linear-wave-equation prediction (Section 3.3). Time estimate: this turn.
- **Deliverable 3v2:** Extend to $L = 4, 5, 6$ and 4-point operators. Extract scaling exponents. Time estimate: subsequent turn.
- **Deliverable 4v2:** Compare scaling exponents to integer-EFT prediction; classify outcome A/B/C/D.
