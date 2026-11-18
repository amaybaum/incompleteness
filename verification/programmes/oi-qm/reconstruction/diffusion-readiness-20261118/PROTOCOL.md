# Detector readiness from a temperature gradient

**Paper-only source assessment protocol.** Source snapshot
`5704fc484a3a3e187185dbf9ea16c7797bbd571c`. Scientific writer: Codex. A separate
non-author reviews the pushed scientific checkpoint.

[Accountable Issue #1363](https://github.com/amaybaum/incompleteness/issues/1363)
· [#866 authorization](https://github.com/amaybaum/incompleteness/issues/866#issuecomment-6968318250)
· [Programme #1169](https://github.com/amaybaum/incompleteness/issues/1169)
· [Prior bounded #1358 stop](https://github.com/amaybaum/incompleteness/pull/1360).

**Goal link (§A.47).** Decide whether one fixed OI dynamics can produce and
replenish a detector-ready state for #866 before it is used as an input to the
measurement account.

## One existing update

Use the rounded cubic rule of [SM §4.2](../../../../../papers/SM.md) on the periodic
three-dimensional lattice with side length 20 and alphabet size 2^16, the
instantiation already described in that section. If s_i(t) sums the six
neighbor values using representatives 0 through 2^16 − 1, the rule is

```text
x_i(t+1) = floor((s_i(t) + 1)/3) − x_i(t−1)  (mod 2^16).
```

The manuscript reports disturbance spreading for this update. That makes
it a concrete transport candidate to inspect. Its rounded scalar neighbor sum distinguishes it from Native A's
three-bit pool update. The branch
is also distinct from the fixed binary ring and two-site observer in the
[earlier source assessment](../native-apparatus-source-20261113/ASSESSMENT.md).
The screen uses the existing model at its stated standing. The finite
test geometry makes no use of global finiteness of the physical universe.

## Physical benchmark and test order

Langsdorf maintained an ion-sensitive layer by diffusing vapor from a warm
saturated source toward a cooled region. Use the gradient, replenished
vapor and ion-sensitive layer as the physical quantities to account for.
The laboratory's heating and cooling are identified inputs.
[Langsdorf (1939)](https://doi.org/10.1063/1.1751494)
· [Published abstract](https://cir.nii.ac.jp/crid/1360574096153122176).

1. **Source of the gradient.** Locate sites or observables for two regions
   with physically interpretable temperatures. Identify a sourced initial
   or boundary law or native history that provides their difference for the
   detection interval. Trace the driving resources upstream of the ready
   layer. A cooler or bath introduced as data leaves this checkpoint open.
2. **Transport and readiness.** From the same microscopic update and
   source, obtain the heat and working-material transport and a local
   readiness observable. Define the criterion before either detection
   opportunity. In the benchmark, it is a vapor layer sufficiently
   supersaturated to grow droplets on ions for the declared interval.
   Specifying that criterion as a target supplies no microscopic law.
3. **Replenishment.** Follow two detection opportunities under the same
   dynamics and source law. Account for material and heat moved in the
   first, the apparatus residuals and any failed or no-track outcomes.
   Establish the return or maintenance of the readiness criterion before
   the second despite the first event's resource cost. This test treats
   the event as a specified disturbance of the working medium; physical
   sourcing of detection coupling is a separate obligation.
4. **Control.** Use the same update, geometry, working medium and event
   specification with equal-temperature boundaries and otherwise matched
   conditions. Equality must have a source in the same model, just as the
   driven condition must. Compare readiness using the same criterion.
   If both arms meet it, this comparison has not isolated the proposed
   gradient mechanism. Other causes of supersaturation remain possible.

**Stop rule.** The first missing physical link gives **UNSOURCED** at that
checkpoint. A prepared layer, imported diffusion equation, externally
stipulated heat bath or added controller cannot qualify it. A supported
result requires source and transport plus readiness across both
opportunities, including the control. Any independently justified
boundary posit used must be named as a dependency of the result. The
assessment uses paper reasoning within the approved scope.

## Checkpoints for independent review

| Requirement | Evidence to inspect on the pushed assessment head |
| --- | --- |
| One unchanged OI rule | Match the expression and parameter choice against the pinned SM source. |
| Ready state physically sourced | Trace the initial or boundary law, available resources and transport before treating readiness as derived. |
| Two opportunities and equal-temperature control | Check the resource ledger and both outcomes at the common criterion, or check that they are marked unreached at the earlier source stop. |
| Correct scope of any stop or pass | Identify the first unsupported link and distinguish the benchmark and source findings from any native dynamics result. |
| Paper-only scope | Inspect the published diff and the reported basis of the finding. |

Selectable settings, native target coupling and persistent measurement
records would require separately authorized assessments.
