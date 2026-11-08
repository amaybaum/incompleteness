# K1-P1-1 implementation B: drafting log (staging only)

WIP / UNVERIFIED. Staging-branch record of writer `writer-k1p1-impl-b` (hand-off name `writer-k1p1-implB`), Claude
Code session https://claude.ai/code/session_011zDyUSyEszk3JJx83uXKKq. This file is not part of the code freeze; it is
the per-command log required by the preregistration's §19 (Finding 10) and §12 item 2. It is not intended for the
round branch or for `main`.

- **Round** K1-P1-1; control plane PR #1135 at `4ca431afb1bfee0cdf301f0917c73068fdf09b58`, file
  `verification/programmes/oi-qm/reconstruction/round-k1-p1-1/preregistration.md`, blob
  `e7957cd4eff6b6c5d7dfe491fa2f8768a2d3d141`, SHA-256 `904f6ebee14d0ce770a85548353980f2242aadca8e1cb7e39bee2c3779e1d596`.
- **Branch** `staging/k1-p1-1-impl-b-20261106`, cut from `origin/main` at `424f28b1e7b1201e9a13bd0e608e1b0e4ad9f93b`.
  The preregistration names no staging branch or layout; the branch name is the coordinator's.
- **Authority.** amaybaum, #1031 comment 6677496553 (2026-11-06): "Authorize Stage 2: pre-F code drafting, under these
  boundaries: Three independent writers prepare implementation A, implementation B and `controls.py`, using the
  reviewed control plane and separate staging branch. Only static analysis and predeclared synthetic-fixture tests are
  permitted. No computation on the K1 instance, its dynamics or its states. [...]" Not authorized: `F` designation,
  K1-instance enumeration, scientific execution, workflow dispatch, `E`, merge or theorem promotion.

## Hand-off record

- **Received** 2026-11-06, shortly before 05:15Z, from the coordinating session (the session that spawned this writer):
  the task statement naming this round, PR #1135 at `4ca431af`, the owner authorization quoted above, the branch name,
  the worktree path and the rules of this drafting.
- **Read by this writer:** the preregistration at `4ca431af` (whole file, 1271 lines); the adopted text, K1-RDY-1's
  control plane at `F` = `d9b3de012e393262adb20f91ad49627bad48de43`: `preregistration.md` (whole) and amendments A2,
  A3, A5, A8, A9; `AGENTS.md` (supplied in context); the trigger blocks of `.github/workflows/*.yml` at `424f28b1`.
- **Adopted-text digests verified** against the preregistration's §2 table: all six SHA-256 values and blob ids match,
  and `head -n 313 preregistration.md | sha256sum` gives `a93f3f33f0c5a6e8b2467312d184fa2d2e915296490948938c4dd7832c64bb63`.
- **Not read, not fetched:** implementation A, `controls.py`, any branch of the other writers, and any K1-RDY-1 output
  (`gate-table.json`, `result.md`, `derivations/`). No proof file (`LEMMAS.md`, `PROOFS.md`) was read.
- **Delivered:** `verification/lean/k1p1_enum_b.py`, SHA-256 below.

## Command log

Categories: **read** (reading text, listing, counting, digests of text); **static check** (parsing or compiling B
without executing it); **synthetic-fixture run** (§11.2 fixtures only); **git** (branch, worktree, commit, push; no
computation); **file write** (a file written by the editor tool). No command was run on the instance, its dynamics or
its states. Times are UTC, 2026-11-06.

| # | Time (about) | Category | Command | Result |
|---|---|---|---|---|
| 1 | 05:16 | read | `df -h /tmp /home/user` (§A.40 disk check) | 18G free |
| 2 | 05:16 | git | `git fetch origin 4ca431afb1bfee0cdf301f0917c73068fdf09b58` | fetched |
| 3 | 05:16 | read | `git cat-file -t 4ca431af…`; `git show 4ca431af:<prereg> \| wc -l` | commit; 1271 lines |
| 4 | 05:16 | read | `git show 4ca431af:<prereg> > <scratch>/prereg.md`; `sed -n 1,250p`, `250,560p`, `560,900p`, `900,1271p` (via the Read tool) | read whole file |
| 5 | 05:17 | git | `git fetch origin main` | fetched |
| 6 | 05:17 | read | `git cat-file -t d9b3de01…`; `git show d9b3de01:<K path>/<6 files> > <scratch>/K/…`; `sha256sum`; `git rev-parse d9b3de01:<file>`; `head -313 preregistration.md \| sha256sum`; `wc -l` | six digests and blob ids match §2; 313-line digest matches |
| 7 | 05:18 | read | `sed -n 1,120p`, `120,320p`, `320,397p` of K's `preregistration.md`; `cat` of A2, A3, A5, A8, A9 | read |
| 8 | 05:19 | read | `python3 --version`; `grep -n` and a `python3 -I -c` scan of `<scratch>/prereg.md` printing the code points of quoted strings (`T2's`, `H-μ`, `𝓘`, `CC-IMP″`) | Python 3.13.18 locally; apostrophe ASCII, U+03BC, U+1D4D8, U+2033 |
| 9 | 05:19 | read | `git ls-remote --heads origin 'staging/k1-p1-1-impl-b*' 'staging/*k1*'`; `git rev-parse origin/main FETCH_HEAD`; `ls <worktree path>` | no such branch; main `424f28b1`; path absent |
| 10 | 05:20 | git | `git -C /home/user/incompleteness worktree add -b staging/k1-p1-1-impl-b-20261106 <scratchpad>/wt/wk1b 424f28b1…`; `git log -1`; `ls verification/lean`, `ls .github/workflows` | worktree created |
| 11 | 05:20 | read | `python3 -I -c` printing the `on:` block of each `.github/workflows/*.yml` | no `push` trigger matches this branch (below) |
| 12 | 05:24 | file write | `verification/lean/k1p1_enum_b.py` (editor tool) | written |
| 13 | 05:25 | static check | `python3 -I static_b.py verification/lean/k1p1_enum_b.py` (tool below) | exit 0: imports `fractions, hashlib, json, os, sys`; no `/`, no float literal, no `float()`/`eval`/`exec`; every `**` has a non-negative integer exponent (11 sites listed, checked by reading); top level is imports, definitions, constants and the `__main__` guard only |
| 14 | 05:25 | read | `wc -l`, `sed -n 1,6p \| cat -A`, `grep -c '^$'`, `file`, `sed -n 40,80p \| cat -A`, `grep -n '^def \|^class '`, `grep -n 'u2032\|…'` on B | 1250 lines, LF endings; the editor wrote some `\u` escapes as literal characters |
| 15 | 05:26 | static check | `python3 -I -c` AST scan listing every non-ASCII code point in B's string constants; `grep -n stderr.write` | only U+1D4D8, U+2032, U+2033, U+2229 (a docstring), U+03BC, U+03C0, as required |
| 16 | 05:26 | synthetic-fixture run | `python3 -I -B sf_b.py verification/lean/k1p1_enum_b.py` (tool below); `ls verification/lean \| grep -c pycache`; `git status --porcelain`; `date -u` | exit 0: SF-1 lengths [1, 2, 3, 6], least elements [0, 1, 3, 6], coverage 12, per-cycle checks true; SF-2 ranks 3, 0, 2; no bytecode written |
| 17 | 05:27 | read | `git rev-parse 4ca431af:<prereg>`; `sha256sum` of the preregistration, B and the two tools; `git hash-object` of B; `date -u` | digests recorded below |
| 18 | 05:28 | file write | this log | written |
| 19 | 05:28 | read | `sha256sum` of this log and B; `git status` | recorded in the checkpoint comment |
| 20 | 05:28 | git | `git add` of B and this log; `git commit`; `git push -u origin staging/k1-p1-1-impl-b-20261106` | see the checkpoint comment on #1135 |

**Push triggers** (§A.43 item 4), read at `424f28b1`: `verify.yml` and `hidden-sector-replay.yml` trigger on `push`
to `main` only; `bg2-orientation-design.yml` and `bridge-compatibility-research.yml` have `push` path filters naming
other directories; `evidence-replay.yml`, `oret-phasea.yml`, `pe01-bounded-tests.yml` and `project-board.yml` are
dispatch-only. A push of this branch starts no workflow. No pull request is opened from it, so no pull-request run
starts. No dispatch was made.

## Files

| File | SHA-256 |
|---|---|
| `verification/lean/k1p1_enum_b.py` | `1adc93d872cc7a788555c6226fa8644dc7f132a2fab56aa54a391065f09f2440` (git blob `cc5d1d8f2caeaabd1b83d919f3af79d896de129d`) |
| `static_b.py` (scratchpad tool, text below) | `ab1c3ec06ae12738bfdb87fff7017841b01b23d88c20a81b937bfe4adf7a8335` |
| `sf_b.py` (scratchpad tool, text below) | `977d30c9ef494aea438713c5a45b097eb98888d5a5732028593450359d94ece6` |

The tools are not committed as files; their exact text follows, so that each command above can be replayed.

### `static_b.py`

```python
"""Static checks of k1p1_enum_b.py. Parses the file; never imports or runs it."""
import ast, sys
path = sys.argv[1]
src = open(path, encoding="utf-8").read()
tree = ast.parse(src, filename=path, feature_version=(3, 11))
compile(src, path, "exec")          # syntax/bytecode check only; nothing executed, no .pyc written
ALLOWED = {"fractions", "itertools", "json", "hashlib", "sys", "os"}
imports, problems = [], []
for node in ast.walk(tree):
    if isinstance(node, ast.Import):
        imports += [a.name for a in node.names]
    elif isinstance(node, ast.ImportFrom):
        imports.append(node.module)
    elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
        problems.append("true division at line %d" % node.lineno)
    elif isinstance(node, ast.AugAssign) and isinstance(node.op, ast.Div):
        problems.append("true division (aug) at line %d" % node.lineno)
    elif isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
        problems.append("float/complex literal at line %d" % node.lineno)
    elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ("float", "eval", "exec", "__import__", "compile"):
        problems.append("call to %s at line %d" % (node.func.id, node.lineno))
    elif isinstance(node, ast.Attribute) and node.attr in ("log", "sqrt", "exp", "truediv"):
        problems.append("attribute %s at line %d" % (node.attr, node.lineno))
bad = sorted(set(m.split(".")[0] for m in imports) - ALLOWED)
print("imports:", sorted(set(imports)))
print("disallowed imports:", bad)
pows = [(n.lineno, ast.unparse(n)) for n in ast.walk(tree) if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Pow)]
print("power expressions (exponent must be a non-negative int):")
for ln, t in pows: print("  line %d: %s" % (ln, t))
top = []
for node in tree.body:
    if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef)):
        continue
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
        continue   # module docstring
    if isinstance(node, ast.Assign):
        calls = [n for n in ast.walk(node.value) if isinstance(n, ast.Call)]
        ok_calls = all(isinstance(c.func, ast.Name) and c.func.id in ("Fraction", "dict") for c in calls)
        if ok_calls:
            continue
        top.append("assignment with calls at line %d" % node.lineno)
        continue
    if isinstance(node, ast.If) and ast.unparse(node.test) == "__name__ == '__main__'":
        continue
    top.append("%s at line %d" % (type(node).__name__, node.lineno))
print("top-level statements other than imports/defs/constants/main guard:", top)
opens = [(n.lineno, ast.unparse(n)) for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "open"]
print("open() calls:")
for ln, t in opens: print("  line %d: %s" % (ln, t))
print("problems:", problems)
sys.exit(1 if (bad or problems or top) else 0)
```

### `sf_b.py`

```python
"""SF-1 and SF-2 (preregistration section 11.2) on implementation B's generic functions.

Loads B by path (python3 -I -B: no bytecode written) and calls only orbit_partition and
rank_f2 on the fixtures' own inputs. B's module top level defines constants and functions
only (static check), so loading it computes nothing on the K1 instance.
"""
import importlib.util, sys
spec = importlib.util.spec_from_file_location("k1p1_enum_b", sys.argv[1])
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
fails = []

# SF-1: permutation of {0..11} with cycles (0)(1 2)(3 4 5)(6 7 8 9 10 11).
perm = [0, 2, 1, 4, 5, 3, 7, 8, 9, 10, 11, 6]
cycles, ok = b.orbit_partition(perm)
lengths = [len(st) for _, st in cycles]
leasts = [least for least, _ in cycles]
coverage = sum(lengths)
print("SF-1 lengths", lengths, "leasts", leasts, "coverage", coverage, "ok", ok)
if lengths != [1, 2, 3, 6] or leasts != [0, 1, 3, 6] or coverage != 12 or not ok:
    fails.append("SF-1")

# SF-2: F_2 ranks; row bit masks with column 0 as the top bit (B's convention).
def rows_of(mat):
    return [int("".join(str(x) for x in r), 2) for r in mat]
cases = [("identity", [[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
         ("zero", [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
         ("[[1,1,0],[0,1,1],[1,0,1]]", [[1, 1, 0], [0, 1, 1], [1, 0, 1]], 2)]
for name, mat, want in cases:
    got = b.rank_f2(rows_of(mat), 3)
    print("SF-2", name, "rank", got, "expected", want)
    if got != want:
        fails.append("SF-2 " + name)
print("FAILURES:", fails)
sys.exit(1 if fails else 0)
```


## Independent continuation, 2026-11-08 — STATIC ONLY

WIP / UNVERIFIED. Continued by independent Codex agent `k1p1_impl_b_revision`, coordinated
by the root Codex session. This is not the original Claude author session; that historical
provenance and its exploratory run above remain unchanged. The existing staging branch and
single-parent history continue from `e32fe4eea312b1a468ea19ed1f1559d768c5dbda`.
Owner scope: #1031 c6721619842; activation checkpoint: #1135 c6721746629 (provenance).
No freeze, F/E designation, instance computation, dispatch, merge or scientific claim promotion.

Current common inputs are the preregistration and the whole A1 amendment with both fixture
companions at `d92e0882e7609e91e3458193391e89610fffa777`, adopted K rules at
`d9b3de012e393262adb20f91ad49627bad48de43`, root `AGENTS.md`, and the two root briefs
`/tmp/k1p1-revision-common-brief.txt` and `/tmp/k1p1-b-role-brief.txt`.
The root disclosed independent hand acceptance of the fixture expectations, including the
specific SF-2pb negative: it exits 0 recording `bijection=false`; the harness must require
CC-BIJ-prime failure. No other implementation, output, checkpoint or code package was read.
The amendment is the disclosed common behavioural channel, containing no implementation code.

This checkpoint adds all fourteen B admission hashes; fixture CLI/strict usage/refusal paths;
generic bitmask/matrix M1/M2, matrix-power region, orbit/member, rank/Mobius chain and complete
row/CLASS computations shared with the instance route; exact Q10 top-level adversarial fields,
coverage/duplicate/ignore-by-key behavior; and Q5's S0 refusal at rows/final. Existing pending
G6/G7, G6 mismatch, union/null, hypotheses, token order and serializer are retained. Instance-only
inverse construction remains obvious for the future single-entry MU-C2 patch; no patch was made.
No fixture expected answer is encoded in an algorithm. The admission table is input digests only.

**Validation boundary.** Only source parsing/compilation, hashing and inspection occurred.
No candidate code was imported, executed or invoked (including help), no fixture ran, and no
K1 state, dynamics or instance calculation ran. No independent static acceptance is claimed.
Root must separately authorize the exact admitted subprocess fixture commands after its safe-path
review. Instance record schemas/S0/preserved/union-only paths remain statically covered only.
No remaining normative ambiguity identified; synthetic byte equality is untested at this point.

The following table records continuation commands, including reads/digests with no verdict use.
Repeated reads are grouped only where the command is the same with listed literal ranges.
Categories use A1's five names; the old log's git/file-write labels above are historical.

| Category | Commands | Result |
|---|---|---|
| read | `cat /tmp/k1p1-revision-common-brief.txt /tmp/k1p1-b-role-brief.txt /workspace/incompleteness/AGENTS.md` | Handoff and guide; tool display truncated, followed by targeted guide reads |
| read | `wc -l AGENTS.md verification/lean/k1p1_enum_b.py k1p1_enum_b.drafting-log.md /tmp/k1p1-common-d92/* /tmp/k1p1-common-d92/amendments/*` | Counts only; wrong short log path absent, then correct path used |
| read | `cat /tmp/k1p1-common-d92/amendments/A1-frozen-code.md`; `sed -n` ranges `290,540p`, `320,475p`, `260,291p`, `540,608p` on that file | Whole amendment plus targeted rereads after truncation |
| read | `sed -n` ranges `1,400p`, `400,700p`, `700,1000p` of worktree AGENTS; `1000,1210p`, `360,400p` of root guide | Operative guide read; root guide governs |
| read | `sed -n` ranges `1,420p`, `420,740p`, `740,1250p` of B | Own original source only |
| read | `cat /tmp/k1p1-common-d92/amendments/A1-fixtures.json`; `sed -n '165,265p'` of that file | Common definitions and expectations only |
| read | `sed -n` ranges `1,240p`, `235,398p` of A1-fixtures.md | Hand derivations and negative fixture specification |
| read | `sed -n` ranges `1,240p`, `241,530p`, `531,800p`, `800,1040p`, `1041,1271p` of common preregistration | Whole pinned procedure |
| read | `cat verification/lean/k1p1_enum_b.drafting-log.md`; `rg --files .github/workflows`; `git status --short`; `git branch --show-current` | Own prior provenance, path scope, branch confirmed |
| read | `skills.read` cloud-environment-runtime and its networking reference; environment-status tool; `cat /etc/codex/network-policy.json`; `git remote -v`; `df -h /workspace /tmp`; `git status --porcelain` | Managed environment running, network enforced, ample disk, expected remote/only B modified; no credential read |
| read | `git show d9b3de01:<K-prefix>/preregistration.md` and each of A2/A3/A5/A8/A9 | Adopted rule text only, no execution-output files |
| edit | Write `/tmp/k1p1-b-edit.py`; `python3 -I /tmp/k1p1-b-edit.py`; write `/tmp/k1p1-b-add.py`; `python3 -I /tmp/k1p1-b-add.py` | Source splices only; neither imports/executes candidate |
| edit | Write `/tmp/k1p1-b-static.py` | Static checker below |
| static check | `python3 -I /tmp/k1p1-b-static.py` | PASS Python-3.11 AST/compile, allowlisted imports, no true division/inexact literal, all 14 hashes; fixture call graph excludes instance constants/builders/S0/preserved |
| static check | `git diff --check`; `git diff --stat`; `git diff -- verification/lean/k1p1_enum_b.py` | Whitespace clear; own diff inspected |
| read | Python stdin text scan printing each workflow `on:` block | verify/hidden-sector push main only; bg2/bridge unrelated paths; four others dispatch only; neither changed B path matches push triggers |
| edit | Write and run `/tmp/k1p1-b-log.py` | This append only |

Static checker SHA-256: `03306eed6ff1d089aab4d1911045856c5f38fbf521c517337d019eec028aa5c1`.
Its source (parses/compiles candidate AST; never imports/executes it):

```python
import ast, hashlib, json
from pathlib import Path
p=Path('/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py')
s=p.read_text(); t=ast.parse(s, feature_version=(3,11)); compile(t,str(p),'exec')
imports=[]; bad=[]
for n in ast.walk(t):
    if isinstance(n, ast.Import): imports += [x.name for x in n.names]
    if isinstance(n, ast.ImportFrom): imports += [n.module]
    if isinstance(n,(ast.BinOp,ast.AugAssign)) and isinstance(n.op,ast.Div): bad += [('division',n.lineno)]
    if isinstance(n,ast.Constant) and isinstance(n.value,(float,complex)): bad += [('inexact literal',n.lineno)]
    if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id in {'exec','eval','__import__','compile','float'}: bad += [('call',n.lineno)]
assert set(imports) <= {'fractions','itertools','json','hashlib','sys','os'}
assert not bad,bad
funcs={n.name:n for n in t.body if isinstance(n,ast.FunctionDef)}
# Traverse calls from fixture computation, excluding the optional instance-record
# arm of compute_rows, which is statically guarded by record is not None.
seen=set(); todo=['run_fixture']
while todo:
    name=todo.pop()
    if name in seen: continue
    seen.add(name)
    for n in ast.walk(funcs[name]):
        if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id in funcs and n.func.id != 'load_adversarial': todo.append(n.func.id)
forbidden={'N','Q','A_PARAM','D_PARAM','T_WINDOW','INSTANCE','V_CELL','SIGMA_CELLS','CELL_ORDER_N5','K_MAX_CYC2','M10_POWER','CONTROL_EXPECTED','CONTROL_GATES','S0_PAPER_IDS','CLASS_DERIVATIONS','EPSILON_CC_EXACT','N_CC_IMP2'}
assert not seen & {'build_instance','compute_controls','compute_preserved','compute_cyc2','phi_coefficients','phi_inverse_coefficients'}
for name in seen:
    assert not ({n.id for n in ast.walk(funcs[name]) if isinstance(n,ast.Name) and isinstance(n.ctx,ast.Load)} & forbidden),(name,'instance constant')
assign=next(n for n in t.body if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='FIXTURE_INPUT_SHA256' for x in n.targets))
table=ast.literal_eval(assign.value)
fixtures=json.loads(Path('/tmp/k1p1-common-d92/amendments/A1-fixtures.json').read_bytes())
for f in fixtures['fixtures']:
    if 'B' in f['programs']:
        raw=(json.dumps(f['input'],sort_keys=True,separators=(',',':'),ensure_ascii=False)+'\n').encode()
        assert hashlib.sha256(raw).hexdigest()==table[f['id']],f['id']
assert len(table)==14
print('PASS: parse/compile Python 3.11; imports; exact arithmetic AST; all 14 admission pins; fixture call-graph constants')
print('Fixture generic callees:', ', '.join(sorted(seen)))
print('Read arms: load_fixture reads --input; compute_rows record=None selects entries, never load_adversarial')
print('Code SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
```

| Category | Additional checkpoint commands | Result |
|---|---|---|
| read | `sed -n '475,545p' A1-frozen-code.md`; `sed -n '130,168p' A1-fixtures.json`; `sed -n '385,402p' /workspace/incompleteness/AGENTS.md` | Targeted completion of truncated displays |
| static check | Python stdin `git show d92:<path>` versus disposable-copy byte comparison and SHA-256 for preregistration and three A1 files | All four byte-identical; JSON digest `691aedbf0c9e74fdcc64f4c9c35f5e07c8ffc362e74360d4e541df682c750e85` |
| static check | Python stdin scan of both changed files for private-key headers, credential/token patterns, signed URLs, IPv4 and email addresses; `git diff --check`; `python3 -I /tmp/k1p1-b-static.py` | Publication and final static checks; results in checkpoint message |
| read | `sha256sum` of B/log/static/edit scripts; `git hash-object` of B/log; `git diff --name-only`; `git status --short` | Exact pins and permitted path set reported to root |
| edit | `git -c core.hooksPath=/dev/null add verification/lean/k1p1_enum_b.py verification/lean/k1p1_enum_b.drafting-log.md`; `git -c core.hooksPath=/dev/null commit -m 'WIP: apply A1 to independent B with digest-admitted fixtures (static only)'`; `git -c core.hooksPath=/dev/null push origin staging/k1-p1-1-impl-b-20261106` | Forward static-only milestone; resulting immutable SHA/push status reported to root |
| read | `git rev-parse HEAD HEAD^ HEAD:verification/lean/k1p1_enum_b.py HEAD:verification/lean/k1p1_enum_b.drafting-log.md`; `git status --short`; `git log -1 --format=fuller` | Parent/pins/clean-tree confirmation |


## Authorized bounded author fixture verification — 2026-11-08

Authority: root's explicit go-ahead under #1135 c6721877817, after the independent
non-author full static ACCEPT and safe-path review of source commit
`79ff3a7ae5bed4e7ebc044c52bae551362780189`, blob
`63eadd818e59f86c48969552ef144f56b4154b95`; independent hand review of the d92
expectations preceded that review. This records author verification only, not the final
cross-unit integration qualification. No new interpretation or expected answer was adopted.

Actual interpreter: `/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11`,
`Python 3.11.17`. Source SHA-256 before and after:
`c5bfb8d198ed464c093ebf38ddc6f0d0e160f3e5e91395b1f98014c33928c7e5`.
B source is unchanged. The whole batch completed by the result-file mtime
`2026-11-08T13:09:00.471384+00:00`; harness-file mtime was
`2026-11-08T13:08:54.058332+00:00`. No per-subprocess timestamp was captured, so
these are batch bounds only. Tool execution first returned at about 1.002 seconds and
the immediate completion poll returned status 0.

**Results.** All 14 exact d92 admitted B fixtures pass, including NF-1's prescribed B
positive SF-2a. All required output files match the exact canonical expected bytes and
file sets; no extra file occurs. SF-2pb exits 0 and matches the explicit
`bijection=false` expectation and the unchanged SF-2p rank chain. This author harness
does not run controls or claim to have checked CC-BIJ-prime itself.
NF-2 through NF-7 each follows a fresh passing paired SF-1a run, exits 2 and leaves
its fresh output directory byte-identical (NF-4 preserves its sole sentinel file).
The predeclared mixed `--stage members` string occurs only in NF-3's refusal argv.
No candidate was imported, no instance entry point was invoked, no patched mutant or
other implementation/control was read or run, and no K1/scientific computation occurred.
No code or expectation repair was needed.

SF-2a input SHA-256:
`521a0ca03cb42f4d81a93f6cd9bbcc1124fb2f8de6491738e7d4e4f7a8f07bc6`;
exit 0; exact file set `fixture.json`; canonical expected byte equality true;
output SHA-256 `4e6e0448435623c218b2c6041751981d880073482a2d8d70756ea2ff706019e4`;
stdout and stderr both empty. Root coordinates the cross-writer NF-1 pair; this
writer neither executes nor reads A's leg.

External harness SHA-256: `d6b9567c938d775b1e57eee8cb7fe380261c03039ea34ba6e55ac119db803f7a`.
Structured result SHA-256: `8af33f4fb0a6b22c7a4388cf845625f94ea31b345ed994df1144cb119f6d0d22` (canonical bytes, before pretty-printing below).
All exact candidate argv vectors, input digests, exit statuses, file sets and byte
comparisons are retained in the structured report below. Fresh temporary directories
were removed by `TemporaryDirectory` only after all comparisons; this removes disposable
author-test files, not repository evidence.

### Continuation command table

| Category | Command | Result |
|---|---|---|
| read | `git rev-parse HEAD HEAD:verification/lean/k1p1_enum_b.py`; `sha256sum verification/lean/k1p1_enum_b.py`; interpreter `--version`; `git status --short` | Exact accepted source and actual Python 3.11.17; clean starting tree |
| edit | Write `/tmp/k1p1-b-fixtures-20261108.py` through shell heredoc | External bounded harness below |
| static check | `sha256sum /tmp/k1p1-b-fixtures-20261108.py` | Harness digest above; source statically inspected before invocation |
| synthetic-fixture run | `/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11 -I /tmp/k1p1-b-fixtures-20261108.py` | Exit 0; 14 positives plus 6 paired positives, 6 interface negatives; no failures |
| read | Python stdin extracting SF-2a structured report plus harness/report mtime and source/interpreter metadata | Root received passing B SF-2a evidence promptly; batch timing only |
| read | Python stdin printing each structured case and every workflow `on:` block; `git diff -- .github/workflows`; `git status --short`; hashes of B/harness/report | All cases pass; workflows unchanged and no push trigger matches own branch/log path |
| edit | Write/run `/tmp/k1p1-b-fixture-log-append.py` | This log append; full harness/results retained |
| static check | Publication sensitive-pattern scan of both own files; `git diff --check`; `git diff --name-only`; `git diff --exit-code -- verification/lean/k1p1_enum_b.py` | Safe log-only path set, whitespace and unchanged-source checks; exact outcomes in root checkpoint |
| read | `sha256sum` B/log/harness/report; `git hash-object` B/log | Exact pins reported to root |
| edit | `git -c core.hooksPath=/dev/null add verification/lean/k1p1_enum_b.drafting-log.md`; forward log-only `git -c core.hooksPath=/dev/null commit -m 'Record authorized B fixture verification on Python 3.11.17'`; same-branch `git -c core.hooksPath=/dev/null push origin staging/k1-p1-1-impl-b-20261106` | Published checkpoint; if sandbox proxy fails, identical push retried with reviewed escalation, as for prior source checkpoint |
| read | `git rev-parse HEAD HEAD^ HEAD:verification/lean/k1p1_enum_b.py HEAD:verification/lean/k1p1_enum_b.drafting-log.md`; `git status --short`; `git diff HEAD^ --name-only` | Clean-tree, code blob unchanged, log-only confirmation |

The prior source checkpoint's initial sandbox push failed to reach the inherited proxy;
the identical authorized push succeeded outside the sandbox following automatic review.
No branch rewrite or dispatch occurred. This records that transport detail forward.

### Exact external harness

```python
"""Bounded author fixture verification, only B CLI and exact d92 input bytes."""
import copy
import hashlib
import json
import pathlib
import subprocess
import tempfile

PYTHON = '/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11'
WORKTREE = pathlib.Path('/workspace/k1p1-impl-b')
PROGRAM = WORKTREE / 'verification/lean/k1p1_enum_b.py'
COMMON = pathlib.Path('/tmp/k1p1-common-d92/amendments/A1-fixtures.json')
RESULT = pathlib.Path('/tmp/k1p1-b-fixtures-20261108.results.json')
SOURCE_SHA = 'c5bfb8d198ed464c093ebf38ddc6f0d0e160f3e5e91395b1f98014c33928c7e5'
FIXTURES_SHA = '691aedbf0c9e74fdcc64f4c9c35f5e07c8ffc362e74360d4e541df682c750e85'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(obj):
    return (json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False) + '\n').encode('utf-8')


def set_path(obj, path, value):
    target = obj
    for part in path[:-1]:
        target = target[part]
    target[path[-1]] = copy.deepcopy(value)


def snapshot(directory):
    return {p.name: p.read_bytes() for p in directory.iterdir()}


raw = COMMON.read_bytes()
assert sha(raw) == FIXTURES_SHA
assert sha(PROGRAM.read_bytes()) == SOURCE_SHA
spec = json.loads(raw)
fixtures = {f['id']: f for f in spec['fixtures']}
expected_cache = {}
cyc_cache = {}


def expectation(fixture_id, cyc=False):
    cache = cyc_cache if cyc else expected_cache
    if fixture_id in cache:
        return copy.deepcopy(cache[fixture_id])
    f = fixtures[fixture_id]
    field = 'expected_cyc2' if cyc else 'expected'
    if field + '_from' in f:
        result = expectation(f[field + '_from'], cyc)
        result['fixture'] = fixture_id
    else:
        result = copy.deepcopy(f[field])
    if not cyc:
        for change in f.get('expected_set', []):
            set_path(result, change['path'], change['value'])
    cache[fixture_id] = result
    return copy.deepcopy(result)


report = {
    'authority': '#1135 c6721877817',
    'kind': 'author-bounded-fixture-verification',
    'python': PYTHON,
    'python_version': subprocess.check_output([PYTHON, '--version'], text=True).strip(),
    'source_commit': '79ff3a7ae5bed4e7ebc044c52bae551362780189',
    'source_blob': '63eadd818e59f86c48969552ef144f56b4154b95',
    'source_sha256_before': sha(PROGRAM.read_bytes()),
    'fixtures_sha256': sha(raw),
    'cases': [],
}


def positive(fixture_id, root, label):
    f = fixtures[fixture_id]
    assert 'B' in f['programs']
    case_dir = root / label
    case_dir.mkdir()
    input_path = case_dir / 'input.json'
    input_path.write_bytes(canonical(f['input']))
    out = case_dir / 'out'
    out.mkdir()
    argv = [PYTHON, '-I', str(PROGRAM), '--fixture', fixture_id,
            '--input', str(input_path), '--out', str(out)]
    process = subprocess.run(argv, cwd=WORKTREE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    wanted = {'fixture.json': canonical(expectation(fixture_id))}
    cyc = expectation(fixture_id, True)
    if cyc is not None:
        wanted['fixture-cyc2.json'] = canonical(cyc)
    actual = snapshot(out)
    equal = {name: actual.get(name) == data for name, data in wanted.items()}
    ok = process.returncode == f['exit'] and set(actual) == set(wanted) and all(equal.values())
    report['cases'].append({
        'case': label, 'fixture': fixture_id, 'role': 'positive', 'argv': argv,
        'input_sha256': sha(input_path.read_bytes()), 'exit_status': process.returncode,
        'expected_exit': f['exit'], 'output_files': sorted(actual),
        'expected_files': sorted(wanted), 'byte_equal': equal,
        'output_sha256': {name: sha(data) for name, data in actual.items()},
        'stdout_sha256': sha(process.stdout), 'stderr_sha256': sha(process.stderr), 'pass': ok,
    })
    return ok


with tempfile.TemporaryDirectory(prefix='k1p1-b-author-fixtures-') as temp:
    root = pathlib.Path(temp)
    for fixture_id in fixtures:
        if 'B' in fixtures[fixture_id]['programs']:
            positive(fixture_id, root, fixture_id)
    for negative in spec['interface_negatives']:
        if 'B' not in negative['programs']:
            continue
        negative_id = negative['id']
        assert negative_id in {'NF-2', 'NF-3', 'NF-4', 'NF-5', 'NF-6', 'NF-7'}
        source_id = negative['input_from'] or 'SF-1a'
        control_ok = positive(source_id, root, negative_id + '-paired-control')
        case_dir = root / negative_id
        case_dir.mkdir()
        input_path = case_dir / 'input.json'
        if negative['input_from'] is not None:
            data = copy.deepcopy(fixtures[negative['input_from']]['input'])
            for change in negative['input_set']:
                set_path(data, change['path'], change['value'])
            input_path.write_bytes(canonical(data))
        out = case_dir / 'out'
        out.mkdir()
        if negative['out'] == 'nonempty':
            (out / 'sentinel.txt').write_bytes(b'NF-4 sentinel\n')
        before = snapshot(out)
        argv = [PYTHON, '-I', str(PROGRAM), '--fixture', negative['fixture_arg'],
                '--input', str(input_path), '--out', str(out)] + negative['extra_args']
        process = subprocess.run(argv, cwd=WORKTREE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        after = snapshot(out)
        unchanged = before == after
        ok = control_ok and process.returncode == negative['exit'] and unchanged
        report['cases'].append({
            'case': negative_id, 'role': 'interface-negative', 'argv': argv,
            'input_sha256': sha(input_path.read_bytes()) if input_path.exists() else None,
            'exit_status': process.returncode, 'expected_exit': negative['exit'],
            'output_files': sorted(after), 'output_unchanged': unchanged,
            'paired_control_pass': control_ok, 'stdout_sha256': sha(process.stdout),
            'stderr_sha256': sha(process.stderr), 'pass': ok,
        })
report['source_sha256_after'] = sha(PROGRAM.read_bytes())
report['source_unchanged'] = report['source_sha256_before'] == report['source_sha256_after'] == SOURCE_SHA
report['pass'] = report['source_unchanged'] and all(case['pass'] for case in report['cases'])
RESULT.write_bytes(canonical(report))
print(json.dumps({'pass': report['pass'], 'positive_cases': sum(c['role']=='positive' for c in report['cases']),
                  'negative_cases': sum(c['role']=='interface-negative' for c in report['cases']),
                  'failed': [c['case'] for c in report['cases'] if not c['pass']],
                  'source_unchanged': report['source_unchanged'], 'result_sha256': sha(RESULT.read_bytes())}, sort_keys=True))
raise SystemExit(0 if report['pass'] else 1)
```

### Structured author results

```json
{
  "authority": "#1135 c6721877817",
  "cases": [
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-1a",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-1a/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-1a/out"
      ],
      "byte_equal": {
        "fixture.json": true
      },
      "case": "SF-1a",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture.json"
      ],
      "fixture": "SF-1a",
      "input_sha256": "0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1",
      "output_files": [
        "fixture.json"
      ],
      "output_sha256": {
        "fixture.json": "83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-1b",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-1b/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-1b/out"
      ],
      "byte_equal": {
        "fixture.json": true
      },
      "case": "SF-1b",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture.json"
      ],
      "fixture": "SF-1b",
      "input_sha256": "c15b30da87758d7d7d762f6cf3b282c0490f9243e7f88d7b97db800811689dc9",
      "output_files": [
        "fixture.json"
      ],
      "output_sha256": {
        "fixture.json": "defa655eb09bbbd7b0e0587bb1a0a5e8495666dc1a9de7586fddf1a440ebcbdb"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-1c",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-1c/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-1c/out"
      ],
      "byte_equal": {
        "fixture.json": true
      },
      "case": "SF-1c",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture.json"
      ],
      "fixture": "SF-1c",
      "input_sha256": "d44e2700ddb8e50e1061c8846d6a8ee82092583af59ac44df0bbac361448643c",
      "output_files": [
        "fixture.json"
      ],
      "output_sha256": {
        "fixture.json": "0c03234c086e97ab117fae3ccddd463094db75faac5189c953d2a3edc64d1880"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-2a",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-2a/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-2a/out"
      ],
      "byte_equal": {
        "fixture.json": true
      },
      "case": "SF-2a",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture.json"
      ],
      "fixture": "SF-2a",
      "input_sha256": "521a0ca03cb42f4d81a93f6cd9bbcc1124fb2f8de6491738e7d4e4f7a8f07bc6",
      "output_files": [
        "fixture.json"
      ],
      "output_sha256": {
        "fixture.json": "4e6e0448435623c218b2c6041751981d880073482a2d8d70756ea2ff706019e4"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-2b",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-2b/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-2b/out"
      ],
      "byte_equal": {
        "fixture.json": true
      },
      "case": "SF-2b",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture.json"
      ],
      "fixture": "SF-2b",
      "input_sha256": "fa77757342a23c1eef2d6d187ec68b4d90d0d395c19b94541cae04c61f74ccbe",
      "output_files": [
        "fixture.json"
      ],
      "output_sha256": {
        "fixture.json": "8906e4231bfabc0fe1b92ae8d8e6d98ed0984a16cd241ef1d95bced6b5aee28b"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-2c",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-2c/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-2c/out"
      ],
      "byte_equal": {
        "fixture.json": true
      },
      "case": "SF-2c",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture.json"
      ],
      "fixture": "SF-2c",
      "input_sha256": "199029401c2707d8af887341846226e3c952dc28323bcc1731a1be9d0e9ac594",
      "output_files": [
        "fixture.json"
      ],
      "output_sha256": {
        "fixture.json": "06d314d23cb1fe75454ba56c5cba659f12bde080095ef95183124defe17cd4c9"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-2d",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-2d/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-2d/out"
      ],
      "byte_equal": {
        "fixture.json": true
      },
      "case": "SF-2d",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture.json"
      ],
      "fixture": "SF-2d",
      "input_sha256": "d93b96d2b626410c2662c5844ab692a64b864a93f31be3743e1c7942cedf402b",
      "output_files": [
        "fixture.json"
      ],
      "output_sha256": {
        "fixture.json": "a4813ec91a3fc7b3929079ac5dffaab80c8b78fcff56141a4faa4bd8b6671aa1"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-2e",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-2e/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-2e/out"
      ],
      "byte_equal": {
        "fixture.json": true
      },
      "case": "SF-2e",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture.json"
      ],
      "fixture": "SF-2e",
      "input_sha256": "c6822bf4650178b6ccab88a20a1ecf088b7522c0c27ac1184abb0fe69e8bcef6",
      "output_files": [
        "fixture.json"
      ],
      "output_sha256": {
        "fixture.json": "0edf4cc50cdd42b6d5e0b7bb048cc42a0254dd9ed520df7a81fee477a507cfcf"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-2f",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-2f/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-2f/out"
      ],
      "byte_equal": {
        "fixture.json": true
      },
      "case": "SF-2f",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture.json"
      ],
      "fixture": "SF-2f",
      "input_sha256": "6420ebd896642128865e250bb82da5780c9694a196a6a5a9df791bcc5ec46f65",
      "output_files": [
        "fixture.json"
      ],
      "output_sha256": {
        "fixture.json": "d7f0da887bf35e2e47f0cbeddcb0414e334cfd06efb0db6ba3c4aaa906dfe69b"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-2p",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-2p/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-2p/out"
      ],
      "byte_equal": {
        "fixture-cyc2.json": true,
        "fixture.json": true
      },
      "case": "SF-2p",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture-cyc2.json",
        "fixture.json"
      ],
      "fixture": "SF-2p",
      "input_sha256": "f7d444061e8c2bfa427f66e5df7ff43ae80bf7b22548391ee340b67b66b845a7",
      "output_files": [
        "fixture-cyc2.json",
        "fixture.json"
      ],
      "output_sha256": {
        "fixture-cyc2.json": "598c50ae04a2892d35f34ea24e73efeecc8d9e499ba3bdc6648b33a264a5f757",
        "fixture.json": "20f14369d2563be85b19083847b8099adbceed994787d08c27ff490a017e0a72"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-2pb",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-2pb/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-2pb/out"
      ],
      "byte_equal": {
        "fixture-cyc2.json": true,
        "fixture.json": true
      },
      "case": "SF-2pb",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture-cyc2.json",
        "fixture.json"
      ],
      "fixture": "SF-2pb",
      "input_sha256": "b8048192ccffc506f9e18981045048633ce9af1ceba1ac5f29c76fc1add20630",
      "output_files": [
        "fixture-cyc2.json",
        "fixture.json"
      ],
      "output_sha256": {
        "fixture-cyc2.json": "a201df97d576ff9bd0178ebcb07c38a3117e588c3997a88ba54bad8c84f50c38",
        "fixture.json": "855a8c2461aac86211ff48fc7b371d79e569f022a350f161e65e2d5dbcac1b4c"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-3",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-3/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-3/out"
      ],
      "byte_equal": {
        "fixture-cyc2.json": true,
        "fixture.json": true
      },
      "case": "SF-3",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture-cyc2.json",
        "fixture.json"
      ],
      "fixture": "SF-3",
      "input_sha256": "9f6fd0a2bb09127350b1b4a8edc323c3989f95fc1097064ecfe96d31740af36a",
      "output_files": [
        "fixture-cyc2.json",
        "fixture.json"
      ],
      "output_sha256": {
        "fixture-cyc2.json": "dcc375bab175cd834cf56f73c95971bfbdec956251b53b97ba6b668cb3d505a6",
        "fixture.json": "03dbc6e9e749d40502a99a64300cf03f14b743e1a9c7047c6ee953e8ac8496e7"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-3f",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-3f/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-3f/out"
      ],
      "byte_equal": {
        "fixture-cyc2.json": true,
        "fixture.json": true
      },
      "case": "SF-3f",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture-cyc2.json",
        "fixture.json"
      ],
      "fixture": "SF-3f",
      "input_sha256": "80319c62df77dc8a95a16d4e640fc0c44cf4a2c9aafa6f30006ba39b2271a8af",
      "output_files": [
        "fixture-cyc2.json",
        "fixture.json"
      ],
      "output_sha256": {
        "fixture-cyc2.json": "eb01524e24e9596939fb3906487df876bbb65ef850ec5ebc04da7f5585556abd",
        "fixture.json": "45fef3a178d7d59a0e1b835f7db84c86f09164efe9411138bb6612be4d7bcede"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-3g",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-3g/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/SF-3g/out"
      ],
      "byte_equal": {
        "fixture-cyc2.json": true,
        "fixture.json": true
      },
      "case": "SF-3g",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture-cyc2.json",
        "fixture.json"
      ],
      "fixture": "SF-3g",
      "input_sha256": "03dae8724f09cbbe68e983a6dd1717f370ddf4bf2ea194c4a7716f1ca02c8064",
      "output_files": [
        "fixture-cyc2.json",
        "fixture.json"
      ],
      "output_sha256": {
        "fixture-cyc2.json": "283c6b399dd898e7899fc859e2a192490997ec9ef0d105ff27267f178e4bb90e",
        "fixture.json": "ef2c67ff777fd36042d1ceb117d4fd4717033869f39069806547225020b10b18"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-1a",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-2-paired-control/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-2-paired-control/out"
      ],
      "byte_equal": {
        "fixture.json": true
      },
      "case": "NF-2-paired-control",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture.json"
      ],
      "fixture": "SF-1a",
      "input_sha256": "0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1",
      "output_files": [
        "fixture.json"
      ],
      "output_sha256": {
        "fixture.json": "83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-1a",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-2/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-2/out"
      ],
      "case": "NF-2",
      "exit_status": 2,
      "expected_exit": 2,
      "input_sha256": "731fe83e337e733c5905006a51c2c9a4f18f3118a8f30b9a2e76955354dd5d71",
      "output_files": [],
      "output_unchanged": true,
      "paired_control_pass": true,
      "pass": true,
      "role": "interface-negative",
      "stderr_sha256": "bf05bf233075559334db9e1665030a4486abd6f0255121a24039a980d26395fd",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-1a",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-3-paired-control/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-3-paired-control/out"
      ],
      "byte_equal": {
        "fixture.json": true
      },
      "case": "NF-3-paired-control",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture.json"
      ],
      "fixture": "SF-1a",
      "input_sha256": "0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1",
      "output_files": [
        "fixture.json"
      ],
      "output_sha256": {
        "fixture.json": "83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-1a",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-3/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-3/out",
        "--stage",
        "members"
      ],
      "case": "NF-3",
      "exit_status": 2,
      "expected_exit": 2,
      "input_sha256": "0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1",
      "output_files": [],
      "output_unchanged": true,
      "paired_control_pass": true,
      "pass": true,
      "role": "interface-negative",
      "stderr_sha256": "694f14388d29a016111c3a6cb2ff130cf1e0e7180483fff9c14bc39ca31f9fd4",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-1a",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-4-paired-control/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-4-paired-control/out"
      ],
      "byte_equal": {
        "fixture.json": true
      },
      "case": "NF-4-paired-control",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture.json"
      ],
      "fixture": "SF-1a",
      "input_sha256": "0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1",
      "output_files": [
        "fixture.json"
      ],
      "output_sha256": {
        "fixture.json": "83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-1a",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-4/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-4/out"
      ],
      "case": "NF-4",
      "exit_status": 2,
      "expected_exit": 2,
      "input_sha256": "0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1",
      "output_files": [
        "sentinel.txt"
      ],
      "output_unchanged": true,
      "paired_control_pass": true,
      "pass": true,
      "role": "interface-negative",
      "stderr_sha256": "d839f3d0b5032c6068a95e42f4d81331bbdc90a4fb38230dfcdddd8dc6afa868",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-1a",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-5-paired-control/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-5-paired-control/out"
      ],
      "byte_equal": {
        "fixture.json": true
      },
      "case": "NF-5-paired-control",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture.json"
      ],
      "fixture": "SF-1a",
      "input_sha256": "0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1",
      "output_files": [
        "fixture.json"
      ],
      "output_sha256": {
        "fixture.json": "83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-1b",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-5/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-5/out"
      ],
      "case": "NF-5",
      "exit_status": 2,
      "expected_exit": 2,
      "input_sha256": "0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1",
      "output_files": [],
      "output_unchanged": true,
      "paired_control_pass": true,
      "pass": true,
      "role": "interface-negative",
      "stderr_sha256": "bf05bf233075559334db9e1665030a4486abd6f0255121a24039a980d26395fd",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-1a",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-6-paired-control/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-6-paired-control/out"
      ],
      "byte_equal": {
        "fixture.json": true
      },
      "case": "NF-6-paired-control",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture.json"
      ],
      "fixture": "SF-1a",
      "input_sha256": "0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1",
      "output_files": [
        "fixture.json"
      ],
      "output_sha256": {
        "fixture.json": "83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-9",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-6/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-6/out"
      ],
      "case": "NF-6",
      "exit_status": 2,
      "expected_exit": 2,
      "input_sha256": "b7799cd412fe6f8e018f8b64ff4224909b74cea82319f2cafae6fce8e2183feb",
      "output_files": [],
      "output_unchanged": true,
      "paired_control_pass": true,
      "pass": true,
      "role": "interface-negative",
      "stderr_sha256": "03efb65678531c1ddb43c045541dd036d9fb7b0c24fdb6ff78d45d6c4a478983",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-1a",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-7-paired-control/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-7-paired-control/out"
      ],
      "byte_equal": {
        "fixture.json": true
      },
      "case": "NF-7-paired-control",
      "exit_status": 0,
      "expected_exit": 0,
      "expected_files": [
        "fixture.json"
      ],
      "fixture": "SF-1a",
      "input_sha256": "0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1",
      "output_files": [
        "fixture.json"
      ],
      "output_sha256": {
        "fixture.json": "83772256c7154b0c4029792e2a712998aa9835ee23db0abbcd2a87a92cb2f3d4"
      },
      "pass": true,
      "role": "positive",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "argv": [
        "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
        "-I",
        "/workspace/k1p1-impl-b/verification/lean/k1p1_enum_b.py",
        "--fixture",
        "SF-1a",
        "--input",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-7/input.json",
        "--out",
        "/tmp/k1p1-b-author-fixtures-7rnl5uer/NF-7/out"
      ],
      "case": "NF-7",
      "exit_status": 2,
      "expected_exit": 2,
      "input_sha256": null,
      "output_files": [],
      "output_unchanged": true,
      "paired_control_pass": true,
      "pass": true,
      "role": "interface-negative",
      "stderr_sha256": "3378b70bad02e1594db4d17bc91ac85e7cf2935dd56cbaa265cbdfea9200f2d9",
      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    }
  ],
  "fixtures_sha256": "691aedbf0c9e74fdcc64f4c9c35f5e07c8ffc362e74360d4e541df682c750e85",
  "kind": "author-bounded-fixture-verification",
  "pass": true,
  "python": "/workspace/.tools/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11",
  "python_version": "Python 3.11.17",
  "source_blob": "63eadd818e59f86c48969552ef144f56b4154b95",
  "source_commit": "79ff3a7ae5bed4e7ebc044c52bae551362780189",
  "source_sha256_after": "c5bfb8d198ed464c093ebf38ddc6f0d0e160f3e5e91395b1f98014c33928c7e5",
  "source_sha256_before": "c5bfb8d198ed464c093ebf38ddc6f0d0e160f3e5e91395b1f98014c33928c7e5",
  "source_unchanged": true
}
```
