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
