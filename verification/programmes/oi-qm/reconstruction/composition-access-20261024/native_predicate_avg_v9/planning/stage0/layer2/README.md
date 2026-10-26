# NP-AVG-1 Stage 0, Layer 2

**Status: WIP / UNREVIEWED, not frozen; v8 enumeration not authorized.**

This directory holds the Layer-2 draft (the implementation) for independent review. It implements
the frozen Layer-1 specification, `../r5/STAGE0-PLAN-r5.md` (SHA-256 `1a30188e…847e`, frozen at
`f33d8d63`; `../LAYER1-FREEZE.md`), as its §5b requires: the production enumerator, the controls,
the configuration hashes and the execution certificate. Nothing in `../r5/`, `../code-r5/`,
`../design-r5/` or `../LAYER1-FREEZE.md` is changed.

- `LAYER2-PLAN.md` is the implementation plan, tied clause by clause to Layer 1. It contains:
  - the in-run gates, sharding, the stop rule and the dry-run cost procedure;
  - the structured outputs and the certificate;
  - the v8 lock and rule T (implemented as frozen, with provisional wording);
  - the proof-obligation table with statuses, and the invariant→checkpoint table;
  - the CI workflow proposal;
  - the findings in Layer 1 that the reviewer is asked to settle.
- `code/` holds the production, reference and control code. Six files are copied from
  `../code-r5/`, with provenance in the plan's §2. `LAYER2-MANIFEST.json` lists their hashes; it is a
  draft, regenerated at the freeze.
- `design/` holds the bounded local evidence. It ran on toy, planted and small-window instances, on
  S6's carrier and on v8 combinatorics only. `RUN-MANIFEST.json` and `.md` record the commands, exit
  codes, `-O` identity and hashes. `runs/` holds stdout and stderr; `toyrun/` holds the toy run's
  structured files.

Not done, and not authorized:
- any closure on v8's configuration class;
- the full mutant campaign, which is CI-only and needs owner-approved dispatch;
- any workflow file;
- any dispatch.

A bounded run is design evidence, not a proof. The rule-T argument in the plan (§8) is submitted
for review and is not established.
