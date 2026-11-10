# Q-C2-1 implementation under the approved R1–R10 rulings

WIP / UNVERIFIED implementation checkpoint. Writer: Codex. Guiding draft #1218; accountable issue #1169.

The [explicit owner decision](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6778994857)
approves R1–R7 defaults (initial S_max = 100000), R8 alternative, R9 default and R10 narrowing, starting
from accepted paper checkpoint `f634f8e3f2115ef28d11616e0d195221d3ce9cb3`. This record grants no authority.

## First implementation milestone

- The checker uses the accepted zero-argument refusal, named-function builder registry and one counter;
  its entry is s_entry. Fixture-mode guard tests account for counter deltas and one direct refusal.
- The initial owner S_MAX is 100000. Other caps, measured budgets and evidence pins remain unset.
- SHA-256 uses the h_ namespace and includes the third standard test vector. The deprecated fixture-output
  flag is removed; the design's fixture command remains --event fixture.
- The checker represents membership with ordered dictionary keys and canonical tuples rather than sets.
  The verifier uses its own v_unique helper and does not call the solver's collection helper.
- Control B enforces the revised registry, signature, first-statement/reference-site, entry and no-set rules.
  The verifier builtin allowlist no longer admits set. CC-NAT's accepted conditional proof review gates C;
  this does not remove the theorem's hypotheses or supply physical source evidence.

## Validation at this milestone

Syntax parsing and the actual static checker-B, controls-B, C-EXACT and C-INDEP scans pass. These scans
read source text only. Importing controls for these scans evaluates only standard-library definitions
and the inert workflow-text formatter; no checker module, scientific builder, solver, fixture or native
state enumeration is imported or run. The checker --self-test and local A3 remain unexecuted.

## Remaining implementation before independent review

The approved choices still need full propagation into the preregistration and historical-plan annotations.
The implementation must still complete the A3b/fixture marker, input pins, evidence ZIP binding, complete
event/attempt inventory, designation/approval/e-entry/verdict modes, caps/extreme-ray and stress-accounting
changes, role-specific budgets/VOID/UPR-BC/ablation reporting, and the corresponding permitted isolated
non-scientific self-tests. Existing IMPL-DELTA-r14d remains the historical detailed obligation list;
the present checkpoint does not claim those items complete or scripts certified. Independent review
must inspect a later complete immutable implementation checkpoint; paper acceptance is not inherited.

No scientific computation, local A3 fixture solving, design/stress/confirmation/gate/decisive run,
workflow dispatch/rerun, actual workflow splice, round branch, F/E/freeze, physical premise or merge is
authorized or performed. The future design-run request must state all pending evidence and measurements.
#866 source NOT PASSED; Q-C2-2 inactive; #1210 and #1216 untouched; #1228 branch work complete.
