# Phase 1 Results — Trace-Out Fractional-Power Calculation

**Date:** May 11, 2026
**Status:** Phase 1 complete; Phase 2 design requires revision before execution
**Companion to:** PHASE_1_SCOPING.md (initial specification)

---

## Executive summary

Phase 1 Deliverables 2 (exact $L=2$, $q=2$ implementation) and 3 (sampling benchmark for $L=3, 4, 8$) were executed. The computational machinery (bijection validation, trace-out averaging, operator evaluation) works correctly. Three substantive findings emerged that the initial Phase 1 scoping did not anticipate:

1. **The framework's wave equation is linear over $\mathbb{F}_q$** (specifically $\mathbb{F}_2$ at $q = 2$). Time-evolution of uniform-random states is exactly invariant, and cycle lengths on small lattices are trivially short (period 2 at $L = 2$, period 6 at $L = 3$).

2. **Visible-sector-only operators have zero hidden-state variance trivially.** The Phase 1 specification chose operators with support only on visible sites, which by construction cannot detect trace-out effects.

3. **The fractional-power hypothesis requires measuring effective-Lagrangian coefficients, not visible-sector observables.** This is substantially more involved than the initial scoping anticipated and amounts to implementing a Wilsonian RG procedure on the OI substratum.

Each of these is a substantive scientific finding. The first two are pipeline-discovery findings (the kind of thing only learned by executing the calculation, not by paper analysis). The third reveals that the Phase 1 spec under-defined the calculation: it specified machinery without specifying *what quantity* the machinery should compute.

---

## Detailed findings

### Finding 1: Linear wave equation has trivial small-lattice dynamics

The OI substratum wave equation per Substratum §3.3(b):
$$f(x, t+1) = \left[\sum_{\hat{\mu}} f(x+\hat{\mu}, t) + \sum_{\hat{\mu}} f(x-\hat{\mu}, t)\right] - f(x, t-1) \pmod{q}$$

At $q = 2$, this is a *linear* equation in the field $\mathbb{F}_2$. The iteration map $\phi$ is a linear map on $\mathbb{F}_2^{2L^3}$. Linear maps over finite fields have:

- Cycle lengths dividing the order of the map in $GL(N, \mathbb{F}_q)$
- No dynamical-system mixing (deterministic permutation with simple orbit structure)
- Time-invariant marginals on uniform-random initial states

**Empirical verification:**
- $L=2$, $q=2$: All 65,536 states lie on cycles of length 1 (256 fixed points) or 2 (32,640 cycles). No longer cycles exist.
- $L=3$, $q=2$: All sampled states lie on cycles of length 6.
- Uniform-random samples give *exactly time-invariant* observable values (within Monte Carlo noise).

**Implication:** Any test of trace-out dynamics that involves uniform-random initial states and waits for "decay" of correlations will trivially show no decay. This is not a refutation of the framework's prediction — it's a feature of how the test was set up. The framework's prediction is about *effective coupling renormalization*, which is a static (T-independent) quantity in the Wilsonian sense.

**Implication for Phase 2:** Time-evolution-based measurements of correlation decay are the wrong measurement strategy. The right strategy is static measurement of effective Lagrangian coefficients at multiple lattice sizes.

### Finding 2: Operator support matters

The Phase 1 scoping specified four operators (bilinear, trilinear, quartic, kinetic) defined on visible sites only. By construction, such operators have:

$$\text{Var}_h[O_V(s)] = 0 \quad \text{when } O_V \text{ has no hidden-site components}$$

This is mathematically trivial and physically empty. The exact $L=2$ calculation correctly returned $\text{Var}_h = 0$ for all four operators — a clean confirmation that the implementation is correct, while also revealing that the *measurement* was empty.

**Implication for Phase 2:** Operators must be defined on the full lattice and include hidden-site components. The trace-out then maps a full-lattice operator $O^{\text{full}}$ to an effective operator on the visible sector $O^{\text{eff}}_V$:
$$O^{\text{eff}}_V(v) = \frac{1}{|H|} \sum_h O^{\text{full}}(\text{combine}(v, h))$$

The dependence of $O^{\text{eff}}_V$ on $v$ is what carries the trace-out information.

### Finding 3: What "fractional-power suppression" means as a lattice measurement

The original Phase 1 scoping conflated two distinct measurements:

**(A) Variance of effective observables:** $\text{Var}_v[O^{\text{eff}}_V(v)]$. Measures how much the trace-out preserves about the visible state. This is what the initial implementation tried to compute (but failed because of Finding 2).

**(B) Scaling of effective Lagrangian coefficients with cutoff:** for an effective theory $\mathcal{L}_{\text{eff}} = \sum_D c_D(\Lambda) O^{\text{eff}}_D$, measure how the coefficients $c_D(\Lambda)$ scale with the cutoff scale $\Lambda$ (which on the lattice is $\Lambda \sim 1/a \sim L$). Fractional-power suppression means $c_D(\Lambda) \sim \Lambda^{-\alpha(D)}$ with non-integer $\alpha(D)$.

**Measurement (B) is what the fractional-power hypothesis actually predicts.** To compute it on the lattice requires:

1. Selecting an operator basis for the effective Lagrangian.
2. Computing lattice correlation functions of the operators on the full system.
3. Fitting the correlation functions to extract effective Lagrangian coefficients.
4. Repeating at multiple lattice sizes $L$ to extract scaling.
5. Fitting the scaling exponents and comparing across operators of different mass dimension.

This is the **same procedure as standard lattice EFT extraction.** It's well-defined but substantially more involved than the initial scoping anticipated.

### What the initial Phase 1 spec got right and wrong

**Got right:**
- The lattice model (cubic $d=3$, wave equation, periodic BCs)
- The bijection structure and how to implement it
- The visible/hidden partition choices
- The resource estimates (sampling at $L=8$ is chat-tractable, $L=16$ is borderline)
- The pre-registration discipline (Outcomes A through D were specified before execution)

**Got wrong:**
- The operators (visible-only is empty)
- The measurement procedure (variance of visible-only observables doesn't test the hypothesis)
- The conflation of dynamical correlation decay with static coupling renormalization

**Got incomplete:**
- The connection between "fractional-power suppression" and a concrete lattice observable
- The role of operator basis choice in defining what "suppression" means

---

## Revised path forward

### Option A: Implement proper Wilsonian RG extraction

This would be a substantial calculation, properly executing Steps 1-5 above. Resource requirements:

- Operator basis selection: requires careful match between OI lattice variables and SM EFT operators. Possibly Mathematica/sympy-aided.
- Correlation function computation: feasible by stochastic sampling at $L = 4, 6, 8$.
- Coefficient extraction: requires fitting machinery (least squares + error propagation).
- Scaling fits: standard log-log fits.

**Honest assessment:** This is a 1-3 chat-session pipeline. Phase 1 (the revised spec) is chat-tractable. Phase 2 (execution) is chat-tractable for $L \leq 8$. Phase 3 (analysis) is chat-tractable.

### Option B: Defer to offline, return to literature for guidance

Search the lattice-QFT literature for established procedures for extracting effective Lagrangian scaling from non-standard substratum dynamics. The non-Gaussian-bath trace-out is unusual; literature on similar calculations (e.g., trace-out of fast modes in non-Gaussian baths in condensed matter) might provide tools.

This is chat-tractable as literature work; it doesn't require execution.

### Option C: Accept the honest result and report back

The current Phase 1 results show:

1. The framework's substratum (as currently specified, with linear wave equation) has dynamically trivial small-lattice behavior.
2. Testing fractional-power suppression requires a more sophisticated measurement procedure than initially scoped.
3. The "offline-heavy" original classification of GEMs 53-54 was wrong in the sense that Phase 1 is chat-tractable, but right in the sense that getting to a useful answer requires substantial additional work.

**Composite-Higgs cluster confidence: unchanged at 55-70%.** The Phase 1 work neither confirms nor refutes the fractional-power hypothesis. It clarifies what would need to be measured to test it.

### Recommendation

Option C (honest report) plus an offline note that Option A is the path to actual resolution. The Phase 1 deliverable served its stated purpose (determining whether the work is chat-tractable and what it would take to do it properly), even though the answer was more nuanced than anticipated.

---

## Computational machinery produced

All code is in `oi_lattice_code/trace_out_fractional/`:

- `lattice.h` — state representation and site indexing
- `wave_eqn.c` — bijection $\phi$ and inverse $\phi^{-1}$
- `exact_L2.c` — exact enumeration at $L=2$, validation of bijection, cycle enumeration
- `operator_conditioning.c` — variance decomposition (revealed Finding 2)
- `sample_main.c` — sampling benchmark for larger $L$
- `PHASE_1_SCOPING.md` — initial specification (this companion document)
- `PHASE_1_RESULTS.md` — this document

The machinery is reusable for the Option A revised calculation. Specifically:
- `wave_eqn.c` is correct and validated.
- `sample_main.c` provides the right sampling infrastructure.
- A new `effective_lagrangian.c` would need to be written, replacing `operator_conditioning.c`, to compute and fit effective coefficients.

---

## Methodology note

This Phase 1 exercise illustrates §A.13's fourth refinement in action. The default-offline label on GEMs 53-54 was correctly challenged by user prompt; Phase 1 scoping was executed chat-tractably; execution revealed that the calculation is *more* tractable than originally feared (the resource estimates are excellent: $L=8$ is seconds) but *less* immediately conclusive than originally hoped (the measurement procedure needs revision).

**Specifically what §A.13's fourth refinement allowed:** without Phase 1 scoping, GEMs 53-54 would have remained "speculative, offline." After Phase 1 scoping and partial execution, they are "structurally explicit but measurement-procedure-needs-revision" — a much more useful state for downstream decisions.

**What §A.13's fourth refinement did NOT achieve:** the calculation didn't resolve the open question in a single turn. It scoped the question more precisely and revealed that one more revision of the measurement strategy is needed before execution can be informative. This is the normal pattern of research-stage calculations and doesn't reflect any failure of the methodology.

**For future exploratory calculations:** the Phase 1 deliverable should include not just "specify the lattice model and operators" but also "specify the quantity being measured and how it connects to the hypothesis being tested." The initial Phase 1 scoping document specified the former but under-specified the latter; that gap is what produced Finding 2 and Finding 3.
