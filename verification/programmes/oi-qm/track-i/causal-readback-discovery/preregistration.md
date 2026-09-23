# Realization-level causal-readback discovery audit

Owner-called after merges #540 and #541, from clean `main` at
`d894306609813ce24279592f14e51bd40613f414`.

This commit is the preregistration only. It freezes the physical parent condition and the mandatory controls before any proof, probe, Lean definition, manuscript edit, Barandes application, or publication-record change.

## Why this round exists

The two preceding audits closed the upstream interface question in layers.

- #540 established that Barandes-style unitary/Born representability does not require a uniquely selected invariant global ensemble; the fixed transition law is the relevant correspondence datum, while standalone probabilities remain contingent/preparation data.
- #541 established that the maintained observer-realization layer genuinely supplies a rooted stochastic family once a realization and its fixed hidden prior are declared, with the counting/maximal-entropy construction providing a canonical common-prior baseline but structured fixed priors remaining allowed.

What is still missing is the physical bridge from the original history-readback idea to the rooted one-time marginal obstruction already proved in #538. The existing manuscript C4 is history-sensitive memory and does not by itself imply marginal collision/revival. Conversely, #538's `C4e` and `C4r` are useful observable signatures but are not themselves a physical account of how information is written, stored, and read back.

This round therefore searches for a neutral **realization-level causal parent condition**. It must live on the physical reversible realization, not on `Γ_t` alone, so that any implication to `C4w`, `C4e`, `C4r`, or P-indivisibility is earned rather than definitional.

## Frozen realization layer

Work on a finite realization

`R = (V, H, φ, μ_H)`

with:

- finite visible carrier `V`;
- finite hidden carrier `H`;
- deterministic reversible update `φ : V × H ≃ V × H`;
- one fixed normalized hidden prior `μ_H`, common to every visible root in that realization;
- rooted preparation `X_0 = a`, `H_0 ~ μ_H`;
- visible readout by the first projection.

For each root `a`, write

`Γ_t(a,j) = P(X_t = j | X_0 = a)`.

The prior is part of the realization datum. No theorem in this round may silently quantify away its value. #541's canonical uniform prior is one selected baseline, not the only manuscript-permitted preparation law.

## The parent condition: physical content frozen before formalization

The name under study is `CausalReadback`. The Lean spelling may differ, but any accepted formalization must preserve all three clauses below and must not be weakened after seeing a proof failure.

The parent expresses a **causal cycle**

`visible root -> hidden memory -> later visible effect`.

The clauses are deliberately stated on the realization rather than on the rooted matrices.

### W — write

A visible preparation must causally affect the hidden sector under the same exogenous hidden seed.

There must exist distinct roots `a != b`, a hidden seed `h` with `μ_H(h) > 0`, and a time `w > 0` such that, when the two runs start from `(a,h)` and `(b,h)`, their hidden components after `w` steps differ.

Equivalently in words: changing only the visible root while holding the hidden preparation fixed changes the later hidden state.

This excludes mere pre-sampled hidden response data whose hidden state never acquires information from the visible preparation.

### S — store

The written distinction must remain available in hidden degrees of freedom at a later storage time while the current visible value alone does not resolve the relevant histories.

There must exist a storage time `s >= w` and a visible value `x` that occurs with positive probability under both rooted preparations such that the root-conditioned hidden laws at that same current visible value differ:

`Law(H_s | X_s=x, X_0=a) != Law(H_s | X_s=x, X_0=b)`.

The clause is conditional on the **same current visible value**. It therefore means that the hidden sector retains information not contained in the current visible endpoint alone.

No equality of the full rooted visible rows `Γ_s(a,-)` and `Γ_s(b,-)` is required here. Exact marginal collision is intentionally not built into the parent.

### R — read

The stored hidden distinction must have a later causal visible consequence, and that consequence must appear in the actual rooted visible process rather than only in a counterfactual hidden channel.

There must exist `t > s` such that both of the following hold for the same root pair and stored visible value:

1. **causal hidden-to-visible leg:** holding the current visible value `x` fixed, propagating the two root-conditioned hidden laws from time `s` through the same deterministic future dynamics gives different visible output laws at time `t`;
2. **actual readback:** the rooted visible laws at `t` differ, `Γ_t(a,-) != Γ_t(b,-)`.

Clause (1) makes the read causal rather than correlational: at the storage surface the visible value is held fixed and only the hidden conditional differs. Clause (2) requires that the information actually reappear in the observer's one-time statistics, not merely exist as a latent counterfactual effect that cancels after averaging over the rest of the visible support.

### Timing

The admissible order is

`0 < w <= s < t <= K`

for a finite horizon `K`. `w=s` is allowed: writing and storage need not occupy two separately resolvable time steps. The read must occur later.

Calling `K` physically accessible requires whatever existing accessibility/timescale condition the manuscript already uses. The formal parent itself supplies no new clock assumption.

## Why the parent is not `C4e` or `C4r` by definition

The store clause asks only for a common current visible value with different hidden conditionals. It does **not** require

`Γ_s(a,-) = Γ_s(b,-)`.

The read clause asks for later rooted separation and for a causal hidden contribution, but does **not** require that total-variation distinguishability increase from `s` to `t`.

Therefore neither `C4e` nor `C4r` is syntactically part of `CausalReadback`. Their relation to the parent is a theorem/counterexample question.

## Frozen target order

Attempt the following in order.

### T1 — history-level consequence

`CausalReadback -> C4w`.

Here `C4w` means the maintained history-sensitive condition: two positive-probability visible histories with the same current visible state have different future conditional laws, equivalently positive history-conditioned memory in the finite setting.

The proof, if it exists, must use the common-current-visible storage surface plus the causal hidden-to-visible read. It must not replace `C4w` by a rooted marginal condition.

### T2 — exact marginal revival

Attempt

`CausalReadback -> C4e`.

This implication is explicitly preregistered as **possibly false**. Failure is an admissible and informative outcome because the parent does not require exact equality of rooted rows at the storage time.

If false, preserve the counterexample. Do not strengthen the parent after seeing it.

### T3 — quantitative marginal revival

Independently attempt the weaker existing target

`CausalReadback -> C4r`.

Because `C4r -> PIndivisibleWithin` is already proved in #538, success here would close the marginal bridge without exact collision.

This implication is also not assumed true in advance.

### T4 — fallback observable child only under a second freeze

If both T2 and T3 fail while the parent still appears physically correct, the round may search for a weaker observable child provisionally named `C4cr` only under the following discipline:

- first record the exact counterexamples to T2/T3;
- then commit a separate preregistration amendment **before** defining or proving `C4cr`;
- the amendment must state the candidate in observable/rooted terms and a non-tautological route by which it could forbid stochastic divisibility;
- `C4cr` may not be defined as `PIndivisibleWithin`, as the nonexistence of a stochastic propagator, or by directly embedding the desired conclusion.

No `C4cr` theorem is accepted from an after-the-fact definition chosen solely because it makes the proof go through.

## Mandatory controls

All four controls are binding. A parent formalization that fails the required behavior is rejected or explicitly reported as a different notion.

### N1 — XOR/history-memory control: must fail the parent while satisfying C4w

Use the existing finite-horizon XOR/history-memory law from the C4 audit: it has maximal history-conditioned memory while its rooted one-time family remains mixed over the audited window.

Required behavior:

- `C4w`: yes;
- `CausalReadback`: no within that horizon.

This prevents ordinary history dependence or a pre-sampled response table from being renamed physical readback.

If a particular reversible completion of the XOR law appears to satisfy the parent only because the completion itself writes an explicit history ledger, that dependence on completion must be reported: the control is about what the observed law forces, not what an arbitrarily enriched realization can be made to contain.

### P1 — delayed visible revival: must satisfy the parent

Use the existing delayed-revival law

`Γ_1 = I`, `Γ_2 = J/2`, `Γ_3 = I`

with a reversible realization in which the initial visible distinction is carried through hidden memory during the mixed stage and later returned to the visible sector.

Required behavior:

- `CausalReadback`: yes;
- `C4e`: yes for the known witness;
- hence `C4r` and P-indivisibility by the existing #538 theorems.

This is the positive calibration of the parent.

### N2 — uncoupled reversible product: recurrence is not readback

Use an uncoupled product update

`φ(v,h) = (σ_V(v), σ_H(h))`

with arbitrary finite permutations and a fixed hidden prior.

Required behavior:

- finite recurrence may occur;
- `CausalReadback`: no, because the visible root never writes into the hidden sector and hidden variation never mediates the visible evolution.

This prevents finite recurrence itself from being counted as causal readback.

### P/N prior-dependence pair — same dynamics, opposite divisibility verdicts

Fix

`V = H = {0,1}`

and

`φ(x,h) = (x XOR h, h)`.

The same bijection and the same partition are evaluated under two manuscript-permitted fixed priors.

1. Uniform hidden prior:
   `Γ_1 = J/2`, `Γ_2 = I`, hence the rooted family is P-indivisible over the two-step horizon.
2. Point-mass prior `δ_0`:
   `Γ_1 = Γ_2 = I`, hence the rooted family is P-divisible.

The clean isolation is `φ^2 = id`, so `Γ_2 = I` under every prior and only the one-step map changes.

Required theorem-level conclusion if kernelized:

> P-divisibility is not a property of `(φ, partition)` alone; the fixed preparation prior `μ_H` can change the verdict.

This control does **not** by itself decide whether either prior satisfies `CausalReadback`; that must follow from the frozen W/S/R clauses, not be stipulated to match the divisibility result.

It also freezes the consequence discipline for the later OI chain: any statement that the physical OI realization is P-indivisible must name the canonical-baseline selection or another physical preparation principle. It may not silently quantify over all allowed fixed priors.

## Completion dependence guard

`CausalReadback` is a property of a **declared realization**, while `C4w`, `C4e`, `C4r`, and the rooted family are observable/process-level objects.

Different reversible completions of the same visible process may carry different hidden mechanisms. Therefore the round must distinguish:

- **realization sufficiency:** a particular declared realization has W/S/R;
- **process forcing:** every faithful realization of a given visible law must have the relevant causal mechanism.

The first is the immediate target. The second is stronger and is not inferred without proof.

In particular, a positive realization witness may not be reported as saying the visible law uniquely determines that hidden causal architecture.

## Prior-selection guard

#541 permits structured realization-specific priors and supplies a canonical uniform baseline. The parent is evaluated **after** a prior has been declared.

The round must therefore report results in one of these forms, as earned:

- under the canonical counting/uniform baseline;
- for every fixed prior satisfying explicit hypotheses;
- for a named realization-specific prior;
- or prior-dependent, with the dependence exposed.

No unqualified `OI -> P-indivisible` statement is admissible if the proof changes truth value with `μ_H`.

## Barandes boundary guard

No Barandes theorem is used to prove W, S, R, C4w, C4e, C4r, or P-indivisibility.

If the round succeeds, the later correspondence step remains logically separate:

`OI realization -> sourced rooted stochastic family -> physical causal readback / nonclassical sector`

and independently

`sourced rooted stochastic family -> Barandes unitary/Born representation`.

Representability must not be made equivalent to P-indivisibility. #540's phase/gauge/Hamiltonian/dilation freedom remains binding.

## Admissible outcomes

The round must report one of the following headline classes, with T1–T4 and all controls reported separately.

**A — full bridge through existing `C4e`.** The parent survives the controls and implies `C4w` and `C4e`; #538 then gives `C4r` and P-indivisibility.

**B — bridge through `C4r` but not exact collision.** The parent survives the controls and implies `C4w` and `C4r`, while `CausalReadback -> C4e` is false. Exact marginal collision was a sufficient special case, not the physical essence.

**C — history bridge succeeds, existing marginal signatures are too strong.** The parent survives the controls and implies `C4w`, but neither `C4e` nor `C4r` follows. A separately preregistered `C4cr` search may then be warranted.

**D — parent itself fails calibration.** The W/S/R schema cannot simultaneously reject XOR/uncoupled controls and accept delayed revival, or it becomes completion-dependent in a way that defeats the intended physical claim. The notion must then be abandoned or reformulated in a new round rather than patched after proof.

**E — prior dependence blocks an unqualified physical theorem.** A mathematically adequate parent exists, but whether the physical OI realization satisfies it or reaches P-indivisibility depends on `μ_H` in a way not fixed by the current physical principles. The canonical baseline may still give a conditional theorem, but the unconditional OI claim remains open.

These classes are not mutually exclusive with the prior-dependence qualification; the result must state both the bridge outcome and the prior scope.

## Non-doings

This preregistration does not:

- define a Lean predicate;
- add or edit any Lean file;
- edit the manuscript, book, README, census, bibliography, or release record;
- redefine manuscript C4;
- assert `CausalReadback -> C4e` or `C4r`;
- assert that the XOR or prior-dependence controls have any hidden mechanism beyond what the frozen calibration requires;
- apply Barandes;
- claim operational QM, phases, coherent controls, a unique Hamiltonian, or a unique dilation;
- claim that the canonical prior is the only physically allowed preparation;
- claim process-level uniqueness of the hidden realization.

Status: **preregistered; no proof or probe execution has begun.**
