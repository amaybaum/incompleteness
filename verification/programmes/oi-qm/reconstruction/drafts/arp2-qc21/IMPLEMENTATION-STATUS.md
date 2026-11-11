# Q-C2-1 implementation under the approved R1–R10 rulings

WIP / UNREVIEWED CORRECTION HEAD. Current writer for new work: Claude, from `98582070` (owner confirmation 2026-11-11, stated in #1218 c.6785751650); ChatGPT reviews. ChatGPT and Codex authored earlier checkpoints. Guiding draft #1218; accountable issue #1169. Claude independently REVISE-reviewed previous head `2f3a8b83`; no descendant has independent ACCEPT.

The [explicit owner decision](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6778994857)
approves R1–R7 defaults (initial S_max = 100000), R8 alternative, R9 default and R10 narrowing, starting
from accepted paper checkpoint `f634f8e3f2115ef28d11616e0d195221d3ce9cb3`. This record grants no authority.

## Implemented components

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
- The approved R1–R10 choices are propagated into preregistration r15, including designation-based R8
  and R10's conditional landing language at every listed dependent site. OWNER-DECISIONS.md quotes the
  explicit authorization. Prior r14d plans/choices are marked historical rather than current defaults.
- Host-reader primitives cover complete pages with stable counts/unique identities, saturated-window
  splitting, all attempts, recursive-tree fallback, and actual comment/entry reads. Archive binding uses
  the exact run/head/name/digest and single in-memory member, with a fresh-record comparison. Their CLI
  integration and full order/verdict enforcement are still unfinished; no inventory is claimed captured.
- The fixture-mode marker checks the declared placeholder shape. ZIP rules reject mode changes, wrong
  member reads, file-path construction, aliases and escaping resources. Only inert template text exists;
  no workflow file or splice tree is created.
- The solver now emits ordered nonnegative preparation-removal witnesses, checks them independently,
  enumerates retained-ray facets with a visit bound, and reconstructs models on every original preparation.
  C-SYM has a separate exchanged-certificate verifier and uses the fragment's budget bounds. Its decisions
  contribute counters to stress accounting. These are unexecuted implementation changes pending review.
- B-P alone decides B under the 32-preparation/nine-setting safeguard; report-only failures do not void it.
  B-P has distinct measured-cap/budget placeholders. Complete decisive output, including scientific VOID,
  exits zero. The restricted QM comparison uses the four D22 CNOT-marker arms and no outcome relabelling.
- The stress generator defines three separate seeded coset instances per shape, ST-BP's over-maximum
  exception, fixture/completion/C-SYM records, and the exact 1203-term mechanical timeout/budget rule.
  B-S4F/B-RAY definitions, largest-flagged B-C horizon, depth-one diagnostics and the structured read-set
  ablation comparison are implemented in source. None has been scientifically executed in this session.

## Validation at this milestone

Syntax parsing and the actual static checker-B, controls-B, C-EXACT and C-INDEP scans pass. These scans
read source text only. The test loader now compiles inspected control definitions and metadata, omitting
the unused CFGS configuration-table comprehension. Earlier component checks imported controls and thereby
initialized that unused 16-tuple reference table as well as inert workflow strings; they did not execute a
native update, orbit, solver, certificate, fixture or scientific CLI. The earlier blanket statement that
the import initialized only strings was too broad and is corrected here. The checker --self-test and
local A3 remain unexecuted.

`scripts/implementation_selftest.py` initially passed nine isolated non-scientific test groups, now extended
to fourteen: actual static scans;
guard/constructor/verifier-alias rejection mutations; mode/refusal behavior with computation stubs;
standard hash vectors and generic collections; marker forgery; pagination failures including Forbidden;
calendar/window saturation; and synthetic archive binding/resource mutations. Host responses are mocked,
scientific/CLI/process entry points are blocked, and only inspected safe checker definitions are compiled.
These are implementation checks, not fixture outcomes, scientific evidence or independent acceptance.

## Independent first-component review and author corrections

The separate [component review](https://github.com/amaybaum/incompleteness/pull/1218#pullrequestreview-5849442749)
returned REVISE at `76ca53f9458e4bad9b80555c5a68af15ebe63083`; report SHA-256
`f57abf9f3f778fb438f310994a342aed23a8a7257dde3d75a06becafd968982c`. Its limited scope is preserved.

| Finding | Author correction pending focused independent confirmation |
| --- | --- |
| GI-B1 | The refusal-removal mutation targets the actual zero-argument call within s_build_c and retains the requirement that the source changes and B rejects it. |
| GI-B2 | Signature checking covers positional-only, ordinary, keyword-only, variable and default parameters. |
| GI-B3 | The two environment sites require the exact caller/arguments: s_mode(sys.argv, os.environ) in s_refusal, and s_entry(sys.argv, os.environ) in the unique main guard; relocation is rejected. |
| GI-B4 | The checker prohibits constructor references to set/frozenset, including aliases, as well as displays/comprehensions. |
| GI-B5 | The second component review at 3b4765cc found a definition-time assignment-expression bypass. The correction scans defaults, annotations, decorators and class-definition expressions for module rebinding. The separate reviewer accepted that scoped correction at cf37600d; subsequent full-head implementation review is still required. |
| Local nit | The obsolete pending/CC-NAT-gates-nothing comment is corrected to the actual conditional/STAB review scopes. |

All five negative cases are exercised in the isolated static tests. No full-script ACCEPT is claimed.

## Protocol integration and current gate

The declared modes now have source implementations: A3b/template wiring; strict input/pin and protected-T
checks; complete-event/attempt classification; actual approval, designation, retake and archive binding;
order/e-entry/verdict and freeze resource recomputation. Orbit controls, depth-one diagnostic reports,
ADA functions, completion/UPR-BC statuses and the frozen limitation texts are connected. The preregistration
documents pin serialization, non-circular E identity and provenance-only SOURCE_BASE. The original baseline
workflow is retained as verify.yml.input for source-only guard tests; it contains no new splice.

IMPLEMENTATION-DISPOSITIONS maps A1–A15, B1–B9, D1–D39 and the seven scoped reviewer findings to the source.
The previous milestone at `2f3a8b83` received independent REVISE (Claude, #1218 c.6784569758). Its 14 isolated groups passed under that reviewer; the new writer's additional non-scientific B1/B3/B4/B5 groups are source changes **not yet independently run or accepted**. Earlier checks covered current source/static guards,
metadata predicates, synthetic tokens/notes/resources and the inert template. Neither those checks nor
the author ledger certify scientific paths. The full fixture-bearing self-tests remain separately gated.

Required source RCH/DSN paths, final D/T0, the execution-source binding, future recorded branch names,
measured budgets and artifact pins remain unresolved and fail closed. The runs API access probe succeeds;
the connector rejects the activity endpoint, leaving T0 provenance unavailable. The design/confirmation
literal all-non-B-success rule was independently REVISE. The owner has now approved exact B1 conditional outcomes in #1169 c.6784808669; new code and preregistration apply that rule, but require focused independent acceptance. No design-run readiness is inferred from this source milestone.

No scientific computation, local A3 fixture solving, design/stress/confirmation/gate/decisive run,
workflow dispatch/rerun, actual workflow splice, round branch, F/E/freeze, physical premise or merge is
authorized or performed. The future design-run request must state all pending evidence and measurements.
#866 source NOT PASSED; Q-C2-2 inactive; #1210 and #1216 untouched; #1228 branch work complete.

## ChatGPT correction pass after Claude's REVISE (2026-11-11)

- **B1 / owner-approved:** event-specific A42 job and ARP-1 keeper outcomes; KTRANS reports `success` plus marker **only `skipped`**; all other required conclusions `success`. Added strict frozen guard/matrix/source-name checks and synthetic good/bad controls. This is the exact owner decision #1169 c.6784808669, not the earlier proposed success-or-skip marker variant.
- **B2 / author patch:** M-SOLVER and M-BUDGET use SG-1-valid 32-preparation/nine-setting/ACC inputs and report-only controls; forbidden scientific self-tests were **not** executed.
- **B3 / author patch:** missing/truncated/mistyped decisive cap and budget fields fail C-BUDGET; controller check is now separately coded rather than byte-identical. Host-mocked isolated tests were added, not run here.
- **B4 / author patch:** activity uses `gh api --paginate --slurp` to follow host cursor Link rel=next, validates the returned structured page arrays/IDs and fails closed. GitHub activity endpoint access and T0 remain **UNRESOLVED**; no host activity inventory exists.
- **B5 / author patch:** requires a valid deciding step 2/3/4, null on undecided, and 4 for C-SYM; synthetic negatives added.
- **CI / review:** ordinary research PR CI may run; neither automatic CI nor a local static author check is a non-author implementation ACCEPT. Request fresh non-author review on the final exact head, with any new findings handled separately.
- **Open:** see the open list at the end of this record.

The source remains a paper/implementation candidate, not an executed model. No A3, solver, fixture, stress, dispatch or physical source step was undertaken by ChatGPT. No design-run authority follows. #866 NOT PASSED.

### Minor-finding disposition (author-side; still independently unreviewed)

N1: preregistration now explicitly distinguishes historical draft D (`fd539e15`) from a future owner-approved execution D; the literal script D_SHA still names that historical candidate, and **no design source may run until D/T0/source bindings are independently reconciled**. N2: `v_q` rejects bool. N3: decisive C-CERT/C-BUDGET red labels now use `-decisive` to avoid fixture-label collision. N4: each `budget.respected` is derived from that fragment's typed C-BUDGET validation, not merely LP status. N5: report the uncharged C-SYM facet enumeration in the runtime-proxy limitation. N6: owner retention commitment remains PENDING. N7: OWNER-DECISIONS now quotes the actual UTC owner timestamp. N8: current writer/status and author/review split are clarified. N9: historical r14x revision notes are retained in the *research draft only*, explicitly scheduled for removal or re-tracing before F under a separate gate; the draft is not the frozen F source. N10: fixed stress seeds are no longer called pending. N11: F/E designation parser now requires a complete `Designate <stage> <sha>` phrase, not a stray stage letter. All require exact-head non-author re-review; these statements are dispositions, not acceptance.

## Claude correction pass from `98582070` (2026-11-11; author-side, not independently reviewed)

At `98582070` the isolated harness `scripts/implementation_selftest.py` passed 14 of 18 groups. The four failures and
their corrections:

- **B4 test.** The assertion `'page=' not in argv` also matched `per_page=100`. The test now parses the activity URL's
  query and requires `per_page=100` and no `page` parameter; the source was already cursor/Link-paginated.
- **C-INDEP on `v_q` (N2).** `type(s) is bool` uses the names `type` and `bool`, which C-INDEP does not admit in a
  verifier. The rejection is now `s is True or s is False`, which is equivalent for booleans and uses only constants.
  The scan is unchanged.
- **Control B on controls.py.** The B1 rule's workflow parsing used `re.search` and `re.findall`; control B admits only
  `re.fullmatch`. The section, matrix and top-level job-name extraction now use `str.find`, slicing, `split` and
  `startswith`. The frozen `if:` blocks, matrix tuple and job-identity checks are unchanged. Control B is unchanged.
- **Synthetic tokens and notes.** Root cause: the B3 correction makes C-BUDGET red on any decided record without
  typed `budget_values`/`cap_values` and counters, as C.4 requires. The controller's synthetic decisive record
  `synthetic_meas` predates this and carried no limit fields, so `decide` recomputed C-BUDGET red, gave B-VOID and
  disagreed with the record's flags (X, VOID). That produced the token, the six report-only cases and the Level-1
  note failures; several other checks passed only vacuously. The synthetic B-P record now carries typed limits within
  bounds. The two "leaked report-only verdict" cases carry complete typed limits, so each fails for its named defect
  (unverified certificate; `pivots` over its budget) and not for missing fields. No control was loosened.

After these changes the harness passes 18 of 18 (`python3 -I -B`, Python 3.13, scratch directory); `py_compile`
passes for the three scripts. Not run: the checker or controls `--self-test`, `--stress`, local A3, any fixture, LP,
solver, certificate, design, gate or decisive run, or Lean.

Open items are listed at the end of this record.

## Claude correction pass 2 (2026-11-11; author-side, not independently reviewed)

Responds to the non-author delta review [#1218 c.6785757458](https://github.com/amaybaum/incompleteness/pull/1218#issuecomment-6785757458)
(D1–D3 were fixed by the previous pass).

- **D4.** C.3's S1/E conclusion condition now cites C.7's B1 table for `workflow_dispatch`, matching
  `run_class_run_success`. C.7's header names C.3 instead of C.8, which is unchanged.
- **D5.** C.5(g)'s frozen extra-argument set includes `--slurp`, and the text states the activity read's cursor (Link
  `rel="next"`) pagination and its page-array and unique-id validation, matching `GH_EXTRA` and `gh_get`.
- **C.7 wording.** The comparison sentence now states what the code compares (the four keyed blocks, the matrix and
  the job names; steps by exact name). The harness adds the listed mutation cases: A42 `failure` on either event, a
  renamed keyed step (keep, axiom-report, marker), a changed keyed guard or `id` (all four blocks), and a missing
  matrix shard on dispatch.
- **N3.** The controller's `decide` appends `C-CERT-decisive`/`C-BUDGET-decisive`, the checker's names.
- **N4.** `respected` keeps its rule; preregistration's `budget` schema now defines it: true exactly when the fragment
  was given a verdict and its typed limits held, so a withheld fragment reads false.
- **N7/N8.** OWNER-DECISIONS quotes the B1 decision verbatim with author and time; the writer statement is in its own
  section, sourced to #1218 c.6785751650. An unsourced process remark was removed from this record.
- **N11.** C.3 (`order.json`, `verdict`) and APPROVAL-ENTRIES freeze the `Designate F <sha>` / `Designate E <sha>`
  phrase, matching `run_class_designation_errors`. This is precondition text, not a designation.
- **B2 residue.** M-BUDGET's reported-only case now uses the same fragment decided without a budget as the valid B-P
  (so it is within its own limits) and asserts that `k_fragment_controls` keeps C-BUDGET and C-CERT green. This is a
  definition in the gated checker self-test; it was **not executed**.

The isolated harness passes all 18 groups after this pass; `py_compile` passes. Nothing scientific was run.

**Open list at this head.** N9 (the
r14a–r14d revision notes must be removed or re-traced before F). B4's real activity-endpoint read, T0 and the host
inventory. The B2 M-BUDGET/M-SOLVER definitions are unexecuted. All corrections await independent review.

## N1: execution base D (2026-11-11)

By owner decision #1169 c.6789676675 (OWNER-DECISIONS), `D` = `cac5d26441dd33e9348151487e4df7b547195481`, re-confirmed
equal to `main`'s head when the round PR is opened (a moved `main` makes its then-current head `D` by the same
decision). `controls.py`'s `D_SHA`, the preregistration's *The objects*, DESIGN-RUN-REQUEST and PLAN state it. Checked
read-only: `verify.yml.input`, and `.github/workflows/verify.yml` at both `fd539e15` and `cac5d264`, are blob
`3a9dc8a97fd6f9d6d5f17cf390b5aabf37d65233`; every `INPUTS` pin in `controls.py` equals its blob at `cac5d264`; and
`fd539e15..cac5d264` changes only `papers/SM.{md,tex,pdf}`. Remaining `fd539e15` citations name ARP-1's landing
(precondition 1, M-ARC) or DESIGN-DS's drafting snapshot. `SOURCE_BASE` stays unset until a separately authorized
local A3 or design tree.
