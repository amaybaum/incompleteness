# Native recombination: two-read no-signalling source screen

Accountable home: #866; feeds #1169. Guiding draft: #1173.
Writer: ChatGPT Work coordinating session. Separate independent reviewer required.
Scope: paper only; one candidate and source audit, no implementation or physical posit adoption.

## 1. Decision protocol fixed before this unit's derivation

Authority: [owner activation and fixed rule](https://github.com/amaybaum/incompleteness/issues/866#issuecomment-6704318875).
Drafting snapshot: `3c446206c56e39dbd46dde77c96e91c30e904956`.
Candidate: [finite-wave correlation recombination](https://github.com/amaybaum/incompleteness/blob/9d24914c5006d775315189dadf56769e1e9cc847/verification/programmes/oi-qm/reconstruction/correlation-recombination-20261107/DESIGN.md),
reviewed at `9d24914c5006d775315189dadf56769e1e9cc847`.
The later shared-parity two-system apparatus is a different candidate and is not substituted.
Earlier results are known inputs; this is not a blinded protocol or an F/E designation.
This section is committed before appending the new source assessment and derivation.

1. **Common experiment.** Identify a common uncontrolled preparation law, two physically
   available Alice choices, Bob's fixed local protocol, and his complete accessible
   history through two reads. Include apparatus information, saved records, timing,
   readiness and failures. Alice's selected program may differ; do not change the
   uncontrolled hidden preparation with that choice. Record sharing after the isolated
   stage is allowed and is outside this comparison.
2. **Test.** Derive the complete Bob-history law for each Alice choice. Equal laws pass
   this bounded no-signalling test; unequal laws fail it, with an explicit history and
   probability witness. Equality of each one-read marginal is insufficient.
3. **Control.** B3's single-site measurement/instrument behavior must hold on the same
   model: identify its preparation, coupling, outcome and usable continuation, with their
   physical sources. Importing a matching formula from B3's different carrier is not a pass.
4. **Countercontrol.** A Bell-local classical shared-variable control with independent
   settings should pass no-signalling while obeying the classical Bell ceiling.
   Passing no-signalling alone supplies no quantum distinction. Compare the required
   Bell/Tsirelson restriction from #914 row 16; it is not enough to fit one Bell table.
   “Classical” here denotes the Bell-local control class, not a ban on deterministic ontology.
5. **Stop.** If equality requires a restriction without a physical source, identify it
   and stop. If the physical choice map, complete law or same-model B3 control is missing,
   report the specific source/specification gap rather than invent a pass or failure.
   Do not hide the problem by dropping accessible records, selecting only successful
   trials or installing a new preparation/reset/access rule.
6. **F2 and extension.** Locate and reuse the existing resource-conditioned
   sufficiency/assembly statements at their proved scopes. Audit what physical resource
   the candidate supplies. Reproving those statements is outside this unit.

The source review must distinguish material on main from unlanded research, inspect the
supporting claims and their assumptions, and retain observer-relative access throughout.
Only this file is in the author write scope. The candidate and previous papers remain
unchanged. No scientific run, workflow dispatch, manuscript change, merge or successor
mechanism is authorized.

## 2. Result and first stopping point

**Author result: STOP — physical experiment/interface not supplied.**
The native candidate supplies a complete conditional law for its declared passive
receiver. It does not supply the two selectable Alice interventions, one common
physical preparation, and the full Bob apparatus needed to turn that law into the
commissioned isolated-setting comparison. B3's instrument has not been realized on
this same finite-wave model. Consequently there is no physical no-signalling PASS
or FAIL for this candidate from the present sources.

The first missing object is a source-level protocol map: a preparer/controller
operating under one underlying law, implementing Alice's two choices with their
actual supports and timing, and defining Bob's read/access boundary through the
second read. The existing two correlated laws are not that map. This is a specific
source gap, not a theorem that OI cannot supply such a map.

The conditional calculation below sharpens the future test without filling the gap
by assumption. The same receiver exposes the input parity. Equalizing its two
setting-conditioned parity laws would equalize these registered records; whether a
physical mechanism does this while retaining B3 and the required Bell behavior is
precisely unproved. Equal registered records alone would still not certify equality
of an apparatus's larger accessible history.

The paper protocol was first committed at
`24a3f9b315b3245ddc6f4d7f5d4adcba00085b6b`; §§2–7 were appended afterward.
Independent review and ordinary repository CI are recorded on #1173 at an exact
head. This is branch research, not an established physical result on main.

## 3. What the candidate actually defines

Use the unchanged candidate's binary fields on the cubic torus with L >= 9:

    Phi(u,v) = (A u-v,u),       R_t = (u_t(0),u_(t-1)(0)).

A sums the six nearest neighbors. The declared receiver is a mathematical proper
subsystem projection, not a constructed laboratory detector. The registered window
starts with R_0 and has fixed ticks; no earlier apparatus records have been proved
absent. The source does supply this observer-realization projection and a common
hidden prior for each declared realization. Those positive results are retained.

For b in {0,1}, DESIGN.md §2 uses a fair Z, u(e_x)=Z,
u(-e_x)=Z XOR b, all other current coordinates in B_3 zero and all previous
coordinates in B_2 zero, with a common independent exterior. These are two
different hidden preparations mu_b at the same receiver root R_0=(0,0).
Each satisfies one parity condition and 86 zero pins. Under uniform counting its
conditioning event has mass 2^-87; that mass is not a physical success rate or
a supplied herald.

The native update and inverse are supplied by the reference wave rule.
No selectable setting register, Alice readout, physical loader, detector interaction,
failure flag or Bell separation geometry is supplied by this preparation formula.
In particular, b is an input-correlation label, not an independently sourced
post-preparation measurement choice.

### 3.1 Exact law of the two registered receiver records

Let T=u(e_x) XOR u(-e_x). Retain the stated zeros and exterior contract, but allow
any joint law of the two input bits. From the same rule,

    u_1 = A u-v,
    u_2 = (A^2-I)u-A v.

Only the two input sites contribute at tick one, so u_1(0)=T.
There is no two-step nearest-neighbor walk from either input to 0 in this
unwrapped geometry, and all other contributing coordinates vanish, so u_2(0)=0.
Thus the entire declared two-read history, including its registered prefix, is

    h_T = (R_0,R_1,R_2) = ((0,0),(T,0),(0,T)).                 (1)

No averaging of one-read marginals was used. Both input values and the exterior
continue in the complete world; the reads are passive, with no reset.

For any *mathematical* input law kappa_x obeying that support contract, put
p_x = kappa_x(T=1). The registered history law is exactly

    P_x^reg = (1-p_x) delta_(h_0) + p_x delta_(h_1).           (2)
    P_0^reg = P_1^reg  iff  p_0=p_1;
    TV(P_0^reg,P_1^reg) = |p_0-p_1|.                         (3)

Here x is only an index of conditional laws until a physical choice map is
provided. Because h_0 and h_1 are distinct, event {R_1=(1,0)} proves (3).
For the candidate's mu_b, p_b=b, so the laws are the two distinct point masses
delta_(h_0), delta_(h_1), with total variation one.

This is **preparation distinguishability**, not the commissioned isolated-setting
verdict. Identifying x with b would silently replace the common uncontrolled
preparation with a choice-dependent hidden law. An actual operation could generate
different post-intervention laws from one common initial law; its construction,
support, timing and accessible records must then be given. The paper does not
forbid such an operation or assert its existence.

The candidate's inputs are one graph edge from the receiver. Their influence at
tick one is ordinary propagation within the reference graph cone. A comparison
that allows Alice to write one of these inputs and Bob to read afterward is not,
without further physical geometry, a comparison of isolated Bell interfaces.
There is no claim that every preparation dependence is prohibited by QM.

### 3.2 Complete physical history and failed attempts

For an actual protocol, H_B must include Bob's program/apparatus information,
read times, saved results, readiness, aborts and other accessible local records.
With a common uncontrolled seed law mu and sourced loaded dynamics, one would
derive

    P_x(H_B in E | Bob's fixed protocol)
        = integral 1[H_B(lambda,x) in E] d mu(lambda).         (4)

Neither the load/interaction map nor H_B for that apparatus is currently supplied.
The observer projection is supplied at the realization layer; the missing item is
its implementation as this controlled, two-wing, complete-record experiment.

Equation (2) is therefore the complete law for the *declared receiver*, not a
fabricated complete laboratory law. If this receiver history embeds into a physical
Bob history, unequal registered laws would already imply unequal full laws.
Equal registered laws would only be necessary: another accessible record could
still signal. A supplied herald would require the joint flag/history law including
failures; conditioning on the analytic event defining mu_b is not a substitute.
Later communication of Alice's records is allowed and lies outside (4)'s isolated
stage. No information is required to remain hidden from every possible observer.

## 4. Same-model B3 control and classical countercontrol

### 4.1 B3 is not yet a control pass on this model

B3 §§1–6 uses a nonzero real four-component signal, represented in C^2; a quadratic
sensor; independent seed slots; ready reference carriers; and a detector-conditioned
exchange that retains the old signal. Under the uniform seed benchmark its two-read
law, rows/columns ordered 1,0, is

    [[cos(theta)^2 cos(phi)^2, cos(theta)^2 sin(phi)^2],
     [sin(theta)^2 sin(phi)^2, sin(theta)^2 cos(phi)^2]].       (5)

Its conditional outgoing signal is the recorded basis carrier. The same fixed
qubit instrument, both port calibrations, balanced and off-center preparation,
phi=0 repeatability and phi=-theta continuation are compared. B3 itself identifies
native carrier/control and exchange/public-access sourcing gaps.

The binary-wave candidate has no sourced map to that carrier, drive family,
sensor/seed law, reference bank, exchange or coupled read access. Equation (1)'s
return of a classical bit is not (5)'s instrument control. Nor does a global
permutation representation of the binary world provide these selectable operations.
A same-model proof must identify their physical realization and account for other
available reads; it may not splice B3's real model into this finite one.

**Control status: NOT SUPPLIED on the candidate.** No mathematical failure of a
fully specified B3 realization is claimed, and no qualified no-signalling success
is printed over this absent control. B3's conditional result remains unchanged.

### 4.2 Classical behavior can give equal complete histories

The candidate is already a classical reversible calculation. Its existing
decorrelation control (DESIGN.md §6) keeps the same ready region and draws the two
input bits independently and fairly. Then T is fair, and for either inert label x,

    P_x^reg = (1/2) delta_(h_0) + (1/2) delta_(h_1).           (6)

Both entire registered histories agree, although the records retain a common
classical parity across time. This is a conditional algebraic control; the inert
labels are not two newly sourced measurement choices, and no physical decorrelator
or full two-wing apparatus is thereby constructed.

For a complete Bell-local classical control with independent settings, include
memory and local random seeds in a common response variable Omega. Bob's two-read
history, including local apparatus and failure records, has the form G_y(Omega);
Alice's setting x does not enter that function and p(Omega) is common. Therefore

    P(H_B=h | x,y) = sum_Omega p(Omega) 1[G_y(Omega)=h],       (7)

independent of x. Adaptive local second choices can be part of y's fixed decision
rule. This demonstrates why memory and reuse are compatible with classical
no-signalling. It is a mathematical control class, not a physical restriction
newly imposed on the target. A graph-cone-separated realization of the same local
wave rule falls in this class under Main §3.3's screened-local hypotheses, provided
the separation covers the entire read/access window.

For the every-run binary Bell outcomes in that theorem, the same common-response
construction obeys |S_CHSH| <= 2. No selected-success Bell statistic is being bounded
without its required detection assumptions. A quantum Bell example reaches 2 sqrt(2);
a no-signalling PR table reaches 4. Main §3.3 already records that the unrestricted
finite response construction admits the latter. No-signalling alone cannot select
the quantum set or establish either direction of #1169's equivalence.

### 4.3 The stopping rule forbids an unsourced repair

Three apparent shortcuts would fail the fixed rule:

- Replacing the original two correlations by the common fair-input law makes (6)
  equal, but does not source selectable quantum measurements or preserve B3.
- Declaring the parity coordinate, old record or preparation log inaccessible could
  remove a witness on paper. A physical access restriction must explain why the
  actual observer cannot use it; it cannot just discard available data.
- Choosing graph separation to enforce pointwise local independence gives (7) under
  the screened-local hypotheses, but then the existing Bell ceiling applies. To
  reach the target Bell violation one needs a sourced departure from those
  hypotheses, together with full-history no-signalling and a quantum correlation
  bound; none is supplied by simply enlarging the inaccessible sector.

These are diagnostics, not adopted successor mechanisms. At the missing physical
protocol map and same-model control, this unit stops. It does not insert a reset,
fresh masking law, special prior or read restriction to obtain a pass.

## 5. F2: use the existing assembly at its actual scope

The current PROGRAMME.md §5, Arc F, F2 specifies a physically transparent and
separately testable extension sufficient for finite operational QM, with normalized
probabilities, available tests and arbitrary finite composites; necessity and
minimality are assessed separately. Arc D's physical-lift seam requires the *same
source* to survive ancilla attachment/discard, instruments and composite operations.
#914 distinguishes extension, sufficiency and necessity as open programme
obligations, while naming the conditional assembly results that already exist.

The checked kernel interfaces give a precise reusable destination:

| Existing result | Granted data and scope | Not supplied for this candidate |
| --- | --- | --- |
| GeneralCarrier.exactAll_iff_physical_general | Every nonempty finite A; ExactAllFiniteEndomorphicQuantumOps iff the five PhysicalCompletionConditions | A physical realization of those conditions on the native carrier |
| MinimalRepertoire.qm_of_oiPlusMin and oiPlusMin_iff_qm | On the existing matrix-operation theory, implementation locality, phase-free richness and embedded observation suffice, with the converse | Native sources of that package and its operational interpretation |
| OperationalAssembly.circuit_available | An available preparation, composite unitary control, native ancilla readout and the theory's closure fields assemble an available instrument family | Availability of that control/readout/preparation in this wave experiment |
| OperationalAssembly.pureSeedPrep_available_of_swap | Uniform attachment, readout, feed-forward and the specified ancilla swap control yield a pure seed | Physical implementation of the used readout, swap and resource supply |

FiniteOperationalTheory already uses complex-matrix linear branch maps and supplies
availability/closure structure. Its readout's local Lüders form is derived from the
readout-existence and spectator-independence fields; it is not an unconditional
claim that the native detector exists. The five conditions are valid probabilities,
inert spectators, composite unitary control, iterated ancilla closure and trivial
ancilla consistency. ExactAll covers the system and every positive composite
level. These statements are not being reproved here.

ImplementationLocality's current InstAvail is a whole-instrument protocol predicate
with step, readout, coarse-graining, bind and discard constructors. It does not
license arbitrary recombination of separately available branches. The existing
instrument-realization audit and its recorded migration matter at precisely this
source boundary.

Operational equivalence means equality of the covered experimental histories in a
common interface, including the operations the physical model actually admits.
Matching a few receiver laws or having an abstract equality of available matrix
operations does not by itself construct that interface or the two-way map.
The accepted Gate A ledger retains all density preparations, instruments and finite
adaptive depths in J_exact(A). This bounded two-read screen does not narrow it.

Thus the next missing proof is physical extension/sourcing, not another proof of
the assembly theorem. Even a future successful bounded no-signalling/B3/Bell test
would supply only evidence at that scope; arbitrary composition, all admitted
operations and both directions would remain to be proved.

## 6. Source pins and verification scope

Current main snapshot: `71b190f7e8eaf1eb3e1002e3f6c1cd833afacddd`.
Research inputs are at the drafting snapshot `3c446206c56e39dbd46dde77c96e91c30e904956`
unless their original reviewed head is named. File blobs were checked; labels or
Issue state are not used as scientific premises.

| Material source | Pin / checked content | Role and limit |
| --- | --- | --- |
| [Candidate DESIGN.md](DESIGN.md) | Blob `b390714035a3da06d9007420a41957be2b07c348`; unchanged from reviewed `9d24914c` | Conditional preparation, native rule, passive receiver and physical-source boundary |
| [B3](../oi-qm-ext-1/measurement-exchange.md) | Blob `aeaa8ca03f187bd0adda82532faf3154f4b4dd5f`; unchanged from reviewed `1514d3bb` | Conditional same-instrument law and explicitly unsourced native exchange |
| [Gate A](../oi-qm-ext-1/endpoints.md) | Blob `d9d92e038a8022e854586101067ce4de9789fdf6` | Common model, fixed uncontrolled law, all accessible procedures and full target |
| papers/oi_lattice_code/trace_out_fractional/wave_eqn.c | Main blob `c56e64cef4922cf61b8854a6626585154060ad18`; wave_step/inverse equations | Reference mod-q rule only; neither packed execution nor the header's obsolete coefficient-selection claim |
| papers/Main.md §3.3 | Main blob `a954cfb47c740766b8ca6ab9027a46bbf6fa2f94` | Pointwise graph cone, screened Bell ceiling and unrestricted PR countercontrol |
| verification/audits/operational/rooted-observer-family-sourcing/result.md Q2–Q7 | Main blob `34ea388d0fd47afe07bc9b41c79fe074898d493a` | Supplied realization projection/common prior/structured-law scope; no selectable correlated-input loader |
| verification/programmes/oi-qm/PROGRAMME.md, Arc D/F2 | Main blob `03ea3bdd774ae225bf6058231f90e566d7593fad` | Extension target and physical lift seam, not evidence that the extension is supplied |
| OIBridge/GeneralCarrier.lean, PhysicalCharacterization.lean, LevelOneSeam.lean | Main: `778fd9fc8ccc26084bced15f15c1148d648870e6`, `1a96e2454009638cee5bd3569b3bbcd5ec791d3a`, `57805fe4ff5cd7b37ffa5ebe026f817a366605aa` | Exact statements and their five-condition/composite definitions |
| OIBridge/MinimalRepertoire.lean, OperationalAssembly.lean | Main: `7df37d3f606350f547985c3d577faba106a76a56`, `592d8203c488914fe36c3e1b1371eb5efa9af3ca` | Existing sufficiency and resource-consuming circuit/seed assembly |
| OIBridge/ImplementationLocality.lean; operational/instrument-realization-audit.md | Main: `d96b65bd262e658baf0be52cfaf4b6e33de0dd28`, `5100df79fafbb67440401341d9699d9184985fec` | Whole-instrument provenance and migration; no free branch mixing |
| substratum/continuous-substates/native-link-sourcing-gate.md | Main blob `cb0577802d0a85c36883d21274813cca45fe1d14` | Actual reference rule versus added pointer/interaction models |

The OIBridge paths are under verification/lean-mathlib/.
The final two abbreviated audit/programme paths are respectively under
verification/audits/ and verification/programmes/.
The later two-system-interface.md is a separate author analysis awaiting its own
review; its shared-parity signalling calculation is not a premise of (1)–(7).

This unit used source inspection and written derivations only. No simulation,
enumeration, Lean build or scientific execution was performed. Ordinary PR CI
checks repository consistency and does not certify a physical resource.

## 7. Closeout and routing

The fixed test remains **not evaluable as a physically supplied isolated-setting
experiment**. Its registered-receiver conditional law is (2), with exact equality
criterion (3). The same-model B3 control is missing; the classical controls show
why equal histories alone would be insufficient.

#866 retains the first concrete task: source the common preparer/setting/interaction
map and its complete public access through reuse. The existing ready/fresh supply,
measure selection and retention obligations remain at #1147, #1059 and #1032;
composite sourcing remains at #868 and reusable instrument composition at #913.
These are existing dependencies, not newly authorized units. #1143 retains its
distinguishing test and #914 row 16 its Bell/Tsirelson obligation. #1169's full
equivalence remains open. No successor mechanism is adopted and no issue is closed.
