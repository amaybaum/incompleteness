# Rooted observer-family sourcing audit — result

Determination for `ROOTED-OBSERVER-FAMILY-SOURCING-AUDIT.md`, executed on branch
`rooted-observer-family-sourcing` from clean `main` at
`44cb78080d48c786a27257271bff78cf99afd530`.

## Headline verdict

**Outcome B — the maintained observer-realization layer sources a realization-relative rooted family and a canonical/default common-prior baseline, but it does not uniquely force the same rooted family across all allowed preparations.**

This is stronger than #538's S-B sourcing gloss and narrower than the abandoned #539 reconciliation branch. No #537 or #538 theorem is retracted. The correction is one of **layer and quantifier**:

- bare/reduced `Substratum` does not determine a unique invariant law on all of `Conf`;
- the maintained manuscript's observer-realization layer contains additional stated structure: the observer cut, the visible/hidden factorization used for the finite realization, a selected counting/maximal-entropy default, and realization-specific fixed hidden priors;
- once a realization and its fixed `μ_H` are declared, the rooted family is defined without any verdict-driven choice;
- different permitted `μ_H` generally yield different visible laws, so the architecture does not select one universal rooted family across all preparations.

No new Lean theorem was needed: the only potentially ambiguous point — whether the prior used by #538 is common across the roots — is stated directly at the realization layer and the canonical baseline factorization is elementary.

## Q1 — visible/hidden split

**Sourced at the maintained observer layer.**

`papers/Main.md` §1.2 defines an observation as the triple `(S, φ, V)` with `V ⊊ S` and explicitly defines the hidden sector as the complement `H = S \ V`. The proper-part decomposition is described as constitutive of the adopted perspectival primitive, not as an arbitrary observer map chosen later.

The same section then writes the phase-space/product decomposition

`Γ = Γ_V × Γ_H`

and the visible/hidden Hamiltonian split. The manuscript calls the product decomposition idealized and points to its approximation discussion, so the product form is a realization-level model structure rather than a theorem that every microscopic description literally factors in that way.

**Classification:** observer cut primitive/constitutive; finite product factorization the declared realization model used downstream.

This is precisely the structure absent from the reduced `OIBridge.Substratum` record used by #537. The absence there cannot be promoted into corpus-wide absence.

## Q2 — visible root preparation

**Sourced at the finite realization layer.**

The Stinespring/trace-out construction in Main §3.2 takes an arbitrary visible input `ρ_V` together with one fixed hidden state and evolves the product. On the classical fixed basis, choosing `ρ_V` to be the point preparation at visible value `a` gives exactly the rooted preparation required here.

The already-kernelized #538 realization makes the same convention explicit: for a root `a`, draw the hidden state from the fixed prior, evolve `(a,h)`, then project to the visible carrier. That kernel object was previously treated as only a conditional mathematical layer because #537 was read as a corpus-wide sourcing no-go. The manuscript evidence above shows the preparation form itself is already part of the maintained realization architecture.

**Classification:** visible root is a legitimate preparation variable, not an extra statistical-mechanics principle.

## Q3 — hidden preparation law

The audit had to keep three notions separate. The corpus does.

### (i) Canonical/default law

Main Lemma 3 selects the finite counting measure among invariant laws by maximal entropy. `OIBridge.CanonicalMeasure` formalizes all four relevant clauses separately:

- `counting_invariant`;
- `counting_maximal_entropy`;
- orbit-level uniqueness;
- `invariance_does_not_select` as the guard against turning the selection principle into global uniqueness from invariance.

Main then states in the measure-as-realization-datum remark that this canonical measure supplies the framework's **baseline transition matrices and physical realization**.

### (ii) Structured preparation law

The same remark immediately says that the default does not preclude structured preparations: a §3.4 realization **carries its own fixed hidden prior `μ_H` as part of the realization datum**, and the emergent law is a function of

`(φ, partition, μ_H)`.

It explicitly notes that the same bijection and partition under different priors generally yield different visible laws.

### (iii) Unique invariant global ensemble

Not supplied, and not needed here. #537's `ensemble_underdetermined` remains binding for the reduced substratum under its hypotheses; `CanonicalMeasure.invariance_does_not_select` remains binding in general.

**Classification:** a canonical selected default exists; structured `μ_H` is allowed as realization/preparation data; unique global invariance does not select among them.

## Q4 — common-prior condition

**Yes, per declared realization.**

The manuscript says a realization carries **its own fixed hidden prior `μ_H`**, singular, and makes the visible law depend on `(φ, partition, μ_H)`. It does not specify a family `μ_H(·|a)` indexed by the visible root. The #538 kernel's `RootedRealization` faithfully spells out that reading with the field

`prior : H → ℝ`

and documents it as “the fixed hidden prior, shared by every root.” Its `rootedMap` then uses that same `prior h` for every row `a`.

### Canonical baseline calculation

At the exact finite product realization, let the selected counting law be uniform on `V × H`. For nonempty finite carriers,

`P(V=a,H=h) = 1/(|V||H|)`

and

`P(V=a) = |H|/(|V||H|) = 1/|V|`.

Therefore

`P(H=h | V=a) = 1/|H|`

for every `a` and `h`. Conditioning the canonical counting law on any visible root thus produces the **same uniform hidden prior for every root**. This is exactly the common-prior baseline used in Main §3.2, where the hidden state is `ρ_H = I_m/m`.

This earns a canonical/default rooted family. It does **not** imply that every structured preparation uses the uniform prior; Main explicitly allows other fixed `μ_H`.

**Classification:** common prior sourced per realization; canonical common uniform baseline selected by the default measure; value of the prior not universally fixed across all preparations.

## Q5 — reversible evolution

**Available as a stated realization premise, not derived purely from observation.**

Main Lemma 3 and its status remark are explicit: the bijective substratum is the reversible representative used by the reconstruction, motivated partly by observed near-unitarity; reversibility is a representation choice/physical premise in the finite realization, not a theorem from the two observation axioms alone.

On that declared layer, the total update is a bijection. Main §3.2 uses a bijection on `C_V × C_H`; #538's `RootedRealization.step` is correspondingly an equivalence `V × H ≃ V × H`.

**Classification:** stated realization datum / reconstruction premise, not newly sourced by this round and not newly derived.

## Q6 — visible readout

**Sourced at the observer-realization layer.**

The observer is the declared proper subsystem `V`; the hidden sector is its complement. The observable law is obtained by marginalizing over `H`. In the finite product realization this is the canonical first projection from `V × H` to `V`; in the Hilbert-space description Main writes the corresponding partial trace over `H`.

#538's `rootedMap` uses exactly this projection, taking the first component after `t` reversible steps.

The correct scope statement is therefore:

- there is no observation-map field in the reduced `Substratum` record audited by #537;
- there **is** a declared observer projection at the maintained physical realization layer.

Both statements are true. The earlier corpus-wide gloss that the architecture determines only `φ` collapsed these layers.

## Q7 — assembled rooted family

**Yes, realization-relative, with a canonical/default baseline.**

For any declared finite realization with fixed prior `μ_H`, the maintained data define

`Γ_t(a,j) = Σ_h μ_H(h) · 1[π_V(φ^t(a,h)) = j]`

or equivalently

`Γ_t(a,j) = P(X_t=j | X_0=a)`.

This is exactly the already-kernelized `CausalReadback.rootedMap`, and `rootedMap_isRowStochastic` proves every such map is row-stochastic once the fixed realization datum is supplied.

The canonical counting/maximal-entropy baseline gives one non-tuned instance with uniform `μ_H`, common to all roots. Structured realizations give other rooted families by supplying another fixed `μ_H`.

The strongest earned statement is therefore:

> **C1–C4 observer realization + its declared fixed hidden prior `μ_H` defines a rooted stochastic observer family; the selected counting measure supplies a canonical common-prior baseline. The bare substratum does not uniquely determine which permitted preparation prior, and hence which rooted family, is physically realized.**

That is Outcome B, not A: the family is genuinely sourced **as realization data**, but not uniquely forced across all realizations/preparations.

## Exact relation to #537

No theorem changes.

`ensemble_underdetermined` proves that A5 plus a nontrivial configuration space prevents `EnsembleDetermined φ`, where `EnsembleDetermined` means exactly one invariant probability law on the whole state space. That result survives untouched.

What does not survive as a corpus-wide statement is the old explanatory gloss that invariance is the only ensemble structure the architecture states or that the architecture has no observer map beyond `φ`. Those claims are accurate only for the **reduced `Substratum`/A1–A5 layer frozen by #537**. The maintained observer-realization layer separately states a visible cut/projection and a measure-selection/preparation structure.

This result therefore subsumes the mathematical insight of the closed unmerged #539 branch without inheriting its damaged publication-record edits.

## Exact relation to #538

The #538 mathematics is unchanged:

`C4e -> C4r -> PIndivisibleWithin`

on a rooted family, with the history-level manuscript C4 separated from those one-time marginal predicates.

The sourcing verdict is revised at the correct layer. #538 called the family only conditionally available because it inherited #537 as a corpus-wide interface no-go. The present audit establishes that the fixed visible/hidden realization with one common prior is not an invented repair: it is already the data model of the maintained finite realization, and its canonical uniform-prior instance is already selected as the baseline.

This does **not** mean manuscript C4 implies C4e or C4r. That remains false/unproved exactly as #538 reports.

## No new Lean required

A new theorem was considered but is unnecessary for this sourcing determination.

- Common-prior usage is already formalized by `CausalReadback.RootedRealization.prior` and `rootedMap`.
- Row stochasticity is already proved by `rootedMap_isRowStochastic`.
- Canonical-measure selection and non-uniqueness from invariance are already formalized in `CanonicalMeasure`.
- The only new arithmetic observation — uniform counting on a finite product conditions to the same uniform hidden marginal for every visible root — is elementary and follows immediately from cardinalities; no competing sourcing outcome turns on a difficult formal lemma.

A later consolidation round may kernelize that conditioning identity if it becomes load-bearing in a manuscript theorem, but it is not needed to decide this audit.

## Next frontier — causal readback, now properly staged

The rooted observer family is no longer the upstream blocker. The next round should define a neutral **realization-level** physical parent condition expressing

> visible information is written into hidden memory and later observably read back,

on a structure rich enough to see both full visible histories and rooted one-time marginals.

Then test independently:

`CausalReadback -> C4w`

and

`CausalReadback -> C4e -> C4r -> P-indivisibility`.

The two children live at different observational levels and must remain separate. This round makes no prediction that both implications will succeed.

Only after that physical readback condition is sourced should the rooted first-order family be mapped across the exact Barandes boundary. Even then, #540's phase/gauge/dilation result remains binding: mathematical unitary/Born representability does not by itself source the physical coherent-control repertoire.

## Preserved boundaries

This result does not:

- retract #537 or #538;
- claim a unique invariant ensemble;
- claim that every preparation uses the counting prior;
- claim that the bare reduced `Substratum` record carries the observer cut;
- redefine manuscript C4;
- prove `CausalReadback -> C4w`, `C4e`, or `C4r`;
- apply Barandes;
- identify Barandes indivisibility with the OI P-divisibility predicate;
- source phases, coherent controls, Hamiltonians, instruments, or full operational QM;
- edit any manuscript or existing Lean file.

Status: **Outcome B recorded. The rooted observer family is sourced at the maintained realization layer, with a canonical common-prior baseline and preparation-relative alternatives; the next research target is the realization-level causal-readback parent condition.**