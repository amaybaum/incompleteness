# The representation and sector necessity audit (post-Level III)

Level III established that the laws do not select a Hilbert-space representation or a
superselection sector: the quasilocal algebra, its state space and its OI-induced discrete
dynamics are fixed without either, and a sector choice enters as an input of the
initial-condition kind (`state_selection_audit` in `OIBridge/RegionTower.lean`; GR §3.3).

That leaves a narrower question, which is what this thread investigates:

> **Does any actual OI prediction require a distinguished representation or sector, beyond
> choosing a state?**

This is an audit, not a level. The first entry is an evidence round with no Lean development:
its purpose is to decide whether the question has a positive instance in the live corpus before
anything is constructed. The decision tree is fixed in advance. If no live claim requires a
distinguished sector, representation construction stands as optional mathematics, exactly as the
instrument thread left infinite-support availability. If one does, the entry names the exact
claim and the minimum additional sector- or state-selection principle it needs — and stops there,
because independence and necessity are separate tests that no round has run.

## The distinction the audit turns on

A **state** condition constrains which state on a fixed algebra obtains. A **sector** condition
constrains which representation of that algebra the theory is set in, and is not expressible as a
property of a state on the algebra alone. The two are routinely stated in the same vocabulary —
"vacuum", "KMS", "Fock" — and the standard QFT treatment of several of them is representation-level,
so the vocabulary does not settle the classification and each occurrence is read for what its
argument actually consumes.

Two occurrences are singled out for scrutiny in advance rather than assumed harmless: GR's
Bunch-Davies/α-vacuum and KMS material, because state sensitivity is not automatically sector
sensitivity and the question is whether those conditions can be stated as properties of states;
and Structure §10.4, because it explicitly builds a Fock space and a von Neumann algebra.

## Method

The live corpus (`papers/*.md`, `book/*.md` at this commit) was searched for GNS, Fock,
representation, superselection, vacuum, ground state, KMS, normal state, cyclic, irreducible,
spontaneous symmetry breaking, Bunch-Davies, unitarily inequivalent, and choice/distinguished/
preferred representation. Each load-bearing occurrence was classified. The countercheck is the
one the instrument census used: not "could this be restated without a sector?" but "does the
existing argument already run on state data?" — an occurrence counts as state-level only where
the corpus's own argument makes it so.

Raw counts mislead on two search terms and are reported here so the census can be re-run: a
case-insensitive search for `GNS` matches inside "assignments" and "designs" (23 apparent hits in
`papers/`, 3 real), and `representation` is dominated by finite point-group representation theory,
a different sense of the word (below).

## The census

| Class | Finding |
|---|---|
| **1. Ordinary state condition inside the existing state space** | GR §3's thermal conditions. H-balance is the ratio of detector transition rates `Γ↑(ω)/Γ↓(ω) = e^{−τ_K ω}` over "the finite frequency window the observer can probe", with an explicit finite-observer error budget; GR §3 states its own status in its heading — "**H-balance is a selection condition, not a representation theorem**". GR §3 Step 4's KMS condition is recorded by the corpus as state-dependent in the same place it is used: "whether the emergent state belongs to that KMS class is state-dependent, and which class it occupies is H-spectrum, which §2 records as underivable from S1–S4". The Explainer's Bell reference graph "in the uniform/vacuum class" is a class of preparations. Kernel-side, `state_selection_audit` records the admissible state space as convex, containing the reference family, with the reference state the unique normalized state invariant under the substratum's own bijective and phase interventions |
| **2. Finite-stage Hilbert language, no infinite representation choice** | Main §3.4's `S ⟺ D ⟺ Q_fb` is fixed-basis on finite carriers over a finite horizon. Substratum Lemma 24.1's GNS/Stinespring step runs on the cyclic subspace `C_B` reachable from the visible factor — a finite configuration space under the framework's effective finiteness, with any larger `C_H` decomposing as `C_B ⊕ C_D` and `C_D` decoupled at every order (the boundary-only dependence lemma). Structure §10.4's substratum-scale Hilbert space is `ℓ²(C_V)` on a finite region's configuration space. SM's spontaneous chiral symmetry breaking is diagnosed by **finite-volume scaling** — `Z_S` at small `m` growing eightfold between `L = 16` and `L = 32`, with the peak shifting — not by an infinite-volume limit with a vacuum choice |
| **3. Representation terminology used explanatorily or to state the negative** | The Level III scope sentences in GR §3.3, Main §3.4 and the Explainer, which *deny* selection: "no Hilbert-space representation and no superselection sector is selected at the level of the laws". Methodology's contrast with the QFT situation makes the same point in the other direction: with infinitely many degrees of freedom "the choice of representation is a substantive interpretive problem", whereas "the framework's setting is finite" and the analogue of "which representation" becomes "which representative within the equivalence class", answered by the gauge classification conditional on Lemma 24.1. GR §7's "vacuum sector" is the Ricci-flat solution set of classical general relativity, an unrelated sense |
| **4. Genuinely load-bearing distinguished representation or sector** | **None found.** No live claim consumes a representation or sector as such. The nearest thing is a **state**-class principle, which the audit question excludes and which the corpus has already named and priced — see below |
| **5. Genuinely ambiguous** | Two items, recorded rather than resolved: the algebraic status of H-state's "vacuum class", and Structure §10.4's algebra-channel pair. Both below |

A search artifact, not a class: most of the 285 `representation` hits in `papers/` are
finite-group representation theory — the cubic point group `O ≅ S₄`, its irreducible
representations, and the six-link decomposition `6 = 3 ⊕ 2 ⊕ 1` from which the gauge group is
read. These are finite-dimensional representations of a finite group, not representations of an
operator algebra, and bear on the question only by sharing a word.

## The four candidates, adjudicated

**GR's α-vacua and KMS — state, and finitely checkable.** In the standard treatment de Sitter
α-vacua are unitarily inequivalent, so this is where a sector requirement would show up if one
existed. GR's argument does not use the inequivalence. What it uses is the reverse/forward
detector ratio

> `R_α(ω) = e^{−2πω/H} ((1 + r e^{πω/H}) / (1 + r e^{−πω/H}))²`,  `r = e^α`,

and its zero-frequency slope, to establish that the infrared limit does not remove state
dependence. Every quantity consumed is an expectation value over the finite frequency window the
observer can probe. Two states in different α-classes are separated by their values on finitely
many observables, which is state data. The same holds for the KMS condition of Step 4, whose
class-membership the corpus itself marks state-dependent and refers to H-spectrum.

**Structure §10.4's Fock space and von Neumann algebra — a real construction, no live claim on
it.** The construction is genuine and representation-dependent: `ℓ²(C_V)` resolves at long
wavelength to the Fock space `H_V^OI`, and `A_V^OI` is defined by a bicommutant taken on that
space. Its role, stated by the corpus, is Step 1 of a four-step \*-isomorphism recipe whose Steps
2–4 are open and deferred; §11.3 lists "Same algebra-channel class: **Open**". The framework's
predictions are attributed elsewhere: §10.2 places Cabibbo, Koide and the rest with the
reconstruction theorem, and §12.5's no-GUT prediction rests on cubic-commutant decomposition,
coupling running and the fermion determinant. No prediction currently depends on the pair.

**SM's spontaneous symmetry breaking — group content plus a finite-volume diagnostic.** The
structural claim of SM §4.11 is representation content in the gauge-theoretic sense: chiral
symmetry forbids explicit masses, and the minimal scalar breaking to `U(1)_em` is
`H = (1, 2, +½)`. The supporting numerics are finite-volume scaling. What is state-level in the
neighbourhood is named as such by SM itself — the effective operator is octahedral-invariant only
if the condensate is, an order-parameter condition, and SM records it as a dependency.

**SM's θ-vacuum structure — a parameter, and already open.** The mapping table pairs T-invariance
of the wave equation with "`θ ∈ {0,π}` in QCD; `θ̄` not fixed", and gives the trace-out's role as
"Narrows parameter value; H-top, H-det open". The claim is that a substratum symmetry narrows a parameter of the
emergent effective action, with the bridge conditions unproved and strong CP recorded as open. No
sector is selected, and no closed claim rests on the passage.

## Where the burden actually sits

The audit's one substantive positive finding is not a sector requirement. GR §3 already records
that ℏ and the `1/4` coefficient are conditional on **H-state** — "the emergent cutoff-scale modes
lie in the freely falling adiabatic/de Sitter vacuum class" — and gives the reason it cannot be
discharged: Main's realization theorem admits different fixed hidden priors `μ_H` over the same
`(φ, partition)`, so vacuum-like and excited laws are both realizable, and the canonical uniform
invariant measure is an equilibrium/typicality principle rather than an energy-minimization one.
The corpus's own conclusion is stated there: "**An additional state principle is therefore
logically necessary.**"

That is a selection principle of exactly the kind the audit question sets aside — it selects a
state, not a representation — and it is already named, already priced as not derivable, and
already carried as a condition on the two claims that depend on it. This audit adds no new burden
and discharges none.

## The two ambiguous items

**The algebraic status of H-state's "vacuum class".** The corpus calls H-state a state principle
and derives its necessity from a freedom in the hidden prior, which is state freedom. But
"adiabatic/de Sitter vacuum class" is stated in the standard QFT vocabulary, where the notion is
usually presented representation-side, and the corpus does not restate it as a property of a state
on an algebra. The expectation is that it is state-side — an adiabatic or Hadamard condition is a
condition on a two-point function — but the audit records this as unresolved rather than asserting
the reformulation it did not carry out.

**The scope of "the quasilocal algebra" in this question.** GR's thermal conditions constrain
states of the *emergent* QFT. Level III's quasilocal algebra is the lattice object built from the
substratum's finite-region matrix algebras. The corpus does not construct a map between the two,
and this audit does not assume one. So the finding that GR's conditions are state-type and
finitely checkable is a statement about the emergent theory's states; whether those conditions
transport to states on `OI_Q`'s quasilocal algebra is a separate question that no round has asked.

## The finding

> No live OI prediction requires a distinguished representation or superselection sector. The
> conditions that carry real weight are conditions on states, and where a state-selection burden
> exists it is already named as H-state and already carried as a stated condition on the claims
> that depend on it.

**Status of this finding.** It is a survey of the corpus at this commit, not a theorem, and shares
the standing of the instrument census: it can be invalidated by a future claim and should be
re-run if one is added that consumes a representation or sector as such. Level III's negative —
that the laws select neither — *is* a theorem, and is not restated here.

**Consequence for the thread.** By the decision tree fixed above, representation construction —
GNS representations of the quasilocal algebra, sector theory, an algebraic account of the emergent
Fock description — stands as optional mathematics outside the core programme, in the position the
instrument thread left infinite-support availability and Level III left continuous time. The two
ambiguous items are the places to look first if that judgement is revisited.

## What is not claimed

That OI *forbids* a distinguished sector; this is an audit of what the corpus requires, not an
impossibility result. That H-state is discharged, weakened, or shown unnecessary — it stands
exactly as GR states it. That H-state is uniquely determined, or that no other state principle
would serve. That the emergent QFT's states and `OI_Q`'s quasilocal states have been connected.
That Structure's algebra-channel comparison would remain prediction-free if its open steps were
completed. That the census is exhaustive of any corpus but this one.

## Status after the first entry

| Question | Status |
|---|---|
| R1. Does a live prediction require a distinguished representation or sector | **answered negatively for the current corpus** (this entry) |
| R2. Are GR's thermal conditions statable as properties of states | **yes for the emergent theory**: they consume expectation values over a finite frequency window. Transport to `OI_Q`'s quasilocal states is a separate open question |
| R3. Is H-state's "vacuum class" a state condition algebraically | **open**, recorded as ambiguous. Expected state-side; the corpus does not carry out the reformulation |
| R4. Does Structure §10.4's algebra-channel pair carry a prediction | **no live claim depends on it**; Steps 2–4 of its recipe are open in the corpus |
| R5. Is representation construction required work | **no**, on the current corpus: optional mathematics outside the core programme |
