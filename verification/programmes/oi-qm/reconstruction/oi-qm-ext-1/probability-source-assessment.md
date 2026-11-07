# Probability sourcing for the recent OI–QM interfaces

**WIP / UNVERIFIED — paper assessment; independent review pending, 2026-11-07.**

Accountable: #1059; feeds #1169. Guiding draft: #1173. Sole writer:
`writer_probability`, on
`research/oi-qm-probability-assessment-20261107`.
Drafting base: `235305e24b22633848f1b399efb77fbba5f8b4df`;
main source snapshot: `71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd`.

The owner's 2026-11-07 request authorizes a distinct paper assessment, derivations,
draft publication and independent review. The scope and writer are recorded in
[#1059](https://github.com/amaybaum/incompleteness/issues/1059#issuecomment-6704793000)
and the [three-thread authorization](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6704790395).
These links are authorization provenance, not scientific evidence.

## 1. Fixed selection and stopping contract

This assessment will inspect the existing probability contracts before proposing
any mechanism. Its selected objects are the already-used finite reversible
realization and rooted hidden-law construction, the accepted local component at
the drafting base, the earlier correlation-recombination screen, B2/B3's threshold
seed, and the abstract two-system candidate's calibrated source. Selection is by
their actual use in the current research, not by agreement with quantum answers.

Four questions remain separate:

1. What physically prepares a distribution of hidden states?
2. What theorem represents a supplied observable law in Born form?
3. What independently justified assumptions select the quadratic Born rule?
4. Does one preparation law work across admitted settings, complete observer
   histories, failures and reuse?

For each object the final assessment will state the carrier/dynamics, source law,
readiness conditioning, operational access and setting interface; identify which
claim is derived, assumed, unsourced or refuted within its stated hypotheses; and
give the first missing physical ingredient. Mathematical conditioning will not
be called a preparation procedure. Invariance and maximum-entropy selection will
not be identified with actual-orbit frequencies or physical loading. Fair finite
bits, continuum seeds and a calibrated Bell bias will not be interchanged.

**Stopping rule.** If the source review does not supply a preparation mechanism,
an independently justified selection principle, or a common-setting physical
interface, stop at that specific missing ingredient. Do not choose a distribution
because it fits the target, infer an automatic reset, or assemble incompatible
realizations into an equivalence claim. No new physical premise is adopted.

## 2. Preserved writer and decision boundaries

The existing `writer-born` retains #1082 and
`research/born-sel-b-measure-20261104` at
`e50917cab03a1c8db6fd668ecad2a04c880399db`. Its paused measure analysis, pending
post-acceptance review repairs, C-1 and files are untouched. This assessment neither
repairs nor accepts that work by implication.

The [owner's measure rulings](https://github.com/amaybaum/incompleteness/issues/1059#issuecomment-6650820790)
and [later pause](https://github.com/amaybaum/incompleteness/issues/1059#issuecomment-6654026901)
remain in force for that thread. OQ-14 API-field semantics, the CC-ORDER gating
decision and scope O1 are not decided here. C-1 is unfrozen and unrun.

No simulation, enumeration, implementation, Lean/scientific run, physical-premise
adoption, freeze, special workflow dispatch, merge or manuscript promotion is
authorized. Source reading, hand derivations and cheap static checks are the
verification modes of this unit. A different reviewer must examine the completed
assessment at an immutable pushed commit.

## 3. Sources and prior work

The §1 contract was pushed before this analysis. Sources were inspected at their
actual definitions and theorem statements. [M] below means content on the main
snapshot above; [R] means conditional research content, not an established
native physical resource.

| Source | Content used and scope |
| --- | --- |
| [Main §§1.2, 3.1–3.4, 4.5](https://github.com/amaybaum/incompleteness/blob/71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd/papers/Main.md) [M] | Counting selected by maximum entropy; structured fixed priors allowed as realization data; Born representation distinguished from exponent selection; posit (iv) is not derived |
| [CanonicalMeasure.lean](https://github.com/amaybaum/incompleteness/blob/71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd/verification/lean-mathlib/OIBridge/CanonicalMeasure.lean) [M] | orbit_invariant_unique, counting_invariant, counting_maximal_entropy, invariance_does_not_select; finite permutation and supplied-law hypotheses, no apparatus |
| [Equivalence.lean](https://github.com/amaybaum/incompleteness/blob/71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd/verification/lean-mathlib/OIBridge/Equivalence.lean) [M] | RevReal.init, RevReal.law, D_imp_Qfb, finite_horizon_equivalence; initial numerical weights are input data |
| [StochasticInterface.lean](https://github.com/amaybaum/incompleteness/blob/71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd/verification/lean-mathlib/OIBridge/StochasticInterface.lean) [M] | Ensemble uniqueness under transitivity and failure with disjoint invariant sets; does not override the richer realization layer |
| [Rooted-family sourcing audit, Q2–Q7](https://github.com/amaybaum/incompleteness/blob/71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd/verification/audits/operational/rooted-observer-family-sourcing/result.md) [M] | Declared observer projection, legitimate roots, fixed common hidden prior per realization and canonical counting baseline |
| [QB3 evidence](https://github.com/amaybaum/incompleteness/blob/71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd/verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/QB3-EVIDENCE.md) and [review](https://github.com/amaybaum/incompleteness/blob/71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd/verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/QB3-EVIDENCE-REVIEW.md) [M] | μ-form / μ-number classification and finite-bijection counterexamples; paper proofs, not kernel proofs; no extrapolation to native-wave statistics |
| [BSB at the preserved #1082 head](https://github.com/amaybaum/incompleteness/blob/e50917cab03a1c8db6fd668ecad2a04c880399db/verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/BORNSEL-B-MEASURE.md) [R] | Overlap check: N2, N5, N6 already distinguish invariance, relaxation, conditioning and rational weights. Its entire post-ACCEPT delta is not accepted here; the applications below use [M] or their own short arguments |
| [Physical interface §§4–5](https://github.com/amaybaum/incompleteness/blob/235305e24b22633848f1b399efb77fbba5f8b4df/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/physical-interface.md) [R] | Accepted local component: exact field rule, ready ensemble, controller-inclusive history and outgoing world; no physical factory or same-model B3 realization |
| [Recombination design](https://github.com/amaybaum/incompleteness/blob/235305e24b22633848f1b399efb77fbba5f8b4df/verification/programmes/oi-qm/reconstruction/correlation-recombination-20261107/DESIGN.md) and [source screen](https://github.com/amaybaum/incompleteness/blob/235305e24b22633848f1b399efb77fbba5f8b4df/verification/programmes/oi-qm/reconstruction/correlation-recombination-20261107/NO-SIGNALLING.md) [R] | Prepared parity laws; the accepted scoped screen does not construct physical choices or a complete apparatus, so gives no complete physical no-signalling verdict |
| [B2 §§1–4](https://github.com/amaybaum/incompleteness/blob/235305e24b22633848f1b399efb77fbba5f8b4df/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/measurement-source.md) and [B3 §§1–6](https://github.com/amaybaum/incompleteness/blob/235305e24b22633848f1b399efb77fbba5f8b4df/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/measurement-exchange.md) [R] | General seed law, fixed comparator and fresh-resource sequential law; conditional studies with source gaps retained |
| [Two-system interface §§2–4](https://github.com/amaybaum/incompleteness/blob/235305e24b22633848f1b399efb77fbba5f8b4df/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-system-interface.md) [R] | Its definition of calibrated source/herald. Author analysis with independent review pending; this assessment does not accept its separate reuse-failure analysis |
| [Thread 1 preparation/loading §§4–7](https://github.com/amaybaum/incompleteness/blob/acbcbd0fea30485b400d4802646145d8066ddd89/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/preparation-loading.md) [R] | One native tick transports a supplied common precursor law into the accepted ready law; it still does not construct the factory |
| [Gate A §§2–3](https://github.com/amaybaum/incompleteness/blob/235305e24b22633848f1b399efb77fbba5f8b4df/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md) [R] | One common loaded model, complete histories, fixed uncontrolled law, exact versus approximate endpoint; proposed contract, not a source theorem |

The QB3 evidence's standing limitation is preserved: **OI has not yet been shown
to derive the Born rule or select the physical probability measure.** This is
not a replacement review of the five-branch investigation or its native runs.
No Lean build or scientific program was run.

### 3.1 Primary literature checked before any new mechanism

| Source inspected | Applicable result or proposal | What OI would still have to supply |
| --- | --- | --- |
| E. T. Jaynes, *Information Theory and Statistical Mechanics*, Phys. Rev. 106, 620 (1957), [DOI](https://doi.org/10.1103/PhysRev.106.620), abstract | Maximum entropy assigns probabilities from specified partial knowledge as an inference principle | Physical state space, constraints and preparation records; agreement with the actual preparation/sampling process |
| F. Logiurato and A. Smerzi, *Born Rule and Noncontextual Probability*, [arXiv:1202.2728v2](https://arxiv.org/html/1202.2728v2), §II, Theorem 1 | Conditional Born derivation using Hilbert states/observables, noncontextual probabilities and further measurement assumptions; the stated theorem has dimension at least three | Physical contexts and probability assignments, including their noncontextual relation; no hidden-state factory follows |
| S. Aaronson, *Is Quantum Mechanics An Island In Theoryspace?*, [quant-ph/0401062v2](https://arxiv.org/pdf/quant-ph/0401062), §2 | Nontrivial linear norm-preserving amplitude transformations distinguish the 2-norm from other p-norms in that setting | Physical amplitude carrier, transformation family and probability interpretation; a permutation alone does not supply that family |
| L. Masanes, T. D. Galley and M. P. Müller, *The measurement postulates of quantum mechanics are operationally redundant*, [arXiv:1811.11060v2](https://arxiv.org/html/1811.11060v2), §§II.1–II.4, IV | Measurement theorem uses quantum pure-state/unitary/composite structure, specified outcome-function consistency including associative composition, and finite state estimation | Those structures on one physical realization; no native preparation distribution follows from a permutation alone |

These are assumption maps, not new proofs or unconditional endorsements of every
interpretation of these papers. Known Born-selection mathematics is reused.
No exponent/context premise is adopted; the O1 target remains undecided. Jaynes
provides an independent rationale for considering the existing counting default
as an epistemic assignment, not a dynamical factory. No new measure mechanism is
proposed after this review.

## 4. What already follows about the measure

### 4.1 Selected baseline, invariant law and physical source

For finite S and a supplied permutation Φ, CanonicalMeasure proves uniformity of
an invariant probability law supported on one cycle, invariance/maximal entropy
of counting on S, and nonuniqueness of invariant laws when disjoint nonempty
invariant sets exist. Thus **invariance alone selects the global weights** is
refuted under that last theorem's hypotheses. This is not a no-go for a physical
selection principle. Main already selects a counting default by a separate
maximum-entropy postulate and permits structured fixed hidden priors.

On a nonempty finite product V × H, canonical counting gives

    P(H=h | V=a)=1/|H|

at every visible root a. A declared realization with any other fixed hidden
prior instead supplies the already-defined family

    Γ_t(a,j)=Σ_h μ_H(h) 1[π_V Φ^t(a,h)=j].                   (1)

The same μ_H is used for every root. It would be inaccurate to say the maintained
corpus lacks an observer map or a common-prior family. The physical question is
which preparation is available and why that law describes it.

An invariant prior, its posterior conditional on a record, and empirical
frequencies along an actual orbit are different objects. Conditioning on a
time-dependent record need not preserve invariance. Finite recurrence does not
by itself identify finite-window frequencies with ensemble weights. The owner's
selected C-1 comparison addresses a particular frequency/representation
question; this unit does not answer, execute or revise it.

### 4.2 Born representation versus source selection

In D_imp_Qfb, the unitary is the supplied dynamics' permutation matrix and
init := R.init copies the initial law. Its deterministic step weights are zero
or one. Changing source weights can change the observable law while preserving
its Born representation; the landed QB3 swap/CE-8 examples demonstrate this on
generic finite bijections.

| Question | Strongest present support |
| --- | --- |
| Is a numerical physical preparation law derived? | Not supplied for the recent apparatus candidates by the sources inspected here |
| Does a supplied finite observable law have a fixed-basis Born representation? | Existing finite-horizon theorem |
| Is the quadratic rule physically selected for the full operation family? | Not supplied by that theorem or by selecting a detector seed; additional operational assumptions remain |
| Does one physical preparation work across settings, histories and composition? | Separate common-realization obligation; using one symbol μ does not prove it |

## 5. Probability contracts of the recent studies

### 5.1 Accepted ring component: common conditional fair-bit law

The finite state-dependent binary ring has 2L bits, L ≥ 9, with

    f_i(u)=u_(i-1) XOR (u_(i+1) OR u_(i+2)),
    F(u,v)=(f(u) XOR v,u).

Its ready assignment I_c(z,ξ) fixes eleven zero bits and the visible program c;
z is fair and ξ has a common independent product-counting law. Receiver R at
site 0 and controller C at site 1 each expose both time slices. At visible root

    a_c=((0,0),(c,0)),

eight hidden ready pins remain. For global counting ν_0 and ready event E_c,

    ν_0(E_c)=2^-12,
    ν_0(hidden readiness | a_c)=2^-8,
    Law(Z,Ξ | E_c)=Unif({0,1}) × ν.                          (2)

These are conditioning masses, not demonstrated herald success probabilities.
The two programs really share the hidden prior at this declared cut. This is a
non-Bell-calibrated mathematical source for the finite fair bit, conditional on
the selected baseline and ready event.

The already-derived complete observer history is

    R_0=(0,0),      C_0=(c,0),
    R_1=(c OR z,0), C_1=(z,c),
    R_2=((1 XOR c)z,c OR z), C_2=(c,z).                      (3)

The controller learns z for either program. Given C_1, the observer's posterior
on Z is a point mass, even though the input ensemble was fair. Receiver-only
masking does not hide Z from this whole observer.

F preserves ν_0 at every fixed tick. Unconditioned baseline evolution therefore
does not make E_c certain. A physical factory, request actuator, honest herald,
discarded attempts, logs, elapsed time and consumed resources are still needed.
This is a source gap, not impossibility of preparation with accounted resources.

The outgoing world is F²I_c(z,ξ), not a new sample. At tick 2 the controller's
previous coordinate is z: z=1 violates a ready-zero pin. For c=1 the receiver's
previous coordinate is 1, so that program never returns to the original ready
slice then. These are readiness statements, not physical failure rates.
No automatic reset or unlimited fresh-bit supply follows.

**Status:** common conditional prior and two-tick law **derived under the
supplied ensemble**; factory and reusable preparation policy **unsourced**.
They remain #866/#865/#1147 work, not a source of B3's continuum law.

### 5.2 Cubic recombination: different hidden laws at the same root

The earlier linear-wave realization is Φ(u,v)=(Au−v,u) on a cubic binary torus.
Its μ_b is counting conditioned on 86 zero pins and one parity constraint,
so ν_0(E_b)=2^-87, or 2^-85 after the common receiver root is fixed.
Its individually fair inputs satisfy u(s+) XOR u(s−)=b.

μ_0 and μ_1 have different hidden joint laws at that same visible root.
Equal individual marginals do not construct a common preparation switch. The
source screen's two registered records are deterministic functions of the
prepared parity. For parity weight p their law is (1−p)δ_h0+pδ_h1; the equality
criterion for two indexed laws is not a test of two physical Alice choices.

**Status:** recovery of a supplied classical correlation **derived**; native
preparation, selectable controls, full apparatus history and same-model B3
behavior **unsourced**. No physical no-signalling failure of native OI is
established. The ring's common-prior improvement does not supply this different
model's loader retrospectively.

### 5.3 B2/B3: source and detector response must be assessed together

B2/B3 use real modes represented by nonzero z ∈ C², the **posited** sensor

    t(z)=|z_1|²/(|z_1|²+|z_2|²),

and an atomless seed q ∈ (0,1) with common law μ. The comparator 1[q<t(z)]
gives

    p_1(θ)=F(cos²θ),  F(t)=μ((0,t)).                         (4)

B2 already proves that matching every θ ∈ [0,π/2] for this fixed response is
equivalent to F(t)=t. Its competing symmetric density 6q(1−q) gives
F(t)=3t²−2t³: endpoint and balanced calibrations agree, but at θ=π/3 the two
probabilities are 1/4 and 5/32. This is reused work, not a new selection theorem.

The seed never changes under those dynamics. Its marginal invariance cannot
select between these laws; calibration and port symmetry do not select one
either. A coordinate change can transfer a density into the response function.
The physical claim concerns their combined pushforward, not the word “uniform”
alone. The quadratic sensor also requires a source.

B3 exchanges the old carrier with a supplied ready reference. With two
independently prepared seed cells it derives

    P(b,1)=p_b(θ)F(t_b(φ)),
    P(b,0)=p_b(θ)[1−F(t_b(φ))],
    t_1(φ)=cos²φ, t_0(φ)=sin²φ.                             (5)

Uniform seeds give the fixed qubit instrument law at this scope. Equation (5)
uses independence of the second cell from the first-slot interaction; unchanged
marginal law does not license reuse of the old seed. The reference bank keeps
the old signal and is consumed. Additional measurements require fresh banks
or an accounted reset. Loader failures are not supplied by assuming readiness.

**Status:** (4)–(5) **derived conditional laws**; uniform physical seed,
quadratic sensor, exchange, ready references, access and fresh supply
**assumed/unsourced physical ingredients**. Fitting μ to (4) does not derive
the Born rule.

### 5.4 Abstract Bell source: keep its separate review boundary

The earlier two-system candidate stipulates fair R, independent C with
P(C=1)=η, and a setting-independent ready herald H with rate h. Its first-read
definition on H=1 gives

    P_η(a,b | x,y,H=1)=½ w_η(a XOR b XOR xy),
    w_η(1)=η, w_η(0)=1−η.

Its η_*=(1−1/√2)/2 is explicitly selected from the quantum comparator:
**assumed calibration**, not a native source. The stipulated herald retains
failure mass 1−h with outcomes ⊥; it does not construct a failure monitor.
The cross-wing interaction is another independent source assumption.

The same file reports a separate repeated-use failure with retained R,C.
Independent review is pending. This assessment neither accepts nor repairs
that analysis. Sourcing η_* alone would not cure or review a dynamics/access
failure, and that hypothetical candidate's failure would not refute all native
OI measures.

## 6. Finite source boundary and the actual preparation-law test

### 6.1 Exact rational weights from finite counting

This elementary consequence is restated for the recent consumers. It is not a
new Born theorem or a replacement review of #1082's Lemma U.

Let Λ be nonempty finite with uniform law, with all resources for a fixed finite
deterministic protocol π included in its initial configuration. Let G_π record
its complete output. For an output event B and nonempty source event A_π,

    P(G_π∈B)=|G_π^-1(B)|/|Λ|,
    P(G_π∈B | A_π)=|A_π∩G_π^-1(B)|/|A_π|.                 (6)

Proof: each initial state has weight 1/|Λ|; summing over the indicated fibres
gives the first identity, and division by P(A_π) gives the second. All resulting
weights are rational. The unconditional law retains the complement A_π^c.
Appending finitely many independent uniform finite resources leaves the same
conclusion. No exhaustive enumeration is involved.

Such a source can yield an exactly fair bit but not an atomless uniform variable
on (0,1), nor exact irrational weight η_* through finite deterministic readout
and positive conditioning. The latter follows from irrationality of 1/√2.
This is a restriction on **finite uniform resources at this interface**.
Existing representation theorems permit real-valued nonuniform priors as input;
they are not excluded by (6).

Approximation, a differently justified nonuniform law, an infinite source or a
compatible resource completion could change the hypotheses. Each needs its
own physical source account. None is adopted here. A finite approximation
does not establish Gate A's exact all-parameter endpoint. The ring's fair bit
cannot silently become B3's continuum seed or the Bell calibration.

### 6.2 Test the loader's weighted fibres, including failed attempts

For one actual native factory/request process, let λ have an independently
justified law μ fixed before the setting. Its deterministic map for request c
must retain at least

    L_c(λ)=(A_c,Z_c,M_c,W_c),

where A records real readiness/failure, Z the candidate input, M all accessible
preparer/controller records including attempts and timing, and W the remaining
world. Its joint law is

    P_c(A=a,Z=z,M=m,W∈D)
      = μ{λ:L_c(λ)∈{a}×{z}×{m}×D}.                         (7)

This is a test template, not a proposed native opcode. A physical L_c must be
constructed first. Finite uniform μ turns (7) into a fibre-count identity;
other laws give weighted fibres. Source weights and readiness events must be
justified before using quantum target probabilities.

One common μ is not enough: loading can correlate the request with uncontrolled
variables or select different accepted subensembles. For positive-probability
successful records,

    P_c(Z=z | A=1,M=m)
      =P_c(A=1,Z=z,M=m)/P_c(A=1,M=m).                       (8)

Equal total success rates across c do not force equality of the numerators
or accepted source laws. Required uncontrolled-state and shared-prefix
independence must hold on the actual loaded law and setting mechanism.
Future program choices cannot change an already shared experimental past.

Nor may “Z remains fair” be imposed after every record: accessible records can
reveal it, as C_1 does in (3). Its actual posterior must enter subsequent
predictions. A fresh-resource claim needs a physically prepared new resource
whose conditional independence is proved.

## 7. Outcome, compatibility and smallest next step

### 7.1 Strongest result and first stopping point

The strongest positive result is **realization-relative**: the counting
baseline conditioned on stated readiness yields the local component's common
fair-bit prior and complete two-tick law. Existing mathematics represents
that supplied law in Born form. It does not physically prepare the apparatus,
select B3's response–measure pair or derive the Bell source.

The first missing physical ingredient is a native factory/request process
with an accounted law of readiness, failures, full preparer/controller access,
residual state and consumed resources. The sources inspected here do not
supply it. Stop at this **physical preparation and source-law gap**, without
adding fitted weights or claiming a universal impossibility.

| Classification | Statement |
| --- | --- |
| **Derived, conditional** | Local common fair-bit prior/law from its supplied ensemble; existing Born representation; source-accounting identities (6)–(8) |
| **Assumed** | Canonical maximum-entropy assignment, structured ready states, B3's seed/response/reference resources, Bell weights and herald |
| **Unsourced here** | A native apparatus preparation law and compatible supply across the full operational interface |
| **Refuted at stated scope** | Invariance alone fixes global weights when disjoint invariant sets exist; finite uniform resources give exact η_*; B2 symmetry/calibration alone fixes its uniform seed |
| **Open, preserved** | #1082 delta review and C-1 decisions; physical exponent/context selection; separate two-system review; full equivalence |

### 7.2 Compatibility with the other threads

Thread 1 and this assessment can use the same binary ring, update, observer cut
and conditioned ensemble. At the cited Thread 1 head, one ordinary tick takes
a previous-slice request to the target controller and preserves the common
hidden law. Its precursor requires three hidden zeros and five hidden
correlations, again an event of mass 2^-8 conditional on its visible root.
The fair bit is Z=Y_2 XOR X_4 with a free independent Y_2. This transports the
supplied law; it does not create it. A physical preparer that reads both Y_2
and X_4 learns Z even earlier than C_1. Its acquired records must therefore
be included before combining the claims.

Thread 2 needs a sourced joint preparation and local operation family in one
model. Changing a setting-independent prior alone cannot remove the
screened-local Bell ceiling while its locality hypotheses remain. This unit
supplies no missing cross-system dynamics or quantum correlation bound.

Cubic linear recombination, the state-dependent binary ring, real B3 apparatus
and the abstract Bell construction have different carriers, operations, laws
and access contracts. They currently form an obligation map, not assembled
physical ingredients. A useful marginal cannot be imported while discarding
its readiness, history or fresh-resource conditions. In particular, a finite
local fair bit does not supply B3's continuous seed and independent banks.

### 7.3 One discriminating next proof

Thread 1 now identifies the exact precursor resource but stops before a native
factory. The next construction must physically produce that common precursor
and actuate its request; then prove **its complete preparation law** (7) for
both requests at #866/#1059. Use the same dynamics and baseline, retain failure mass and full
accessible preparation history, and check both the claimed successful ready
law and independence of the uncontrolled source through physical loading.
Derive the preparer's/controller's acquired information instead of redrawing Z.

A proposed process that only gives the inverse image of the ready event has
relocated the conditioning requirement, not met this physical source test.
If Thread 1 stops there, retain that precise gap and identify the independently
motivated resource needed for a factory. Do not fill it with a newly chosen
measure or a pending C-1 decision.

This is one existing joint obligation, not a duplicate issue or a new research
mechanism. It discriminates an available preparation from a conditional initial
state. Success would source one apparatus input; quantum measurement behavior,
Bell/composition and consistent reuse still need their own same-model proofs.

## 8. Verification and independent review

Author work used source inspection and hand algebra. Static checks cover the
one-file content, whitespace, balanced fences and accidental credential-like
material. No simulation, enumeration, implementation, build, special workflow,
freeze or merge was performed.

A different reviewer must check this paper at its immutable pushed head,
especially the source/realization distinction, finite-counting scope, controller
posterior, preserved earlier review statuses, literature assumptions and
separation from writer-born's paused scope.

Each [R] citation above supports only its stated conditional research claim in
this draft. Any landing would need its own §A.42 support audit and authorization.
This paper makes no enduring native-equivalence claim.
