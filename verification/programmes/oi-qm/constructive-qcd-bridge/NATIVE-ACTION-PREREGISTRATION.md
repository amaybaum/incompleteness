# GA-1: native gauge-link dynamics and action sourcing

Status: research preregistration draft; no execution or physical premise adopted.
Guiding PR: #1003. Drafting parent: `2234f62b171d95ce2be41aeaa72b4da7ae6210cb`.
This checkpoint is on a separate staging branch for the designated writer to
review and integrate; it does not transfer ownership of #1003's branch.

## 1. Question and authority

Does one specified OI microscopic update physically source evolving
gauge-invariant link observables and select their law, rather than merely
admit a covariant description? Link availability, dynamical evolution,
stationary measure, effective action and operational access are separate claims.

The owner authorized preregistration and independent review only on 2026-11-01.
No new experiment, calculation, simulation or Lean build is authorized here.
No manuscript, ROADMAP, premise, proof grade, F/E designation, special workflow
or merge changes. MR-1 #1023, Lane A #1009, PC-1 #1022 and their protocols and
writer branches are outside the write scope. Finite-horizon S ⇔ D ⇔ Q_fb is
an established input, not a physical gauge mechanism or a target to reopen.

This is not a native V3 round or an F candidate. Independent acceptance of
this plan would establish readiness for a source audit, not authorize a run.

## 2. Fixed starting evidence and limits

| Anchor | What it supplies; what must remain conditional |
| --- | --- |
| #1003 parent, `constructive-qcd-bridge/README.md`, blob `948c7ee84dba205da2590a787b06f6020f707c9b` | Exact ambient SU(2) Wilson-versus-squared-functional countercontrol. Covariance alone does not select an action. No native OI counterexample is inferred. |
| `papers/SM.md` at `c596904a9adf61649e65c9035d9d2ad7011f56a8`, blob `e5aa24ba7c81e6d53d9c7d9ea90268b730d03eff`, §§3.1, 4.1, 4.2, 6.1 and 6.5 | H-link/H-cust and single-copy assumptions; coefficient/observer closure qualifications; induced determinant proposal; explicit exponential non-abelian link candidate, measure and map hypotheses; abelian flat-image obstruction and H-observer-bundle/H-Y-vertex. These existing constructions must be examined before any absence claim. |
| `OIBridge/A6Instantiation.lean` at the same `c596904a`, blob `dc8060f0f4ffe26d3adea7139462430120c4a30c`; `BackgroundIndependence.lean` and ROADMAP P1 | Covariant link-coupled interface and its conditional physical identification. `a6cov_all`, `pk1_packaging`, `pk2a_bridge`, `cx1_complex_covariance`, `cx3b_complex_not_A1` delimit the formal scope. The historical finite-A1 result is not a prohibition on the owner-adopted infinite-carrier research formulation. |
| `papers/oi_lattice_code/trace_out_fractional/wave_eqn.c` at `c596904a`, blob `c56e64cef4922cf61b8854a6626585154060ad18` | A finite scalar reference update with coefficient 1 and intended inverse; not a uniquely selected physical coefficient, six-component gauge mechanism or source of a determinant measure. |
| #1003 comment 6526315429 | Conditional site-only equivariant-link rigidity argument, pending independent review. Its full free-transitive site-action premises must be tested before use. Fixed nontrivial background curvature is allowed; fluctuating loop conjugacy classes are the issue. |
| #1011 `4e7ddb70749e7ee49f43f5af2707a84524d1226a` and comment 6546748788 | Separate classical recursive/profinite controls and scoped F2-1 gap. Frozen G★ has a reported overstatement; neither it nor its correction selects a gauge action. No adoption or modification here. |

These are exact historical anchors, not a claim that they are current main.
At source-audit start, record current main and compare relevant source passages
against these pins. Preserve both versions; a material change requires a reviewed
amendment, not silent substitution. Before a gap/no-go claim, search papers,
book/FULL, Lean, verification records and the existing §6.5 implementations.
Classify paper proofs, formal statements, finite controls and hypotheses separately.
External constructive-QCD announcements are deferred; no theorem comparison or
mass-gap inference is part of GA-1.

## 3. Bounded stages and candidate gate

**Stage S, prospective source audit:** trace at most three existing families,
in this order: (a) SM §6.5's exponential non-abelian construction and its stated
measure; (b) the packaged link-coupled A6 interface and its proposed physical
instantiation; (c) the native scalar reference construction as a control.
Use read-only source inspection and written dependency tracing. No new evaluation
of candidate loops, determinants, spectra, fits or outcome statistics occurs at S.
If no complete candidate is sourced, close S as `GAP-SOURCE` with the missing
map, dynamics or measure condition named. Otherwise report `SOURCE-CANDIDATE`
with every conditional input listed. These are source-audit dispositions only,
separate from §6's outcome-execution table; neither licenses computation.
Record operational access independently as specified below. This is not a
global no-go.

**Stage A, prospective candidate amendment:** before any outcome computation,
the designated writer must publish one immutable, independently reviewed GA★
containing all the following, then obtain separate owner execution authorization:

1. Carrier S, microscopic update φ and inverse, all apparatus/environment fields,
   graph, alphabet, volume/boundaries and fixed parameters. Infinite/continuous S
   is allowed with measurable dynamics and normalized states; total finiteness
   is not required by GA-1. Distinguish local observer finiteness from total S.
2. Oriented map U[S], its reverse-edge rule, gauge group/action and complete
   state-dependence. Cite a physical source for every map/parameter choice.
   A freely specified background M is not an evolved microscopic link field.
3. Observer map Obs, normalized μ, preparation, allowed operations, physical
   setting/readback coupling C where operational access is claimed, records,
   timing, flags, failures and residual and outgoing state. For a passive-law
   claim, define the mathematical observable and prior explicitly and mark
   operational access open or not claimed; do not invent a physical coupling.
   A passive mathematical observable is not available readback.
4. An (Obs, μ) fork fixed before outcomes: either an independently justified
   target-independent selection rule with a source-deletion control and one
   independent consequence, or a precisely defined admissible class, with at
   least two distinct members and a proof obligation of invariance across the
   whole class. Two convenient examples do not establish class-wide invariance.
5. The architecture of the proposed action: static pushforward measure, path
   measure, or evolution generator. State the exact correspondence being claimed.
   An invariant measure does not determine dynamics. An effective action must
   name a reference measure and support; singular images require a supported or
   coarse finite formulation, not an undefined density against Haar measure.
6. Explicit treatment of the scalar-law/energy-shell stationarity assumption,
   real-to-complex map, unitarization/exponential prescription, matter operator,
   determinant reweighting and H-link/H-cust wherever used. An imported Gaussian,
   determinant or Wilson weight is an input until independently derived from φ.
7. One fixed finite geometry, bounded observation horizon, exact witnesses or
   justified numerical error bounds, resource cap, observable set and disjoint
   calibration/hold-out set. Freeze candidate enumeration and tie-breaking before
   measurements; later variants require new units. No outcome-driven tuning.
8. One consequence not used to choose the map, prior or parameters, with an
   explicit falsifier. Freeze expected relations/intervals and controls before
   evaluation. A failed prediction counts against that candidate.

No candidate is selected by this document. A missing GA★ field blocks execution.
Reading an existing result during S is provenance work, not a new prediction.

## 4. Ordered tests for a later, separately authorized run

L1 (native source): establish the physical map and same-update evolution of the
declared link carrier, gauge-covariance scope, normalized measure and stated
observable map. Conditional assumptions are listed rather than adopted.
Operational access is a separate axis: `ACCESS-SOURCED`, `ACCESS-OPEN` or
`ACCESS-NOT-CLAIMED`, with evidence and domain. Missing physical readback limits
operational claims; it does not imply absence of an evolving physical law.

L2 (gauge dynamics): on the *native reachable support*, show at least one
nonconstant gauge-invariant loop conjugacy class, and its evolution under φ.
Distinguish variation between preparations from within-trajectory evolution,
and static background curvature from either. Non-abelian exponentials of
differences must not be replaced by pure-gauge products of site exponentials.
If the source only supports a passive observable, report that restriction.

L3 (law/action selection): derive the declared measure/generator from the same
φ, Obs and μ; determine whether the Wilson functional, its square, a mixture,
or another law is selected. The target is identification of what the source
selects; Wilson form is not a success premise. Compare alternatives on actual
reachable support: ambient nonproportionality alone may disappear there.
State whether uniqueness is proved only inside a frozen candidate class.

Only after L1–L3 may a separately reviewed matching unit compare a minimal
loop and connected correlator with a quantum gauge theory. A determinant
formula, a positive quadratic term or a finite match is not Yang–Mills/QCD
equivalence, continuum existence, confinement or a mass gap.

## 5. Required controls and invariant checkpoints

GA★ must instantiate these obligations with executable or written checks, exact
domains and rejection rules; no generic label counts as a passed control.

| Invariant or hazard | Required checkpoint before a verdict |
| --- | --- |
| Fixed native source, no added action | SOURCE: map every load-bearing operation and weight to a pinned source; unsupported additions force GAP-SOURCE/conditional scope. |
| φ, inverse and measure | DYN: two-way inverse and preservation/stationarity proof or scoped exact checks; no ergodicity from invertibility or finite tests. |
| Orientation/covariance | GAUGE: reverse links, gauge-transformed states and loop conjugation checked against independent identities; distinguish transformed background data from a physical intervention. |
| Flat or fixed-curvature extraction | FLAT: pure-gradient and applicable site-rigidity controls must reject an evolving-loop claim, including nontrivial constant background C. |
| Nonvacuous dynamic-loop detection | LOOP+: an explicitly non-native dynamic-link reference must pass the detector; never count its positive as OI evidence. |
| Wilson versus squared action | ACTION: preserve README's exact SU(2) alternative and test distinguishability on native support. If indistinguishable there, report unresolved selection rather than choose one. |
| Supported measure versus ambient variation | SUPPORT: evaluate whether all perturbations/vertices used in a response lie in the microscopic image; retain abelian flat-image and §6.5 conditional non-abelian candidates separately. |
| Selection by conditioning | RECORD: compare full attempted/rejected/herald/timing records and unnormalized branch masses; accepted-only agreement cannot select the law. |
| Physical access and reusable state | ACCESS: for each claimed operation, remove the sourced actuator/readback and require loss of that operation; no private decoder or externally switched φ. Any claimed reuse retains the full outgoing/resource state. Passive-law-only candidates carry ACCESS-OPEN or ACCESS-NOT-CLAIMED; no actuator/reuse control is asserted passed for them. GA★ fixes applicability before outcomes. |
| Fixed (Obs, μ) fork and independent consequence | FORK/IP: check the frozen selection/deletion prediction or full class-invariance obligation; evaluate the hold-out with fixed uncertainty and no refit. |
| Error/decision integrity | VALID: independent exact or error-bounded check, deliberately broken orientation/weight/record/source mutations, structured exit/results evidence and an exhaustive decision self-test. |

Controls needing transplantation use the candidate's own C/map rule unchanged
where defined. GA★ must type-check the transplant; inability to transplant is
a named limitation, never permission to substitute a friendlier coupling.

## 6. Exhaustive disposition and review boundary

Apply these rows in order only to the separately authorized outcome-execution
stage, not Stage S. Every reported result also carries its independent access
status; no law token by itself establishes operational readback.

1. `NOT-RUN`: no authorized execution or a missing/review-pending GA★. This is
   GA-1's present execution state; readiness review is reported separately.
2. `VOID`: any required control, fixed-input check or error bound fails, or a
   measurement starts but is incomplete. Retain the failed attempt.
3. `GAP-SOURCE`: a required carrier/map/dynamics/measure construction is missing;
   this differs from an explicitly specified conditional input tested below.
4. `REJECT-CANDIDATE`: a valid native test falsifies its frozen prediction or
   necessary property. State the precise tested class, not a universal no-go.
5. `KINEMATIC-ONLY`: covariant links exist but evolving gauge-invariant data is
   absent. Passive readout alone does not trigger this row.
6. `DYNAMICS-ONLY`: L1/L2 pass but no selected law/action is established.
7. `CONDITIONAL-LAW`: an explicit law is derived only with named independently
   unproved inputs; list every such input and which L-level it affects.
8. `NATIVE-LAW`: L1–L3 and the independent consequence pass without an unsourced
   physical input, within the frozen scope. Report the actual law, including an
   alternative to Wilson, with proof layer and uniqueness domain separately.

An exact-commit reviewer must check source fidelity, control nonvacuity,
decision coverage and the physical/mathematical boundary before GA-1 readiness
is accepted. GA★ then needs its own independent exact-commit review and owner
execution decision. Any later evidence requires ordinary CI verification and
independent exact-commit review before scientific promotion. Neither review
nor green automatic PR CI grants F/E status or merge permission.
