# Observer-primitive reconciliation — result

Determination for `OBSERVER-PRIMITIVE-RECONCILIATION-AUDIT.md`, on branch
`observer-primitive-reconciliation` from `main` at
`44cb78080d48c786a27257271bff78cf99afd530`.

## Headline verdict

**Outcome B — split-layer reconciliation.**

The mathematics of #537 stands. Its corpus-level gloss does not stand without a scope qualifier.

The reduced `Substratum` layer formalized in `OIBridge/SubstratumInterfaceAudit.lean` carries the
site type, alphabet, finite-range rule, phase-space configuration type and the bijective update. It
carries neither an observer proper part, nor a visible/hidden product, nor a projection to visible
outcomes, nor a measure-selection field. On that reduced layer, #537's result is exact: A5 fixes the
zero configuration, any other configuration lies off that fixed orbit, and invariance alone leaves
more than one invariant probability law. The single-orbit route is therefore closed on every
nontrivial A5 substratum.

The maintained manuscript observation layer is richer. `papers/Main.md` §1.2 explicitly defines an
observation as `(S, φ, V)`, adopts the perspectival reading under which `V ⊊ S` is constitutive of
the observation primitive, states the visible/hidden phase-space decomposition, and uses the
visible projection `π_V` in its marginalization formula. The same section explicitly selects the
counting law by a maximal-entropy **selection principle**, while saying in the same breath that this
is not uniqueness from invariance alone. `OIBridge/CanonicalMeasure.lean` already mirrors that
status distinction: it proves invariance and maximality of counting and separately proves
`invariance_does_not_select`.

The realization/preparation layer is richer again. `papers/Main.md` states that a structured
realization may carry its own fixed hidden prior `μ_H` as realization data, and
`OIBridge/CausalReadback.lean` represents exactly that situation by `RootedRealization V H`, whose
`prior` is supplied data.

The three layers must therefore not be identified.

## T1 — primitive census

| Object | Reduced `Substratum` kernel | Maintained manuscript observation layer | Realization/preparation layer |
|---|---|---|---|
| total dynamics | represented by `Substratum.φ` | stated | supplied by the realization |
| observer proper part / visible cut | absent | **primitive under the adopted perspectival reading** | represented by a chosen `V × H` carrier |
| visible projection | absent | **stated with the visible/hidden phase-space decomposition** | `Prod.fst` in an exact product realization |
| global counting law | definable; invariant and maximal entropy are proved in `CanonicalMeasure` | **selected by the stated maximal-entropy principle** | may be used as the baseline law |
| preparation-specific hidden prior | absent | explicitly allowed as realization data | **supplied datum** (`RootedRealization.prior`) |

The manuscript's product phase-space decomposition is qualified on the maintained surface as an
idealization whose approximation quality is treated elsewhere. This result preserves that
qualification. A proper subset by itself is not being promoted into a product.

## T2 — map sufficiency

**Positive at the maintained manuscript layer; negative at the reduced substratum layer.**

`V ⊊ S` alone would not be enough: a named proper part is not a function from total configurations
to visible outcomes. The maintained manuscript states more than the subset relation, however. It
states the visible/hidden phase-space product and writes the marginal law with the projection
`π_V`. In the exact product realization used by `CausalReadback`, that map is the first projection.
Thus the maintained observation model supplies the observation map it uses.

Nothing in this verdict derives that map from A1–A5, and nothing adds it to `Substratum` by
implication. The formal substrate-to-observer bridge remains incomplete if the target is to have the
kernel itself represent every manuscript input.

## T3 — ensemble sufficiency

The four frozen claims separate as follows.

1. **Invariance alone selects a law — NO.** `invariance_does_not_select` and #537's fixed-point
   specialization remain binding. No result is weakened.
2. **Maximal entropy selects a canonical global law — YES AS AN ADOPTED SELECTION PRINCIPLE.** The
   maintained manuscript explicitly adopts counting as the baseline canonical law and explicitly
   says this is a selection principle, not uniqueness from invariance. `counting_invariant` and
   `counting_maximal_entropy` certify the mathematical properties of the selected law; they do not
   turn the principle into a consequence of invariance.
3. **That global law induces a common hidden prior in an exact finite product realization — YES,
   CONDITIONAL ON THAT EXACT PRODUCT MODEL.** Uniform counting on `V × H` assigns the same mass to
   every pair. Conditioning on any visible root therefore leaves the uniform law on `H`, independent
   of the root. This is elementary finite counting, not a new physical principle. The maintained
   manuscript separately labels the product decomposition as idealized, so the conclusion is not
   exported beyond that exact model without an approximation argument. No new Lean theorem is
   added in this determination because the result is not needed to repair #537's scope.
4. **An arbitrary structured preparation prior is thereby fixed — NO.** The maintained manuscript
   explicitly says a realization may carry its own fixed hidden prior `μ_H` as realization data.
   The canonical counting law is a default baseline, not a constraint on all representations or
   preparations.

The apparent conflict between #537 and Lemma 3 therefore dissolves: #537 proves that the default law
is not forced by invariance; Lemma 3 says the framework adopts an additional maximal-entropy
selection rule for the baseline law.

## T4 — scope of #537

The following are **correct on the reduced substratum layer** and remain mathematically exact:

- `EnsembleDetermined φ` fails for every nontrivial A5 substratum with a fixed zero configuration;
- the wave substratum has the same failure when its alphabet has more than one letter;
- transitivity/single-orbit determination is closed by the fixed point;
- read-write-family existence alone privileges no readout locus;
- no observation map is present in the `Substratum` record itself.

The following corpus-level paraphrases require qualification and must not be repeated unscoped:

- “the architecture states only `φ`”;
- “invariance is the only ensemble constraint the architecture states”;
- “the architecture determines neither `Obs` nor `μ`.”

The corrected form is:

> The **reduced A1–A5 substratum kernel audited by #537** carries `φ` but no observer projection or
> measure-selection field, and invariance alone does not determine an ensemble. The **maintained
> manuscript observation model** additionally states an observer cut/projection and adopts a
> maximal-entropy counting law as its baseline selection principle; preparation-specific hidden
> priors remain realization data.

No theorem statement from #537 needs retraction. The repair is a scope repair to comments, audit
summaries and transfer language.

## T5 — downstream consequence

A **baseline rooted observer family is available conditionally on the manuscript's own stated
inputs**: take the exact visible/hidden product model, its visible projection, the deterministic
bijective step, and the canonical counting selection. In the exact finite product case the induced
hidden prior is uniform and common to every visible root, so this data has the shape required by
`RootedRealization` and hence by `rootedMap`.

This is not a derivation of the observer interface from A1–A5. It is a reconciliation showing that
the maintained manuscript had already declared the extra inputs whose absence #537 correctly found
in the reduced kernel.

This positive baseline does **not** earn the stochastic-to-quantum correspondence audit by itself.
#538's `C4e => C4r => P-indivisibility` theorem remains a mathematical implication; the manuscript's
history-level C4 has not been proved there to imply either candidate at the readback window.

### Baseline control check — why immediate marginal revival is not the next target

There is an exact four-state full-counting control on `V = H = Z/2Z`:

> `φ(p,c) = (c, p XOR c)`, with visible coordinate `c` and the uniform hidden prior.

`φ` is a bijection. Under the canonical full counting law, conditioning on `X₀ = c` leaves `p`
uniform, and direct enumeration gives

- `Γ₁ = J/2`;
- `Γ₂ = J/2`;
- `Γ₃ = I`;
- `X₂ = X₀ XOR X₁`, so the order-two history gap is maximal.

Thus the manuscript baseline itself can have maximal history readback while the first two rooted
one-time maps are identical. Canonical counting therefore does **not** repair the failed implication
“history-level C4 at this window => immediate `C4e`/`C4r` at this window.” But finite recurrence
later returns the rooted map to the identity, producing the collision-then-separation pattern at the
recurrence scale.

This control is a determination calculation, not a new kernel theorem. It redirects the next audit
toward the manuscript's already-stated global readback route rather than toward strengthening #538's
window-local candidates after the fact.

## T6 — preserved results

Unchanged and still binding:

- `ensemble_underdetermined`, `waveSubstratum_ensemble_underdetermined`, and `phi_fixes_zero`;
- `invariance_does_not_select`, `counting_invariant`, `counting_maximal_entropy`;
- the #536 `NonnegBounded` sourcing ceiling and its fixed-gate/phase consequences;
- #538's `C4e => C4r => P-indivisibility` results and the absence of the manuscript-C4 window-local converse;
- #533–#535's exact/dense finite-QM operational benchmarks.

## What changes next

The next execution commit should be prose-only unless an independent kernel target is opened:

1. scope `OIBridge/StochasticInterface.lean` comments to the reduced substratum layer without
   changing definitions or theorem statements;
2. append a reconciliation cross-reference to the frozen #537 audit rather than rewriting its
   preregistered body;
3. qualify the #537 entry in `verification/README.md` and any generated census note that repeats
   “invariance is the only ensemble constraint the architecture states”;
4. update the session/frontier summary only after those repository surfaces are consistent.

A separate later round may formalize the baseline product-counting bridge if it becomes
load-bearing. It should not be added merely to make the reconciliation look stronger.

## Research frontier after the reconciliation

The observer-map question is no longer correctly phrased as “invent or source a map from A1–A5.”
The maintained framework already declares the map at its observation layer. Nor should the next
round try to force manuscript C4 into #538's window-local `C4e`/`C4r`: the four-state full-counting
control above shows why that implication is false at the readback window.

The next question is instead:

> Does the existing kernel already support the manuscript's global chain “history-level C4 implies
> some non-permutation rooted map; finite recurrence returns the rooted map to identity; stochastic
> inverse rigidity then yields P-indivisibility somewhere in the recurrence cycle” on the canonical
> baseline interface recovered here, without a preparation-specific prior?

The stochastic-inverse step is already kernelized in `EquivalenceChain.isPermMatrix_of_stochastic_inverse`.
The remaining audit is therefore specifically the C4-to-non-permutation step and its interface with
the recurrence statement, not a new stochastic-inverse proof and not an immediate-revival theorem.
The fixed nonclassical gate remains a separate empirical boundary.

Status: **Outcome B recorded. No prior theorem retracted; scope repair required.**
