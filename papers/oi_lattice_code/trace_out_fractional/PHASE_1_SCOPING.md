# Phase 1 Scoping — Trace-Out Fractional-Power Suppression Calculation

**Date:** May 11, 2026
**Status:** Phase 1 scoping (per §A.13 fourth refinement)
**Target:** GEMs 53-54 (trace-out fractional-power mechanism); §B.2.108 Option (a)
**Methodology:** §A.13's three-phase pipeline framing, applied to research-stage exploratory calculation

---

## 1. The hypothesis to test

The composite-Higgs cluster's open question is whether OI's substratum derives $v \ll f$, where $v \sim 246$ GeV is the Higgs vev and $f \sim M_{\mathrm{Pl}}$ is the compositeness scale forced by the framework's structure (SM §8.8). The framework's current commitment is that $v$ is solution-specific (Tier 3) — the bijection $\varphi$ determines $v$ but no structural derivation forces $v$ to be 17 orders of magnitude below $f$.

GEMs 53-54 surfaced an alternative possibility: the trace-out over the hidden sector might produce operator-dimension-dependent suppression with fractional powers of the trace-out parameter. If so, operators of different mass dimensions would be suppressed by different powers of $M_{\mathrm{Pl}}$, with the suppression powers determined by the substratum structure rather than being free parameters.

The specific numerical pattern that motivated the hypothesis:
- Higgs hierarchy: $v / M_{\mathrm{Pl}} \sim 10^{-17}$
- Cosmological-constant hierarchy: $\Lambda^{1/4} / M_{\mathrm{Pl}} \sim 10^{-30}$ (so $\Lambda / M_{\mathrm{Pl}}^4 \sim 10^{-120}$)
- Seesaw hierarchy: $m_\nu / v \sim 10^{-12}$ (so $\Lambda_{\mathrm{seesaw}} \sim v^2 / m_\nu \sim 10^{16}$ GeV)

If a single trace-out mechanism produces operator-dimension-dependent suppression with exponents $\alpha(D)$ where $D$ is the operator's mass dimension, the empirical hierarchies would correspond to:
- $v \sim M_{\mathrm{Pl}} \times f_{\mathrm{trace}}^{\alpha(4)}$
- $\Lambda^{1/4} \sim M_{\mathrm{Pl}} \times f_{\mathrm{trace}}^{\alpha(4)/2}$ (for a $D=4$ vacuum-energy operator with $\Lambda$ being a $D=4$ density)
- $\Lambda_{\mathrm{seesaw}}^{-1} \sim M_{\mathrm{Pl}}^{-1} \times f_{\mathrm{trace}}^{\alpha(5)}$ (for the $D=5$ Weinberg operator)

The hypothesis is testable: if the trace-out produces such a relationship with $\alpha(D)$ determined by structural calculation (not by fitting), the framework's content is substantially extended. If the trace-out produces integer-power suppression (standard EFT scaling), the hypothesis is refuted.

## 2. The lattice model to be implemented

### 2.1 Substratum

The framework's substratum is a finite-bijection $(S, \varphi)$ on a $d = 3$ cubic lattice with:
- $L^3$ lattice sites (parameter to scan)
- A field value at each site from an alphabet of size $q$ (default $q = 2$ for tractability; framework allows any $q \geq 2$)
- The bijection $\varphi$ implementing the lattice wave equation: $f(x, t+1) = \alpha \left[\sum_{\hat{\mu}} f(x + \hat{\mu}, t) + \sum_{\hat{\mu}} f(x - \hat{\mu}, t)\right] - f(x, t-1) \pmod{q}$, with $\alpha = 1$ fixed by the maximum-signal-speed requirement (Substratum §3.3(b))

For the wave equation to fit in a deterministic bijection, the state at each site at time $t$ must encode both $f(x, t)$ and $f(x, t-1)$ — effectively a $q^2$-dimensional state per spatial site, which makes the per-site state space size $q^2 = 4$ for $q = 2$.

**State space size:** $(q^2)^{L^3} = q^{2 L^3}$. For $L = 2$, $q = 2$: $2^{16} = 65{,}536$ states (trivially enumerable). For $L = 3$: $2^{54} \approx 1.8 \times 10^{16}$ (enumeration infeasible; sampling required). For $L = 4$: $2^{128}$ (sampling only).

### 2.2 Partition

The framework's visible / hidden partition is structurally specified but admits several concrete choices for a finite-lattice realization:

**Choice A (causal partition):** Visible = lattice sites within a causal patch of size $L_V^3$ centered on the observer; hidden = the complement. This is the cosmological-horizon analog applied to a finite lattice.

**Choice B (subset partition):** Visible = a fixed subset of $N_V$ sites (e.g., every other site in checkerboard pattern, or one corner block); hidden = the complement. Simpler to implement but loses the causal structure.

**Choice C (mode partition):** Visible = low-momentum modes of the lattice Fourier transform; hidden = high-momentum modes. This is closest to standard QFT trace-out (Wilsonian integration).

For Phase 1, **Choice A is the framework-correct choice** (matches the cosmological-horizon trace-out treated in [Main] and GR papers). Choices B and C are simpler but produce results that may not match the framework's actual trace-out structure.

For Phase 2 (small-lattice test), **Choice B with a corner-block visible region** is computationally simplest while still producing a non-trivial trace-out. The corner-block partition tests whether the *structural form* of fractional-power suppression appears; matching numerical exponents to physical hierarchies requires Choice A and larger lattices.

### 2.3 Operators

The trace-out produces an effective dynamics on the visible sector. To extract dimensional suppression, we need to compute the effective coupling for operators of different mass dimensions.

**Operators to test:**

1. **$D = 4$ bilinear** (Higgs-mass-like): $\mathcal{O}_2(x) = f(x, t) \cdot f(x, t)$. This is the simplest operator and corresponds to a mass term in the emergent EFT.

2. **$D = 5$ trilinear** (Weinberg-like): $\mathcal{O}_3(x) = f(x, t)^2 \cdot f(x + \hat{\mu}, t)$. The Weinberg operator's emergent form involves three field operators with appropriate Lorentz structure; on the lattice this maps to a trilinear in $f$ with nearest-neighbor structure.

3. **$D = 6$ quartic** (four-fermion-like): $\mathcal{O}_4(x) = f(x, t)^2 \cdot f(x + \hat{\mu}, t)^2$. Tests the next-higher operator class.

4. **$D = 4$ kinetic** (gauge-boson-mass-like): $\mathcal{O}_K(x) = [f(x + \hat{\mu}, t) - f(x, t)]^2$. Tests whether kinetic operators are suppressed differently from mass operators (this would distinguish gauge-boson-mass-style suppression from scalar-mass-style suppression).

### 2.4 What the trace-out computes

Starting from the full bijection $\varphi$ on $S$, partitioned into $S = V \cup H$ (visible $\cup$ hidden):

For each visible-sector observable $O_V$, the trace-out produces an effective time-evolution operator on $V$ alone:
$$U_{\mathrm{eff}}[O_V](t) = \frac{1}{|H|} \sum_{h \in H} O_V(\varphi^t(v, h))$$

where the sum is over hidden-sector states $h$ at $t = 0$, and $\varphi^t$ is the bijection iterated $t$ times. The effective dynamics on $V$ is non-unitary (it's a stochastic process per the framework's characterization theorem) and non-Markovian.

**For each operator $\mathcal{O}_D$**, the effective coupling is extracted from the time-averaged or stationary-state value of $\langle \mathcal{O}_D \rangle_V$ in the trace-out dynamics. The dependence of $\langle \mathcal{O}_D \rangle_V$ on the lattice size $L$ and the visible-fraction $|V|/|S|$ produces the scaling we want to extract.

**Specifically:** if $\langle \mathcal{O}_D \rangle_V \sim L^{-\alpha(D)}$ at fixed visible fraction in the large-$L$ limit, then $\alpha(D)$ is the dimensional-suppression exponent for operator $\mathcal{O}_D$.

## 3. Phase 2 computational approach

### 3.1 Choice of method

Three computational approaches are available:

**Method 1: Exact enumeration.** Enumerate all $q^{2 L^3}$ states, apply $\varphi$, compute exact trace-out. Feasible only for $L = 2$, $q = 2$ ($2^{16}$ states), or possibly $L = 3$, $q = 2$ with careful memory management ($2^{54}$ states — needs sparse representation).

**Method 2: Stochastic sampling.** Sample bijection orbits uniformly from the configuration space, apply $\varphi$, average observables over samples. The wave equation's orbit structure (cycles of various lengths on the configuration space) determines sampling efficiency. For $L = 4$ to $L = 16$, this is the appropriate method.

**Method 3: Transfer-matrix.** Decompose the bijection into transfer operators between time slices, diagonalize the transfer operator restricted to the visible sector, extract effective dynamics from the spectrum. Most efficient for $L$ up to maybe $L = 8$ but requires implementation of the framework's specific transfer-matrix structure.

**Recommendation for Phase 2:** Start with Method 1 at $L = 2$ to validate the implementation against known structural features (e.g., the wave equation must conserve total field momentum modulo $q$). Then move to Method 2 (stochastic sampling) at $L = 4, 6, 8$ to extract scaling.

### 3.2 Resource estimate

**Method 1 at $L = 2$, $q = 2$:** Configuration space $2^{16} = 65{,}536$. Each state's evolution under $\varphi$ is $O(L^3) = O(8)$ operations. Total: $\sim 5 \times 10^5$ operations per time step. For $T = 100$ time steps and $\sim 4$ operators: $\sim 2 \times 10^8$ operations total. **Estimated runtime: seconds in C; tens of seconds in Python.** Feasible in a single chat turn.

**Method 2 at $L = 4$, $q = 2$:** Configuration space $2^{128}$. Sampling $N_{\mathrm{samp}} = 10^4$ orbits, each evolved for $T = 100$ time steps. Per-sample cost: $O(L^3 \cdot T) = O(6400)$ operations. Total: $\sim 6 \times 10^7$ operations per operator. **Estimated runtime: seconds to minutes in C; minutes in Python.** Feasible in a single chat turn.

**Method 2 at $L = 8$, $q = 2$:** Per-sample cost $O(L^3 \cdot T) = O(51{,}200)$ operations. With $N_{\mathrm{samp}} = 10^4$: $\sim 5 \times 10^8$ operations per operator. **Estimated runtime: minutes to tens of minutes in C; tens of minutes to hours in Python.** Borderline for a single chat turn; needs benchmarking.

**Method 2 at $L = 16$:** $L^3 = 4096$, per-sample $O(L^3 \cdot T) \sim 4 \times 10^5$, with $N_{\mathrm{samp}} = 10^4$: $\sim 4 \times 10^9$ operations per operator. **Estimated runtime: tens of minutes to hours in C.** Likely requires offline execution.

### 3.3 Code structure

The implementation should follow the existing `oi_lattice_code/` conventions:

```
oi_lattice_code/trace_out_fractional/
├── lattice.h              # State representation, partition definition
├── wave_eqn.c             # Bijection implementation: f(x, t+1) = sum_neighbors(f) - f(x, t-1) mod q
├── trace_out.c            # Trace-out: sum over hidden-sector states, average observables
├── operators.c            # The four operators (bilinear, trilinear, quartic, kinetic)
├── exact_L2.c             # Method 1 driver for L=2 validation
├── sample_main.c          # Method 2 driver for L=4, 6, 8
├── analyze.py             # Scaling extraction: fit log<O_D>_V vs log L for each D
└── README.md              # Phase 1 spec + Phase 3 pre-registration
```

## 4. Phase 3 pre-registration

### 4.1 Closure criteria

The Phase 2 calculation produces, for each operator $\mathcal{O}_D$ and each lattice size $L$, an effective coupling $\langle \mathcal{O}_D \rangle_V (L)$. Fitting $\log \langle \mathcal{O}_D \rangle_V$ vs $\log L$ produces a scaling exponent $\alpha(D)$.

**Outcome A (fractional powers with hierarchy match):** If $\alpha(D)$ is non-integer and the values produce the empirical hierarchies $10^{-17}$ (Higgs) and $10^{-120}$ (CC) when extrapolated to $L \sim M_{\mathrm{Pl}}/a$ (where $a$ is the lattice spacing), the trace-out fractional-power mechanism is *empirically supported at small lattice* and warrants extended investigation. This would shore the composite-Higgs cluster substantially — from 55-70% toward 75-85%.

**Outcome B (fractional powers without hierarchy match):** If $\alpha(D)$ is non-integer but the values do not produce the empirical hierarchies, the trace-out mechanism is *real but does not explain the actual physical hierarchies*. The framework's commitment to $v$ as solution-specific (per §B.2.108) is reinforced; the trace-out produces interesting structural features but does not resolve the open question. The composite-Higgs cluster confidence remains at 55-70%.

**Outcome C (integer powers):** If $\alpha(D)$ is integer for all operators tested (standard EFT scaling), the fractional-power hypothesis is refuted at the small-lattice level. GEMs 53-54 are demoted from "speculative open conjecture" to "refuted hypothesis." The composite-Higgs cluster confidence is unchanged (the framework's existing scoping is already correct).

**Outcome D (no clean scaling):** If the data shows non-monotonic behavior or fits poorly to a power law, the calculation needs larger $L$ to resolve. Phase 2 would extend to $L = 16$ (offline) and the conclusion would depend on the extended scaling.

### 4.2 Falsification criteria

The calculation refutes the hypothesis if any of:

- $\alpha(D) \in \mathbb{Z}$ for all four operators tested at $L = 2, 4, 6, 8$
- $\alpha(D)$ is not a function of $D$ only (depends sensitively on the partition choice, operator definition, or lattice-specific artifacts)
- $\alpha(D)$ scaling extrapolated to physical $L$ produces hierarchies inconsistent with observed values by more than a factor of $10^3$

Each falsification outcome is informative: it tells us which class of mechanisms is structurally impossible, narrowing the search for $v \ll f$ explanations.

### 4.3 Framework propagation

**If Outcome A:** SM §8.8 is updated to commit to fractional-power suppression as the structural mechanism for $v \ll f$; the composite-Higgs cluster gets a major confidence upgrade.

**If Outcome B:** SM §8.8 remains as-is (the framework's commitment to $v$ as Tier 3 stands); GEMs 53-54 are updated in OI_MASTER to record that trace-out does produce structural effects but not the specific hierarchy claimed.

**If Outcome C or D:** GEMs 53-54 are recorded as refuted (Outcome C) or inconclusive at chat scale (Outcome D); the composite-Higgs cluster confidence is unaffected.

## 5. Phase 1 deliverables

This document constitutes Phase 1 deliverable 1 (specification). Phase 1 deliverable 2 is a Method 1 prototype in C/Python that exercises the smallest case ($L = 2$, $q = 2$). Phase 1 deliverable 3 is a resource benchmark establishing whether Method 2 at $L = 4, 6, 8$ fits within a chat turn.

Deliverables 2 and 3 are next-step work that fits in a separate turn. If the user wants to proceed, deliverable 2 (working $L = 2$ implementation) would be the next concrete output.

## 6. Honest assessment

This Phase 1 scoping has done the following:

1. **Stated the hypothesis precisely.** Trace-out produces operator-dimension-dependent fractional-power suppression with specific structural exponents.

2. **Specified the lattice model.** $d = 3$ cubic lattice with wave-equation bijection (already in framework specification).

3. **Identified the partition.** Three concrete options (A causal, B subset, C mode); A is framework-correct, B is computationally simplest for first pass.

4. **Selected operators.** Four operators of mass dimensions 4, 5, 6 and kinetic-vs-mass distinction.

5. **Sized the computation.** Method 1 at $L = 2$ is trivially feasible; Method 2 at $L = 4, 6, 8$ is single-chat-turn feasible; $L = 16$ is borderline / offline.

6. **Pre-registered outcomes.** Four distinct outcomes (A through D) with specified confidence-impact and framework-propagation responses.

This Phase 1 work does *not* commit to the calculation succeeding. It does commit to the calculation being well-specified enough that a successful or failed outcome is interpretable.

**Status update for §B.2.108 Option (a):** Per §A.13 fourth refinement, Option (a) is no longer "offline-heavy." Phase 1 is complete; Phase 2 (Method 1 implementation at $L = 2$) is chat-tractable as a next step. The composite-Higgs cluster's open question now has a defined computational path to either resolution or refutation.

---

## Next-turn decision point

The Phase 1 deliverable above is complete. To proceed to Phase 2 in this chat:

- **Deliverable 2:** Implement Method 1 at $L = 2$ in C and Python, run it, verify the wave equation's structural features (momentum conservation, time-reversal invariance, orbit structure), and produce the first effective-coupling values.

- **Deliverable 3:** Benchmark Method 2 at $L = 4, 6, 8$ to determine the actual runtime envelope.

If these complete in chat, Phase 2 is fully chat-tractable and we can proceed directly to Phase 3 (scaling extraction and outcome classification).

If they don't (e.g., Method 2 at $L = 8$ is too slow), Phase 2 splits cleanly into chat-tractable Method 1 + Method 2 small-$L$ + offline Method 2 large-$L$.

Either way, the Option (a) work is no longer "offline-heavy" in any informative sense — it's a well-decomposed pipeline.
