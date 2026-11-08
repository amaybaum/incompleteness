# Controls continuation drafting log (staging only)

Writer: writer-k1p1-ctl, continued 2026-11-08 by the independent Codex agent
k1p1_controls_revision. This is not the original Claude session; its header and
commit e4ee843c87005b2f48e9e2081ed7dc12e41c0f0e remain original provenance.
Authority: owner's 2026-11-08 continuation, root activation #1135 c6721746629,
owner scope #1031 c6721619842; common/role handoffs supplied by root.

Shared inputs: AGENTS.md, d92 preregistration and all A1 companion files,
coordinator's common behavioral clarification that SF-2pb must fail CC-BIJ′ and
SF-2p must pass. No other implementation source, output or revised checkpoint,
no provisional patch package, and no historical K1 output read.

This checkpoint is WIP / UNVERIFIED and STATIC ONLY. The generic per-output
checks, strict PR-CR6, adopted pending/union reporting, fixed rosters, isolated
git and structured run preconditions/check files are drafted. Remaining work:
full synthetic harness, render/schema/markers, final instance mutation paths,
and root-supplied final patch SHA256 bindings. No candidate invoked/imported;
no fixture or K1 map/state computation. Undefined remaining old OPEN handlers
are unfinished code paths, not an accepted final implementation.

Commands to this milestone (categories per A1 §12; read commands were batched):

| Category | Commands |
| --- | --- |
| read | `cat /tmp/k1p1-revision-common-brief.txt /tmp/k1p1-controls-role-brief.txt /workspace/incompleteness/AGENTS.md`; repeat exact briefs plus AGENTS ranges 1–460, 461–920, 921–1368 after initial truncated display |
| read | `wc -l` on briefs, AGENTS and common spec; `rg --files` to locate controls and drafting logs; `git status --short`; `git show --stat --oneline HEAD`; `git ls-files` filtered for drafting/log files |
| read | `cat` / `sed -n` reads of d92 preregistration ranges 1–300, 301–610, 611–935, 936–1271 and 936–1020; A1 full and ranges 298–325, 320–610, 580–620; fixture MD full and 1–110; fixture JSON full (large display bounded by tool) |
| read | `sed -n` controls ranges 1–170, 190–698, 699–1143, 1144–1740, 1620–1725; `rg -n '^def ...'` to index original controls |
| read | `rg -n 'push:|branches:|paths:' .github/workflows/*.yml`; `sed -n` trigger portions of all four push-triggered workflows |
| edit | Wrote and ran `/tmp/revise-controls-phase1.py` and `/tmp/revise-controls-stage.py` as text-only editing scripts; wrote this staging-only log |
| static check | Twice parsed only controls bytes with `ast.parse` and `compile(tree, path, 'exec')`, without executing compiled code; PASS |
| static check | `git diff --check`; AST import/division/top-level audit and sensitive-source scan shown in milestone command; SHA256 and git blob computation |
| edit | `git add` only controls.py and this own staging log; forward single-parent commit; ordinary branch push after trigger inspection |

Push inspection: verify/hidden-sector pushes are main-only. BG2 and bridge
compatibility paths do not match either changed path. Other workflows have no
push event. No PR, dispatch, freeze, merge or metadata edit performed here.

## Full phase-1 static delivery

The full adopted code paths are drafted, still WIP / UNVERIFIED pending independent
static review and separately permitted bounded synthetic verification. The earlier
unfinished OPEN handlers have been removed. Generic own checks share their actual
instance functions with the fixture route (including the parameterized rank chain
and PR-E comparisons). The synthetic route constructs its universe/map from the
pinned input only and never calls an instance execution, S0 or preserved-result
computation. It writes no checks file. All 14 fixture entries, the declared
analogues and NF-1–NF-7, MU-C3′, RF/RN/RM and AI cases are included. Rendering
uses the same schema/grammar/projection/marker functions in synthetic and full
profiles. All instance-only mutations remain statically reviewed paths only.

Two specific common-spec clarifications from root, with no implementation-code
channel: SF-2pb must exit 0 with bijection=false and both per-program CC-BIJ′
checks must fail, after SF-2p's passing good-inverse control. NF-3 expressly
requires the invalid `--fixture` / `--stage members` mixture, which must be
rejected before any instance code; this specific refusal test is the exception
to A1 §5.6's overbroad “never passes --stage” sentence. Neither negative is
skipped or turned into a pass. Root retains the safe-path execution gate.

Final reviewed MU-C1/C2/C3 patch SHA256 constants are the sole explicit binding
dependency left for code completion: all are `None`, which causes refusal (2)
before any self-test invocation. No provisional package was read. The final
bindings must be supplied by root and checked independently; an absent patch,
unbound patch or mismatched patch never passes. The exact applier fails a
nonapplying hunk (1). No K1 or synthetic runtime result is claimed here.

Further command log:

| Category | Commands |
| --- | --- |
| edit | Wrote `/tmp/controls-render-fragment.txt`, `/tmp/controls-synthetic-fragment.txt`, `/tmp/controls-mutations-fragment.txt`; used Python `Path.read_text`/slice splices and exact `str.replace` edits to own controls.py only |
| static check | Repeated `ast.parse` + `compile` (in memory only) after each substantive splice, then `ast.parse(..., feature_version=(3,11))`; no candidate module execution |
| read | `rg -n` searches for OPEN/reference/definition/parameter/exception/render paths in own controls; `sed -n` reads of own resulting ranges 455–490, 800–837, 1300–1456, 1940–2030, 2430–2495 and 2490–2580 |
| read | `sed -n` remaining exact d92 fixture JSON ranges 1–82, 83–139, 128–160, 160–198; earlier full JSON reads also contained the remaining fixture tables |
| read | `sed -n` common A1 ranges 301–319, preregistration ranges 908–936; `command -v ruff`, `command -v pyflakes` (neither installed); `git status --short`; `df -h /workspace /tmp` |
| static check | `/tmp/k1p1-controls-static-audit.py`: Python3.11 grammar/in-memory compilation, allowed imports, no true division/dynamic exec, symtable unresolved-global scan, literal-only exact roster comparison and uniqueness, direct synthetic-call/file-name audit and sensitive-source scan; PASS |
| edit | Initial ordinary push failed due default sandbox network; same push with network access succeeded, publishing e5c9dcb782af7932b0bf8d825e3a8902d2b4d5d4; no forced ref movement |
| static check | `git diff --check`; SHA256 of edit/static scripts and controls; git blob ids and changed-path inspection |
| edit | Updated this staging-only log; forward commit and ordinary push of complete static draft after rechecking trigger scope |

No tool self-test, V3/verifier/corpus run, candidate `--help`, fixture execution,
instance run/check/render/self-test or scientific computation has been performed
by this continuation. The task-specific static-only instruction takes precedence
over generic local-smoke-check guidance. Exact synthetic commands and outputs
will be logged separately if root explicitly authorizes them after safe review.

Static/edit helper digests (SHA256; the helpers edit/inspect source and were not
candidate/fixture execution harnesses):

- revise-controls-phase1.py: a1408f8bbe53ed118540fc304f3e374bae4b22f416e38d219a056b9e63a30126
- revise-controls-stage.py: 780616161d95a84f66f7fcfc86b68cb3481fb06161eb687576fb0f2ce1635eae
- controls-render-fragment.txt: 9941d24a15f3fb742dc87354dd7b4ad031ee606dd4ed6845181b5c33aaaee2dd
- controls-synthetic-fragment.txt: 30629ba5d4dcd893ace7116e23fc3bb38f1052161b8722d7c4311e73b4632f8a
- controls-mutations-fragment.txt: 92111991255eb9f3a423c1526df19026269523b908f3484ffe0b57fedc837409
- k1p1-controls-static-audit.py: 8204acb06f82798644bcaddb720be90b873ba944b7e455427fdbc12cae128e54
