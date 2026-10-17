# Relative-gate transport and pair-interface integration

This planning note tracks two related design packages on the pair-interface research branch.
It proposes no adoption or new mathematical result. The source records retain their own evidence levels;
their reported builds and computations have not been independently rerun for this note.

## Source packages

- [Relative two-NOT transport record](https://github.com/amaybaum/incompleteness/blob/f435a13c5c5a36945f702ca2f9119ac2434bddb2/verification/programmes/oi-qm/reconstruction/relative-gate-design/result.md).
- [Combined pair-interface statement](https://github.com/amaybaum/incompleteness/blob/f435a13c5c5a36945f702ca2f9119ac2434bddb2/verification/programmes/oi-qm/reconstruction/pair-interface-design/statement.md).
- [Thread F's hypothesis and transport audit](https://github.com/amaybaum/incompleteness/blob/804843f16b67061ac258ce00cefa2425d1b688c2/verification/programmes/oi-qm/reconstruction/f2-research-threads/F-relative-gate.md).

The source branch also contains finite-reconstruction and carrier-descent work. A future adoption package
must select its own dependencies explicitly rather than import that branch's entire diff.

## First priority: the available-test interface for #822

[KINF-COPY-1 (#822)](https://github.com/amaybaum/incompleteness/pull/822) proposes a selector stated using the maximal product cone.
The relative-gate design supplies a proposed route from the available-test cone to that surface.
Review and incorporate that route into #822's unfrozen preregistration before any F designation:

- [ ] Specify the relative two-NOT predicate and the exact positivity clauses it changes.
- [ ] State each transport direction separately with its required cone inclusion.
- [ ] Identify which effect-soundness and orbit hypotheses establish the needed cone equality.
- [ ] Select and pin the module bytes, imports, native namespace, registry entries and probe interface.
- [ ] Include the axis-test failure and the source's conclusion-level countercontrol.
- [ ] Retain the warning that the positive distinct-NOT example is also a one-NOT gate:
      satisfiability does not show that type covariance admits more gates than copy naturality.
- [ ] Re-measure the selected executable tree against the round's chosen base and retain its evidence.

This PR does not edit #822's control plane or designate a freeze.

## Second package: the conditional pair assembly

The pair statement connects admitted matrix operations, state-cone compatibility and available preparations/tests.
Its preparation cone and test inventory must be connected to the intended observer model explicitly.

- [ ] Review the pair assembly with every closure, admission and compatibility premise displayed.
- [ ] Keep state-cone equality separate from implementation-class membership and drivability.
- [ ] Keep test availability separate from membership in a mathematical effect family.
- [ ] Distinguish dense rational tests from the extra settings needed for exact CHSH attainment.
- [ ] Specify what transfers to [#829](https://github.com/amaybaum/incompleteness/pull/829) and [#823](https://github.com/amaybaum/incompleteness/pull/823),
      and which carrier, compatibility and availability premises remain independent obligations.

## Review milestone and evidence

First deliver a proposed #822 preregistration diff plus a dependency ledger for the pair assembly.
The two packages may require separate native rounds; this note does not decide that question.
Historical design builds are provenance, not F/E attestations or adopted kernel results.
Before any enduring result lands, retain its source, structured expected results and regeneration recipes
under AGENTS §A.42. No manuscript or programme status is changed by this plan.
