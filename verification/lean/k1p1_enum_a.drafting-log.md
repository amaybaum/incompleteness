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
