# One common physical experimental interface: source and selection gate

Accountable #866; feeds #1169; guiding draft #1173.
Writer: ChatGPT Work coordinating session; separate independent reviewer.
Paper-only design/source assessment, not implementation or premise adoption.

## 1. Selection and decision contract, fixed first

[Owner activation](https://github.com/amaybaum/incompleteness/issues/866#issuecomment-6704542441).
Drafting snapshot: `d3754dfc3a9d4416a34b6bc422a0f2033eac7176`.
Main source snapshot: `71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd`.
This section is committed before the new derivation. Existing results are known
inputs, not blinded observations; this is not an F/E designation.

1. Start with actual native carrier/update/control/readout sources. Select at most
   one common interface for a stated physical mechanism, not a desired Bell table.
2. Specify common preparation/source law, program loading, system-controller
   interaction, observer-relative complete records, failures, outgoing state and
   resources through reuse. Mark every ingredient native, conditional mathematical,
   explicitly proposed extension, or unsupplied.
3. Any extension proposal must state a mechanism or independently meaningful physical
   condition and an independently checkable consequence beyond the correlation it
   is intended to support. A restatement of quantum behavior is not a source.
   Proposal does not establish physical availability or adopt a new premise.
4. Retain B3's measurement behavior on the same model, complete local-history
   no-signalling, a classical control, the Bell/Tsirelson/PR distinction and Gate A's
   complete operational target. Justify the experiment before claiming its Bell verdict.
   A preparation label is not a selectable isolated measurement, and access restrictions
   need physical support.
5. Stop at the first decisive source or structural obstruction. State the precise
   carrier, encoding, controls and observation class of any negative result.
   Do not generalize to all native OI or replace the obstruction with a fitted mechanism.
6. Reuse F2's existing conditional assembly; a proposed interface does not physically
   source those theorems' hypotheses merely by satisfying their notation.

The accepted correlation-recovery/source screen and the earlier abstract two-system
candidate remain distinct. The latter's separate review is outside this unit.
Only this file is in write scope. No scientific execution, simulation, special
dispatch, implementation, manuscript change, merge or other programme activation.

## 2. Selected source and physical motivation

Use the explicit state-dependent ring rule already written in papers/SM.md §3.1,
at main `71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd`, blob
`de1466b0c004339d60f1490e494e8f5037020948`.
Its motivation in that source is a coupling graph that responds to the physical
state. This precedes this unit's measurement question; no Bell probabilities are
used to choose its adjacency rule or coefficients.

For site i, the left neighbor is i-1. The right input is i+2 if u_(i+1)=0
and i+1 otherwise. The new field is the sum of those two inputs minus the
previous field, modulo q. The retained previous slice makes the whole update
reversible. Select q=2 and a ring of L>=9 sites for this bounded source test.
Use a signal at site 2, control at site 1 and receiver at site 0.
The declared observer includes the two-slice coordinates at both 0 and 1,
so its controller is not silently removed from its accessible record.

This is a different already-stated native example from the fixed cubic linear
wave used in correlation recovery. No conversion between those rules is claimed.
It is also distinct from Native A's three-bit nonlinear rule and the abstract
two-system Bell model. Their source laws and successful components are not imported.

The purpose is to assess whether this actual state-dependent coupling supplies a
common controlled interface. Main §3.3's screened-local Bell ceiling is a known
constraint, not a new surprise: a bounded-range local example is not selected as
a complete isolated Bell model. Physical preparation/loading, complete access,
same-model B3 behavior and reuse still have to be assessed.

Only the displayed update rule will be used from SM's example. Its broader
isotropy/continuum or graph-regularity claims are not premises of this unit.
The new paper must derive its own finite rule, inverse, dependency bounds and
record laws. Source location on main is not a certificate of physical availability.

## 3. Outcome: a source-based local coupling, not a Bell interface

**Author result:** the selected, already-stated graph rule implements a nontrivial
control-to-signal coupling under one fixed reversible dynamics. A single structured
hidden prior serves both visible program values. The complete two-read formal
observer law and outgoing-world law are derived below.

This earns a conditional local component. It does not earn the requested physical
experimental interface. The first physical gate is a native preparer/controller
that produces the stated ready region and selects its program with accounted
resources and records. A physical read/logging mechanism is also unsupplied.
No same-model B3 realization is supplied. The bounded-range example retains the
known screened-local Bell ceiling for separated wings.

The new independent consequence of the chosen rule is explicit: after one tick,
the controller itself contains the input bit, even when the receiver is constant;
after two ticks its previous slice still contains that input. Its outgoing state
therefore cannot be treated as a fresh ready apparatus. This behavior follows
from the preexisting rule, not from fitting a desired Bell distribution.

**Selection disposition:** retain the calculation as a source-based local
coupling/record control; do not select it as a complete Bell-experiment model.
This is not a failure of native OI generally. The rule is an example in SM's
state-dependent-geometry branch, itself a stated physical hypothesis, not a law
uniquely derived from bare OI or evidence that this ring describes a laboratory.

Protocol checkpoint: `307262d7ada56a0ee81598585167a663e91c6b53`.
Concrete source-selection checkpoint: `a98a0803babf9c8c0b9b4ff4aef9942d32782a0b`.
Review and CI are recorded at an immutable head on #1173; no main-established
physical result or independent review of the earlier Bell toy is claimed here.

## 4. One model, common preparation and complete observer cut

Write W=(u,v) for the current/previous binary fields on the ring. SM's rule reduces
exactly to

    f_i(u) = u_(i-1) XOR (u_(i+1) OR u_(i+2)),
    F(u,v) = (f(u) XOR v, u),
    F^-1(a,b) = (b, a XOR f(b)).                              (1)

If u_(i+1)=0, the selected right input is u_(i+2); if it is 1, the selected
input is that 1. This is Boolean OR, not addition of both right inputs.
The inverse in (1) proves global bijectivity for every field configuration.
The same map applies for every control and signal; no controlled opcode or
state-dependent replacement of the global dynamics is inserted.

Let C be the controller at site 1 and R the receiver at site 0.
The declared observer sees both complete local two-slice coordinates:

    R_t=(u_t(0),u_(t-1)(0)),  C_t=(u_t(1),u_(t-1)(1)),
    O_t=(R_t,C_t),           H=(O_0,O_1,O_2).                 (2)

This observer is a proper subsystem for L>=9. Its own program c is public
at t=0. Access to C after that tick is retained, rather than hidden to improve
the apparent receiver behavior. H is the complete joint projection history
for this declared observer. Physical apparatus with more accessible registers
must include them too; storing all past projections is not supplied merely
by defining H.

### 4.1 Quiet-buffer preparation and its exact source status

Let c be the program and Z a fair input bit, independent of c. Set

    u_0(1)=c, u_0(2)=Z,
    u_0(i)=0 for i in {-2,-1,0,3,4,5},
    u_(-1)(i)=0 for i in {-1,0,1,2,3}.                       (3)

The remaining original fields Xi have one common product-counting law nu,
independent of c and Z. They are retained as physical state, not erased.
These are eleven ready-zero pins. They cover the two-tick dependency region
of both observed sites; L>=9 makes the displayed coordinates distinct.
The quiet buffer is a simple finite initialization contract for testing the
local coupling. Its convenience is not a physical preparation proof.

Write I_c(z,xi) for this complete field assignment. With visible subsystem
V={0,1} on both slices, the two roots are

    a_c=((0,0),(c,0)).

The hidden prior is the *same* for c=0 and c=1: Z is fair, five hidden
current fields and three hidden previous fields are zero, and the complement
has law nu. Thus this is a legitimate common-prior rooted realization of
Main and the rooted-family audit. It differs from merely relabelling the
old correlation preparations, whose hidden priors differed at one visible root.

That realization-level positive result does not construct a laboratory act
that loads a_c and the eight hidden ready pins. No private field write,
external reset, independently chosen post-interaction state, or preparation
dependent on a future distant setting has been supplied.

For the uniform counting law nu_0 on all 2L original bits, let E_c be (3)
including the specified value of c. Then

    nu_0(E_c)=2^-12,
    nu_0(eight hidden ready pins | visible root a_c)=2^-8.    (4)

The other four constraints fix the visible root. Conditioning nu_0 on E_c
gives exactly the selected law of I_c(Z,Xi), with no calibrated Bell weight.
These are conditioning masses, not demonstrated herald/success probabilities.

Because F is a permutation, F^t preserves nu_0 for every fixed tick t.
Unconditioned native evolution of that counting baseline cannot make E_c
certain: its mass remains 2^-12. Conditioning on the final visible root
still leaves the hidden eight-pin event with mass 2^-8. This isolates a
preparation resource requirement, not a prohibition of structured priors.
A supplied low-entropy preparation, a real herald with its discarded runs,
or a different physically justified source could change that premise.
None is constructed by the present two-tick calculation.

## 5. Exact coupling, full records and outgoing state

Let v=u_(-1). On (3), the first step gives

    u_1(-1)=c,   u_1(0)=c OR z,   u_1(1)=z,
    u_1(2)=c,    u_1(3)=z.

Substitution into the unchanged second step gives

    u_2(0)=c XOR (z OR c) = (1 XOR c)z,
    u_2(1)=(c OR z) XOR (c OR z) XOR c = c.                 (5)

Here juxtaposition is Boolean AND. All old-local terms from (1) are included.
Exterior Xi cannot affect these entries in this window because (3) covers
their initial dependency region.

The complete declared observer history is therefore

| Tick | Receiver R_t | Controller C_t |
| --- | --- | --- |
| 0 | (0,0) | (c,0) |
| 1 | (c OR z,0) | (z,c) |
| 2 | ((1 XOR c)z,c OR z) | (c,z) |

Call this history H_c(z). It determines z from C_1's current coordinate,
for either program. The actual joint history/world law is

    Law(H,W_2 | program c)
      = (1/2) sum_(z=0,1) integral
          delta_(H_c(z), F^2(I_c(z,xi))) d nu(xi).           (6)

This retains the whole outgoing world, source bit, program and correlations.
It is a complete conditional law, not an independent-bath replacement.
Reversibility retains information globally; no public inverse operation follows.

### 5.1 Controls and a consequence beyond the receiver response

For c=0, the receiver reads z and retains it in its two-slice pair:
R_1=(z,0), R_2=(z,z).
For c=1, the receiver-only history is constant:
R_1=(1,0), R_2=(0,1), for both z values.
Thus the program genuinely changes the receiving interaction in this model.

The controller prediction is independent evidence about the mechanism:
C_1=(z,c) and C_2=(c,z). If those coordinates are accessible, the apparently
masked receiver does not hide z from the *whole observer*. Discarding C from
the analysis would change the access contract. This is a local input-access
fact, not Alice-to-Bob signalling: c is this observer's own visible program.

Deterministic z=0 and z=1 are exact calibration countercontrols for (5).
They are mathematical input slices, not additional physically available
preparations. Fair mixing gives (6) without inserting a quantum angle law.
The complete rule is a classical deterministic field evolution; this source
test does not distinguish it from a classical apparatus.

### 5.2 Continuation, record storage and failed preparations

The actual W_2 is a valid input to F, so passive continuation exists.
It is not certified as an input to another desired measurement operation.

In particular, the original contract requires the controller's previous
coordinate to be zero. At t=2 that coordinate is z. On the conditional
z=1 half of the prepared law, W_2 is therefore outside the original ready
slice, whatever the exterior. Also, for c=1 the receiver's previous
coordinate is 1 at t=2, so that program never returns to (3)'s ready slice.
These are readiness-set statements, not physical failure probabilities.
They do not require every valid instrument to reset to its initial slice:
a compatible next-stage contract or an accounted reset/fresh bank could work,
but neither is constructed here.

The previous slice retains a value for the next tick; it is not an arbitrary
lifetime memory or a physical implementation of repeated record readback.
No new setting request, clock, append-only log or completion flag has been
implemented. A readable bit at one cut cannot be called a reusable instrument.

F is total, so it has no algebraic evolution failure. A physical loader's
failures are unspecified. If Psi is the fixed observation/world map from
any initial field and p=2^-12, the canonical baseline obeys

    Psi_#nu_0 = p Psi_#nu_0(. | E_c)
                 + (1-p) Psi_#nu_0(. | E_c^c).              (7)

The complement is retained, not renormalized away. E_c is not a supplied
acceptance flag. Any real preparer must provide its attempt count, timing,
failure/no-read behavior and residual state under one common law.

## 6. Physical source ledger and the Bell selection gate

| Ingredient | What this one model supplies | Status still required |
| --- | --- | --- |
| Carrier and evolution | Exact binary specialization of SM's stated ring example; (1) and its inverse | Physical motivation comes from the existing state-dependent-geometry proposal; no claim of empirical selection or derivation of this ring from bare OI |
| Common preparation | One fixed structured hidden prior across roots a_0,a_1; explicit count in (4) | Native source/preparer for the ready fields with resources, failures and records |
| Program choice | Different visible c roots with unchanged hidden law; no target-weight adjustment | A selectable controller/loading operation realized by the same physical dynamics |
| Coupling | c selects which right input enters the receiver through (1); derived joint response (5) | This local coupling is not B3's quadratic sensor and record-conditioned exchange |
| Read access | Declared complete projection of sites 0 and 1, with controller backreaction retained | Physical read interaction, clock, readable storage and any larger apparatus access |
| Continuation | Full W_2 and native F continuation, with no reset or erased fields | A compatible next instrument or sourced reset/fresh resources; original ready slice is not recovered |
| B3 control | No same-model carrier/drive/sensor/reference/exchange map is supplied | NOT SUPPLIED; matching a local bit or repeat is not the B3 instrument |
| Bell/composites | A bounded-range local dynamics with an explicit dependency envelope | A justified two-wing interface and the required quantum correlation set; neither comes from this local source test |

B3's real two-mode carrier and uniform-seed detector have a known conditional
measurement law, but no map from this binary ring to its preparation, U_theta,
quadratic sensor or exchange is given. Their resources cannot be imported
to fill the ledger. Nor may a probability p(theta)=cos(theta)^2 be imposed
on Z and relabelled a native derivation.

The interaction in (1) uses sites i-1, i+1 and i+2, plus the old local slice.
Consequently every field after t ticks depends only on original sites within
ordinary ring distance 2t. This uniform dependency envelope is valid even
though the selected right edge varies with the state.

Consider any proposed two-wing realization using this same rule, local
setting writes at one cut and a response-complete preparation independent of
the settings. If each wing's *entire* accessible read region lies outside
the other setting region's two-tick dependency envelope (ordinary distance
greater than 4 suffices), its complete local history through these two ticks
is pointwise independent of the distant setting. Classical memory is included.
Main §3.3's screened-local theorem then gives CHSH <= 2 for every-run binary
outcomes. No success-conditioned Bell statistic is silently substituted.

This is a conditional restriction on separated implementations of this
bounded-range rule, not a claim that a two-wing apparatus has been constructed.
Calling the adjacent controller and receiver Alice and Bob does not make
their interaction an isolated Bell experiment. Allowing their causal cones
to meet changes that premise; an average no-signalling/quantum-bound proof
would still be needed.

Thus state-dependent adjacency alone is not the missing quantum resource.
SM/Main also discuss preparation-indexed longer edges; the explicit ring rule
tested here supplies no such channel. Its source, preparation, measurement
access and full-history/no-superquantum constraints remain part of the open
H-Bell/composite problem. This paper does not invent a long-edge law or a
masking distribution to rescue the candidate.

**First physical stop:** the accounted native preparation/loading operation.
The formal common-prior experiment and local coupling are available as
mathematics. A physical experimental interface, B3 control and a complete
Bell candidate have not passed selection. No new extension is adopted.
A future extension proposal must supply its actual mechanism and independent
consequence, not just assert that this ledger can be filled.

## 7. Existing assembly, source checks and disposition

F2 remains the existing physical-extension objective. GeneralCarrier's
exactAll_iff_physical_general and MinimalRepertoire.qm_of_oiPlusMin already
assemble exact finite endomorphic quantum operations within their stated
matrix-operation/interface and resource hypotheses. The source pins and
checked definitions are retained in the accepted [source screen](../correlation-recombination-20261107/NO-SIGNALLING.md#5-f2-use-the-existing-assembly-at-its-actual-scope).
The current main snapshot is unchanged from that review. No assembly theorem
is reproved or used to assert an available native controller.

Main §3.4's action-labelled classical dilation also starts from supplied
target laws and action-ledger writes. It does not compile those writes into
the present F or establish the loader in §6. That valid representation
result is preserved without treating it as physical actuation.

The following material sources were read, with assumptions inspected:

| Source | Exact pin and role |
| --- | --- |
| papers/SM.md §3.1 | Main `71b190f7`, blob `de1466b0c004339d60f1490e494e8f5037020948`; the explicit ring rule and state-dependent-geometry motivation, not its broader isotropy/continuum claims |
| papers/Main.md §§1.2, 3.3, 3.4 | Same main, blob `a954cfb47c740766b8ca6ab9027a46bbf6fa2f94`; counting/structured-prior distinction, screened-local Bell theorem, representation/action-dilation scope |
| verification/audits/operational/rooted-observer-family-sourcing/result.md Q2–Q7 | Same main, blob `34ea388d0fd47afe07bc9b41c79fe074898d493a`; fixed hidden prior and supplied realization-level projection |
| [Gate A](endpoints.md) | Drafting snapshot `d3754dfc`, blob `d9d92e038a8022e854586101067ce4de9789fdf6`; common source/program contract and complete target |
| [B3](measurement-exchange.md) | Same snapshot, blob `aeaa8ca03f187bd0adda82532faf3154f4b4dd5f`; actual carrier, sensor, exchange and source boundary |
| [Accepted preceding screen](../correlation-recombination-20261107/NO-SIGNALLING.md) | Same snapshot, blob `25294da402b60f87c578a675a1a0793f76f4236f`; fixed distinctions and previously checked F2 sources |

The source search also inspected the continuous-substates native actuation,
selector, nonlinear-compensation and later-controller records. Those use
Native A's three-bit h(A,B,D)=(B,D,A XOR BD), separate source contracts and
different observer access. Their computational results, review labels and
resources are not premises of (1)–(7) and are not silently combined with this
ring. In particular a known symbolic decoder or a timely random label is
not a physical write in the chosen model.

This result is a written derivation with explicit finite conditional
assumptions. No code, simulation, enumeration, Lean build or physical test
was performed. Ordinary PR CI is repository verification. Separate review
must check the binary specialization, inverse, support/pin counts, full
controller history, outgoing-state qualification and source/Bell scope.

#866 retains the preparation/control/access construction. Existing fresh/ready
supply, probability-source, retention and composite/reuse obligations remain
at #1147, #1059, #1032, #868 and #913; no work there is activated. #914's
Bell/Tsirelson requirement and #1143's distinguishing test remain open.
#1169's whole-model equivalence is unchanged. The accepted correlation
recovery and the separately unreviewed abstract Bell toy remain distinct.
