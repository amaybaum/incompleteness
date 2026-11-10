# NATIVE-PREP-SRC-1 — Quiescent-bank loading and preparation-source viability

**Author disposition: STOPPED / UNSOURCED. Physical-source gate: NOT PASSED.**
Paper-only author assessment; independent non-author review is a separate gate.

Accountable home: [#866](https://github.com/amaybaum/incompleteness/issues/866); coordination: [#1169](https://github.com/amaybaum/incompleteness/issues/1169). Writer: Codex. The owner said **“Authorize the bounded preparation unit”** in the current Codex conversation on 2026-11-10; the [recorded scope](https://github.com/amaybaum/incompleteness/issues/866#issuecomment-6765161496) permits one source-first preparation screen and a separate review, with a viability assessment if the source fails. Source/drafting snapshot D is main `cac5d26441dd33e9348151487e4df7b547195481`.

## 1. One screened proposal and its stop

The sole proposal is **ordinary native loading from a quiescent bank containing a request and a seed**. A bank of zero-valued two-slice fields is a simple product-form resource for classical initialization. Preparation-loading §6 already identifies ordered ancillas/reservoirs as possible resources that must be accounted for. SM §3.1 supplies the actual forward update. The motivation is ordinary memory preparation and information transport, with no quantum probability table or fitted rule.

The bank is a **proposed incoming resource**, not an independently established physical source. “Quiescent” here means specified zero fields, not a derived vacuum, ground state, cold bath or energy minimum. The source screen must identify an executing producer of that resource and selectable request before treating its subsequent loading as physical preparation.

**First missing executing link:** no producer of this ordered bank, its common incoming law and selectable request is identified in the inspected source packet. Supplying a simpler product distribution does not supply that producer. The candidate fails physical qualification at its incoming-resource link. No bank factory, reset, herald or alternative candidate is constructed after this stop.

The input-side comparison below makes the failure precise: this bank satisfies the eight precursor constraints, requires **more** ordered coordinates than their existing conditional law, and supplies only a restricted ready-state law. It is a mathematical source-accounting countercontrol, not a successful physical mechanism.

## 2. Fixed model and existing target

All indices are modulo a ring of L>=9. Keep the unchanged rule

```text
f_i(X) = X_(i-1) XOR (X_(i+1) OR X_(i+2))
F(X,Y) = (f(X) XOR Y, X).
```

The original observer reads `(X_0,Y_0,X_1,Y_1)` at each admitted cut. It receives no extra bank-read port. At the precursor cut the request root is

```text
b_c: X_0=X_1=Y_0=0, Y_1=c.
```

Preparation-loading §4 identifies the following eight hidden constraints, denoted E:

```text
X_(-1)=X_2=X_3=0,
Y_(-2)=X_(-3), Y_(-1)=X_(-2),
Y_3=X_4 OR X_5,
Y_4=X_5 OR X_6,
Y_5=X_4 XOR (X_6 OR X_7).
```

Its common law eta is the canonical-root law U_c conditioned on E, with the prescribed independent fair free fields. One F tick transports that supplied law to its full target I_c. This retained conditional transport is reused at its actual scope; no inverse image is called a producer.

## 3. The proposed simpler input and its exact resource account

Let `V={-3,-2,...,7} mod L` and `m=|V|=min(L,11)`. The proposed bank law beta_c is:

```text
X_j=0                     for every j in V;
Y_j=0                     for every j in V except 1 and 2;
Y_1=c;
Y_2=Z, with Z fair;
all X and Y coordinates outside V independent fair, also independent of Z.
```

This is one normalized product law with the same uncontrolled fields for both c values. It is a compact description of **supplied initial data**. It is not a random-bit generator, a setting writer or a physical preparation protocol. For L=9,10,11 the bank covers the whole ring; for larger L it is a finite window. No proper local apparatus is claimed for all ring sizes.

Every X field appearing on the right side of E is zero in this bank, and the five dependent Y fields are zero. Thus beta_c is supported on E. Also `Z=Y_2 XOR X_4=Y_2`. Applying the existing transport identity pointwise places F(beta_c) in the old ready **set**. This input check does not derive the physical source of a single bank bit.

**The full source law changes.** Beta_c is a strict subensemble of eta: for example `X_4=0` under beta_c, while X_4 is fair under eta. After loading, the retained field at site 4 is therefore fixed in F(beta_c) and fair in the old I_c law. The native pointwise ready conditions are preserved; the complete old preparation/world law is not reproduced. No equality of arbitrary later complete histories is asserted. A subset of ready states is not automatically the full previously specified source.

The ordering account is exact hand counting relative to U_c, not a physical energy calculation. The visible root already fixes four bits. The bank additionally fixes `m-2` X coordinates and `m-3` Y coordinates, leaving Y_2 free. Hence its additional ordered coordinates number

```text
r = (m-2)+(m-3) = 2m-5,
H(U_c)-H(beta_c) = r bits,
U_c(bank event) = 2^(-r).
```

The bank has `2(L-m)+1` free bits, so its entropy is `2L-2m+1`; U_c has entropy `2L-4`. This independently gives the same deficit. It is 13 bits for L=9, 15 for L=10, and 17 for L>=11, compared with the existing eight-bit deficit of eta relative to U_c. The short product-form description uses an extra 5, 7 or 9 ordered bits beyond eta.

This count concerns **this chosen bank only**. It is not a minimum for all product sources, a universal apparatus-memory bound, a heat/work cost, or a trial-success probability. No ensemble event has become an implemented acceptance flag. The comparison shows why syntactic simplicity cannot by itself establish a cheaper or physically available resource.

## 4. What the source audit supplies

All main-supported sources below were read at D. Relative links resolve to the same unchanged files in this draft.

| Source and exact main blob | Claim consumed here and its limit |
| --- | --- |
| [SM §3.1](../../../../../papers/SM.md#31-background-independence), `7d805ac879cfd9561c0ede14507ad0c5b8e7b238` | The selected state-dependent rule and its reversible two-slice dynamics. It supplies no physical identification of the bank as a cold reservoir. No continuum, isotropy or graph-degree claim is used. |
| [Preparation-loading §§3–6](../oi-qm-ext-1/preparation-loading.md), `1802ea3c335eb7457739fa5af13b3aefd0c603af` | Exact root, E, eta/I_c transport, eight-bit reference deficit and the existing alternatives requiring ordered resources or a real herald. The latter are possibilities to source, not implemented devices. |
| [Physical interface §§2–6](../oi-qm-ext-1/physical-interface.md), `3229ef3cd234e613a4b0cb63bab548e0fec666a9` | Existing native loading/record component and whole-world continuation, with preparation, readout, request and renewal limits. No new physical controller is inherited. |
| [Main §1.2 and §3.4](../../../../../papers/Main.md), `5b73da5743f39aef080d02cc0a06bcaab4704f9f` | Fixed hidden priors are legitimate realization data; the action-labelled dilation constructs a different finite realizer with supplied actions, clock and ledgers. It does not compile a bank producer into this F. |
| [Observer-interface assessment §4.6.2–4.6.3 and §5](../observer-interface-obsmu-20261104/ANALYSIS.md), `7284f4553bebdfae26a8c2a0842eb15371713f1f` | Record conditioning is an existing construction step; H-PREP remains open. The conditional laboratory reduction needs correlations, retained/reliable records and readiness. It does not construct preparations, and using a ready record to supply readiness may be circular. |
| [Book Chapter 18, arrow-of-time discussion](../../../../../book/ch18-beyond.md), `ace0bad4927070061ae4d78e8415dd9a97f6fc16` | A cosmological low-entropy boundary is explicitly stated, with alignment unresolved. It does not identify the local beta_c law, an addressable blank bank, a request source or a native clock. No denial of that existing boundary input is inferred. |

The bank proposal does not acquire a physical source by being permitted realization data. A cosmic low-entropy condition does not specify which local fields are blank or how the apparatus places c while keeping one common uncontrolled law. Nor does conditioning on a future ready event implement a selector of that event.

Static corpus searches covered papers, book/FULL, verification records, Lean sources and tools for blank banks/registers, ordered ancillas/reservoirs, quiescent/quiet resources, native preparation and H-PREP. Relevant hits were read at their source scope. Computation's efficient preparation/control and clock are model hypotheses; the C4 preparation-scope record indexes mathematical predicates, not a bank factory. Native A and other declared apparatus models use different rules or supplied interfaces. None is spliced into this ring, and no other mechanism is selected as another candidate. This supports only the bounded source finding for the present bank.

## 5. Complete preparation and residual-state ledger

| Required link | Status for the one bank proposal |
| --- | --- |
| Actual ordinary F loading | **Derived**, conditional on its incoming state; inherited native operation, not a new actuator. |
| Product law beta_c and eight constraints | **Derived as mathematical input relations**; physical production of beta_c is **unsourced**. This is the first stop. |
| Selectable c and root blanks | **Assumed input**. No native writer or jointly accounted request source is identified. |
| Fair Z and exterior source | **Assumed normalized law**. No physical sampler or full producer/apparatus correlations are supplied. |
| Ordered bank supply | **Unsourced**. “Zero,” “vacuum,” “low entropy” and “available blank” cannot be substituted for one another. |
| Timing, clock, work/energy | Tick ordering is mathematical. Physical start/stop, synchronization and a work/energy account are **unsourced**; no reservoir is assigned zero cost. |
| Observer/controller access | Original two-site/two-slice projection retained as the declared cut. It does not expose all bank pins or provide a readiness sensor. |
| Fail/reject/abort, herald and retries | **Unsourced**. No accepted subset or retry law is implemented; all non-bank source mass remains outside the assumed beta_c experiment. |
| Remaining native field state | Given beta_c, the **entire** output is F(X,Y). The old X field remains in its second component, the exterior is evolved and correlated, and no independent bath is redrawn. |
| Producer, request writer and ancillary records | Their microscopic state, acquired information, emitted records and joint outgoing law are **unspecified** because the device is not constructed, not because they vanish. |
| Renewal/reset | **Unsourced**. Mathematical bijectivity supplies neither an observer-operated inverse nor fresh banks. |
| Persistent measurement record | Remains a separate later obligation. This unit neither requires it as an already supplied resource nor constructs it. It supplies no free preparation-success record. |

There is no physically supplied attempt process on which to define an apparatus success probability. F is total and preserves each ensemble's total entropy; those facts do not create a success/failure display. A real herald would need an actual interaction, observable outcome, full rejected mass, stopping/clock mechanism and retained apparatus state. An adaptive protocol is not ruled out by the old fixed-time counting bound and is not implemented by this bank law.

## 6. Source-viability decision

**End this unit at STOPPED / UNSOURCED. Do not continue the same preparation route by inventing another input law.** The bank's simple mathematical specification has not identified a physical producer. An independent reviewer may accept this source stop without passing any physical gate.

| Question for viability | What this unit supports | Decision within the present scope |
| --- | --- | --- |
| Is the selected SM ring ruled out? | No. The native update and conditional transport stand; no universal obstruction to preparation has been proved. | Retain it as a mathematical testbed. Pause its promotion as a sourced preparation apparatus until a genuine producer/resource lead is identified. |
| Are eight explicit hidden constraints the unique physical target? | No. They are the existing sufficient complete-source contract, not a proved necessary form for every operational implementation. The present stronger bank satisfies them with a different law. | Preserve the old target and its qualifications. Any proposed weaker target needs a separately authorized operational justification with complete histories; this unit makes no replacement. |
| Has a simpler initial law solved preparation? | No. This product law has a larger ordering deficit and still needs physical production. | Stop substituting shorter descriptions for producer evidence. A separately justified resource/boundary condition would have to be identified and accounted for before adoption. |
| Is the original observer impossible or sufficient for a herald? | Neither conclusion is established. No bank-readable sensor, autonomous preparation controller or success log is supplied. | Keep the original cut. Any changed apparatus/interface requires independent physical motivation and separate authorization. |
| Should there be another nearly identical source screen now? | The inspected sources have not supplied a new executing link. Repeating conditional input transport does not close it. | **No automatic continuation.** Return a model/target/interface/source-viability decision to the owner before another producer candidate or scientific test. |

The recommendation is therefore to retain the accepted conditional mathematics and stop this fixed-source construction pipeline here. A future choice among resource justification, a revised operational target or a different physical realization must follow new independent source evidence, not a preference for matching QM. No such alternative is investigated or authorized by this report.

## 7. Reference standing and verification

| Off-main reference | Attached claim | Classification |
| --- | --- | --- |
| #866 issue | Accountable home | **Provenance**; no mathematical premise supplied by the issue. |
| #866 comment 6765161496 | New one-unit owner authorization and stopping rule | **Authorization provenance**; its operative limits are stated here, not used as physical evidence. |
| #1169 issue | Coordination | **Provenance**; no equivalence or source result inherited. |

Earlier stopped reports and the concurrent selection review motivate this phase administratively; none is a scientific premise of the bank calculation. Its proof is given here, and each consumed external source claim is supported in the named main files at D. No off-main Page or prior acceptance is substituted for a physical producer. Before any eventual landing, the exact source reachability and added review/status references require their own §A.42 item-8 trace. No integration exception or scientific promotion is granted here.

Verification is source inspection, bounded hand algebra/counting, and document/path/whitespace/publication checks. No simulation, enumeration, numerical probe, Lean execution, physical construction, new premise, F/E, special dispatch/rerun, frozen-record edit or merge occurred. Ordinary automatic draft-PR CI is repository validation, not a native preparation experiment. A separate non-author reviewer must check the pinned source packet, small-ring aliases, entropy count, distinction from the full eta/I_c law, physical stop and viability scope.
