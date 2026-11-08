# K1-P1-1 implementation A: drafting log (staging; WIP / UNVERIFIED)

Writer `writer-k1p1-impl-a` (coordinator label `writer-k1p1-implA`), Claude Code session
`session_011zDyUSyEszk3JJx83uXKKq`. Branch `staging/k1-p1-1-impl-a-20261106`, cut from `origin/main` at
`424f28b1e7b1201e9a13bd0e608e1b0e4ad9f93b`. Control plane: PR #1135 at
`4ca431afb1bfee0cdf301f0917c73068fdf09b58`. Authority: #1031 comment 6677496553 (amaybaum, 2026-11-06), Stage 2,
pre-F code drafting: static analysis and predeclared synthetic-fixture tests only; no computation on the K1
instance, its dynamics or its states.

This log lists every command this writer ran, with its category (preregistration §19, Finding 10): **read**,
**edit**, **static check**, **synthetic-fixture run** or **run on the instance**. No command of the last two
categories was run. `k1p1_enum_a.py` was never executed or imported, and no file was written outside this
writer's worktree and its scratchpad.

## Hand-off

- Received: the preregistration at `4ca431af`, and the adopted text of its §2 at K1-RDY-1's `F`
  `d9b3de012e393262adb20f91ad49627bad48de43`. That text is `preregistration.md` and amendments A2, A3, A5, A8 and A9,
  each read at `F` and checked against §2's blob ids and SHA-256 values. Nothing else was received.
- Not read: implementation B, `controls.py`, their branches, any other writer's output, K1-RDY-1's `result.md`,
  `gate-table.json` or `derivations/`, and `LEMMAS.md` and `PROOFS.md`.
- Delivered: `verification/lean/k1p1_enum_a.py`, SHA-256
  `9d4eb0a778333a6606ab507bacd026e56e054ec03cfe38288cf2d22c5c080825`, git blob
  `7cf3579a532de051cc35c1202666f443a04df804`, 1099 lines.

## Commands, in order

| # | Category | Command (paths abbreviated: `P` = the K1-P1-1 preregistration path, `K` = K1-RDY-1's record directory, `wk1a` = this worktree) | Result |
|---|---|---|---|
| 1 | read | `git fetch origin 4ca431af…`; `git cat-file -t 4ca431af…`; `git show 4ca431af:P \| wc -l`; `df -h /tmp` | commit; 1271 lines; 18G free |
| 2 | read | `git show 4ca431af:P \| sed -n 1,320p`, then `320,700p`, `700,1000p` and `1000,1271p` | the preregistration in full |
| 3 | read (digests and counts) | `git cat-file -t d9b3de01…`; for each of the six §2 files: `git rev-parse d9b3de01:K/<f>` and `git show d9b3de01:K/<f> \| sha256sum`; `head -313 \| sha256sum`; `wc -l` | all six blob ids and SHA-256 values equal §2's table; the 313-line digest is `a93f3f33…bb63`; 397 lines. No verdict uses these |
| 4 | read | `git show d9b3de01:K/preregistration.md \| sed -n 1,240p \| cat -n`, then `sed -n 240,397p` | `K` in full |
| 5 | read | `git show d9b3de01:K/amendments/{A2,A3,A5,A8,A9}…` | the five adopted amendments |
| 6 | read | `python3 --version`; `which python3.11 pyflakes flake8 mypy ruff pylint`; `python3 -c "import pyflakes"`; `git status --porcelain`; `git branch --show-current`; `git worktree list`; `git show 4ca431af:P \| grep -n -i staging` | Python 3.13 default, 3.11 present; ruff, flake8 and mypy present, pyflakes absent; no staging branch named in P |
| 7 | read and setup | `git fetch origin main`; `git ls-remote origin refs/heads/staging/k1-p1-1-impl-a-20261106`; `git rev-parse origin/main`; `git -C /home/user/incompleteness worktree add -b staging/k1-p1-1-impl-a-20261106 wk1a origin/main`; `ls verification/lean` | the branch did not exist; `origin/main` = `424f28b1`; worktree created |
| 8 | read | `git branch --unset-upstream`; `git status -sb`; an inline `python3` that prints each `.github/workflows/*.yml` trigger block (reads the YAML text only) | upstream unset; triggers listed |
| 9 | read | `ls .github/workflows`; `sed -n '/^on:/,/^jobs:/p' .github/workflows/verify.yml`; `grep -l "^  push:"` over the workflows | four workflows have `push` triggers. `verify.yml` and `hidden-sector-replay.yml` take `main` only. The path filters of `bg2-orientation-design.yml` and `bridge-compatibility-research.yml` do not match `verification/lean/k1p1_enum_a*`. A push of this branch starts no workflow |
| 10 | edit | Write tool: create `verification/lean/k1p1_enum_a.py` | draft |
| 11 | edit | inline `python3` string replacements in the draft (adds a probe mode in place of a stand-in adversarial table, narrows CT-INC to CC-PART, adds an early float check, drops unused parameters) | edited; A not executed |
| 12 | static check | `python3.11 -c "py_compile.compile(…, cfile=<scratchpad>, doraise=True)"`; `ruff check --no-cache --isolated`; `flake8 --isolated --max-line-length=100`; `mypy --ignore-missing-imports --no-incremental --cache-dir=/dev/null` | py_compile ok; ruff exit 1, 46 style findings (UP031 percent-format, I001, EXE001, FURB136, PIE810); flake8 exit 1 (E741, E127); mypy: no issues |
| 13 | read (counts) | `wc -l`; `file`; `sed -n 40,60p \| cat -A`; `git status --porcelain` | 1100 lines, LF endings |
| 14 | read (counts) | `grep -n` of top-level definitions; `grep -c ""`; `awk 'NF==0' \| wc -l` | no duplicated definition |
| 15 | edit, static check | inline `python3` replacements: drop shebang, sort imports, `max(0, k)`, rename `l`, single `startswith`, one continuation line; then ruff (`--ignore UP031`), flake8, py_compile, mypy | ruff exit 1 (I001 only); flake8 exit 0; py_compile ok; mypy: no issues |
| 16 | edit, static check | `ruff check --select I001 --fix`; `ruff check --ignore UP031`; flake8; `sed -n 44,58p` | ruff exit 0; flake8 exit 1 (E302) |
| 17 | edit, static check | inline `python3`: one blank line before `class Refusal`; ruff (`--ignore UP031`); flake8 | ruff exit 0; flake8 exit 0 |
| 18 | static check | `python3.11 -I <scratchpad>/k1a-static/ast_scan.py verification/lean/k1p1_enum_a.py`. The scan parses the file with `ast` and never imports it. It checks imports against §8.1's allowlist (`fractions`, `itertools`, `json`, `hashlib`, `sys`, `os`), float and complex literals, `/` and `/=`, calls to `float`, `eval`, `exec`, `compile` and `__import__`, and top-level statements other than definitions, constants and the `__main__` guard | exit 0; imports `fractions, hashlib, itertools, json, os, sys`; no finding |
| 19 | read | Read tool, `k1p1_enum_a.py` lines 726–925 (static re-reading of R5a–CLASS) | no change |
| 20 | read (digests and counts) | `sha256sum`, `git hash-object`, `wc -l` of `k1p1_enum_a.py`; `date -u` | the values under Hand-off |
| 21 | edit | Write tool: create this log | — |
| 22 | edit (git) | `git add` of the two files; `git status --porcelain`; `git commit`; `git log --oneline -1`; `git diff --name-only origin/main..HEAD`; `git push origin HEAD:refs/heads/staging/k1-p1-1-impl-a-20261106`; `git rev-parse HEAD` | commit `bb92c29b26042466334189a5a61e415e603b9672`, touching only these two paths; pushed |
| 23 | edit (git), read | the edit adding rows 22 to 24; `git commit`; `git push` (same refspec); `gh run list --branch staging/k1-p1-1-impl-a-20261106` | this log's second commit; the run list is checked for workflow runs on this branch |
| 24 | post | ToolSearch `select:mcp__github__add_issue_comment`; one checkpoint comment on #1135 | the comment records the head of row 23 |

Ruff's UP031 (percent-formatting) findings are left as written: they are style only and valid in Python 3.11.

## Synthetic fixtures

None run. Preregistration §11.2 proposes SF-1 to SF-3 and SF-M, to be fixed with hand-derived answers in the
code-freeze amendment, and run by `controls.py self-test --synthetic`. It gives no means by which a fixture reaches
implementation A:
- A's command line names only the stage, the record and output directories and the pinned digest;
- "the implementations carry no test hooks" (§11.3);
- `controls.py` may not import A (§8.1).

SF-2 tests B's rank method, and SF-3's system is not yet stated. No fixture is therefore predeclared in a form
runnable against A, and this writer invented none.

## Independent A continuation, 2026-11-08 — static checkpoint

The historical author/session and command log above are preserved. Current writer:
`writer-k1p1-impl-a`, independent Codex continuation agent `k1p1_impl_a_revision`
under the root coordinator, not the original Claude session. Original staging
head: `caea695c875179fb9b310739c4aa2a9196332fe4`. Root activation:
#1135 c6721746629; owner scope: #1031 c6721619842. The common and A-role briefs
were read in full. Current common procedure and fixture blobs are the four
specified files at `d92e0882e7609e91e3458193391e89610fffa777`.

Shared inputs are the preregistration, all A1 documents, the six adopted K rule
files at `d9b3de012e393262adb20f91ad49627bad48de43`, current root `AGENTS.md`,
the two coordinator briefs and this writer's own original code/log. A1 is the
disclosed common behavior channel containing no implementation code. Root
also disclosed independent acceptance of the d92 hand-derived expected values,
and the specific SF-2pb negative: exit 0 with bijection false. No other writer's
code, output, draft package or checkpoint was accessed. No scientific library
or shared formatter/library is used.

The continuation is STATIC ONLY. No candidate was imported or invoked, including
help, fixtures, instance commands or controls. No K1 dynamics, states, S0 values,
member counts or row outcomes were computed. No fixture map was evaluated by
an auxiliary script. Expected fixture JSON was read as specification only;
it is never loaded by candidate code. No freeze, dispatch, merge or promotion.

Changes: parameterized cell forms, tuple orbit walk, symbolic propagation,
readiness/rows/tokens/CLASS and guard are shared by both routes. K's cell-form
builder, preserved-result measurements and S0 are instance-only. Fixture admission
checks exact id and raw SHA-256 before JSON parsing; rank-only ids are refused.
Q1–Q5 pending/G6/union/S0 behavior and Q10–Q12 schemas/refusals are implemented.
Output payloads are checked before writes, with rollback of owned paths on I/O
failure. Single exact-division helper is retained for the later MU-C3 patch.

Remaining evidence: independent static re-review, root safe-path permission,
permitted CLI synthetic fixture comparisons and independent synthetic review.
This checkpoint makes no runtime-correctness or scientific claim. Current local
Python is 3.12.14; Python 3.11 grammar was checked statically. Python 3.11 and
ruff/flake8/mypy/pyflakes are not installed in this execution environment.

### Continuation commands (ordered tool invocations)

Each semicolon here denotes separate source/read/check commands as shown, not
execution of the candidate. Inline Python below is source editing or AST/document
inspection only. Scratch scripts are separate from candidate code.

| # | Category | Commands / exact input scope | Result |
|---|---|---|---|
| C1 | read | `cat /tmp/k1p1-revision-common-brief.txt /tmp/k1p1-a-role-brief.txt` | full briefs |
| C2 | read | `cat /workspace/incompleteness/AGENTS.md`; `ls /tmp/k1p1-common-d92`; `git status --short`; `cat verification/lean/k1p1_enum_a.py` | initial reads; large output truncated, followed by chunk reads below |
| C3 | read | `wc -l /workspace/incompleteness/AGENTS.md /tmp/k1p1-common-d92/*`; `rg -n` definitions/comments/OPEN/Undetermined/CONTROL_EXPECTED in A; `cat` own drafting log | source outline; wc flags directory (no computational effect) |
| C4 | read | `sed -n '1,460p'` AGENTS; `wc -l` A1 files and `cat` A1-frozen-code | oversized output; chunked re-reads follow |
| C5 | read | `sed -n '461,920p'` AGENTS; `sed -n '1,220p'` A1 | chunks (oversized output re-read where truncated) |
| C6 | read | `sed -n '221,440p'` A1 | full chunk |
| C7 | read | `sed -n '441,660p'` A1 | full chunk |
| C8 | read | `sed -n '1,280p'` common preregistration | full chunk |
| C9 | read | `sed -n '281,560p'` common preregistration | full chunk |
| C10 | read | `sed -n '561,840p'` common preregistration | full chunk |
| C11 | read | `sed -n '841,1100p'` common preregistration | full chunk |
| C12 | read | `sed -n '1101,1300p'` common preregistration; `sed -n '921,1140p'` AGENTS | preregistration completed |
| C13 | read | `sed -n '1141,1368p'` AGENTS; `sed -n '1,200p'` A1-fixtures.md | full chunks |
| C14 | read | `wc -lc` A1-fixtures.*; `sed -n '201,420p'` A1-fixtures.md; `sed -n '1,325p'` own A | fixture MD completed |
| C15 | read | `sed -n '1,125p'` A1-fixtures.json | full chunk |
| C16 | read | `sed -n '126,195p'` A1-fixtures.json | full chunk |
| C17 | read | `sed -n '196,349p'` A1-fixtures.json; `sed -n '326,575p'` own A | fixture JSON completed |
| C18 | read | `sed -n '350,460p'` and `sed -n '790,920p'` AGENTS; `git show d9b3de01:K/preregistration.md` through `sed -n '1,220p'` | rule read |
| C19 | read | `git show d9b3de01:K/preregistration.md` through `sed -n '221,397p'`; `git show` each of K amendments A2, A3, A5, A8, A9 | six adopted rules read in full, no prior execution output |
| C20 | read | `sed -n '576,725p'` own A; `sed -n '660,870p'` common A1; `sed -n '735,790p'` AGENTS | own controls/source and remaining rule chunks |
| C21 | edit | heredoc creates `/tmp/k1p1-a-edit.py`; `python3 /tmp/k1p1-a-edit.py` | source-only rewrite of own A: map/row refactor and adopted semantics |
| C22 | edit | heredoc creates `/tmp/k1p1-a-edit-inputs.py`; `python3 /tmp/k1p1-a-edit-inputs.py` | Q10/Q11 validation source edits |
| C23 | edit; static check | heredoc creates `/tmp/k1p1-a-driver.txt`; inline `pathlib` replacement of A's driver; inline `ast.parse(feature_version=(3,11))`, `compile` of AST without eval/exec, import and numeric AST scans | parse/compile pass; six permitted imports; no float literals or true division |
| C24 | read; static check | `git diff --check`; `git diff --stat`; `sed -n '195,330p'` A; `rg -n` map/instance/OPEN references in A; `rg -n -A18 '^on:' .github/workflows/*.yml`; `command -v ruff python3.11`; `git status --short` | clean whitespace; own code only; push triggers exclude branch/paths; tools unavailable |
| C25 | static check; read | inline AST allowlist/no-float/no-division/no-dynamic-exec scan; literal admission-table comparison with A1; `git show` byte comparisons of all four common files against d92 copies; SHA-256 source/doc digests; Python version | all static checks pass; candidate never imported or evaluated |
| C26 | read | `python3 -m pip show ruff pyflakes flake8 mypy` | packages unavailable (exit 1); no installation |
| C27 | edit | `cat >>` own drafting log, this continuation section and command table | provenance/checkpoint record |
| C28 | static check; read | inline source/log sensitive-pattern scan (private keys, token families, signed URLs, IP and email patterns); code `sha256sum` equivalent and `git hash-object`; hashes of edit helpers/driver source; `git diff --check` | zero sensitive matches; whitespace clean |
| C29 | edit; read | append these rows; `git add` only own A/log; `git commit` forward; `git push origin HEAD:refs/heads/staging/k1-p1-1-impl-a-20261106`; `git rev-parse HEAD`; `git status --short` | static milestone (exact push/head reported to root) |

Static checkpoint source SHA-256:
`0e8721e5fe1c8fc8540d36ce2eed84d812a5630867ec4af56d920169466b3fdd`;
blob `2252965843430155fedfbc8855a5d23d13c2c920`.
Edit helper SHA-256 values: map refactor `85f489753b0a0107485e4d29f55339f09efac8d13f969c7296e36702762b43a7`;
input schemas `5a255f5e23ef96f1668f189f59a4ae58dd4d54f052b216797638f27fb591dc20`;
driver source text `95c535144dc4aea451fb230cae18e2b5530af2d6c23becef2a3a1ccc3b6fae48`.

Push trigger inspection: verify and hidden-sector push events name main;
bridge-compatibility and bg2 path filters exclude these two paths. All remaining
workflows are dispatch-only. This ordinary original staging branch push starts
no push-triggered workflow. No PR metadata/comment write by this continuation.

### Static milestone completion and continued static reread

C29 committed `ce6f0f2c3192fedf5b459d48a58579e6787486ee`. Its first push
attempt failed because the default sandbox could not connect to the configured
proxy; it did not update the remote. The same refspec succeeded with the tool's
network permission, forwarding remote caea695c to ce6f0f2c. No source changed.

| # | Category | Commands | Result |
|---|---|---|---|
| C30 | edit | `git push origin HEAD:refs/heads/staging/k1-p1-1-impl-a-20261106` with network permission | successful ordinary forward push of ce6f0f2c |
| C31 | read | `sed -n '1,200p'` and `sed -n '330,530p'` own A | generic map/frame and strict schemas reread |
| C32 | read | `sed -n '530,660p'`, `sed -n '770,1028p'`, `sed -n '1029,1285p'` own A | token/guard/admission/driver reread |
| C33 | static check; read | inline `symtable` global-name analysis; AST function call-name closure from fixture_payload and forbidden instance constant/function check; `git show`/`git rev-parse` six adopted K rules and SHA-256 comparisons with §2 | no unresolved globals; fixture closure excludes instance code/constants; all six pinned blobs/hashes match |
| C34 | edit; static check; read | append this log section; `git diff --check`; source/log sensitive-pattern scan; code/log digests and blobs; re-read all workflow trigger blocks; `git add` only own log; `git commit`; identical ordinary staging `git push` with network permission; `git rev-parse HEAD`; `git status --short` | log-only forward checkpoint, source unchanged |

No defect or actual normative ambiguity was found in the continuation's static
reread. Runtime behavior remains unverified. No fixture or instance invocation
has occurred. The source SHA-256 and blob remain exactly those of ce6f0f2c.


## Bounded A author fixture verification, 2026-11-08

Root authorization: #1135 c6721877817, after the independent expectation review
and root-reported non-author static ACCEPT plus SAFE-path review of the unchanged
code at ce6f0f2c, blob `2252965843430155fedfbc8855a5d23d13c2c920`.
Root supplied the actual interpreter
`/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11`
(Python 3.11.17). This is bounded author verification, not independent review or
cross-unit integration qualification. Earlier static-only statements above
record the preceding phase; the first candidate invocation is C37 below.

Source before and after: blob `2252965843430155fedfbc8855a5d23d13c2c920`,
SHA-256 `0e8721e5fe1c8fc8540d36ce2eed84d812a5630867ec4af56d920169466b3fdd`.
No source change was needed. Only this staging log changes.

Eight admitted positives passed: SF-1a, SF-1b, SF-1c, SF-2p, SF-2pb, SF-3,
SF-3f, SF-3g. Each exited 0; each output directory held exactly fixture.json;
every byte equalled the canonical expected object from d92 A1-fixtures.json.
SF-2pb is the prescribed wrong-inverse negative, recorded with bijection false;
its passing good-inverse control is SF-2p. No primed checks or controls program
were run here.

NF-2 through NF-7 passed, each immediately after its SF-1a positive control:
each exited 2 and left its output directory unchanged, including NF-4's
sentinel. NF-3 deliberately carries the invalid mixed --stage members flag
and was authorized as a refusal check on the statically proved safe path;
no instance route was invoked. These are 20 candidate subprocess invocations.
No candidate import, B or controls read/run, patched mutant, extra toy system,
scientific/K1 computation, instance command, freeze, dispatch or merge occurred.

**NF-1 remains pending and was not run.** The d92 prescribed positive control
is B on SF-2a. Root's follow-up prohibited substituting an A positive, prohibited
B access by this writer, and will coordinate A's refusal after independently
receiving/verifying B's control result. No claim that all seven A negatives
passed is made here. The initially written external harness had an optional
unexecuted A smoke-pair path; root rejected substitution before any harness run,
and C37 removed that path. The executed harness quoted below skips NF-1.

| # | Category | Commands | Result |
|---|---|---|---|
| C35 | read | `git status --short`; `git rev-parse HEAD`; `git rev-parse HEAD:verification/lean/k1p1_enum_a.py`; `sha256sum verification/lean/k1p1_enum_a.py`; actual Python 3.11 `--version` | clean e7a6bddf; reviewed source identity; Python 3.11.17 |
| C36 | edit; read | heredoc creates external `/tmp/k1p1-a-fixture-check.py`; `sha256sum` | unexecuted draft harness SHA-256 2e9b244ff17fe0595a789df1ed7284083db212c4afcd4109c72a50de6f961aef |
| C37 | edit; read; synthetic-fixture run | inline pathlib edit removes unexecuted NF-1 smoke substitution; `sha256sum` external harness; `/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11 -I /tmp/k1p1-a-fixture-check.py` | harness exits 0; 8 positives and 6 paired negatives pass, 20 candidate subprocess calls; NF-1 not run |
| C38 | edit; read | inline pathlib append of this section, complete external harness source and structured report | no candidate invocation; report read only |
| C39 | static check; read; edit | Python 3.11 AST parse/compile without eval of own candidate; source/log sensitive-pattern scan, source/log/harness/report digests and blobs; workflow trigger inspection; `git diff --check`; own-log-only `git add` and forward `git commit`; ordinary original staging `git push` with network permission; `git rev-parse HEAD`; `git status --short` | log-only forward milestone, source unchanged; root receives exact head |

Scratch inputs, outputs and report remain in
`/tmp/k1p1-a-author-fixtures-kuknd4j5/`. The full external harness follows.
It serializes input/expected documents, invokes only A as a subprocess and
compares bytes/file sets/statuses; it evaluates no map itself.

Executed harness SHA-256: `77d10dc6d3c740d3d53fa0366f10baea478e6af57ea1c8988345ada49ca00f76`.

```python
"""External A author check: exact d92 fixtures; never imports the candidate."""
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile

PYTHON = pathlib.Path('/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11')
SOURCE = pathlib.Path('/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py')
COMMON = pathlib.Path('/tmp/k1p1-common-d92/amendments/A1-fixtures.json')
WORKTREE = pathlib.Path('/workspace/k1p1-impl-a')
EXPECTED_SOURCE_HASH = '0e8721e5fe1c8fc8540d36ce2eed84d812a5630867ec4af56d920169466b3fdd'
EXPECTED_SOURCE_BLOB = '2252965843430155fedfbc8855a5d23d13c2c920'
EXPECTED_COMMON_HASH = '691aedbf0c9e74fdcc64f4c9c35f5e07c8ffc362e74360d4e541df682c750e85'
A_IDS = ('SF-1a', 'SF-1b', 'SF-1c', 'SF-2p', 'SF-2pb', 'SF-3', 'SF-3f', 'SF-3g')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8') + b'\n'


def clone(obj):
    return json.loads(json.dumps(obj))


def assign(obj, path, value):
    parent = obj
    for key in path[:-1]:
        parent = parent[key]
    parent[path[-1]] = clone(value)


def source_identity():
    return {'sha256': digest(SOURCE.read_bytes()),
            'blob': subprocess.check_output(['git', 'hash-object', str(SOURCE)], cwd=WORKTREE, text=True).strip()}


def output_snapshot(path):
    return {p.name: digest(p.read_bytes()) if p.is_file() else 'NONFILE'
            for p in sorted(path.iterdir())}


def main():
    assert sys.version_info[:2] == (3, 11)
    before = source_identity()
    assert before == {'sha256': EXPECTED_SOURCE_HASH, 'blob': EXPECTED_SOURCE_BLOB}
    common_bytes = COMMON.read_bytes()
    assert digest(common_bytes) == EXPECTED_COMMON_HASH
    document = json.loads(common_bytes)
    fixtures = {entry['id']: entry for entry in document['fixtures']}
    scratch = pathlib.Path(tempfile.mkdtemp(prefix='k1p1-a-author-fixtures-'))
    report = {'schema': 'k1p1-a-author-fixture-check', 'version': 1,
              'authority': '#1135 c6721877817', 'interpreter': str(PYTHON),
              'python_version': sys.version, 'source_before': before,
              'common_sha256': digest(common_bytes), 'scratch': str(scratch), 'runs': []}

    def expected(fid):
        entry = fixtures[fid]
        if 'expected' in entry:
            return clone(entry['expected'])
        obj = expected(entry['expected_from'])
        obj['fixture'] = fid
        for change in entry['expected_set']:
            assign(obj, change['path'], change['value'])
        return obj

    def run(label, fid, input_obj, expected_exit, expected_obj=None, extras=(), nonempty=False, absent=False):
        case_dir = scratch / label
        case_dir.mkdir()
        input_path, output_path = case_dir / 'input.json', case_dir / 'out'
        output_path.mkdir()
        if not absent:
            input_path.write_bytes(canonical(input_obj))
        if nonempty:
            (output_path / 'sentinel.txt').write_bytes(b'NF-4 preserved sentinel\n')
        original_output = output_snapshot(output_path)
        command = [str(PYTHON), '-I', str(SOURCE), '--fixture', fid,
                   '--input', str(input_path), '--out', str(output_path), *extras]
        proc = subprocess.run(command, cwd=WORKTREE, capture_output=True)
        after_output = output_snapshot(output_path)
        item = {'case': label, 'fixture_arg': fid, 'command': command,
                'input_sha256': None if absent else digest(input_path.read_bytes()),
                'exit_status': proc.returncode, 'expected_exit': expected_exit,
                'files': sorted(after_output), 'stdout_sha256': digest(proc.stdout),
                'stderr_sha256': digest(proc.stderr)}
        if expected_exit == 0:
            target = canonical(expected_obj)
            actual_path = output_path / 'fixture.json'
            actual = actual_path.read_bytes() if actual_path.is_file() else None
            item.update({'expected_sha256': digest(target),
                         'actual_sha256': None if actual is None else digest(actual),
                         'exact_file_set': sorted(after_output) == ['fixture.json'],
                         'byte_equal': actual == target})
            item['pass'] = (proc.returncode == 0 and item['exact_file_set'] and item['byte_equal'])
        else:
            item['out_unchanged'] = after_output == original_output
            item['pass'] = proc.returncode == expected_exit and item['out_unchanged']
        report['runs'].append(item)
        print(json.dumps(item, sort_keys=True, ensure_ascii=False), flush=True)
        return item

    for fid in A_IDS:
        run(fid, fid, fixtures[fid]['input'], 0, expected(fid))

    # NF-1 is pending root coordination of its independently run B control.
    assert not sys.argv[1:]
    for negative in document['interface_negatives']:
        if 'A' not in negative['programs']:
            continue
        nid = negative['id']
        if nid == 'NF-1':
            continue
        run(nid + '-control', 'SF-1a', fixtures['SF-1a']['input'], 0, expected('SF-1a'))
        input_fid = negative['input_from']
        inp = clone(fixtures[input_fid]['input']) if input_fid is not None else None
        if inp is not None:
            for change in negative['input_set']:
                assign(inp, change['path'], change['value'])
        run(nid, negative['fixture_arg'], inp, 2, extras=negative['extra_args'],
            nonempty=negative['out'] == 'nonempty', absent=input_fid is None)

    report['source_after'] = source_identity()
    report['source_unchanged'] = report['source_after'] == before
    report['nf1_scope'] = 'pending root coordination of prescribed B SF-2a positive control; not run'
    report['pass'] = report['source_unchanged'] and all(item['pass'] for item in report['runs'])
    destination = scratch / 'report.json'
    destination.write_bytes(canonical(report))
    print(json.dumps({'report': str(destination), 'report_sha256': digest(destination.read_bytes()),
                      'runs': len(report['runs']), 'pass': report['pass'],
                      'source_after': report['source_after']}, sort_keys=True), flush=True)
    return 0 if report['pass'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
```

Structured report SHA-256: `9c5cbf64fb4a43a4230c52e485515a1d3591a25a0a7d6191db18d8f40d46f27f`.

```json
{"authority":"#1135 c6721877817","common_sha256":"691aedbf0c9e74fdcc64f4c9c35f5e07c8ffc362e74360d4e541df682c750e85","interpreter":"/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","nf1_scope":"pending root coordination of prescribed B SF-2a positive control; not run","pass":true,"python_version":"3.11.17 (main, Oct  3 2026, 01:05:36) [Clang 22.1.3 ]","runs":[{"actual_sha256":"83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4","byte_equal":true,"case":"SF-1a","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-1a","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/SF-1a/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/SF-1a/out"],"exact_file_set":true,"exit_status":0,"expected_exit":0,"expected_sha256":"83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4","files":["fixture.json"],"fixture_arg":"SF-1a","input_sha256":"0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1","pass":true,"stderr_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"actual_sha256":"defa655eb09bbbd7b0e0587bb1a0a5e8495666dc1a9de7586fddf1a440ebcbdb","byte_equal":true,"case":"SF-1b","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-1b","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/SF-1b/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/SF-1b/out"],"exact_file_set":true,"exit_status":0,"expected_exit":0,"expected_sha256":"defa655eb09bbbd7b0e0587bb1a0a5e8495666dc1a9de7586fddf1a440ebcbdb","files":["fixture.json"],"fixture_arg":"SF-1b","input_sha256":"c15b30da87758d7d7d762f6cf3b282c0490f9243e7f88d7b97db800811689dc9","pass":true,"stderr_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"actual_sha256":"0c03234c086e97ab117fae3ccddd463094db75faac5189c953d2a3edc64d1880","byte_equal":true,"case":"SF-1c","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-1c","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/SF-1c/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/SF-1c/out"],"exact_file_set":true,"exit_status":0,"expected_exit":0,"expected_sha256":"0c03234c086e97ab117fae3ccddd463094db75faac5189c953d2a3edc64d1880","files":["fixture.json"],"fixture_arg":"SF-1c","input_sha256":"d44e2700ddb8e50e1061c8846d6a8ee82092583af59ac44df0bbac361448643c","pass":true,"stderr_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"actual_sha256":"20f14369d2563be85b19083847b8099adbceed994787d08c27ff490a017e0a72","byte_equal":true,"case":"SF-2p","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-2p","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/SF-2p/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/SF-2p/out"],"exact_file_set":true,"exit_status":0,"expected_exit":0,"expected_sha256":"20f14369d2563be85b19083847b8099adbceed994787d08c27ff490a017e0a72","files":["fixture.json"],"fixture_arg":"SF-2p","input_sha256":"f7d444061e8c2bfa427f66e5df7ff43ae80bf7b22548391ee340b67b66b845a7","pass":true,"stderr_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"actual_sha256":"855a8c2461aac86211ff48fc7b371d79e569f022a350f161e65e2d5dbcac1b4c","byte_equal":true,"case":"SF-2pb","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-2pb","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/SF-2pb/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/SF-2pb/out"],"exact_file_set":true,"exit_status":0,"expected_exit":0,"expected_sha256":"855a8c2461aac86211ff48fc7b371d79e569f022a350f161e65e2d5dbcac1b4c","files":["fixture.json"],"fixture_arg":"SF-2pb","input_sha256":"b8048192ccffc506f9e18981045048633ce9af1ceba1ac5f29c76fc1add20630","pass":true,"stderr_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"actual_sha256":"03dbc6e9e749d40502a99a64300cf03f14b743e1a9c7047c6ee953e8ac8496e7","byte_equal":true,"case":"SF-3","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-3","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/SF-3/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/SF-3/out"],"exact_file_set":true,"exit_status":0,"expected_exit":0,"expected_sha256":"03dbc6e9e749d40502a99a64300cf03f14b743e1a9c7047c6ee953e8ac8496e7","files":["fixture.json"],"fixture_arg":"SF-3","input_sha256":"9f6fd0a2bb09127350b1b4a8edc323c3989f95fc1097064ecfe96d31740af36a","pass":true,"stderr_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"actual_sha256":"45fef3a178d7d59a0e1b835f7db84c86f09164efe9411138bb6612be4d7bcede","byte_equal":true,"case":"SF-3f","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-3f","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/SF-3f/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/SF-3f/out"],"exact_file_set":true,"exit_status":0,"expected_exit":0,"expected_sha256":"45fef3a178d7d59a0e1b835f7db84c86f09164efe9411138bb6612be4d7bcede","files":["fixture.json"],"fixture_arg":"SF-3f","input_sha256":"80319c62df77dc8a95a16d4e640fc0c44cf4a2c9aafa6f30006ba39b2271a8af","pass":true,"stderr_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"actual_sha256":"ef2c67ff777fd36042d1ceb117d4fd4717033869f39069806547225020b10b18","byte_equal":true,"case":"SF-3g","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-3g","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/SF-3g/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/SF-3g/out"],"exact_file_set":true,"exit_status":0,"expected_exit":0,"expected_sha256":"ef2c67ff777fd36042d1ceb117d4fd4717033869f39069806547225020b10b18","files":["fixture.json"],"fixture_arg":"SF-3g","input_sha256":"03dae8724f09cbbe68e983a6dd1717f370ddf4bf2ea194c4a7716f1ca02c8064","pass":true,"stderr_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"actual_sha256":"83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4","byte_equal":true,"case":"NF-2-control","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-1a","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-2-control/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-2-control/out"],"exact_file_set":true,"exit_status":0,"expected_exit":0,"expected_sha256":"83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4","files":["fixture.json"],"fixture_arg":"SF-1a","input_sha256":"0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1","pass":true,"stderr_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"case":"NF-2","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-1a","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-2/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-2/out"],"exit_status":2,"expected_exit":2,"files":[],"fixture_arg":"SF-1a","input_sha256":"731fe83e337e733c5905006a51c2c9a4f18f3118a8f30b9a2e76955354dd5d71","out_unchanged":true,"pass":true,"stderr_sha256":"e22571e2ab64beebcbb1bf3d20624b4ed2b7044886b75641a56db478b81dca39","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"actual_sha256":"83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4","byte_equal":true,"case":"NF-3-control","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-1a","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-3-control/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-3-control/out"],"exact_file_set":true,"exit_status":0,"expected_exit":0,"expected_sha256":"83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4","files":["fixture.json"],"fixture_arg":"SF-1a","input_sha256":"0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1","pass":true,"stderr_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"case":"NF-3","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-1a","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-3/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-3/out","--stage","members"],"exit_status":2,"expected_exit":2,"files":[],"fixture_arg":"SF-1a","input_sha256":"0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1","out_unchanged":true,"pass":true,"stderr_sha256":"237e35cee811ce1ad33be102a0064dd9a808eba3f29d02bbc91ff4b5c84c8fe0","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"actual_sha256":"83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4","byte_equal":true,"case":"NF-4-control","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-1a","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-4-control/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-4-control/out"],"exact_file_set":true,"exit_status":0,"expected_exit":0,"expected_sha256":"83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4","files":["fixture.json"],"fixture_arg":"SF-1a","input_sha256":"0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1","pass":true,"stderr_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"case":"NF-4","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-1a","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-4/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-4/out"],"exit_status":2,"expected_exit":2,"files":["sentinel.txt"],"fixture_arg":"SF-1a","input_sha256":"0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1","out_unchanged":true,"pass":true,"stderr_sha256":"9ae274c568885fbab712e7d25f0f5d7a9bec26a4186fc1b995bf39538b041e5a","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"actual_sha256":"83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4","byte_equal":true,"case":"NF-5-control","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-1a","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-5-control/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-5-control/out"],"exact_file_set":true,"exit_status":0,"expected_exit":0,"expected_sha256":"83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4","files":["fixture.json"],"fixture_arg":"SF-1a","input_sha256":"0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1","pass":true,"stderr_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"case":"NF-5","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-1b","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-5/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-5/out"],"exit_status":2,"expected_exit":2,"files":[],"fixture_arg":"SF-1b","input_sha256":"0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1","out_unchanged":true,"pass":true,"stderr_sha256":"e22571e2ab64beebcbb1bf3d20624b4ed2b7044886b75641a56db478b81dca39","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"actual_sha256":"83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4","byte_equal":true,"case":"NF-6-control","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-1a","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-6-control/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-6-control/out"],"exact_file_set":true,"exit_status":0,"expected_exit":0,"expected_sha256":"83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4","files":["fixture.json"],"fixture_arg":"SF-1a","input_sha256":"0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1","pass":true,"stderr_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"case":"NF-6","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-9","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-6/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-6/out"],"exit_status":2,"expected_exit":2,"files":[],"fixture_arg":"SF-9","input_sha256":"b7799cd412fe6f8e018f8b64ff4224909b74cea82319f2cafae6fce8e2183feb","out_unchanged":true,"pass":true,"stderr_sha256":"0449ab5e94177fa6555ee76115bf9a15acbe9ffc3209ed659def73367ffa7c31","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"actual_sha256":"83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4","byte_equal":true,"case":"NF-7-control","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-1a","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-7-control/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-7-control/out"],"exact_file_set":true,"exit_status":0,"expected_exit":0,"expected_sha256":"83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4","files":["fixture.json"],"fixture_arg":"SF-1a","input_sha256":"0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1","pass":true,"stderr_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},{"case":"NF-7","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-1a","--input","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-7/input.json","--out","/tmp/k1p1-a-author-fixtures-kuknd4j5/NF-7/out"],"exit_status":2,"expected_exit":2,"files":[],"fixture_arg":"SF-1a","input_sha256":null,"out_unchanged":true,"pass":true,"stderr_sha256":"ca2a41869cf7bf40ba896114568dc4881846a928e4d91129b0bbc6bd00fd483e","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"}],"schema":"k1p1-a-author-fixture-check","scratch":"/tmp/k1p1-a-author-fixtures-kuknd4j5","source_after":{"blob":"2252965843430155fedfbc8855a5d23d13c2c920","sha256":"0e8721e5fe1c8fc8540d36ce2eed84d812a5630867ec4af56d920169466b3fdd"},"source_before":{"blob":"2252965843430155fedfbc8855a5d23d13c2c920","sha256":"0e8721e5fe1c8fc8540d36ce2eed84d812a5630867ec4af56d920169466b3fdd"},"source_unchanged":true,"version":1}
```


## Prescribed NF-1 cross-context pair completed, 2026-11-08

Root's #1135 c6721924692 verifies the independently executed B SF-2a positive
control before this A refusal. Root reports Python 3.11.17, exact canonical
SF-2a input SHA-256
`521a0ca03cb42f4d81a93f6cd9bbcc1124fb2f8de6491738e7d4e4f7a8f07bc6`,
exit 0, the exact singleton fixture.json output and expected bytes, with output
SHA-256 `4e6e0448435623c218b2c6041751981d880073482a2d8d70756ea2ff706019e4`.
Root identifies B's log-only checkpoint as
`f9a051c5ee11f97d73195dab39607d9691828b44`. This writer received that
coordination/result statement from root only, and did not read B's code, output,
report, log or checkpoint. B was not rerun here and no A positive was substituted.

Root then specifically authorized only A's prescribed SF-2a unsupported-id
refusal. It was run once with the same canonical common input and a fresh empty
output directory. Exit status 2; output remained empty and unchanged. Source
identity before/after remained blob `2252965843430155fedfbc8855a5d23d13c2c920`,
SHA-256 `0e8721e5fe1c8fc8540d36ce2eed84d812a5630867ec4af56d920169466b3fdd`.
The prescribed NF-1 pair is therefore a B positive in B's independent context,
then an A refusal in A's context, linked by root's coordination record.

Together with C37, all eight A positives and all seven prescribed A interface
negatives have passed author verification. The six earlier negatives have
local A positive pairs; NF-1 has the prescribed cross-context B positive pair.
This remains author verification, not independent cross-unit qualification.
No other test or candidate invocation occurred in this step; no instance work.

| # | Category | Commands | Result |
|---|---|---|---|
| C40 | edit; read; synthetic-fixture run | heredoc creates `/tmp/k1p1-a-nf1-check.py`; `sha256sum`; `/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11 -I /tmp/k1p1-a-nf1-check.py` | one A NF-1 refusal; harness exit 0; candidate exit 2 and empty unchanged output; source unchanged |
| C41 | edit; read | inline pathlib appends this section, full external NF-1 harness and structured report | no extra candidate run |
| C42 | static check; read; edit | source/log sensitive-data scan and digests/blobs; workflow push-trigger inspection; `git diff --check`; `git diff --stat`; own-log-only `git add`; forward `git commit`; ordinary original staging `git push` with network permission; `git rev-parse HEAD`; `git status --short` | log-only completion checkpoint, code unchanged |

The external harness and retained structured report follow.

Harness SHA-256: `53ef0ecd24abff934961983f5b7f93952f6f25f28c6e29f1f7fe9dc0efecfa4a`.

```python
"""Only A's NF-1 refusal, after root verified the prescribed B SF-2a control."""
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile

python = '/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11'
source = pathlib.Path('/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py')
common = pathlib.Path('/tmp/k1p1-common-d92/amendments/A1-fixtures.json')
expected_source = {'blob': '2252965843430155fedfbc8855a5d23d13c2c920',
                   'sha256': '0e8721e5fe1c8fc8540d36ce2eed84d812a5630867ec4af56d920169466b3fdd'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8') + b'\n'


def identity():
    return {'blob': subprocess.check_output(['git', 'hash-object', str(source)], text=True).strip(),
            'sha256': digest(source.read_bytes())}


assert sys.version_info[:2] == (3, 11)
before = identity()
assert before == expected_source
raw = common.read_bytes()
assert digest(raw) == '691aedbf0c9e74fdcc64f4c9c35f5e07c8ffc362e74360d4e541df682c750e85'
fixture = next(item for item in json.loads(raw)['fixtures'] if item['id'] == 'SF-2a')
input_bytes = canonical(fixture['input'])
assert digest(input_bytes) == '521a0ca03cb42f4d81a93f6cd9bbcc1124fb2f8de6491738e7d4e4f7a8f07bc6'
scratch = pathlib.Path(tempfile.mkdtemp(prefix='k1p1-a-author-nf1-'))
input_path, out = scratch / 'input.json', scratch / 'out'
input_path.write_bytes(input_bytes)
out.mkdir()
original_output = sorted(out.iterdir())
assert original_output == []
command = [python, '-I', str(source), '--fixture', 'SF-2a', '--input', str(input_path), '--out', str(out)]
proc = subprocess.run(command, cwd='/workspace/k1p1-impl-a', capture_output=True)
after = identity()
unchanged = sorted(out.iterdir()) == original_output
report = {'schema': 'k1p1-a-author-nf1', 'version': 1, 'case': 'NF-1',
          'root_pair_record': '#1135 c6721924692',
          'pair_scope': 'B positive independently executed and verified by root before this A refusal; B artifacts not read',
          'B_control_checkpoint': 'f9a051c5ee11f97d73195dab39607d9691828b44',
          'python_version': sys.version, 'command': command,
          'input_sha256': digest(input_bytes), 'source_before': before, 'source_after': after,
          'exit_status': proc.returncode, 'expected_exit': 2, 'out_unchanged': unchanged,
          'files': sorted(p.name for p in out.iterdir()),
          'stdout_sha256': digest(proc.stdout), 'stderr_sha256': digest(proc.stderr),
          'pass': proc.returncode == 2 and unchanged and before == after}
report_path = scratch / 'report.json'
report_path.write_bytes(canonical(report))
print(canonical(report).decode('utf-8'), end='')
print(json.dumps({'report': str(report_path), 'report_sha256': digest(report_path.read_bytes())}, sort_keys=True))
raise SystemExit(0 if report['pass'] else 1)
```

Report path: `/tmp/k1p1-a-author-nf1-fl9ik8_9/report.json`; SHA-256: `95052191cd1bc18ec8fa981a6b97735fcdf022080ef77e07479088b7794237ba`.

```json
{"B_control_checkpoint":"f9a051c5ee11f97d73195dab39607d9691828b44","case":"NF-1","command":["/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11","-I","/workspace/k1p1-impl-a/verification/lean/k1p1_enum_a.py","--fixture","SF-2a","--input","/tmp/k1p1-a-author-nf1-fl9ik8_9/input.json","--out","/tmp/k1p1-a-author-nf1-fl9ik8_9/out"],"exit_status":2,"expected_exit":2,"files":[],"input_sha256":"521a0ca03cb42f4d81a93f6cd9bbcc1124fb2f8de6491738e7d4e4f7a8f07bc6","out_unchanged":true,"pair_scope":"B positive independently executed and verified by root before this A refusal; B artifacts not read","pass":true,"python_version":"3.11.17 (main, Oct  3 2026, 01:05:36) [Clang 22.1.3 ]","root_pair_record":"#1135 c6721924692","schema":"k1p1-a-author-nf1","source_after":{"blob":"2252965843430155fedfbc8855a5d23d13c2c920","sha256":"0e8721e5fe1c8fc8540d36ce2eed84d812a5630867ec4af56d920169466b3fdd"},"source_before":{"blob":"2252965843430155fedfbc8855a5d23d13c2c920","sha256":"0e8721e5fe1c8fc8540d36ce2eed84d812a5630867ec4af56d920169466b3fdd"},"stderr_sha256":"0449ab5e94177fa6555ee76115bf9a15acbe9ffc3209ed659def73367ffa7c31","stdout_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","version":1}
```
