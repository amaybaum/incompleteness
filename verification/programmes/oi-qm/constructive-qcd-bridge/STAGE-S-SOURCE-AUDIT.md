# GA-1 Stage S: native gauge-link and action source audit

**Source-audit disposition: GAP-SOURCE.**
This is a source-audit disposition for the three families fixed in GA-1, not an
outcome-execution verdict or an impossibility theorem. No GA★ candidate is selected.
The conditional non-abelian construction in SM §6.5 remains available for research.

Protocol: `NATIVE-ACTION-PREREGISTRATION.md` at
`3874c239c5954062f0eac09b7e7710a055da3a56`, unchanged. The owner authorized Stage S
only: source inspection and dependency tracing. No candidate observable, loop,
determinant, spectrum, fit, simulation, exact probe or Lean build was evaluated.
Existing source code and reported results below were read, not rerun or recertified.

## Source snapshot and comparison with the protocol pins

Current main was pinned at `5914c17cd0d82e67b0803e6bc1f2278fd95c4a80`.
All source coordinates below refer to that commit unless explicitly historical.
The audit's drafting parent remains the accepted #1003 head `3874c239`.

The protocol's historical main anchor `c596904a9adf61649e65c9035d9d2ad7011f56a8`
is retained, not silently replaced. The relevant comparison finds:

- SM §6.5:803 now explicitly qualifies the smooth on-shell field by the
  stationary-law and Gaussian-limit proposal. The link-map/status passage at
  :809–811, measure-reduction passage at :290–298 and induced determinant
  passage at :681 are unchanged. The qualification reinforces an obligation
  already named by the protocol; no new measure is adopted.
- SM §4.1:230 separately corrects the coefficient's isotropy/gaplessness reading;
  no coefficient or observer operator is selected by this audit. Other SM
  changes concern onsite-chirality wording and cross-references.
- The two A6 Lean modules and scalar `wave_eqn.c` are unchanged. ROADMAP's A6
  covariance/physical-identification scope is unchanged; other roadmap updates
  do not source a gauge action.

This comparison is a source-pin addendum submitted to the same independent
review as this report. It alters no protocol test, control, candidate or premise.
Any later material source substitution still requires a reviewed amendment.

## A. First family: SM §6.5's exponential non-abelian construction

| Link in the proposed chain | Source and strongest support located | Boundary relevant to GA-1 |
| --- | --- | --- |
| Microscopic versus observer dynamics | SM §4.1:222–284, §4.2:290–298 | The modular-linear rule, rounded candidate and normalized observer operator have distinct hypotheses. The text explicitly leaves whether one realized map supplies both the structural chain and required stationary law open. |
| Scalar ensemble | SM §4.2:290–298; §7.5 gap (i):1225 | A smooth Gaussian scalar law is proposed, not supplied by the operator factorization. A real positive quadratic shell, limiting regime, normalization and zero-mode treatment are additional obligations. |
| Ensemble versus occupied orbit | Same passages; `verification/audits/manuscript/sm-source-reconciliation-20261029/README.md`, measure-reduction crosswalk | A uniform ensemble on an invariant finite shell does not require a single-cycle dynamics. Identifying one occupied orbit's empirical law with that full-shell ensemble is a different obligation. Shell fragmentation is not absence of an invariant ensemble. |
| Gauge carrier | SM §4.4–4.6, especially :340–380 | The six-link geometric decomposition is distinguished from H-link, single-copy and H-cust physical identifications. Those hypotheses do not specify a microscopic evolution law for links. |
| Link map | SM §6.5:811 | The proposed map is the exponential of a Lie-algebra-valued nearest-neighbour matter difference, with scale `2π/q`. It is an existing candidate, not a construction introduced here. Its map-selection argument carries the amplitude-scale operational input of Substratum §4:270–272; that input is not derived there. |
| Non-abelian curvature versus abelian flatness | SM §6.5:811; `papers/oi_lattice_code/foundations/induced_source_probes.py`, IS1–IS3; `gauge_support_probes.py`, GS1–GS7 | The retained analysis distinguishes noncommuting exponentials of differences from pure-gauge products of site exponentials. IS2/IS3 implement exact truncated-series checks on fixed non-abelian configurations. They do not implement a native trajectory, prove its stationary law or select an action. The abelian support obstruction is not transferred to SU(2)/SU(3). |
| Determinant weight | SM §4.2:290–292; §6.1:681; §6.5:809–811; §7.5:1225 | The scalar-to-determinant measure **and observable** map remains independently open. Solving scalar stationarity alone would not discharge it. The staggered factorization is an operator identity, not that measure map. |
| Interacting concentration and matching | SM §6.5:803–813 | The candidate's near-identity pushforward/free-energy comparison is reported with finite numerical support and named hypotheses. It is not a source of the determinant weighting from the microscopic update. |
| Observer access | SM §4.7.1.1:494–517; §6.5:811; `bargmann_bridge_probes.py`, scope BB5/BB6 | A mathematical link functional is not physical readback. The hypercharge observer-bundle/vertex conditions are separate from the non-abelian candidate and from each other. The scoped native-permutation probe is not a general obstruction to all observer bundles. |

### The surviving source gap

The source does supply a conditional non-abelian link construction and stated
candidate measures. The missing link is an explicit, fixed microscopic-to-observer
construction that identifies the proposed weighted link law with the law induced
by the **same** native update and a separately justified normalized state, with
the relevant observable correspondence. This is a sourcing obligation, not a
claim that the determinant formula is mathematically invalid.

There are two independent measure questions here: obtaining the proposed scalar
stationary law, and obtaining the determinant-weighted gauge/matter law and
observables from it. The maintained SM §4.2 and §7.5 passages explicitly keep both
open. The source audit therefore does not collapse them into an ergodicity test,
substitute a Gaussian by convenience, or infer the second from the first.

SM §6.5:805 also distinguishes reported matching under **Wilson dynamics on the
image** from direct sampling of the proposed measure, for which it reports a
failure at the archived comparison point. The same passage says the original
archived numerical code is no longer extant. This audit records that source's
qualification; it neither re-establishes the numbers nor infers a general
universality failure. A Wilson-generated sampler cannot serve as an independent
source of Wilson selection in GA-1.

The retained `oi_su3_hmc.c` header states a determinant-weighted independent-link
integral without a Wilson plaquette term. `oi_su2_hmc.c`:116–145,180–205,239–255,
305–316 stores link matrices `U`, generates pseudofermions, performs molecular
dynamics and applies a Metropolis decision. This is code for a specified sampling
model. No identification of those sampler trajectories with the scalar native
update is supplied by those routines. Conversely, absence of such an
identification there does not invalidate that sampling model in its stated scope.

## B. Second family: the packaged A6 link-coupled interface

`OIBridge/BackgroundIndependence.lean`:117–136 defines `linkF N M`, transported
coupling `gaugeLink g M` and `A6Cov N M`; `a6cov_all` at :161 proves covariance
for every coupling of that interface. `A6Instantiation.lean`:103–135 packages
this rule, and :216–226 explicitly leaves the coupling as a parameter with no
instance chosen. Its A4Exact statement carries translation invariance of M as
a hypothesis (:199–209). These are retained formal statements, not fresh builds.

This formal source is positive evidence for the covariant interface and the
second-order packaging. It does not choose a state-dependent map `U[S]`, an
evolution law for independent link variables, or a gauge measure/action. Replacing
the parameter M by a configuration-dependent prescription would require its own
source/instantiation check; the parameterized theorem does not certify that
replacement automatically.

The historical `cx3b_complex_not_A1` concerns the finite-A1 interface. It is not
a rejection of the owner's observer-relative finiteness formulation or of
normalized infinite/continuous research carriers. Removing total finiteness
does not, by itself, select a measure or an action.

ROADMAP P1:725–745,802–821 and the A6 instantiation result preserve the same
conditional physical-identification boundary. Book ch05:137–143 and its FULL
counterpart explicitly distinguish gauge symmetry from Wilson dynamics.
The full free-transitive site-action hypothesis of #1003's conditional rigidity
comment has not been shown to hold for this family; that lemma is not used as
an OI-wide no-go or a substitute for this source trace.

## C. Third family: the scalar reference control

`papers/oi_lattice_code/trace_out_fractional/wave_eqn.c` specifies a two-slice
modular scalar update and inverse routine. Its actual `lattice.h` specialization
declares `L=2`, `Q=2`, a finite scalar alphabet and bit-packed state. The general
formal family `waveF`/`waveSubstratum` in `SubstratumInterfaceAudit.lean`:160–182
keeps d, L, q and α as parameters. The literal C implementation and that broader
formal family are not silently identified.

This is a concrete dynamics source. A bijection's uniform finite ensemble and
the invariant-ensemble/occupied-orbit distinction are available without importing
a Gaussian. Neither the scalar update's source nor the displayed formal family
specifies the §6.5 non-abelian link map with its proposed determinant-weighted
measure as its native law. The separately retained abelian gradient construction
is a flat-image control, not the missing non-abelian source. The explicit
state-dependent graph example in SM §3.1 is another stated update, not an
automatic identification with the §6.5 gauge measure.

The cross-check against `OIBridge/CanonicalMeasure.lean` preserves its positive
finite results: counting measure is invariant and maximal-entropy, while
`invariance_does_not_select` guards against uniqueness from invariance alone.
That module does not identify counting measure with the §6.5 smooth scalar law
or its determinant weighting. `GaugeDimension.lean` formalizes the engineering
dimension of a stated Yang–Mills coupling; it does not select that action from φ.

## Audit scope, discovery and disposition

The source search covers papers and companion manuscripts, book/ch05 and FULL,
the formal A6 and scalar interfaces, maintained roadmap and reconciliation
records, and retained gauge/foundation code. Discovery used repository-wide
source searches for `H-observer-bundle`, `H-Y-vertex`, `stationary-law`,
`near-identity`, `pushforward`, `scalar-to-determinant` and `exponential map`,
with direct reads of the large SM passages that indexed search can miss.
The report does not claim to classify every microscopic extension or every
unmerged research branch. Historical/source comments are not substituted for
proofs, and no result is promoted because a string occurs in a source.

| Stage-S obligation | Checkpoint and outcome |
| --- | --- |
| Pin source versions without changing the protocol | Current-main comparison above; both old and current anchors retained; addendum reviewed with this report. |
| Preserve existing candidate rather than assert none exists | Family A records the exponential non-abelian candidate, map input and separate measure obligations. |
| Distinguish physical law, parameter covariance and sampler dynamics | Families A/B/C trace each separately; no cross-identification is assumed. |
| Preserve controls and scientific boundaries | Abelian support and ambient Wilson-versus-squared results retained at their scopes; no new control run or native-support comparison. |
| Keep operational access independent | `ACCESS-OPEN` for a physically read-out version of the proposed law; no actuator or reuse claim. This status does not erase the conditional kinematic construction. |

**Stage-S disposition: GAP-SOURCE.** Within the three audited families, no complete
same-update source package was located that fixes the proposed native link law
with the required state/measure and observable correspondence. This is compatible
with the explicitly conditional §6.5 construction and the formal covariance
results; neither is refuted or removed.

The next missing deliverable is that source package, or a precisely declared
conditional package whose added inputs have independent justification and whose
remaining scope is stated honestly. This report does not authorize choosing
such inputs, constructing GA★, or running a candidate to rescue the gap.
Any GA★ needs its own independent exact-commit review and separate owner execution
decision. Manuscripts, ROADMAP, proof grades, frozen protocols, Lane B, Lane A,
MR-1, PC-1 and main are unchanged; no merge or F/E designation is requested.
