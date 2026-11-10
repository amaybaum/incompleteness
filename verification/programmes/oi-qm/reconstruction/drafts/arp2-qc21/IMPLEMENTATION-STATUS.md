# Q-C2-1 implementation under the approved R1–R10 rulings

WIP / UNVERIFIED implementation checkpoint. Writer: Codex. Guiding draft #1218; accountable issue #1169.

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
The current milestone is a complete source candidate for full non-author implementation review, with safe
negative coverage still being expanded. Fourteen isolated groups cover current source/static guards,
metadata predicates, synthetic tokens/notes/resources and the inert template. Neither those checks nor
the author ledger certify scientific paths. The full fixture-bearing self-tests remain separately gated.

Required source RCH/DSN paths, final D/T0, the execution-source binding, future recorded branch names,
measured budgets and artifact pins remain unresolved and fail closed. The runs API access probe succeeds;
the connector rejects the activity endpoint, leaving T0 provenance unavailable. The design/confirmation
literal all-non-B-success rule is preserved strictly; its compatibility with D's intentional PR A42 skip
is a focused review question. No design-run readiness is inferred from this source milestone.

No scientific computation, local A3 fixture solving, design/stress/confirmation/gate/decisive run,
workflow dispatch/rerun, actual workflow splice, round branch, F/E/freeze, physical premise or merge is
authorized or performed. The future design-run request must state all pending evidence and measurements.
#866 source NOT PASSED; Q-C2-2 inactive; #1210 and #1216 untouched; #1228 branch work complete.
