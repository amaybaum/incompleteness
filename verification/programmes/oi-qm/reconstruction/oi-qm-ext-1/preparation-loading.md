# Physical preparation and selectable loading of the accepted local component

Accountable #866; coordinates with #865 and #1147; feeds #1169.
Guiding draft #1173. Sole author: writer_preparation.
Paper-only investigation; no simulation, implementation or premise adoption.

## 1. Selection and stopping contract

[Owner scope](https://github.com/amaybaum/incompleteness/issues/866#issuecomment-6704791244).
Starting component: [physical-interface.md](physical-interface.md) at
`235305e24b22633848f1b399efb77fbba5f8b4df`, blob
`3229ef3cd234e613a4b0cb63bab548e0fec666a9`.
Current source snapshot:
`71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd`.
This contract is published before the new derivation. The preceding component
and its source gaps are known inputs, not blinded observations.

Select one native preparation/loading proposal: use the delayed-slice channel
of the component's existing second-order ring dynamics to load a visible
request and an incoming signal during one additional forward tick. Its
motivation is the explicit old-local-field term of the preexisting physical
rule, rather than a desired Bell table or a new gate. Determine the complete
precursor source needed for that proposal before calling it a preparer.

1. Keep the same binary ring, update, observer cut and target ready contract.
   Derive the actual precursor-to-ready map and check whether both request
   values use one uncontrolled source law independent of the request.
2. Distinguish an inverse image or conditioned law from an available
   preparation. Track the origin of the request, source, ready correlations,
   clock, preparer, failures and all accessible preparation records.
3. Derive the full declared observer history, including acquired controller
   information and remaining state. If an additional apparatus is proposed,
   include its access and discarded information; do not assume it resets.
4. Keep all unselected mass. A mathematical condition is not a herald, and its
   measure is not an apparatus success probability.
5. Stop at the first unsupplied physical ingredient. If native evolution only
   relocates the readiness resource, name its precise input requirement and
   state what would distinguish a real construction from that relocation.
6. Preserve the accepted local response, the absence of a supplied same-model
   B3 realization, and the screened-local Bell ceiling. Neither successful
   loading nor improved readout would establish the quantum composite route.
7. Report derived, assumed, unsourced and refuted claims separately. Do not
   substitute another source model or resolve an owner decision by assumption.

This branch writes only this file. Existing studies and their separate review
statuses remain unchanged. A different reviewer will inspect a pushed immutable
checkpoint. No simulation, enumeration, scientific execution, implementation,
freeze, dispatch, merge or manuscript claim promotion is authorized.

## 2. Source and literature review before the proposal

The accepted component supplies the exact binary specialization of SM §3.1's
state-dependent ring example. Its finite two-slice rule is the only dynamics
selected here; SM's broader graph regularity, continuum and isotropy claims
are not premises. The example is a stated physical branch, not a law uniquely
forced by bare OI or experimentally selected for a laboratory.

Main's measure-as-realization-datum remark and the rooted-observer audit
Q2–Q7 supply positive architecture: a visible preparation root, a fixed hidden
prior shared across roots, and the observer projection are legitimate
realization data. Counting is the selected baseline and structured priors are
allowed. None of that is denied by asking for an embedded device that produces
this particular structured preparation through the selected ring rule.

Main §3.4's action-labelled dilation realizes supplied laws and action writes.
It is not a compiler of those writes to this ring. The #865 drive-source plan
likewise distinguishes a mathematical operation family from its physical
supply. #1147 owns general native readiness; this bounded #866 paper does not
resolve that obligation or activate a general ready-state implementation.

The retained Native A actuation, setting-feasibility and later-controller
records distinguish a symbolic inverse coordinate or a potential causal path
from a supplied actuator. They use a different three-bit local rule and source
law. Their gates, readiness, computational results and review status are not
imported as premises for the present binary ring.

Two primary literature controls sharpen the preparation accounting:

- C. H. Bennett, [Logical Reversibility of Computation](https://www.cs.princeton.edu/courses/archive/fall06/cos576/papers/bennett73.html),
  IBM Journal of Research and Development 17 (1973), 525–532:
  reversible computation can retain inputs and intermediate information;
  restoring workspace requires an accounted construction. Its Turing-machine
  construction supplies no compiler or physical controller for this ring.
- R. Landauer, [Irreversibility and Heat Generation in the Computing Process](https://doi.org/10.1147/rd.53.0183),
  IBM Journal of Research and Development 5 (1961), 183–191:
  preparation and resetting cannot be excluded from the physical accounting.
  The ring presently has no Hamiltonian, temperature or bath model, so this
  paper will use finite support/information accounting, not claim a heat cost.

Source pins at the current main snapshot:

| Source | Blob | Role |
| --- | --- | --- |
| papers/SM.md §3.1 | `de1466b0c004339d60f1490e494e8f5037020948` | Existing second-order state-dependent rule |
| papers/Main.md §§1.2, 3.3, 3.4 | `a954cfb47c740766b8ca6ab9027a46bbf6fa2f94` | Prior/root architecture, Bell ceiling and dilation scope |
| verification/audits/operational/rooted-observer-family-sourcing/result.md | `34ea388d0fd47afe07bc9b41c79fe074898d493a` | Realization-relative positive source findings Q2–Q7 |
| verification/programmes/substratum/continuous-substates/native-actuation-boundary.md | `dd78320afd2e70a33136c0fefcf2a1929764afdc` | Context: inverse coordinates versus physical actuation |
| verification/programmes/substratum/continuous-substates/native-setting-source-feasibility.md | `5c0c84e1a35a7bc63c326dec3b9c3acb08859678` | Context: independent labels do not implement a private write |
| verification/programmes/substratum/continuous-substates/native-later-operand-and-controller.md | `de08b209a38ebd3bcc6222d48d1d724f5ce6921b` | Context: causal contact versus selectable physical instrument |

The #865 planning source is
`verification/programmes/oi-qm/reconstruction/research-planning/physical-drive-source.md`
at `9fc5ec2e26a7445851bbd4524da3a83ddda62a04`, blob
`94162a4398a3f64b84a6d16ce7ca6852e54081b2`; it records scope, not a proved
physical drive. Issue/PR links record accountability and review provenance;
they do not provide the mathematical premises.

## 3. The unchanged model and the target preparation

All indices are modulo a ring of L>=9 sites. A full state contains two binary
fields. Keep the exact rule of the accepted component:

    f_i(u) = u_(i-1) XOR (u_(i+1) OR u_(i+2)),
    F(u,v) = (f(u) XOR v, u),
    F^-1(a,b) = (b, a XOR f(b)).                         (1)

The inverse is a mathematical identity. The proposed physical evolution
below uses F forward only; no observer-operated inverse is assumed.

Let A=u_0 and B=u_(-1). The accepted target I_c(z,xi) has

    A_1=c, A_2=z,
    A_i=0 for i in K={-2,-1,0,3,4,5},
    B_i=0 for i in J={-1,0,1,2,3}.                       (2)

Its free coordinates are independent fair bits, including Z=A_2; Xi denotes
the other free coordinates. This is the previously supplied structured
preparation law, not a newly derived physical distribution. The observer
sees the complete two-slice coordinates at sites 0 and 1:

    R_t=(u_t(0),u_(t-1)(0)),
    C_t=(u_t(1),u_(t-1)(1)),  O_t=(R_t,C_t).             (3)

The target visible root is a_c=((0,0),(c,0)). Its hidden prior is the same
for both c. There are eleven ready-zero pins and one specified program bit:
four constraints fix a_c; eight further constraints concern hidden fields.

## 4. A native one-tick loading proposal and its exact boundary

Write the precursor at t=-1 as W_(-1)=(X,Y)=(u_(-1),u_(-2)).
The natural delayed-slice proposal is to place the request in Y_1 and let
one ordinary F tick load it into A_1. This uses the rule's existing old-local
term; it introduces no request-dependent update rule.

First find the complete source that makes this proposal reproduce (2).
By (1), the unique precursor of I_c is

    J_c(z,xi) = (B, A XOR f(B)).                        (4)

Equation (4) alone is only an inverse image. The following explicit
description identifies what a physical source would have to supply.

### 4.1 One common precursor law

Set the visible precursor root to

    b_c=((0,0),(0,c)),
    equivalently X_0=X_1=Y_0=0, Y_1=c.                 (5)

Relative to that root, require these eight hidden constraints:

    X_(-1)=X_2=X_3=0,                                  (6a)
    Y_(-2)=X_(-3),  Y_(-1)=X_(-2),                     (6b)
    Y_3=X_4 OR X_5,
    Y_4=X_5 OR X_6,
    Y_5=X_4 XOR (X_6 OR X_7).                          (6c)

Draw every remaining X coordinate as a fair independent bit; draw every
remaining Y coordinate as a fair independent bit, independently of those X
coordinates. In particular Y_2 is free. Set

    Z=Y_2 XOR X_4.                                    (7)

The five Y relations in (6b–c) determine distinct Y coordinates. Indices on
their right may coincide modulo L for small allowed L; none of the counting
or independence arguments requires those right-side indices to be distinct.

This is a fixed hidden law eta shared by b_0 and b_1. Only the visible
coordinate Y_1 changes with c. The free source bits and all eight hidden
requirements are independent of the selected request. No probability is
chosen as a function of c or of a quantum measurement angle.

**Forward derivation.** Since X_(-1)=X_0=X_1=X_2=X_3=0,

    f_0(X)=0,        f_1(X)=0,       f_2(X)=X_4,
    f_(-2)(X)=X_(-3),               f_(-1)(X)=X_(-2),
    f_3(X)=X_4 OR X_5,
    f_4(X)=X_5 OR X_6,
    f_5(X)=X_4 XOR (X_6 OR X_7).

Thus A=f(X) XOR Y has A_0=0, A_1=c, A_2=Z and every other
required zero in K. Its previous field B=X has the five zeros in J.
For fixed X, each remaining unpinned A_i is a different independent fair
Y_i translated by the fixed bit f_i(X). The translations preserve their
product-counting law and independence from X. Equation (7) has the same
property. Therefore the full forward law is exactly the law of I_c(Z,Xi),
including all unobserved coordinates, rather than just the desired receiver
marginal.

In particular, the two precursor laws are genuinely common-prior rooted
preparations. Changing only Y_1 from c to 1 XOR c changes only A_1 after
this tick; B and every other A coordinate remain identical pointwise.
That is a conditional native transport identity. A physical operation that
creates or changes Y_1 is not supplied by contrasting two input states.

The three zero fields and five relations in (6) are an explicit specification
of the incoming apparatus/source resource. They are not the construction
of a device that prepares it. Computing (4) on paper does not implement
the inverse, install the correlations or authorize writes to hidden fields.

### 4.2 Canonical-source countercontrol

At the same precursor root b_c, let U_c have the uniform hidden prior,
without (6). Then the loaded controller value is

    A_1=c XOR (X_2 OR X_3).                            (8)

Under U_c, it equals the requested c with probability 1/4, and equals
1 XOR c with probability 3/4. These numbers follow directly from two
independent fair bits, not an enumeration or an experimental run.
For example, X_2=1 is a precise failed-input witness regardless of X_3.
Merely declaring the same visible request therefore does not guarantee
the requested loading in the canonical source.

The event (6) has probability

    U_c[(6)] = (1/2)^3 (1/2)^5 = 2^-8.                (9)

The first factor fixes the three X values. Conditional on all X, each of the
five distinct unconstrained Y coordinates must equal one specified value,
so the second factor holds even when right-side X coordinates coincide.
Conditioning U_c on (6) gives exactly the common source eta above.

Equivalently, under uniform counting on the full 2L-bit ring, the joint
event (5)–(6) has mass 2^-12, equal to the target's twelve-constraint mass.
These are conditional ensemble masses. No physical herald, trial,
acceptance rate or observed loading-error rate has been constructed.

## 5. Complete observer and outgoing-state accounting

For the proposal's supplied source, the accepted component now follows
one native loading tick. Its complete declared projection history is

| Tick | Receiver R_t | Controller C_t |
| --- | --- | --- |
| -1 | (0,0) | (0,c) |
| 0 | (0,0) | (c,0) |
| 1 | (c OR z,0) | (z,c) |
| 2 | ((1 XOR c)z,c OR z) | (c,z) |

The first row follows from (5). The t=0 row is the forward result above.
For the next two rows, direct substitution into the same F gives

    u_1(-1)=c, u_1(0)=c OR z, u_1(1)=z,
    u_1(2)=c, u_1(3)=z,
    u_2(0)=c XOR (z OR c)=(1 XOR c)z,
    u_2(1)=(c OR z) XOR (c OR z) XOR c=c.

Let H'_c(z) denote the four-row history. With nu the original law of Xi,
the full law of history and outgoing ring is

    Law(H', W_2 | supplied request c and source eta)
      = (1/2) sum_(z=0,1) integral
          delta_(H'_c(z), F^2(I_c(z,xi))) d nu(xi).     (10)

This is also F^3_# of the precursor ensemble with its projection history
retained. Every field, free source bit and correlation remains in the
outgoing state. There is no bath replacement or independent fresh output.

The declared controller learns Z at t=1 for both settings. For c=1 the
receiver-only history is constant, but the full observer's history is not.
This remains a local apparatus fact, not a two-wing signalling experiment.

The actual physical preparer is presently unsupplied. If a future preparer
reads both X_4 and Y_2, it already knows Z by (7) before the interaction;
if its records are accessible, that information belongs in the observer's
history. Merely calling the source uncontrolled does not hide those records.
Conversely (6) does not logically require reading Y_2: the source specification
leaves it free. Whether a particular native factory acquires Z depends on
its actual implementation and complete records. It cannot be settled by the
two-site projection alone.

Similarly, (10) is the full world law for this declared ring, not a law for
an omitted external preparation apparatus. Adding a preparer, request
generator, clock or readout hardware requires their state in the joint lift
and their accessible logs in H'. The native t labels specify timing
mathematically; a controllable physical start, clock and permanent log are
not supplied by using them.

## 6. Resources, failed preparations and reuse

### 6.1 Readiness has been transported, not generated

At fixed root b_c there are 2^(2L-4) canonical hidden states. The acceptable
precursors in (6) number 2^(2L-12). The latter ensemble has eight fewer
bits of Shannon entropy than U_c; equivalently its relative entropy to
U_c is eight bits. This follows because it is the uniform conditional law
on a fraction 2^-8 of U_c's support.

There is no entropy production in this calculation: F is a permutation
and preserves the total entropy of each supplied ensemble. It changes
eight ready pins at the target into three pins and five correlations at
the preceding cut. It does not create their ordering from the uniform
source. The global counting law is invariant under every fixed number
of F ticks. Simply waiting from that unconditioned law leaves the target
event's probability at 2^-12.

These support counts also identify the scoped reset obstruction. An
injective transformation on this closed ring cannot map all
2^(2L-4) states of U_c into the 2^(2L-12)-state target support.
A real preparation may use a different initial source, an ordered
ancilla/reservoir whose state changes, a physically supplied herald with
rejected runs, or a compatible enlarged apparatus. Those are possibilities
to account for, not prohibited by this count. Adaptive stopping requires
its stopping rule, clock, records and entire failure law; it is not covered
by the fixed-time invariance argument.

For a reversible reset of an otherwise unrestricted k-bit register to a
fixed value, any auxiliary output that retains the lost alternatives must
distinguish 2^k inputs if no other output does. This elementary injectivity
requirement explains the relevance of retaining preparer/environment state;
it is not a proof that this ring realizes such a reset. Neither an energy
cost nor a universal eight-bit cost for every different preparation protocol
is inferred from (9).

### 6.2 No missing runs or automatic success flag

Define Psi(W) to contain the projections at W,F(W),F^2(W),F^3(W) and the
entire final F^3(W), starting at t=-1. For p=2^-8 the canonical-root source
has the exact decomposition

    Psi_# U_c
      = p Psi_# U_c(. | (6))
        + (1-p) Psi_# U_c(. | not (6)).                  (11)

The first term is (10). The complement is retained. There is no instruction
to discard it, and (6) is not a supplied accessible success flag. All
trajectories evolve for the same three ticks; failures are failures of the
desired input contract, not undefined native dynamics.

For the explicitly supplied eta, the algebraic loading meets (2) on its
whole support. That conditional certainty cannot be called demonstrated
reliability of an unsupplied physical factory. The factory's attempts,
timing, errors, logs, state changes and consumed resources remain unknown.

### 6.3 Outgoing state and the next use

W_2 in (10) is a legal input for another F tick. It is not the original
ready slice or a certified boundary for another desired instrument:

- If z=1, the controller's previous field at t=2 is 1, violating (2).
- If c=1, the receiver's previous field at t=2 is 1 for either z,
  also violating (2).
- The precursor root (5) is not automatically recovered either: for c=1
  the controller's current field is 1; for c=0,z=1 the receiver pair is
  (1,1). No general readiness conclusion is drawn for the remaining branch.

These are exact set-membership results on the supplied source, not
probabilities of a physical reset failure. A subsequent instrument could
accept a different outgoing contract; there is no demand that every useful
instrument return to (2). Such an interface, or a reset/fresh bank including
its resource state, still needs construction. One retained previous slice
does not implement indefinite readable memory.

## 7. Findings and compatibility conditions

| Category | Result |
| --- | --- |
| Derived from the fixed rule and supplied source | One native tick loads an already supplied request and produces exactly the accepted full preparation law. Both settings have the same precursor hidden law. The full controller history and outgoing ring are (10). |
| Derived source boundary | The exact precursor requires (6); under the canonical rooted source its mass is 2^-8. The inverse-prefix construction only transports that readiness resource. |
| Assumed for the conditional proposal | The state-dependent binary ring is the selected physical example; the structured source eta, visible request root and projection are supplied realization data. Fairness of free bits remains a source premise. |
| Unsourced physical ingredients | A native producer of (5)–(6); selectable request creation with unchanged uncontrolled source; any preparer logs, clock, herald/read hardware, resource renewal and compatible next instrument. |
| Refuted only at the stated scope | Supplying b_c while leaving its hidden sector uniformly unprepared does not guarantee the requested load. Fixed-time unconditioned evolution of counting does not make the ready event certain. The shown output does not automatically recover the original readiness contract. |
| Not inferred | No general OI preparation impossibility, physical no-signalling verdict, quantum measurement or native B3 realization. No full equivalence or new physical principle follows. |

The **first physical stop** is an accounted native producer of the complete
precursor contract (5)–(6), rather than an inverse-image prescription.
Its two distinguishable tasks are an available ready/correlated source eta
and a selectable public request Y_1 with that source held fixed.
If eta is supplied, (1) already derives the following one-tick loading
step. Supplying eta is not a new theorem of this paper.

The following requirements make integration with other threads explicit:

| Interface | Fixed here | Requirement before combining results |
| --- | --- | --- |
| Carrier/dynamics | Binary two-slice ring, L>=9, unchanged F | Any composite or probability mechanism must use this same realized dynamics or supply an explicit justified bridge; Native A, the linear wave, B3 and the abstract Bell toy are not interchangeable |
| Source/readiness | eta in (5)–(7), equivalent after F to the accepted target law | #1059 must assess an actual preparation law including correlations, full output and failure fibres; invariance or Born-form rewriting alone does not supply eta |
| Settings | c in the visible previous-slice request Y_1, transported by F | A real selectable operation/request generator with one common uncontrolled law; #865's continuous/off-axis drive is not proved by this finite-bit transport |
| Access/timing | Sites 0 and 1 on both slices, t=-1 through 2; controller gains Z | Include any preparer/request/read apparatus and logs; no private access or physical clock is inferred |
| Failures/resources | All mass in (11), eight hidden constraints relative to b_c | Account for any ordered source, entropy-bearing output, success flag, failures and renewal; #1147/#1032 readiness/retention obligations remain |
| Continuation | Full F^2(I_c) output, no automatic reset | Supply a compatible next stage or an accounted reset/fresh bank; joint histories must retain the controller's known Z |
| Composition/Bell | Local component only; bounded dependency envelope unchanged | #868 must supply the distinct physical composite mechanism and full-history/quantum-bound proof; preparation/readout improvements do not remove Main §3.3's screened-local CHSH<=2 ceiling |

The accepted single-site coupling is preserved by exact full-law recovery.
B3 is not a passed same-model control: this proposal supplies no map to its
real carrier, quadratic detector or record-conditioned exchange. F2's
existing conditional assembly is reused at its stated resource scope, not
reproved or promoted. The earlier accepted screens and the abstract
two-system study retain their separate review statuses.

## 8. Smallest discriminating next construction and review

The next preparation construction should target (6) explicitly. Specify one
finite native preparer, its independently motivated initial resource law and
an available request register; derive a finite forward F evolution that
produces the required source while retaining all preparer output and logs.
The decisive check is the joint output law for both requests: readiness,
Z, complete accessible preparation records, failures and remaining state.
A choice of an initial law solely because its pushforward equals (2) would
repeat the inverse-image prescription and would not pass this source gate.

The first sub-obligation can be localized even further: producing the quiet
X_2=X_3=0 control neighbors on the original source while leaving Y_1
selectable. Equation (8) shows precisely what fails without them.
Any successful construction must also supply the other constraints in (6);
this sub-obligation alone is not a completed apparatus. If no independent
physical source for that ready resource can be named, stop there without
adopting it. This is apparatus work, not a proposed Bell-table fit.

This paper is a hand derivation and source assessment. No simulation,
enumeration, native experiment, implementation, Lean run, freeze or special
workflow was performed. Cheap publication checks cover formatting and scope,
not scientific validity. A separate reviewer must check (4)–(11), modulo-L
aliasing, common-prior independence, acquired-information and failure
accounting, and the source/Bell boundary at an immutable pushed commit.

The new results remain on a research branch pending that review. The
accepted component at 235305e2 is a substantive off-main dependency, not
mere provenance; any future landing must satisfy AGENTS §A.42 for it and
the source claims. No main-established preparation result is claimed here.
