# NP-AVG-1 Stage 0, Layer 2

**Status: WIP / UNREVIEWED, not frozen; v8 enumeration not authorized.**

This directory holds the Layer-2 draft (the implementation), revision r5, for re-review. It
implements the frozen Layer-1 specification, `../r5/STAGE0-PLAN-r5.md` (SHA-256 `1a30188e…847e`,
frozen at `f33d8d63`; `../LAYER1-FREEZE.md`), as governed by erratum E1
(`../amendments/E1-LAYER1-ERRATUM.md`, in effect), as its §5b requires: the production enumerator,
the controls, the configuration hashes and the execution certificate. Nothing in `../r5/`,
`../code-r5/`, `../design-r5/`, `../LAYER1-FREEZE.md` or `../amendments/` is changed.

r3 filled in E1's rulings: rule T (T1, T2 with S1a's diagnostic status σ, T5, T6), C7's per-record
scope (F3) and the 58 counts (F6). r4 applied the r3 review's R1–R6
(`../../review/LAYER2-R3-REVIEW.md`). r5 applies the r4 review (`../../review/LAYER2-R4-REVIEW.md`)
and the owner's decisions of 2026-10-26: the 24-hour ceiling is one campaign ledger (calibration, count
pass, primary run, mutant campaign, retries, execution overhead); the shard plan is a deterministic
subdivision by representative rank, and the launch rule takes the heaviest shard; the v8 site-pair
count is implemented as a separate count-only module for review, not dispatched. The owner's rulings
are recorded (plan §4.2). Open placeholders, with no default: κ's components u_cal and u_model (the
owner approved the method, not a value), the reserve inside the 24-hour ceiling, the retry allowance,
the v8 survivor cap, the Lemma G-D reference form and O1. The v8 profile is refused while any of them
is open.

- `CHANGES-L2-r5.md` maps each item of the r4 review and each of the owner's decisions to its edit,
  control and mutant; `CHANGES-L2-r4.md` does the same for the r3 review's R1–R6, `CHANGES-L2-r3.md`
  for each E1 item and follow-up, and `CHANGES-L2-r2.md` for the r1 review.
- `LAYER2-PLAN.md` is the implementation plan, tied clause by clause to Layer 1 and E1. It contains:
  - the in-run gates, C7 per record (§3.3a), the deterministic shard subdivision, the campaign
    ledger, the stop rule and the dry-run cost model;
  - the structured outputs and the certificate;
  - the v8 lock, σ and rule T;
  - the proof-obligation table with statuses, and the invariant→checkpoint table with E1's rows;
  - the CI workflow proposal;
  - the points where E1 is ambiguous or not implementable as written now (§13).
- Advisory documents for the owner, each setting nothing:
  - `KAPPA-PROPOSAL.md`: κ by the approved method, the u_model sensitivity, the affordable κ beside
    the justified κ, the reserve and the retry allowance;
  - `SURVIVOR-CAP-PROPOSAL.md`: the cap, derived from a resource and completeness analysis;
  - `FEASIBILITY-AND-REDESIGN.md`: whether the campaign fits the 24-hour ceiling, and redesigns that
    keep every control;
  - `SITE-PAIR-COUNT.md`: the count-only site-pair count (`code/l2sitepairs.py`), its algorithm,
    permitted outputs, guards and resource limit, for review and the owner's authorization;
  - `AMENDMENT-PROPOSAL-V8-COUNT.md`: the unadopted design of the v8 count-only pass;
  - `ci/`: the proposed planted-set-only CI calibration, with its workflow (not under `.github/`,
    not launched), scripts and `CI-CALIBRATION-PROPOSAL.md`.
- `code/` holds the production, reference and control code. Six files are copied from
  `../code-r5/`, with provenance in the plan's §2. `LAYER2-MANIFEST.json` lists their hashes; it is a
  draft, regenerated at the freeze.
- `design/` holds the bounded local evidence. It ran on toy, planted and small-window instances, on
  S6's carrier and on v8 combinatorics only. `RUN-MANIFEST.json` and `.md` record the commands, exit
  codes, `-O` identity and hashes. `runs/` holds stdout and stderr; `toyrun/` holds the toy run's
  structured files; `kappa/` holds the κ calibration repeats, `overhead/` the overhead-factor and
  survivor-cap measurements and the cap's derivation, `subdivision/` the shard subdivision's bounds and
  checks, and `midsize/` the cost model's validation on the mid-size analogue (timing data). The evidence was produced
  on an uncommitted working tree: the files record the HEAD at run time and `tree_clean = false`, so
  they are design evidence only, and they are regenerated at a recorded commit at the freeze.

Not done, and not authorized:
- any closure on v8's configuration class, and any shared-tip, F_G or site-pair count on it;
- the full mutant campaign, which is CI-only and needs owner-approved dispatch;
- placing any workflow under `.github/`, or launching the CI calibration;
- any dispatch.

A bounded run is design evidence, not a proof.
