# SUBSTATE-1: consequences for OI ⇔ QM and the d = 3 carrier

**Status: research-only dependency review.** No change to an OI premise,
manuscript, or physics claim is authorized by this note. Inputs checked:
Main §3.4, SM §2.7 and §4.1; the existing Lean modules
`OIBridge.Equivalence`, `OIBridge.RecurrenceHorizon`,
`OIBridge.RootedRecurrenceBridge`, `OIBridge.GeneralCarrier`,
`OIBridge.DimensionalObstruction`, and the SUBSTATE-1 proof note.
The physics conclusions below are a dependency analysis, not a new theorem.

## 1. Separate three claims that the word "equivalence" can hide

| Claim | Prior evidence | SUBSTATE-1 contribution | What remains |
|---|---|---|---|
| Finite-horizon `S ⇔ D ⇔ Q_fb` | Existing construction, Lean `Equivalence.finite_horizon_equivalence` | None needed: every **finite visible law** already has a finite reversible representative regardless of whether an *actual* hidden physical carrier is infinite | Cross-horizon and operational compatibility |
| Recurrence-cycle rooted P-indivisibility | `RecurrenceHorizon` has the **abstract** overlap + identity-return result; `RootedRecurrenceBridge` obtains the return from the finite microscopic permutation | Weakens one *sufficient* route to obtaining `Γ_L=I`: a finite visible factor can return even if the hidden state does not | A general measure-induced conditional-law bridge from `π∘T^L=π` a.e. to `Γ_L=I`; actual observability/readback |
| Exact full operational QM | `GeneralCarrier.exactAll_iff_physical_general` classifies finite endomorphic instrument availability given **five operational conditions**, including inert spectators, full reversible control and iterated composition; its OI-alone countermodels are separate | An infinite hidden carrier may sidestep the **fixed finite classical-dimension** obstruction in principle; neither continuum cardinality nor recurrence supplies the five conditions | Construct **one** coherent family of preparations, instruments, composites and Bell-relevant responses from the SAME physical dynamics, rather than inserting them as a separate availability premise |

The obstruction at Main:554 is fixed-*finite*-carrier. Moving to an
infinite carrier removes the applicability of that theorem, **not** the
underlying scientific challenge. A bare infinite carrier has no reason
to deliver quantum preparations or composite operations. Conversely,
for every finite experiment the already-proved `S → D` construction
produces a finite surrogate, so representability alone is not a payoff.

A concrete countercontrol: `X = (R/Z) × {0,1}` with identity dynamics,
visible readout the second factor and Haar × uniform prior has infinitely
many hidden states and `Γ_L=I` for every `L`. It has neither a
non-permutation intermediate step nor a native quantum instrument menu.
Continuum cardinality plus visible recurrence is insufficient.

## 2. What can be machine-checked, and the next theorem to close

Already present in the repository:
- `OIBridge.RecurrenceHorizon.pIndivisible_of_identity_return_of_overlap`
  is a **carrier-independent** matrix-family theorem and previously
  Lean checked; it asks for one stochastic intermediate rooted matrix
  with overlap and a later exact identity.
- `OIBridge.EquivalenceChain.isPermMatrix_of_stochastic_inverse`
  proves the non-permutation formulation at the matrix level.
- `OIBridge.GeneralCarrier.general_characterization` is a conditional
  characterization of finite operational QM, not a derivation of its
  conditions from bare OI.

This draft adds `OIBridge.ObservableFactorRecurrence` with a
carrier-arbitrary change-event identity and an abstract finite-visible
stochastic-inverse obstruction. The file is imported by the bridge root
for the automatic GitHub Lean/Mathlib build. **Do not mark it
kernel-verified until CI explicitly succeeds on its exact head.**

The **important remaining formal gap** is not another stochastic
inverse proof. It is the measurable factor theorem: under a probability
measure, finite positive-mass visible cells, and a measurable
measure-preserving bijection `T`, define
`Γ_n(a,b) = μ({π=a} ∩ {π∘T^n=b})/μ({π=a})`.
Then prove `Γ_L=I ⇔ μ({π∘T^L ≠ π})=0`.
The paper proof is elementary, but it has **not** been mechanized here.
A next Lean unit should prove the measure bridge separately with
null-cell handling and the ratio well-defined, then instantiate the
already machine-checked matrix no-go. Do not fake this by assuming
`Γ_L=I` as a field of a purportedly physical realization.

The free-wave all-`L` Fourier proof is another **paper proof**
pending separate Lean verification; the finite-range exact matrix
regression is not a replacement for it.

## 3. The d = 3 question splits into two distinct levels

**Microscopic rule:** SM §4.1, lines 224–240, gives the form
`x(t+1)=α Σ_neighbors x(t)−x(t−1)` under its stated
center-freedom/isotropy/linearity assumptions. It does **not**
derive `α = 1/3` for the finite microscopic bijection. In
particular, SM explicitly says the normalized real/complex
wave operator is an *observer-level lift*. The missing map
`φ → L_obs → Δ_g` is acknowledged in SM §4.1.

**Observer-level rule:** the stable isotropic harmonic branch
uses `α = 1/d = 1/3`. Multiplication by `1/3` is not an
endomorphism of the circle `R/Z` (choosing representatives
changes it), so a direct torus-valued microscopic-style
update with this coefficient is ill-defined. **This does
not refute or obstruct the observer-level operator on real
vector spaces**; the physical lift is not asserted to be a
circle-group endomorphism.

A mathematical compact carrier on which `1/3` is an
automorphism **does exist**: the 3-solenoid, the Pontryagin
dual of the discrete group `Z[1/3]`, equivalently the
inverse limit of circle maps `z ↦ z³`. Multiplication by
3 on `Z[1/3]` is invertible, hence multiplication by 3
and its inverse on the compact dual are continuous group
automorphisms and preserve Haar. A finite product of
these groups therefore supports the normalized linear
nearest-neighbor update as a reversible group automorphism:
`(u,v) ↦ (A u−v,u)` with inverse
`(w,u) ↦ (u,A u−w)` for any endomorphism `A`.
This is a **carrier-existence candidate**, not an
OI-derived projected operator, gauge interaction or
physical realization.

The 3-solenoid is connected: any **continuous group homomorphism**
from it into a nontrivial finite discrete alphabet has only the
trivial image. Hence a useful finite visible readout on this
carrier must be a (typically non-homomorphic) **measurable
partition**, such as thresholding a circle coordinate, rather than
a finite-group quotient analogous to `Z_p → Z/p^kZ`.
This makes its recurrence and information-carrying properties
nonautomatic and is another required control, not an objection
to measurable observation.

Sources for the mathematical vocabulary: Gopal & Imam,
*Periodic points of solenoidal automorphisms in terms
of inverse limits*, Applied General Topology 22 (2021),
https://polipapers.upv.es/index.php/AGT/article/view/14589 ;
for solenoids as duals of rational subgroups and inverse
limits see the same article and standard Pontryagin duality.

**Independent controls to decide the next experiment:**

1. Compare the microscopic `d=3` finite bijection *actually*
   specified by the OI branch, its measure and readout, with
   any alternative carrier. Do not silently substitute the
   observer-level normalized wave operator for `φ`.
2. For a p-adic candidate with `p≠3`, reduction modulo
   `p^k` commutes with linear dynamics; check whether any
   required observational dependence remains after that
   quotient. This route preserves visible periodicity but
   by itself cannot produce the desired independent payoff.
3. For a solenoid candidate, specify a **finite measurable
   partition**, calculate the induced rooted joint
   probabilities from Haar, and test recurrence and
   sensitivity to deep coordinates. Do not infer them
   from group cardinality or compactness.
4. Only then test a pinned **gauge-coupled** update and
   independently distinguish Wilson plaquette action
   from the covariant alternatives in #1003
   (`S_1=Σw` versus `S_2=Σw²`).
5. To count as progress on full QM, demonstrate *more*
   than an unconstrained continuum representation:
   one physical dynamical construction must supply
   at least one of the independent operational controls
   missing from bare OI (not simply assume an instrument
   menu). Bell behavior still requires testing the setting,
   locality and no-signaling hypotheses of Main §3.3/H-Bell:
   a hidden continuum alone changes none of Bell's premises.
   Keep the `S ⇔ D ⇔ Q_fb` theorem unchanged.

**Status:** Research direction OPEN; no supported native
gauge-action selection, readback extension, or full
operational quantum equivalence yet.
