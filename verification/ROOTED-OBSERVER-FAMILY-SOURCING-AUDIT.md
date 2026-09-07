# Rooted observer-family sourcing audit

Owner-called after the Barandes boundary audit, from clean `main` at `44cb78080d48c786a27257271bff78cf99afd530`.

This file is the preregistration only. It freezes the sourcing question before execution. No Lean theorem, manuscript text, bibliography, census status, or Barandes application is changed in this commit.

## Why this round exists

The primary-source Barandes boundary audit found that a uniquely selected invariant global ensemble is not a prerequisite for the stochastic-to-quantum representation route. #537 therefore remains a correct theorem about `EnsembleDetermined`, but it tested a stronger canonical-statistical-mechanics object than the correspondence requires.

The next object actually needed is the rooted first-order observer family

`Γ_t(a,j) = P(X_t = j | X_0 = a)`

induced by an intended finite observer realization. This round asks whether the maintained C1–C4 physical architecture already supplies the realization-level data needed to define that family.

## Frozen target datum

Audit exactly these five ingredients:

1. a visible/hidden split;
2. a visible root or preparation `a`;
3. one common hidden preparation prior `μ_H`, used for all visible roots unless the source explicitly says otherwise;
4. reversible microscopic evolution;
5. visible readout/projection.

No stronger global ensemble condition is introduced.

## Scope

The source of truth for this round is the maintained original C1–C4 physical realization across the manuscript/book and its already-maintained verification mirrors. Bare `OIBridge.Substratum` is not silently promoted to the whole corpus-level observer architecture; conversely, explanatory prose is not silently promoted to a kernel theorem.

The round may inspect the existing canonical-measure and observer-interface Lean only to classify already-formalized statements. It will add no Lean initially unless a narrow theorem is needed to distinguish two otherwise ambiguous sourcing outcomes.

No Barandes theorem is applied in this round. Matching the rooted family to the *type* of first-order transition data audited in #540 is allowed; claiming quantum representation from it is not.

## Frozen questions

### Q1 — visible/hidden split

Where exactly does the maintained corpus state the observer cut / visible-hidden decomposition? Is it part of the observer primitive `(S, φ, V)`, a derived decomposition, a realization choice, or merely explanatory prose?

### Q2 — visible root preparation

Does the architecture license a preparation in which the visible initial value is fixed to `a` while hidden data are sampled independently according to a declared law? Record the exact conditioning/preparation language.

### Q3 — hidden preparation law

Distinguish three claims that must not be conflated:

- the finite counting / maximal-entropy canonical default;
- a realization-specific or preparation-specific hidden prior `μ_H`;
- a uniquely invariant global law on the whole configuration space.

For the first two, ask whether the corpus supplies one common hidden law across all roots `a`. For the third, preserve #537's negative result and do not make it a requirement.

### Q4 — common-prior condition

#538's rooted-family realization uses one fixed `μ_H` common to every visible root. Does the maintained physical realization actually state this, or only root-dependent conditionals `μ_H(·|a)`? If the canonical full counting law is invoked, verify whether conditioning on the visible root yields the same hidden marginal for every root in the declared product realization.

### Q5 — reversible evolution

Is the relevant total update deterministic and reversible/bijective on the finite realization used for the observer law? Record whether this is a primitive C-condition, realization datum, or derived theorem.

### Q6 — visible readout

Is there a canonical projection/readout from total state to the visible sector at the intended realization layer? Distinguish the manuscript observer projection from the reduced `Substratum` record audited in #537.

### Q7 — assembled rooted family

Once the preceding pieces are classified, does the maintained architecture define

`Γ_t(a,j) = P(X_t=j | X_0=a)`

without a verdict-driven choice? State the strongest earned form: canonical baseline, realization-relative family, uniquely forced family, or still-unsourced family.

## Required countercontrols

1. **No return to `EnsembleDetermined`.** A unique invariant global law is not demanded merely because #537 studied it.
2. **No hidden-prior choice by desired verdict.** A `μ_H` may be used only if the maintained corpus states/selects it or if it is explicitly marked as realization/preparation data.
3. **Selection is not uniqueness from invariance.** The maximal-entropy/counting selection principle and `CanonicalMeasure.invariance_does_not_select` must remain simultaneously true if both are present.
4. **Common is stronger than available.** The existence of root-dependent hidden conditionals does not establish the single common prior used in #538.
5. **Baseline is weaker than universal physical preparation.** If conditioning the canonical counting law produces a common uniform hidden prior, that earns a canonical/default rooted family, not a claim that every allowed preparation uses it.
6. **History and marginal levels remain separate.** This round does not define or repair C4 and does not infer `C4w`, `C4e`, `C4r`, or P-indivisibility.
7. **No Barandes application.** Even a fully sourced rooted family does not in this round imply unitary/Born physics or an operational quantum repertoire.

## Admissible headline outcomes

Exactly one headline outcome, with separate answers Q1–Q7.

**A — fully sourced and fixed at the observer-realization level.** The maintained C1–C4 physical realization supplies all five ingredients, including one common hidden preparation law, with no additional realization/preparation datum left free.

**B — sourced realization-relative family, with a canonical/default baseline.** The observer architecture supplies the visible/hidden split, preparation form, reversible evolution and readout; it also supplies a canonical counting/max-entropy baseline that induces a common hidden prior, while permitting realization/preparation-specific `μ_H`. Thus a rooted family is genuinely available and every declared realization with fixed `μ_H` defines one, but the architecture does not uniquely force the same family across all preparations.

**C — partial sourcing only.** The structural observer data are present, but the common hidden prior remains an independent datum with no canonical/default construction sufficient to instantiate #538's rooted family.

**D — no rooted-family sourcing.** One or more structural ingredients required even to define the family are absent from the intended C1–C4 realization.

## Prediction recorded before execution

Outcome **B** is the working prediction. The maintained manuscript appears to distinguish a canonical counting/maximal-entropy default from structured preparations carrying their own fixed `μ_H`. The round must verify the common-prior conditioning and the exact status of each datum before that prediction can become a result.

## Consequence discipline

If B is earned, the correct next statement is not “#537 was wrong” and not “OI uniquely predicts one stochastic observer law.” It is:

> the original observer-realization layer already supplies a legitimate rooted stochastic family, with a canonical/default baseline and with preparation-relative alternatives; #537's reduced-layer invariant-ensemble no-go does not block that construction.

Only after this sourcing round is closed should a separate realization-level `CausalReadback` audit attempt the two children independently:

- history-conditioned memory (`C4w`-type content);
- marginal collision/revival (`C4e -> C4r -> P-indivisibility`).

## Non-doings

This round does not:

- edit the manuscript;
- redefine C4;
- apply Barandes;
- infer phases, coherent controls, Hamiltonians, instruments, or quantum operational equivalence;
- retract any theorem from #537 or #538;
- claim a unique invariant ensemble;
- claim a common prior unless it is sourced or explicitly selected by the maintained realization.

Status: **preregistered; sourcing execution not yet recorded.**