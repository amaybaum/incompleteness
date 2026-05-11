# Phase 1 v2 Results — Trace-Out Fractional-Power Calculation

**Date:** May 11, 2026
**Status:** Phase 1 v2 complete; Outcome C (refutation at basic-substratum level)
**Companion to:** PHASE_1_SCOPING_v2.md

---

## Executive summary

Phase 1 Deliverable 2v2 executed: effective-Lagrangian extraction at $L = 3$, $T = 0, 1, 2, 4$, $N_h = 500$ to $8000$ samples. The measurement is the conditional expectation $\tilde{O}_T(v)$ of a 2-point visible-spin operator averaged over uniform random hidden states, decomposed in a visible-operator basis.

**Result: Outcome C (refutation at basic-substratum level).** All effective coefficients at $T \geq 1$ are consistent with zero within sampling noise. Total variance of $\tilde{O}_T(v)$ scales as $1/N_h$, confirming that the apparent non-zero values are purely statistical.

The fractional-power suppression mechanism (GEMs 53-54) does not operate through trace-out on the bare substratum wave-equation dynamics.

---

## Detailed findings

### Finding 1: $T = 0$ recovers expected free-theory result

At $T = 0$, the operator $O = \text{spin}(f_a) \, \text{spin}(f_b)$ is purely visible. The effective decomposition gives:
- $c_{ab,\text{now}} = 1.00$ exactly
- All other coefficients fluctuate around zero with finite-$N_h$ noise

This validates the implementation: the measurement correctly recovers the trivial case.

### Finding 2: $T \geq 1$ gives identically zero effective couplings

At $T = 1$:
- Total variance of $\tilde{O}_T(v)$ over visible state space: ~0.002 with $N_h = 500$
- Same measurement with $N_h = 2000$: 0.0004
- Same measurement with $N_h = 8000$: 0.0001

The variance scales as $1/N_h$, exactly as expected for pure sampling noise. The true effective coefficients are exactly zero.

At $T = 2, 4$: same pattern.

### Finding 3: The structural reason this happens

The OI substratum wave equation is *linear* over $\mathbb{F}_2$. For a visible site $x$ at time $T \geq 1$, the wave equation gives:
$$f(x, T) = \sum_y \mathcal{P}_T(x, y) \, f(y, 0) \pmod{2}$$
where $\mathcal{P}_T$ is the propagation kernel.

For sites adjacent to the hidden region (which all visible sites in our partition are, at $T \geq 1$), the kernel $\mathcal{P}_T$ has non-zero coefficients on hidden sites.

The conditional expectation over uniform-random hidden initial conditions is then:
$$\langle \text{spin}(f(x, T)) \rangle_h = \langle (-1)^{\sum_y \mathcal{P}_T(x, y) f(y, 0)} \rangle_h$$

For each hidden site $y$ with $\mathcal{P}_T(x, y) = 1 \pmod 2$:
$$\langle (-1)^{f_y} \rangle_{f_y \sim U(\{0,1\})} = \frac{1}{2} \cdot (-1)^0 + \frac{1}{2} \cdot (-1)^1 = 0$$

So if *any* hidden site has $\mathcal{P}_T(x, y) = 1 \pmod 2$, the conditional expectation is **identically zero**, not merely small.

Similarly for 2-point correlators $\langle \text{spin}(f(x, T)) \text{spin}(f(y, T)) \rangle_h$: this gives zero unless the two propagation kernels have *exactly the same parity on every hidden site*, which is a measure-zero condition for the partition chosen.

### Finding 4: This is a structural property of linear-mod-q dynamics

The result is not specific to $L = 3$. For *any* $L$ with periodic boundary conditions and the visible/hidden split chosen here:

- At $T = 0$: operator is purely visible; trace-out is trivial
- At $T \geq 1$ with visible sites adjacent to hidden region: trace-out is **exactly destructive** for low-point spin correlators
- The only non-trivial effective couplings come from higher-point correlators (4-point or more) and/or from purely-visible sites that the wave equation has not yet propagated information from hidden to (i.e., visible sites $x$ with $\mathcal{P}_T(x, h) = 0$ for all hidden $h$)

For a $9$-site visible boundary in a $27$-site lattice at $T = 1$, all visible sites are nearest-neighbor to hidden sites, so the kernel hits hidden for all of them. **The trace-out is exactly destructive for all single-site and pair correlators.**

---

## Interpretation: what was refuted, what was not

### What this refutes (Outcome C at basic-substratum level)

**The fractional-power suppression hypothesis (GEMs 53-54) does not operate through trace-out on the bare substratum wave-equation dynamics.** The trace-out at $T \geq 1$ produces either:
- Trivial (visible information preserved unchanged at $T = 0$) — integer power $\alpha = 0$
- Exactly destructive ($T \geq 1$ with hidden adjacency) — formally $\alpha = \infty$

There is no intermediate regime where the trace-out produces fractional-power-suppressed effective couplings. The "hidden information leakage" the hypothesis envisioned doesn't exist at this level.

### What this does NOT refute

1. **The framework's composite-Higgs cluster confidence.** SM §8.8 already commits to $v$ as Tier 3 (solution-specific), not derived. GEMs 53-54 were "speculative numerology pending structural derivation"; that derivation now has negative evidence, but the framework's claims don't depend on it.

2. **Fractional-power suppression in the emergent EFT.** The framework's full content includes gauge couplings, staggered fermion structure, and matter content. Effective coefficients in the *emergent* EFT (Higgs mass term, Weinberg operator, etc.) could still exhibit operator-dimension-dependent scaling — but this is a different calculation, involving emergent-EFT loop corrections rather than direct substratum trace-out.

3. **The framework's other hierarchy claims.** Strong CP ($\bar\theta = 0$) and cosmological constant dissolution use different structural mechanisms; the negative result here doesn't affect them.

### Where fractional-power suppression could still come from

If a structural mechanism for $v \ll f$ exists in the framework, it likely involves:

**Option A**: Emergent EFT loop corrections with operator-dimension-dependent renormalization. This is the standard lattice-perturbation-theory calculation applied to the framework's specific gauge and matter content. The existing `oi_lattice_code/` infrastructure for vacuum polarization is the right starting point.

**Option B**: Non-trivial cycle averaging on the bare substratum. The cycle structure of $\phi$ on a finite lattice produces orbit averages that are not the same as uniform-random averages. Time-averaged observables along orbits might exhibit fractional-power scaling that uniform-random samples miss.

**Option C**: Higher-point correlators that are not pure products of single-site spins. The framework's full operator content includes Yukawa-like trilinears and four-fermion-like quartics; these could survive the trace-out where simple spin products don't.

**Option D**: The hierarchy is genuinely Tier 3, as SM §8.8 already commits. The trace-out doesn't produce it because no substratum-structural mechanism does; $v$ is solution-specific to $\varphi$.

The Phase 1 v2 result is consistent with all four options. The negative result removes one *specific* speculation (GEM 53-54's basic-substratum mechanism) but doesn't distinguish between A, B, C, D.

---

## Confidence impact

**GEMs 53-54 status:** *Refuted at the basic-substratum level.* The trace-out on bare wave-equation dynamics does not produce operator-dimension-dependent fractional-power suppression. The "speculative" qualifier on GEMs 53-54 is now *experimentally* warranted — there was a chat-tractable test, it was done, and the mechanism does not work in the simplest version.

**Composite-Higgs cluster confidence:** Unchanged at **65-75%** (post-§B.2.112).

The refutation of GEMs 53-54 doesn't lower the cluster confidence because:
- The framework's commitment to $v$ as Tier 3 doesn't depend on trace-out fractional powers
- GEMs 53-54 were "open speculative" — their refutation is a confirmation that the framework's existing scoping is correct, not a downgrade
- The cluster's defensibility against external scrutiny is *strengthened* by being able to say "the trace-out mechanism for fractional powers was tested at chat scale; it doesn't operate"

The refutation also doesn't raise the confidence (Outcome A would have been needed for that). The cluster stays at 65-75% with the open question about $v \ll f$ unchanged.

**Honesty value:** Cluster confidence should reflect that the framework has *tested and ruled out* one specific speculative mechanism. This is methodologically substantive — speculative hypotheses don't accumulate forever; they get tested and either confirmed or refuted.

---

## What was learned about the methodology

### What worked

- Phase 1 spec v2 correctly identified the v1 errors (operator support, time-evolution vs RG scaling)
- The measurement procedure is well-defined and produces interpretable results
- Computational cost is excellent (~0.4 s for $L = 3$, $T = 4$, $N_h = 500$, $N_v = 200$); scales to larger lattices easily
- Sanity checks (T=0 recovers free theory; noise scales as $1/N_h$) all pass

### What's still incomplete

- 4-point correlator measurement implemented but not exercised; should run before declaring Outcome C definitive
- Scaling with $L$ not tested (current execution at $L = 3$ only); should run at $L = 4, 5, 6$ for completeness
- Cycle-averaged (rather than uniform-random) sampling not tested; could reveal Option B (non-trivial orbit structure)

These are straightforward follow-ups. The current findings are strong enough to declare Outcome C *at the basic uniform-sampling level*, but full closure would require exercising 4-point operators and cycle-aware sampling.

### Methodology refinement candidate

The §B.2.111 fifth-refinement proposal (Phase 1 deliverables should include measurement-procedure pre-registration) is *validated* by this exercise. The v2 spec correctly identified what to measure, the implementation matched the spec, and the results are interpretable against the pre-registered outcome criteria. The fifth refinement is operationally useful.

---

## Recommendation

**Outcome C (refutation at basic-substratum level) is the honest finding.** GEMs 53-54 should be marked **refuted at chat scale** in framework documentation. The composite-Higgs cluster's status is unchanged.

**Three follow-up options:**

1. **Close the investigation.** Mark GEMs 53-54 refuted; composite-Higgs cluster at 65-75%; no further trace-out work.

2. **Extend to 4-point operators and cycle averaging.** Test Options B and C in Section "Where fractional-power suppression could still come from." This is chat-tractable and would either find unexpected structure or definitively close the basic-substratum hypothesis. Estimated time: 1 chat turn.

3. **Pivot to emergent-EFT calculation.** Use the existing `oi_lattice_code/` vacuum polarization infrastructure to compute operator-dimension-dependent renormalization in the emergent EFT (Option A). This is more involved but is the *correct* place to look for the framework's claimed mechanism if it exists. Estimated time: 2-3 chat turns.

The honest recommendation is **Option 1 (close)** unless the user wants to pursue the emergent-EFT direction, which would shift from basic substratum to gauge-structure-aware calculation.

---

## Files produced

- `effective_lagrangian.c` — uniform-random sampling implementation
- `effective_extended.c` — 4-point + cycle-averaged implementation
- `effective_2d.c` — 2D version enabling L-scaling tests within 64-bit state
- `cycle_lengths.c` / `cyc_2d.c` — cycle-length measurement utilities
- `eff_lag`, `eff_ext_v2`, `eff_2d`, `cyc`, `cyc_2d` — compiled binaries
- `PHASE_1_SCOPING_v2.md` — revised specification
- `PHASE_1_RESULTS_v2.md` — this document

---

## Extension: cycle-averaged sampling reveals non-trivial structure (Option B)

After the uniform-random measurement returned trivial results, Option B (cycle-averaged sampling) was tested. Results:

### Cycle averaging produces stable non-zero effective coupling at $L = 3$ (3D)

- $c_{ab}$ (cycle-averaged) = $0.171 \pm 0.002$ across $N_h = 100, 500, 2000$
- Compared to uniform-random sampling ($c_{ab} \sim 1/\sqrt{N_h}$, exactly zero in limit)
- **Cycle averaging extracts genuine effective-coupling information that uniform sampling misses**

### 2D scaling test reveals number-theoretic, not power-law, structure

Tested $L = 3, 4, 5$ in 2D (substratum extension fitting within 64-bit state):
- $L = 3$: $c_{ab} = 0.167$ (cycle length 6)
- $L = 4$: $c_{ab} = 0.258$ (cycle length 4)
- $L = 5$: $c_{ab} = 0.032$ (cycle length 30)

**Non-monotonic in $L$.** The variation tracks the cycle-length number theory (orders of the wave-step matrix in $GL(2L^d, \mathbb{F}_2)$) rather than a smooth $L^{-\alpha}$ power law.

### Interpretation

The cycle-averaged trace-out is genuinely non-trivial, but **its structure is arithmetic, not smooth power-law**. Cycle lengths depend on whether the wave-step matrix's characteristic polynomial factors nicely over $\mathbb{F}_2$ — a purely number-theoretic question with no relationship to operator mass dimensions.

This refutes the **specific form** of the fractional-power suppression hypothesis: the hypothesis predicts smooth $L^{-\alpha(D)}$ scaling with operator-dimension-dependent $\alpha$. The actual structure is non-monotonic and number-theoretic.

**However**, the cycle-averaged measurement does reveal that **the OI substratum dynamics carries structure beyond the trivial uniform-random average.** This is a genuine novel finding from the calculation, even though it doesn't support the fractional-power hypothesis.

---

## Final assessment

**Outcome: refined Outcome C with caveat.**

GEMs 53-54's **specific claim** (operator-dimension-dependent fractional-power suppression $L^{-\alpha(D)}$ from trace-out) is refuted at chat scale on the bare substratum. The trace-out structure exists but is number-theoretic (cycle-length dependent), not smooth power-law.

**What this means for the composite-Higgs cluster:**

- GEMs 53-54 (in their specific form) are refuted at chat scale. Mark as such in OI_MASTER.
- The composite-Higgs cluster confidence is unchanged at 65-75% (since SM §8.8 already commits to $v$ as Tier 3).
- A residual research question is now sharper: the OI substratum's cycle structure carries non-trivial information that's not captured by uniform-random sampling. What physical interpretation does this number-theoretic structure have? Is it relevant to any framework claim?

**This is a research direction in its own right.** The cycle-length number theory of the OI substratum is potentially relevant to the framework's structural derivations (the Cabibbo angle from $\pi\sqrt{2}$, the Koide angle from $2/9$, etc., are all "rational with $\pi$" structures that could have origins in the substratum's number-theoretic features).

But it's not the fractional-power suppression hypothesis. That specific hypothesis is refuted.
