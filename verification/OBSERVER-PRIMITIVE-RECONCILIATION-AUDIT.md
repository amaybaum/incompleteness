# The observer-primitive reconciliation audit — what #537 did and did not source

Owner-called from `main` at `44cb78080d48c786a27257271bff78cf99afd530`, the merge of the C4 causal-readback audit.
Preregistered here and committed alone before any result of this round is recorded.

## Why this round exists

`#537` proved a clean theorem about the reduced substratum kernel: under A5, the phase-space dynamics
has a fixed zero configuration, so invariance alone does not determine a unique ensemble on any
nontrivial configuration space. Its census also found no observation map selected by the structures
it froze. The post-#538 handoff therefore summarized the stochastic law as depending on
`(φ, Obs, μ)` while the architecture determines only `φ`.

A corpus check after that handoff exposes a scope question that must be settled before any new
observer principle is invented. The maintained manuscript surfaces state more structure than the
Lean `Substratum` record frozen by #537:

- `papers/Main.md` §1.2 defines an observation as `(S, φ, V)` and treats the proper observer part
  `V ⊊ S` as constitutive of the adopted perspectival primitive; its Lemma 2 states the visible/hidden
  phase-space decomposition and the corresponding projection used by marginalization.
- The same section's Lemma 3 states that the global counting measure is selected among invariant
  measures by a maximal-entropy **selection principle**, explicitly not by uniqueness from
  invariance alone; its realization remark separately permits a fixed preparation-specific hidden
  prior `μ_H` as realization data.
- `book/ch01-observation.md`, the maintained book surface, carries the same `(S, φ, V)` observation
  primitive, visible/hidden decomposition, and maximal-entropy selection language.
- `OIBridge/SubstratumInterfaceAudit.lean`, by contrast, defines `Substratum` from sites, alphabet,
  rule, configuration space and dynamics only. It carries no observer part, visible/hidden
  factorization, projection, or measure-selection field.
- `OIBridge/StochasticInterface.lean` tests `EnsembleDetermined φ` using invariance alone and says in
  its docstring that this is the only ensemble constraint the architecture states.
- `OIBridge/CausalReadback.lean` later introduces an explicit product realization `V × H` together
  with a fixed hidden prior, but that realization is supplied data and was not reported as sourced.

The question is therefore not whether #537's theorem is false. It is whether its *scope* was
correctly propagated from the reduced kernel to the maintained manuscript architecture.

## The question

> Relative to the maintained corpus, what exactly supplies the observer map and the ensemble, and
> which parts are primitive, selected, derived, or still free?

The round must distinguish three layers and may not collapse them:

1. **Reduced substratum layer.** The existing `Substratum` record and A1–A5/A3Family material frozen
   by #537.
2. **Manuscript observation layer.** The maintained `(S, φ, V)` primitive, its stated visible/hidden
   decomposition/projection, and the stated maximal-entropy selection principle.
3. **Realization/preparation layer.** A concrete finite `V × H` realization and any fixed hidden
   prior `μ_H` carried as preparation/realization data.

## Guard

No structure may move between these layers by rhetoric.

- A manuscript assumption is not reported as derived from A1–A5 merely because it is already stated.
- A Lean theorem about the reduced substratum is not promoted to a no-go for a richer manuscript
  primitive that it does not represent.
- A proper-part relation `V ⊊ S` is not silently treated as a product decomposition unless the
  manuscript surface actually states the needed factorization/projection, and any idealization or
  approximation qualification attached to that statement is retained.
- Maximal entropy may count as an adopted selection principle if the maintained corpus adopts it,
  but never as uniqueness from invariance. `invariance_does_not_select` remains binding.
- A global counting law is not automatically identified with an arbitrary preparation-specific
  hidden prior. The round must state exactly when a conditional/common hidden prior follows and when
  it is additional realization data.
- Nothing in this round is named C5. No quantum correspondence theorem is invoked. No fixed gate,
  phase resource or dense-control result is reinterpreted as sourced by this audit.

## Frozen source surfaces

The census is restricted to current `main` at `44cb780` and the following surfaces:

- `papers/Main.md`, especially §1.2–§1.4 and the remarks attached to Lemma 3;
- `book/ch01-observation.md` and the corresponding maintained substratum chapter where needed;
- `papers/Methodology.md` only for the foundation-counting/status language of `V ⊊ S`;
- `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`;
- `verification/lean-mathlib/OIBridge/StochasticInterface.lean`;
- `verification/lean-mathlib/OIBridge/CanonicalMeasure.lean`;
- `verification/lean-mathlib/OIBridge/CausalReadback.lean`;
- the #537 and #538 audit notes and the post-#538 handoff summaries.

No manuscript is edited during the determination phase. If the outcome requires wording repairs,
those repairs are a separate execution commit after the verdict is frozen.

## Tests

### T1 — primitive census

Record whether `(S, φ, V)` and the visible/hidden cut are actually maintained claims, and classify
`V`, the factorization/projection, and any approximation qualifier separately as **primitive**,
**derived**, **selected**, **realization datum**, or **absent**.

### T2 — map sufficiency

Determine whether the maintained observation layer supplies a genuine map from total configurations
to visible outcomes, rather than merely a named subset. The exact positive form must identify the
map/factorization that exists in the maintained corpus. A proper subset alone is insufficient.

### T3 — ensemble sufficiency

Separate four claims:

1. invariance alone selects a law;
2. maximal entropy selects a canonical global law;
3. that global law induces a common hidden prior in an exact product realization;
4. an arbitrary structured preparation prior is thereby fixed.

Each receives its own yes/no verdict. Claims (1) and (4) are expected to fail; claim (2) is expected
to be an adopted principle rather than a theorem from invariance; claim (3) is conditional on the
exact factorized finite realization and must be proved or left unclaimed.

### T4 — #537 scope

Audit every post-#537 sentence that says the architecture determines only `φ`, or determines neither
`Obs` nor `μ`. Classify each as correct for the reduced substratum layer, correct corpus-wide, or in
need of scope qualification. The Lean results themselves are not changed unless a theorem statement
actually overclaims its hypotheses.

### T5 — downstream consequence

State whether a baseline rooted observer family is already available **once the manuscript's own
observer cut and selection principle are taken as inputs**. If yes, say explicitly that this is a
conditional interface supplied by stated primitive/selection structure, not a derivation from
A1–A5. If no, name the exact missing datum.

### T6 — preservation

The following remain untouched regardless of outcome:

- `ensemble_underdetermined`, `waveSubstratum_ensemble_underdetermined`, and the fixed-point theorem;
- `invariance_does_not_select` and all `CanonicalMeasure` theorems;
- #536's `NonnegBounded` sourcing ceiling;
- #538's `C4e => C4r => P-indivisibility` results;
- all exact/dense QM operational benchmarks #533–#535.

### T7 — checks and surfaces

If Lean is added, it goes in a new reconciliation module or a narrowly named bridge module; no
existing definition is broadened in place. Every named result prints only the repository's accepted
axioms. The release gate and R7 guards must remain green. Any prose correction must distinguish
`reduced substratum` from `maintained manuscript observation primitive` literally enough to be
machine-guarded.

## Admissible outcomes

Exactly one headline outcome, with sub-verdicts for map and ensemble.

**Outcome A — #537 stands corpus-wide.** The maintained `(S, φ, V)` language does not actually
supply the required map and/or canonical baseline ensemble. The post-#538 handoff needs no scope
repair, and the exact missing structure is named.

**Outcome B — split-layer reconciliation.** The maintained manuscript already supplies some or all
of the observer interface through an explicit primitive and/or selection principle, while the
reduced A1–A5 substratum kernel does not. #537's mathematics stands but corpus-level summaries are
qualified. Any remaining preparation freedom is stated separately.

**Outcome C — stronger positive bridge.** The maintained observation primitive plus its stated
selection principle canonically determines the baseline rooted interface in a form that can be
represented in the kernel without adding a new physical principle. The bridge is implemented and
its dependence on the manuscript primitive/selection principle is explicit. This does not turn those
inputs into consequences of A1–A5.

## Prediction, recorded before the determination

Outcome B is expected, with a possible C-strength mathematical sub-result for the baseline finite
product case. The maintained manuscript plainly states more than the reduced `Substratum` record:
`V` is part of observation, the visible/hidden projection is used by the marginalization formula,
and maximal entropy is explicitly adopted as a selection principle. At the same time, the corpus
also says structured preparations may carry their own fixed hidden prior, and the product
factorization is qualified as idealized on at least one maintained surface. The likely correct
position is therefore neither “the architecture determines only φ” nor “the observer law is fully
unique”: the baseline interface is supplied at manuscript level by additional stated structure,
while the reduced kernel and preparation-general case retain real freedom.

The prediction is not a result.

## Non-doings

This round does not:

- invent an observer map or ensemble;
- infer a product decomposition from a subset without an explicit source;
- call maximal entropy a consequence of invariance;
- erase #537's fixed-point/no-uniqueness theorem;
- claim that a preparation-specific prior is fixed when only a baseline global law is selected;
- enter the stochastic-to-quantum correspondence audit;
- name or adopt C5;
- edit a manuscript before the determination is complete;
- alter the phase/fixed-gate sourcing verdict.

Status: preregistered; determination not yet recorded.
