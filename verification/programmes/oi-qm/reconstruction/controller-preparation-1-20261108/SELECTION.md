# CP-PREP-1: one routing interaction screened for native controller preparation

**Author source-selection finding: source gate NOT PASSED.** One concrete external
interaction was inspected; no qualifying native preparation interaction was sourced.
Independent selection review is separate from this author finding. No derivation
beyond source selection is started.

Accountable Issue: #866. Writer: Codex /root. Separate reviewer: review_wave_sign.
[Owner scope](https://github.com/amaybaum/incompleteness/issues/866#issuecomment-6718471099)
and [activation](https://github.com/amaybaum/incompleteness/issues/866#issuecomment-6718915044)
are authorization provenance, not physical evidence. Source snapshot: main
f88c184220453badfc9279ab9a86b6785e4db5ff, after the five approved integrations and
their green post-merge checks.

## 1. One candidate and the source gate

The single candidate is the conditional switch of Fredkin and Toffoli,
*Conservative Logic*, International Journal of Theoretical Physics 21 (1982),
219–253, §6.4, Figures 16–17, p.241
([primary paper](https://gwern.net/doc/cs/hardware/1982-fredkin.pdf)).
It is selected for its concrete control-dependent routing interaction, not for
agreement with a desired readiness distribution or a quantum target.
The prior controller report's missing-source finding was already known;
this is not a blinded selection.

The paper routes a data signal according to a control signal using its idealized
billiard-ball interaction. Sections 6.1–6.3 supply the hard-ball kinematics,
fixed reflectors, geometrical clearance and synchronization conventions; input
constants are supplied. These are resources of that external model, not an OI
implementation. The primary text and the Figure 17 diagram were read directly.

The gate requires a source identifying an actual interaction under the selected,
unchanged OI rule, together with its preparation resources, timing and setting
source. Only one bounded interaction is required; an embedding of every possible
billiard-ball computer is not demanded. An abstract gate with the same logical
function, or a specification of a desired initial state, is insufficient.

If a separate reviewer cannot accept that native interaction and its accounted
inputs, stop at the first missing physical link. No alternative interaction,
changed update, simulation, scientific computation, V3 execution or new physical
premise is authorized here.

## 2. The unchanged native target

[Preparation-loading](../oi-qm-ext-1/preparation-loading.md), §§3–4, fixes a binary
ring with L>=9 and, for indices modulo L,

    f_i(u) = u_(i-1) XOR (u_(i+1) OR u_(i+2)),
    F(u,v) = (f(u) XOR v, u).

This is the selected example of SM §3.1, not a rule newly derived from bare OI.
The preparation paper's forward-loading identity is retained with its stated
scope; it is not rederived or enlarged here.

At the precursor tick write (X,Y)=(u_(-1),u_(-2)). The existing target contract
is the visible root

    X_0=X_1=Y_0=0,  Y_1=c,

and all eight hidden constraints

    X_(-1)=X_2=X_3=0,
    Y_(-2)=X_(-3),  Y_(-1)=X_(-2),
    Y_3=X_4 OR X_5,
    Y_4=X_5 OR X_6,
    Y_5=X_4 XOR (X_6 OR X_7).

The remaining coordinates have the common free-bit law specified in that paper;
Y_2 remains free and Z=Y_2 XOR X_4. The uncontrolled source law eta is the same
for both request values c. Physical production of just X_2=X_3=0 would not
supply the complete contract, the request producer, or the rest of the apparatus.

The external switch's control signal has not been identified with Y_1 merely by
giving both a control label. Such an identification needs an executing native
process with a justified common incoming law.

## 3. Source inspection and the apparent Fredkin matches

All repository references below are read at the pinned main snapshot.

| Inspected source | What it supplies and its role here |
| --- | --- |
| [Preparation-loading](../oi-qm-ext-1/preparation-loading.md), §§3–7, and [the retained controller report](../physical-controller-20261107/LEAD.md), §§3–5 | Support for the exact selected rule, complete precursor, known transport identity and existing factory/source stop. Neither supplies a native implementation of the selected switch. |
| [SM](../../../../../papers/SM.md), §3.1; [Main](../../../../../papers/Main.md), §§1.2, 3.4; [rooted-family audit](../../../../audits/operational/rooted-observer-family-sourcing/result.md), Q2–Q7 | Support for the rule and positive realization architecture. A visible root and a common structured hidden prior are legitimate realization data. An action-labelled realization is not an implementation of those actions in this particular ring. No denial of that positive architecture is inferred. |
| [Book Chapter 2](../../../../../book/ch02-substratum.md), §2.3 | The reversible-computation comparison does not identify the physical degrees of freedom or preparation interaction for this candidate. |
| [O-RET DEFINITIONS](../o-ret-routes-20261103/DEFINITIONS.md), comparison table and notes; [DESIGN-PULSE](../o-ret-routes-20261103/DESIGN-PULSE.md), §3.2; [Phase A preregistration](../o-ret-routes-20261103/PREREG-PHASE-A.md), S1/HC-SW; PHASEA-TUPLES.json, fredkin-channel | Contextual definitions of existing conditional sketches, not new evidence of preparation. M_F explicitly adds E-reg: a Fredkin update on presence/value/register variables, a shift, declared access and restricted readiness. It is not identified with the fixed two-slice ring update above. Its numerical retention results are not consumed or rerun. |
| [Native gate v13](../native-y-continuation-20261024/native_gate_v13/REPORT.md), §§1–2, and [its review](../native-y-continuation-20261024/native_gate_v13/review/REPORT.md) | Context: a different three-bit cubic-lattice update and supplied apparatus/source family. The record distinguishes masked nonlinear processing from an isolated available gate. Neither its computations nor its review are imported as a proof about this binary-ring preparation. |
| [Native A standing](../../../substratum/continuous-substates/README.md), standing paragraph | Support for respecting the limited standing stated for files in that directory; no such paper proof is a premise of this binary-ring selection. |
| [Bridge audit checker](../bridge-compatibility-audit/independent_check.py), circuit definition; [channel audit](../round-oi-channel-1-audit/result.md), "Finite stopped protocols" | Context: supplied quantum comparator gates. They do not specify a native producer of the selected precursor. No checker or quantum gate is executed or adopted. |

The tracked-text search used billiard, Fredkin and Toffoli across papers, book,
verification and tools, including Markdown, TeX, Lean, Python and the retained
tuple data. Relevant occurrences were read as their actual model/source claims.
The frozen Phase A implementation was inspected as text only; no frozen record
was changed. Book/FULL copies are one source, not independent evidence.
This was a search for an implementation of the one selected interaction,
not a search for an additional candidate.

The concrete Fredkin sketches therefore were not ignored: their own stated
update and supplied resources do not provide the required identification with F.
Likewise a native nonlinear term in another declared model cannot be spliced
into F by relabelling it. This is a source/type distinction, not a new
impossibility proof or a re-review of their scientific results.

## 4. First missing link and the fixed stop

**First missing physical link:** no source located in this inspection identifies
the selected switch as an executing interaction of the stated F, with actual
native degrees of freedom and a source of its incoming preparation/control
resources. The external interaction description supplies neither that particular
native process nor its input producer. No such map is constructed here.

The following remain unfilled for this candidate:

| Required item | Source-stage status |
| --- | --- |
| One native interaction whose evolution under F implements the selected bounded preparation operation | Not sourced. Same logical function or invertibility does not identify an available interaction. |
| A common physical input/resource law for both requests | Not sourced for this candidate. The allowed realization datum eta and its inverse image do not construct its producer. |
| Preparation of the full root and all eight hidden constraints | Not established. No quiet-neighbor result or complete precursor production is claimed. |
| Physical timing and selectable request loading | Not sourced. The existing tick labels and contrast between c=0 and c=1 preparations do not themselves provide a clock or actuator. |
| Complete preparer knowledge, failures and outgoing state | Not derived. Any eventual process must include its accessible records, failed preparations and correlations, with no free reset or blank supply. |

This stop precedes a preparation derivation. It is unnecessary to invent a
decoder, calculate a herald probability, compile an abstract circuit, or run a
trajectory to reach it. The existing canonical-source mismatch remains a
countercontrol in preparation-loading; no source event mass is promoted into
an apparatus success probability.

The prior record also states that the declared controller later learns Z.
Whether a preparer would learn Z earlier depends on its actual implementation;
it is not asserted to be unavoidable. Because no preparer is sourced here,
there is no new knowledge/privacy or full-history reuse verdict.

## 5. Disposition and verification limits

Select no native interaction from this lead. The source gate is NOT PASSED;
derivation beyond source selection is not started. A reviewer may accept this
bounded stopped-source record without accepting a physical preparer.
It does not show that the switch, all controllers, or all OI preparations are
impossible. No existing conditional or positive result is withdrawn.

No additional candidate was screened. There is no simulation, enumeration,
scientific computation, Lean work, native V3 execution, new physical premise,
manuscript change, integration or issue closure in this unit. Classical
preparation would still not settle retention, coherent readout, Q-A compatibility,
arbitrary composite control or full OI–QM equivalence.

Verification is direct primary-source reading and repository source/type
inspection, plus document/path/whitespace checks. It is not an experimental test,
kernel theorem, exhaustive absence proof or acceptance of an executing
interaction. Ordinary repository CI and independent source-selection review
remain distinct from the physical gate.
