# Detector readiness source assessment

**Disposition: UNSOURCED for the selected rounded cubic update.** The
first unsupported link is a physically identified and supplied local
temperature gradient in that update. The later transport, readiness,
replenishment and control tests are unreached. Independent review is
recorded on [draft #1364](https://github.com/amaybaum/incompleteness/pull/1364).

[Accountable Issue #1363](https://github.com/amaybaum/incompleteness/issues/1363)
· [Parent #866](https://github.com/amaybaum/incompleteness/issues/866)
· [Programme #1169](https://github.com/amaybaum/incompleteness/issues/1169).
Source snapshot `5704fc484a3a3e187185dbf9ea16c7797bbd571c`.
Scientific writer: Codex. [Protocol](PROTOCOL.md) checkpoint
`273e788d478a570c1b309846dfe5aa38bba36efb` precedes this assessment.

**Goal link (§A.47).** Decide whether one fixed OI dynamics can produce and
replenish a detector-ready state for #866 before it is used as an input to
the measurement account.

## What the benchmark supplies

Langsdorf reports a chamber in which vapor from a warm saturated source
diffuses into a refrigerated region. This sustains supersaturation for
condensation on ions. The heated and cooled surfaces are operating inputs
of the physical experiment. This assessment takes their temperature
difference and vapor supply as quantities an OI account would have to
source. The benchmark claim here is limited to what the published abstract
reports. It establishes no OI microscopic mechanism and supplies no matched
two-opportunity control for this assessment.
[Langsdorf (1939)](https://doi.org/10.1063/1.1751494)
· [Published abstract](https://cir.nii.ac.jp/crid/1360574096153122176).

## First unsupported link

The candidate is the periodic, rounded scalar rule with side length 20
and alphabet size 2^16 specified in [SM §4.2](../../../../../papers/SM.md#L284-L298).
SM supplies the recurrence, the mathematical initial states used in its
diagnostics and the observed spreading of perturbations. It reports
energy drift in its real-energy diagnostic for the rounded update and
leaves the energy associated with its orbits open. The modular
quadratic invariant described immediately afterward belongs to the exact
linear rule. Neither diagnostic supplies a temperature observable or the
source of a sustained difference between two local temperatures under
the rounded rule.

The source trace considered the following possible suppliers of that
missing input. All OI sources in this table are read at the snapshot
above.

| Source | What it supplies for the gradient question |
| --- | --- |
| [SM §4.2, rounded update](../../../../../papers/SM.md#L284-L298) | A periodic symbol dynamics and mathematical test preparations. No chamber-region temperature assignment or physical initial or boundary law supplying hot and cold regions is specified. The periodic torus allows internal regions in principle. |
| [SM §4.1, scope of the observer-level lift](../../../../../papers/SM.md#L220-L236) | A separate observer-level wave branch. The identification with the microscopic finite map is open. The wave branch supplies no sourced driving temperature difference for the rounded map. |
| [Main §1.2, realization datum](../../../../../papers/Main.md#L52-L60) | A distinction between the canonical invariant law and conditioned physical realization laws. It does not select a chamber resource history or a local thermal boundary law. |
| [Main §4.6, effective mixing](../../../../../papers/Main.md#L744-L762) | Conditional observer-selection results for the effective channel under a mixing hypothesis. They do not specify where a temperature gradient comes from for this model. |
| [Book Ch. 18, cosmological boundary](../../../../../book/ch18-beyond.md#L200-L214) | An initial low-entropy condition at cosmological scale. It is stated as an input. A map from that condition to the local hot and cold regions and their resource history is absent from the inspected account. |

The first checkpoint requires both a physical meaning for the two local
temperatures and a source for their difference over the detection
interval. The inspected sources provide neither for this candidate.
Prescribing a temperature difference or assigning temperatures to two
chosen symbol densities would supply the missing input by stipulation.
A different, physically justified boundary law could support a conditional
result if shown to apply to this same update.

## Protocol disposition

| Protocol checkpoint | Finding |
| --- | --- |
| Fixed update and benchmark | Matched to SM §4.2 and Langsdorf’s abstract. |
| Source of the local gradient | **UNSOURCED.** Local temperature observables and a physical resource history or boundary law for their difference are missing from the inspected sources. |
| Heat and material transport to readiness | **Unreached.** The gradient source was required first. |
| Two detection opportunities and replenishment | **Unreached.** No native ready layer or first-event residual state was available to account for. |
| Matched equal-temperature control | **Unreached.** There is no sourced driven arm and matched control in this model to compare. |

This is a bounded source finding for the named packet and one existing
update. It leaves open whether a suitable microscopic history or bridge
can be established. No trajectories, simulation, or Lean work enter the
finding. The finite torus specifies the candidate test model. The
assessment does not use global finiteness of the universe.

The former [fixed two-site screen](../native-apparatus-source-20261113/ASSESSMENT.md)
used a binary ring. [Native A's contract](../native-y-continuation-20261024/shared_v12/INTERFACE-CONTRACT.md)
specifies a three-bit local field and a different update. The
[#1358 draft record](https://github.com/amaybaum/incompleteness/pull/1360) provides planning
provenance for that earlier one-lead stop. The present disposition
follows from the sources in this assessment.

**Physical measurement sourcing: NOT PASSED.** The result ends the
authorized assessment at the gradient source.
