# Preparation and readout from one local receiving interaction

**Standing.** Paper-only source assessment for #866, feeding #1169, on
guiding draft #1173. The [owner scope](https://github.com/amaybaum/incompleteness/issues/866#issuecomment-6695164378)
covers one receiving interaction, its preparation/control/access assumptions
and independent review. Review status is recorded on that PR.
Main source snapshot: `f49b768709d262a05471895cec703b31aff19b57`.

**Outcome.** The selected finite reference dynamics supplies a local transfer
equation, not the proposed quantum preparation and measurement interface.
A known incoming background permits exact recovery of the signal; a common
uniform hidden background makes the immediate receiver law independent of it.
These are conditional consequences of the same update, with different stated
preparations. Later access to the background can restore the signal exactly.
Neither case supplies a physically justified quantum restriction.

The candidate stops at its **laboratory preparation/control/access map**:
no source identified in the assessed branch implements the required loading,
settings and restricted readout contract for the B3 benchmark. This is a
bounded source verdict. It does not say OI lacks an observer projection,
a selected default measure, mathematical preparations, or every possible
physical interaction. No replacement candidate or physical premise is adopted.

## 1. What the source already supplies

The source search covered the maintained papers and book mirrors, Lean
interfaces, and the relevant retained preparation, coupling, access and
operational-quotient records. The following distinctions govern this assessment.

| Input | Strongest relevant source | Consequence here |
| --- | --- | --- |
| Embedded observer and visible projection | Main §§1.2, 1.4; rooted observer-family audit Q1, Q6 | A declared finite realization has a visible cut/projection. A particular laboratory identification still needs its physical map. |
| Probability law and preparations | Main §§1.2, 1.5, 3.2, 3.4; rooted audit Q2–Q4 | Selected counting is a canonical baseline; structured fixed hidden priors and rooted visible preparations are allowed realization data. No absence of preparation mathematics is claimed. |
| Finite local update | SM §§3.1, 4.1; the actual equations in `wave_eqn.c` | The reference branch is a reversible two-slice finite wave rule. The coefficient and graph of that branch are declared inputs. |
| Real amplitudes and exact controls | SM §4.1; B1 §§2–6 | A real/complex observer-level lift and B1's exact signed parameter loading are additional bridges. The finite rule is not silently replaced by the normalized real lift. |
| Laboratory preparation from retained records | Current Main's conditional/pushforward definitions; #866's D-OB7/D-OB8 record | Conditioning within a given realization is defined. Identifying it with a laboratory preparation remains H-PREP, an open hypothesis; no creating operation follows from writing a conditional. |
| Quantum operational interface | `OperationalAssembly.FiniteOperationalTheory`; B1/B3/bridge papers | Complex-linear operations, availability and readout premises have a specified mathematical role. This receiver does not instantiate them merely by supplying a stochastic output. |

The rooted audit's positive result is retained: visible roots and one common
hidden prior define an observer family at the realization layer. In the
candidate below, the signal S is outside the receiving observer before the
interaction. Selecting S and preparing its incoming neighborhood is a
different operation from choosing that observer's visible root. Declaring
an initial joint law is legitimate mathematics; it does not exhibit an
autonomous laboratory protocol that produces that law.

Likewise, the reduced `StochasticInterface` result about non-uniqueness of
invariant ensembles is not a claim that the maintained architecture has no
measure-selection principle or observation map. The rooted audit explicitly
corrects that broader reading. The present source verdict does not use it.

## 2. One candidate, at its actual finite level

Take `Lambda=(Z/LZ)^3`, `L>=5`, and `q>=2`. Every field takes
values in `Z/qZ`; no field structure or division is needed.
Let A be the six-neighbor adjacency sum. With current/previous fields
`W=(u,v)`, use the fixed update

    Phi(u,v) = (A u - v, u).

Its inverse is `Phi^(-1)(a,b)=(b,A b-a)`. This is a bijection on the
complete finite two-slice state space. The side-length restriction keeps
the local neighbor geometry used below free of self-edges and triangles.
It is a mathematical model choice, not a claim that the packed C program
was executed at these sizes.

Choose adjacent sites s (signal) and d (receiver). The motivation is the
existing graph interaction: u_s contributes to the receiver's next value,
and u_d contributes to the signal's next value. No pointer kick, normalized
real wave coefficient, setting-controlled swap or measurement opcode is added.

The proposed local observer sees both coordinates at d:

    V_0=(u_d,v_d),              V_1=((A u)_d-v_d,u_d).

These are all of this observer's two-slice coordinates, not a selected
Boolean report. A report g(V) would be an additional interpretation.
The whole world still includes the other sites and both slices; no private,
non-returning reservoir is inferred. This is a receiver component of a
possible apparatus, not a construction of a full observer satisfying C1–C4.

The reference coefficient is one because that is the retained finite
reference rule. SM §4.1 distinguishes this from the observer-level
normalization 1/3 and explicitly rejects maximum-speed selection of the
real-lift coefficient. The old maximum-speed gloss in the C file's header
is not a premise of this paper; its update equations are the source used.

## 3. Derived transfer law and its preparation dependence

Write

    S = u_s,       B = u_d,
    K = sum_(j adjacent d, j != s) u_j - v_d.

Then the complete next receiver state is

    V_1 = (R,B),      R = S+K mod q.                       (1)

This is an exact local dependency identity. It does not infer statistical
independence of K and S. Let C denote an actually retained public prefix,
including V_0, with positive probability. For any specified incoming law,

    P(R=r | S=x,C) = P(K=r-x | S=x,C).                     (2)

If the conditional law of K is a common kappa independent of S at that
prefix, this becomes `kappa(r-x)`. For an actual preparation setting p,
one must establish the relevant joint law after loading; uniform marginals
alone do not establish independence or setting isolation.

Three controls follow without a model run.

**Known background.** If the incoming other five neighbors and v_d are
prepared so that K=k0 is known, the public value R determines
`S=R-k0`. In particular, the ready slice K=0 copies S to the new
receiver coordinate. V_0 can be the same (0,0) for every S, so this
conditional transfer need not assume the receiver already saw the input.
The required preparation of that slice is not established by this example.

**Uniform hidden background.** If, conditional on C, at least one of the
other incoming neighbors is uniform and independent of S and all remaining
summands, K is uniform and

    P(R=r | S=x,C) = 1/q.

The whole V_1 then reveals no additional S information at this step, since
its second coordinate B is already in C. This includes the mathematical
product-counting baseline with fixed receiver coordinates. Conditioning
further on S is an analysis of that law, not a mechanism that selects S.
A structured preparation or a conditioning event that creates correlations
need not retain this conclusion.

**Later background access.** If a later permitted procedure makes K
recoverable and R has actually been retained, then `S=R-K` pointwise.
No independence assumption is needed for this recovery identity.
The paper does not assert that such a procedure is available at the
chosen receiver. It states the check a claimed access restriction must
pass; forgetting K in a one-step marginal is not proof of lasting privacy.

Partial, nonuniform kappa gives a translated classical noise channel by
(2). Nothing in that formula selects a Born curve, a particular kappa or
the physically available preparation family. Choosing those to fit a
quantum outcome would introduce the missing premise rather than derive it.

## 4. Carrier change, second tick and controls

The signal's complete next local state is also fixed by the same update:

    (u'_s,v'_s) = (sum_(j adjacent s) u_j-v_s, S).         (3)

The receiver's old B contributes to the first coordinate. Thus there is
ordinary bidirectional coupling. Equation (3) is not a detector-outcome
controlled exchange with a ready reference, and it does not supply a
conditional quantum outgoing-state interpretation.

For a transparent finite-window check, assume the mathematical initial
configuration `u=x delta_s, v=0`. All other field coordinates start at
zero. Then `u_1=x A delta_s, v_1=x delta_s`, and

    V_0=(0,0),       V_1=(x,0),       V_2=(0,x),
    (u_1(s),v_1(s))=(0,x),
    (u_2(s),v_2(s))=(5x,0),                            mod q.   (4)

Indeed the six neighbors each receive x at the first step. At d there
is no two-step walk from s, since s,d are adjacent and there is no local
triangle; hence `u_2(d)=0`. At s there are six two-step returns,
and the old slice subtracts one x, giving 5x.

This shows why dropping the older coordinate would create a false
second-tick erasure: the complete local receiver still contains x at
that tick. It also checks the unchanged dynamics beyond the first read.
When `gcd(5,q)=1`, the signal's current coordinate at the second tick
again determines x. For other q the displayed formula remains exact;
for q=5 it is zero. No universal return-injectivity claim is made.

The initial zero neighborhood and field x are supplied conditions in
this calculation. No laboratory loading, physically readable clock,
persistent copied record or later reset has been constructed.
Equation (4) is not an O-RET counting verdict or a physical retention
theorem. It nevertheless prevents treating the old signal as an
automatically inert, non-returning workspace in this reference model.

There is also a simple control on alleged setting dependence. For any
fixed initial displacement Delta,

    Phi^t(W+Delta)-Phi^t(W)=Phi^t(Delta).                 (5)

This follows by linearity and induction. If a setting changes only an
initial controller displacement independent of the carrier, its effect
on a raw carrier coordinate is an additive displacement independent of
the incoming carrier. It does not change the update's coupling matrix.
That is not an impossibility theorem for every encoded gate or nonlinear
report, and it does not settle O-SET's open definition. It does show that
a loading offset alone is not a derivation of B1's selectable mixing
coefficients or B3's outcome-controlled exchange.

The retained nonlinear native-actuation record has different local
identities, including background-dependent cross-terms. Those are not
excluded by (5). That record also distinguishes a native algebraic
coupling from an available actuator, usable input and readable output.
This paper neither re-runs nor extends that separate construction.

## 5. The two benchmark checks, without changing the target

### 5.1 Distinguishability

Suppose q>=3, suppose every signal value can be physically prepared
on the same ready slice K=0, and suppose the complete raw receiver is
available. Then three distinct values 0,1,2 have disjoint certain output records.
Pairwise binary reports can distinguish them perfectly. Under the
same fixed-object, preparation-independent test interpretation as the
bridge paper, their quantum density supports must be mutually
orthogonal; a qubit cannot represent them. More generally this
conditional ready/raw family requires dimension at least q.

The quantum support argument is the bridge paper's Lemma 2, not a new
theorem. It includes all preparation-correlated accessible information
in the encoded object. A different target type or extra preparation-label
input changes the comparison.

This check does not identify the finite residues with B1's three angles
or silently assume its drive family. That native encoding has not been
constructed. Unlike E-AR's entire exact point orbit, a fixed finite q
does not here give arbitrarily many distinguishable preparations.
For q=2 this particular count excludes no qubit; enlarging the target
to dimension q also passes this count. Neither fact proves equivalence.

If only a coarse bit g(R) is declared available, any exclusion of the
other raw information needs its own physical justification. Merely
printing g(R) while the same observer can read R changes no accessible
interface. A restriction has to survive later allowed reads and controls,
including any actually accessible background or stored preparation data.

### 5.2 B3's instrument and both reads

Keep the existing qubit target: initial e1, B1 drives U(theta), U(phi),
and the same binary basis instrument. B3 derives, under its specified
uniform independent seeds and ready exchange resources,

    P(1,1)=cos(theta)^2 cos(phi)^2,
    P(1,0)=cos(theta)^2 sin(phi)^2,
    P(0,1)=sin(theta)^2 sin(phi)^2,
    P(0,0)=sin(theta)^2 cos(phi)^2.

In particular the first plus probability is cos(theta)^2, and at phi=0
the second outcome repeats the first. The new receiver has no sourced
mapping from theta,phi to preparation and controlled interaction labels,
nor a supplied fixed operational state dictionary. Equations (1)–(4)
therefore do not constitute this comparison's success or a completed
two-read quantum counterexample. The availability prerequisites fail
before a physical B3 assessment can be completed.

Two limited checks make this precise. Uniform independent K gives a
constant immediate law, so a fixed binary report of that value cannot
produce the full theta-dependent Born curve. More generally, with one
fixed kappa, fixed visible-root data and fixed report, deterministic
loading `S=x(theta) in Z/qZ` can yield at most q immediate
probabilities. It cannot equal cos(theta)^2 for every real theta.
Allowing theta-dependent mixtures over S or the background changes this
premise and may change the result; the mechanism producing those laws
is exactly part of the unsupplied preparation map.

The second raw time-slice coordinate in (4) cannot be counted as a fresh
second quantum measurement or thrown away as irrelevant. Both the
actual native state and any physically retained outcomes must enter a
future comparison. No new seed, blank record or reset is granted for
free. B3's already-proved restricted conditional result is preserved;
this receiver has not physically implemented it.

## 6. Precise stopping point and remaining proof obligation

The assessed branch supplies the native finite update and its conditional
transfer/back-reaction identities. The maintained observer-realization
layer supplies a mathematical visible projection, conditional laws and
permitted realization data. What is not supplied for this receiver is
one physical protocol-to-model map that simultaneously establishes:

1. Which joint signal/background/ready-state laws laboratory preparations
   can produce, with the required independence and causal-prefix properties.
2. How settings physically select the control and detector interaction on
   the same incoming carrier, with the same labels in every use.
3. Which records, old fields and continuations are physically readable,
   and why any omitted information cannot distinguish proposed equivalent
   preparations under later permitted procedures.
4. A common correspondence to B3's states/instrument and ultimately the
   full Gate A interface, with compatible resources and both whole-model
   directions.

The first item is already open for the claimed controlled receiver.
For the fixed visible root, imposing K=0 constrains hidden incoming
fields; specifying a conditional measure on that event is not a
preparation device. The current Main definitions and the rooted audit
do not provide that device, and the source records identify the
corresponding readiness, actuation and preparation obligations.

Consequently this candidate stops at the preparation/control/access
source gate. No background law, loss of raw access, new observer class
or revised quantum target is adopted to repair it. The correct outcome
is an explicit missing physical realization map, with conditional
receiver identities available as checks on any later proposal.

#866 owns that map and the coupled public-access question. Ready-state
supply remains #1147, measure selection #1059, record retention and
cross-read coherence #1032, and the distinguishing experiment #1143.
#1169 retains the full correspondence. These are accountable pointers,
not transfers of authorization or premises supplied by an issue.
The existing GeneralCarrier characterization is reused when its actual
interface and hypotheses have been realized; re-proving it would not
supply the missing map here.

## 7. Source roles and verification boundary

The new candidate assessment is a hand derivation from the explicitly
stated finite rule and conditional initial laws. Its local transfer and
linearity facts are elementary; novelty is not claimed for copying,
masking, linear propagation or the quantum dimension bound.

| Reference | Role in this assessment |
| --- | --- |
| `../../../../../papers/Main.md`, §§1.2, 1.4–1.5, 3.2, 3.4 | Support on main: observer, selected/default and structured laws, conditional histories, and the representation/physical-realization boundary |
| `../../../../../papers/SM.md`, §§3.1, 4.1 | Support on main: finite second-order rule, stated reference-branch assumptions, and separate observer-level lift |
| `../../../../../papers/Substratum.md`, §§3.1–3.3 | Support on main: actual reconstruction inputs and conditional lattice realization; not an apparatus compiler |
| `../../../../../papers/oi_lattice_code/trace_out_fractional/wave_eqn.c`, wave_step and wave_step_inverse | Support on main for the finite update equations only; no new execution or use of its obsolete speed-selection comment |
| `../../../../audits/operational/rooted-observer-family-sourcing/result.md`, Q1–Q7 | Support on main: positive realization-relative observer/preparation result and correction of the reduced-interface overreading; its algebra is read, no historical replay claimed |
| `../../../../lean-mathlib/OIBridge/StochasticInterface.lean` | Scope check on main: invariant-ensemble predicate for the reduced layer, not a corpus-wide absence of observer/measure data |
| `../../../../lean-mathlib/OIBridge/OperationalAssembly.lean`, FiniteOperationalTheory | Support on main for the actual assumed availability/matrix interface; its derived readout form is not relabelled a postulate |
| `../../../substratum/continuous-substates/native-link-sourcing-gate.md` | Support on main: distinction between the native finite update and added pointer/link rules |
| `../../../substratum/continuous-substates/native-actuation-boundary.md`, §§1–3 | Support on main for the stated nonlinear local algebra and access contract only; no reuse of its pending computational verdict |
| `../states-dynamics-audit-20261024/history-architecture-v5/REPORT.md`, preparation cone and public/private contract | Support on main for the existing conditional positive comparison's inputs; its cosine priors and non-returning workspace are not sourced for this receiver |
| `../oi-qm-ext-1/two-mode-drive.md`, `../oi-qm-ext-1/measurement-exchange.md`, `../oi-qm-ext-1/whole-model-bridge.md`, `../oi-qm-ext-1/endpoints.md` | Material support in this PR for B1/B3, the dimension lemma and full target; unchanged prior papers, not claims of physical availability |
| #866 D-OB7/D-OB8, c.6649267203 | Owner-decision provenance: amaybaum, 2026-11-05, accepted conditional-law classification and left H-PREP open; no mathematical source inferred |
| #866 c.6695164378; #1110 | Authorization and separate-writer provenance, respectively; no result from #1110's off-main analysis is used as a proof premise |

The D-OB8 ruling states: “Record H-PREP as an explicit open hypothesis:
identifying a laboratory preparation with conditioning on the observer's
own records within an existing realization.” Its planning status does not
supply the hypothesis.

The B1/B3/bridge/endpoint sources are not yet on main. Their needed content
must accompany any authorized landing of a dependent claim under AGENTS.md
§A.42; a branch or SHA alone is insufficient. The proof of the new receiver
identities is written here so it can be checked without a transient log.

No scientific code, CAS, enumeration, simulation, Lean build or experiment
was used for this assessment. Ordinary automatic PR CI is separate repository
verification. No full OI–QM equivalence, native measurement availability,
physical restriction, manuscript claim or merge is adopted.
