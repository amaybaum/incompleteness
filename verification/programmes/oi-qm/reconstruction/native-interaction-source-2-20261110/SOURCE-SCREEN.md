# NATIVE-INT-SRC-2 — Native boundary write and delayed-slice retention

**Author result: STOPPED / UNSOURCED. Physical-source gate: NOT PASSED.**
Paper-only author source assessment; independent non-author review is a separate gate.

Accountable issue: [#866](https://github.com/amaybaum/incompleteness/issues/866).
Coordination: [#1169](https://github.com/amaybaum/incompleteness/issues/1169).
Writer: Codex. Authority: [owner decision, 10 November 2026](https://github.com/amaybaum/incompleteness/issues/866#issuecomment-6763916830)
and [coordination scope](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6763928950).
Drafting/source snapshot D: `cac5d26441dd33e9348151487e4df7b547195481` (`main`).

## 1. Selection and stop rule

Screen exactly one process: the selected binary ring's **existing boundary write into site 0, followed by retention in its previous-time field**. The source is SM §3.1's state-dependent neighbor assignment, already specialized and calculated in physical-interface §§2–5. Its physical motivation is a coupling graph responding to the field, with a second time slice retaining information. No quantum statistics, target angle, adjustable new gate or changed microscopic rule selects this process.

This candidate is distinct from CP-PREP-1's external Fredkin–Toffoli switch. It is **not a newly discovered coupling**: the native ring component and its preparation-source stop are already in the retained source corpus. This unit audits whether that actual write-and-retain process can supply the newly requested preparation–interaction–persistent-record chain. It does not repeat the earlier coupling proof or reopen its accepted source screen.

The positive test requires an executing native process, a produced common incoming resource law and selectable request, a sourced read/write/retention mechanism, and accounted failure and residual state. A conditional trajectory or a state coordinate named “record” is insufficient. **Stop at the first absent executing link; do not design a replacement or screen another candidate.**

**First absent link:** an accounted native producer of the root/request and common ready precursor feeding the selected interaction. In the existing loader even the quiet control neighbors `X_2=X_3=0` are supplied, while request selection and the other six hidden constraints remain unimplemented. The source evidence below supplies no such producer. Consequently the screen stops in Stage A; Stage B's controlled-settings comparison is not entered.

## 2. Source versions and their actual support

All repository sources in this table were read at D; relative links resolve to those same, unchanged files in this draft. Blobs identify the main-supported versions. Wider claims made by a source are not automatically premises here.

| Source at D | Blob | Claim used and limit |
| --- | --- | --- |
| [SM §3.1](../../../../../papers/SM.md#31-background-independence) | `7d805ac879cfd9561c0ede14507ad0c5b8e7b238` | The explicit ring update and its state-dependent-geometry motivation. No isotropy, continuum or graph-degree conclusion is used. This is a selected model branch, not established universal physics. |
| [Physical interface §§2–5](../oi-qm-ext-1/physical-interface.md) | `3229ef3cd234e613a4b0cb63bab548e0fec666a9` | Actual local coupling, complete declared observer cut, conditional histories and whole outgoing state; preparation, physical readout and reusable storage remain unsourced. |
| [Preparation-loading §§3–7](../oi-qm-ext-1/preparation-loading.md) | `1802ea3c335eb7457739fa5af13b3aefd0c603af` | Exact common precursor, forward transport and canonical-source countercontrol. It explicitly distinguishes the supplied prior/inverse image from its physical producer. |
| [Physical-controller source screen §§2–3, 7–8](../physical-controller-20261107/LEAD.md) | `ca4a61d585025a959eab909de3f6abbbe011eda1` | Earlier native ring source stop, general realization/control distinctions and bounded corpus trace. Its accepted negative finding is preserved, not rerun as a new discovery. |
| [CP-PREP-1 §§1–5](../controller-preparation-1-20261108/SELECTION.md) | `736ea7e3ce4d924f0e749baa2e9541a4913670bd` | The stopped external-switch embedding screen; no successful native switch or preparer is inherited. |
| [Rooted-family source audit Q2–Q7](../../../../audits/operational/rooted-observer-family-sourcing/result.md) | `34ea388d0fd47afe07bc9b41c79fe074898d493a` | Visible roots and a fixed common hidden prior are legitimate realization data; the canonical common-prior family is mathematically sourced. This does not identify a factory executing in this particular F. |

CP-PREP-1's primary comparator was rechecked directly: Fredkin and Toffoli, *Conservative Logic*, IJTP 21 (1982), 219–253, [§§6.1–6.4, especially p.241, Figures 16–17](https://gwern.net/doc/cs/hardware/1982-fredkin.pdf#page=23). Their billiard-ball switch uses collisions, fixed reflectors, arranged timing and supplied input constants. Neither that construction nor CP-PREP-1 identifies its degrees of freedom, reflectors and input sources with an executing process of this ring. This is an **unsourced embedding**, not a proof that embedding is impossible. Its physical-source gate stays NOT PASSED. No new external mechanism is selected here.

## 3. Unchanged dynamics and the one candidate

For `L>=9`, indices modulo L, let the whole state be `W=(u,v)` in `{0,1}^{2L}`:

```text
f_i(u) = u_(i-1) XOR (u_(i+1) OR u_(i+2))
F(u,v) = (f(u) XOR v, u)
F^-1(a,b) = (b, a XOR f(b)).
```

The admitted observer projection is unchanged:

```text
R_t = (u_t(0), u_(t-1)(0))
C_t = (u_t(1), u_(t-1)(1))
O_t = (R_t,C_t).
```

At site 0 the actual next value is `u'_(0)=v_0 XOR u_(-1) XOR (u_1 OR u_2)`. Thus an input at site 2 can enter the receiver through the rule's existing nonlinear term, subject to the other native fields. At the next ordinary update, that receiver value occupies the previous-time coordinate, since the second component of F is the old current field. These are subexpressions of **one whole-ring update**, not independently callable OR, XOR, copy, swap or inverse gates. No field is clamped between ticks.

The producer of the request and the proposed controller's internal state must also be fields evolving by F. Merely treating `C_t` as a controller or `R_t` as a memory does not construct a choice, clock or record-reading operation. No additional apparatus coordinates or private access ports are introduced by this report.

## 4. Input-production ledger and the first stop

For unambiguous comparison with the existing component, use its stated target and loader rather than invent a more convenient ready state. At precursor time `t=-1`, write `(X,Y)` and the visible root

```text
X_0=X_1=Y_0=0, Y_1=c.
```

The **supplied**, request-independent hidden law eta requires all eight hidden constraints:

```text
X_(-1)=X_2=X_3=0,
Y_(-2)=X_(-3), Y_(-1)=X_(-2),
Y_3=X_4 OR X_5,
Y_4=X_5 OR X_6,
Y_5=X_4 XOR (X_6 OR X_7).
```

As in preparation-loading §4.1, draw all remaining X fields independently fair, draw remaining Y fields independently fair and independent of those X fields, then determine the five dependent Y fields by these relations. This specifies a normalized law with the same uncontrolled fields for both c. The hidden source bit is `Z=Y_2 XOR X_4`. The equations specify **what a producer must deliver**, not an executing preparation proposal.

One F tick transports that supplied law to the already studied target `I_c(Z,xi)` at t=0:

```text
A_1=c, A_2=Z,
A_i=0 for i in {-2,-1,0,3,4,5},
B_i=0 for i in {-1,0,1,2,3},
```

with the existing independent fair free-coordinate law. This is preparation-loading's conditional identity, not a new source result. The ring applies its coupling whether or not those pins hold.

| Input/resource | Actual producer in the inspected sources | Status |
| --- | --- | --- |
| Selectable request `Y_1=c` and visible root blanks | Specified as realization data; no finite native request writer or root-preparation process identified | **Unsourced producer; assumed input** |
| Quiet neighbors and all eight hidden precursor constraints | Supplied correlated eta; no preparer, ordered reservoir or herald implementing that law identified | **Unsourced producer; assumed law** |
| `Y_2`, remaining free bits and fair Z | Normalized source law is explicit; a physical sampling/supply mechanism and its correlations with request apparatus are not identified | **Assumed law; unsourced supply** |
| Independent interaction setting | The two c-labelled initial roots are mathematical alternatives. No native actuation implements either request while preserving one common uncontrolled source | **Unsourced** |
| Timing, energy/work resources | F supplies an integer update index. It supplies no apparatus clock, work reservoir or energy-accounting convention for this experiment | **Unsourced apparatus accounting** |

The first executing link therefore fails **before** interpreting the subsequent field transfer as a ready, selectable measurement. Mathematical admissibility of eta remains intact: this report does not demand a uniquely selected global prior or deny the positive realization architecture. It demands the physical producer explicitly required by this owner scope.

For the canonical-root counting law `U_c`, preparation-loading's countercontrol gives `A_1=c XOR (X_2 OR X_3)`, so a visible request alone does not guarantee a correct load. The complete eight-constraint event has conditional mass `1/256` under U_c. That is a reference-ensemble mass, **not an apparatus success rate**. No repeat-until-ready procedure or finite readiness herald is asserted.

## 5. Readout, histories and remaining apparatus: what is and is not supplied

The following is an audit of the **existing conditional trajectory**, not further mechanism derivation after the stop. Physical-interface §5 gives, after a supplied `I_c(z,xi)`, the full declared local history:

| Tick | Receiver `R_t` | Controller `C_t` |
| --- | --- | --- |
| 0 | `(0,0)` | `(c,0)` |
| 1 | `(c OR z,0)` | `(z,c)` |
| 2 | `((1 XOR c)z,c OR z)` | `(c,z)` |

The observer includes both sites and both time slices. At tick 1 it can already distinguish z through C for **either** c; the masked receiver for c=1 does not make the complete observer record independent of z. Keeping only R would change the agreed interface.

The field at the next previous-time coordinate is genuine native retention for one tick. The source gives no separate readout interaction writing an observer log, completion flag, persistent tape, or repeatedly readable stable memory. An abstract history `H=(O_0,O_1,O_2)` is an analyst's description of accessible samples; its existence does not implement a physical history register. The declared access map is an input of this model; its apparatus realization remains open.

At the model level the **entire** residual state is `W_2=F^2(I_c(z,xi))`, not only its displayed R and C coordinates. Its conditional joint law is exactly the already retained

```text
(1/2) sum_(z=0,1) integral delta_(H_c(z), F^2(I_c(z,xi))) dnu(xi).
```

There is no erased exterior or independently resampled bath. At the physical level no preparer/request/clock/log apparatus has been constructed, so their additional internal states, accessible information and joint outgoing law are **unspecified**, not assigned zero size or zero cost. A future sourced device would have to account for them under this same F and access meaning. This report constructs no such device.

| Required operation/account | Source verdict and boundary |
| --- | --- |
| Native boundary coupling and delayed-slice transfer | **Derived** within the selected F; no external gate is needed to execute those field updates. |
| Common ready preparation and request/control write | **Assumed** as input data; executing producer **unsourced**, the first stop. |
| Measurement interaction giving an accessible persistent record | Transient coordinate transfer **derived**; physical logging/readback mechanism **unsourced**. The projection is **assumed** access. |
| Clock and synchronization | Update ordering **derived** from F; an observer-readable clock/start/stop mechanism **unsourced**. |
| Failure, reject, abort and no-read records | F is total, but an apparatus success/failure test and its output symbols are **unsourced**. No failed mass is discarded. |
| Retained apparatus and complete outgoing law | Whole field continuation **derived**, conditional on the input; actual producer/controller/logger residual state **unsourced**. |
| Automatic return to the old ready slice | **Disproved for that conditional trajectory as a general reset claim**: for c=1 the receiver's previous coordinate is 1 at tick 2; for z=1 the controller's previous coordinate is 1. This is the existing readiness-set countercontrol, not a general obstruction to other continuation contracts. |
| Renewal, retry/reset or fresh ordered bank | **Unsourced**. Mathematical invertibility grants no selectable inverse or free blank supply. |

Let E be exactly the conjunction of the eight hidden precursor constraints in §4; the visible root is already fixed by U_c. For any deterministic passive history/world map Psi, retain both terms:

```text
Psi_*U_c = (1/256) Psi_*(U_c | E)
          + (255/256) Psi_*(U_c | E^c).
```

This is the standard conditioning identity with preparation-loading's existing event mass. It describes no implemented herald, acceptance flag or retry protocol. Variable stopping, success/failure logs, attempt counts and consumed apparatus would need a real mechanism before a physical success probability could be stated. No apparatus failure law is inferred from F being total.

## 6. Scope, reference audit and verification

**Disposition: STOPPED / UNSOURCED; no source-qualified interaction selected for Stage B.** The actual boundary coupling is present in the chosen rule, but the authorized preparation–control–persistent-record process has not been sourced in this inspection. This conclusion is bounded to the named process and inspected source packet. It proves neither universal impossibility nor the absence of other native processes. No second candidate is proposed under this authorization.

The corpus search covered papers, book/FULL, verification records, Lean sources and tools for the ring, preparation, physical readout, native clocks and record production. Relevant native ring hits resolve to the sources above. General rooted realizations and action-labelled dilation are mathematical positives; their supplied priors/actions do not compile an actuator into this F. Native A, the linear-wave recovery and other declared apparatus models use different rules or supplied ports; they are context, not imported resources or newly screened candidates. No scientific checker or retained computational result was rerun.

The claim-by-claim off-main reference classification is:

| Reference | Attached claim | Classification |
| --- | --- | --- |
| #866 issue | Accountability for this unit | **Provenance**; no physical conclusion uses its discussion. |
| #866 owner-decision comment 6763916830 | Paper-only scope, one candidate, new guiding draft and separate review permitted | **Provenance of authorization**; its operative scope is stated in this report, not scientific evidence. |
| #1169 issue | Coordination destination | **Provenance**; no equivalence theorem is inferred. |
| #1169 coordination comment 6763928950 | Same bounded writer/reviewer handoff | **Provenance**; no native process is inferred from the handoff. |
| NATIVE-PRED-1 review named in the owner scope | The preceding predictive-capacity investigation motivates a physical source question | **Provenance**; its theorem, proof and acceptance are not premises of this stop. No off-main capacity result is inherited. |
| NATIVE-FACTOR-SRC-1 review named in the owner scope | The preceding factor/source investigation motivates a physical source question | **Provenance**; its factor constructions, obstructions and acceptance are not premises of this stop. No off-main factor result is inherited. |

The six source rows in §2 are **support on main** for their individually stated claims at D. The external primary article supports only the historical comparator description, not any native embedding. A future integration must recheck support reachability and every added review/status reference under AGENTS §A.42; this draft itself establishes nothing on main. A separate reviewer accepting this negative assessment would not pass the physical gate.

Verification consists of source reading, bounded hand substitution of the already stated local update, and document/link/whitespace and publication-scope checks. There is no new simulation, enumeration, numerical probe, Lean execution, physical-premise adoption, F/E designation, scientific dispatch or merge. Ordinary automatic draft-PR CI is repository validation only. Independent review must check the pushed immutable author head, source support, normalized input specification, complete observer cut, first stop and each off-main reference classification.
