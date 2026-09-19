#!/usr/bin/env python3
"""control_plane_base_check.py - run a control plane's preconditions at a commit.

AGENTS.md A.37 separates three commits a control plane can mean by "base":

  D   the drafting snapshot, at which the pre-merge measurements were taken;
  B   the mandated execution base, the certified merge commit on main of the
      latest control-plane artifact governing the round;
  M   a candidate control-plane merge, predictive test state only.

The Act 21 freeze used one name for D and B, and two of its preconditions could
not hold at the real base once the preregistration carrying them was in the
tree. This tool is the mechanical half of the correction. A control plane that
wants its preconditions run carries one fenced block in its markdown:

    ```control-plane-preconditions
    d: <40-hex drafting snapshot>
    b: <40-hex mandated base, only once it exists>
    merged: true|false
    frozen-blob: <path> <40-hex blob expected at the evaluated commit>
    # comments and blank lines are ignored
    {"id": "p1", "scope": "B",    "check": "<shell>", "expect": "empty"}
    {"id": "p2", "scope": "D",    "check": "<shell>", "expect": "empty"}
    {"id": "p3", "scope": "D->B", "check": "<shell>", "expect": "exit0"}
    ```

Each row's `check` is a shell command run at the repository root with `D`, `B`
and `REF` exported. `REF` is the commit under evaluation; `B` is set to the same
commit, since a B-scoped condition is a statement about that tree whether it is
being tested prospectively at M or authoritatively at B. `expect` is one of
`empty` (no stdout), `nonempty` (some stdout) or `exit0` (exit status zero).

What runs where:

  scope B and D->B   the check is executed against --ref. This is the same code
                     path for --mode M and --mode B; the mode is recorded in the
                     output and nothing else differs, which is the point: the
                     condition that passed prospectively at M is the condition
                     that must pass authoritatively at B.
  scope D            a drafting-time fact. It is not re-measured here. The tool
                     checks only that D is recorded (a `d:` header or --d) and
                     that D is an ancestor of --ref.
  frozen-blob        `git rev-parse <ref>:<path>` must equal the recorded blob.

Control-plane files are discovered in the tree of --ref, not the working copy:
any `preregistration.md` or `amendments/amendment-*.md` under `verification/`
whose content carries the block. A tree with no such file is a clean no-op.

Usage:
    python3 tools/control_plane_base_check.py --mode M --ref <candidate merge>
    python3 tools/control_plane_base_check.py --mode B --ref <merge commit> [--d <sha>]
    python3 tools/control_plane_base_check.py --self-test

Exit 1 on any FAIL row, any unreadable block, or a self-test failure.
"""
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

FENCE = "control-plane-preconditions"
SCOPES = ("D", "B", "D->B")
EXPECTS = ("empty", "nonempty", "exit0")
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEADER_KEYS = ("d", "b", "merged", "frozen-blob")
CP_PATH = re.compile(
    r"^verification/.*(?:/preregistration\.md|/amendments/amendment-[^/]+\.md)$")


# --------------------------------------------------------------------------
# the block
# --------------------------------------------------------------------------

class Block:
    """One parsed control-plane-preconditions block."""

    def __init__(self):
        self.d = None
        self.b = None
        self.merged = False
        self.frozen = []       # [(path, blob)]
        self.rows = []         # [dict]
        self.errors = []       # [str], any of which makes the block unusable
        self.present = False


def extract_block(text):
    """The raw lines of the block, or None when the file carries none.

    Two blocks are an error; the caller reports it."""
    lines = text.splitlines()
    starts = [i for i, l in enumerate(lines)
              if l.strip() == "```" + FENCE]
    if not starts:
        return None, None
    if len(starts) > 1:
        return None, "more than one %s block" % FENCE
    i = starts[0] + 1
    body = []
    while i < len(lines) and lines[i].strip() != "```":
        body.append(lines[i])
        i += 1
    if i >= len(lines):
        return None, "unterminated %s block" % FENCE
    return body, None


def parse_block(text):
    """Parse the block out of a control-plane file's text.

    Returns a Block. `present` is False when the file has no block, in which
    case nothing else is populated. Errors are collected, not raised, so a
    caller can print them as FAIL rows."""
    blk = Block()
    body, err = extract_block(text)
    if err:
        blk.present = True
        blk.errors.append(err)
        return blk
    if body is None:
        return blk
    blk.present = True
    for n, raw in enumerate(body, 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("{"):
            try:
                row = json.loads(line)
            except ValueError as e:
                blk.errors.append("line %d: row is not valid JSON (%s)" % (n, e))
                continue
            if not isinstance(row, dict):
                blk.errors.append("line %d: row is not a JSON object" % n)
                continue
            row["_line"] = n
            blk.rows.append(row)
            continue
        m = re.match(r"^([A-Za-z-]+):\s*(.*)$", line)
        if not m:
            blk.errors.append("line %d: neither a `key: value` header nor a "
                              "JSON row: %r" % (n, line))
            continue
        key, val = m.group(1).lower(), m.group(2).strip()
        if key not in HEADER_KEYS:
            blk.errors.append("line %d: unknown header key %r (known: %s)"
                              % (n, key, ", ".join(HEADER_KEYS)))
        elif key in ("d", "b"):
            if not HEX40.match(val):
                blk.errors.append("line %d: `%s:` is not a 40-hex SHA: %r"
                                  % (n, key, val))
            else:
                setattr(blk, key, val)
        elif key == "merged":
            if val.lower() not in ("true", "false"):
                blk.errors.append("line %d: `merged:` must be true or false" % n)
            else:
                blk.merged = val.lower() == "true"
        else:
            parts = val.split()
            if len(parts) != 2 or not HEX40.match(parts[1]):
                blk.errors.append("line %d: `frozen-blob:` needs `<path> "
                                  "<40-hex blob>`" % n)
            else:
                blk.frozen.append((parts[0], parts[1]))
    return blk


def row_problems(row):
    """Shape errors of one row, as strings; empty when the row is well-formed."""
    out = []
    if not isinstance(row.get("id"), str) or not row["id"]:
        out.append("missing id")
    if row.get("scope") not in SCOPES:
        out.append("scope must be one of %s" % ", ".join(SCOPES))
    if not isinstance(row.get("check"), str) or not row["check"].strip():
        out.append("missing check")
    if row.get("expect") not in EXPECTS:
        out.append("expect must be one of %s" % ", ".join(EXPECTS))
    return out


# --------------------------------------------------------------------------
# git plumbing
# --------------------------------------------------------------------------

def git(args, cwd, check=True):
    r = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError("git %s: %s" % (" ".join(args), r.stderr.strip()))
    return r.stdout


def resolve(ref, cwd):
    return git(["rev-parse", "--verify", ref + "^{commit}"], cwd).strip()


def is_ancestor(a, b, cwd):
    r = subprocess.run(["git", "merge-base", "--is-ancestor", a, b], cwd=cwd,
                       capture_output=True, text=True)
    return r.returncode == 0


def blob_at(ref, path, cwd):
    r = subprocess.run(["git", "rev-parse", "--verify", "-q", "%s:%s" % (ref, path)],
                       cwd=cwd, capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def discover(ref, cwd):
    """Control-plane files in the tree of `ref` that carry the block."""
    names = git(["ls-tree", "-r", "--name-only", ref, "verification/"], cwd,
                check=False).splitlines()
    found = []
    for path in sorted(names):
        if not CP_PATH.match(path):
            continue
        text = git(["show", "%s:%s" % (ref, path)], cwd)
        if "```" + FENCE in text:
            found.append((path, text))
    return found


# --------------------------------------------------------------------------
# evaluation
# --------------------------------------------------------------------------

def run_check(cmd, env, cwd):
    r = subprocess.run(cmd, shell=True, cwd=cwd, env=env,
                       capture_output=True, text=True, timeout=600)
    return r.returncode, r.stdout


def judge(expect, rc, out):
    if expect == "empty":
        return out.strip() == ""
    if expect == "nonempty":
        return out.strip() != ""
    return rc == 0


def evaluate(mode, ref, cwd, d_override=None, out=print):
    """Run every block-bearing control plane at `ref`. Returns (n_fail, n_rows).

    One PASS/FAIL line per row, per frozen blob and per block-level error."""
    sha = resolve(ref, cwd)
    files = discover(sha, cwd)
    if not files:
        out("control_plane_base_check: mode %s at %s: no control-plane file in "
            "this tree carries a %s block; nothing to evaluate" % (mode, sha[:12], FENCE))
        return 0, 0
    out("control_plane_base_check: mode %s, REF=%s, %d control-plane file(s)"
        % (mode, sha, len(files)))
    fails = rows_seen = 0

    def line(ok, path, ident, why=""):
        nonlocal fails
        if not ok:
            fails += 1
        out("  %s  %s :: %s%s" % ("PASS" if ok else "FAIL", path, ident,
                                  ("  -- " + why) if why else ""))

    for path, text in files:
        blk = parse_block(text)
        for e in blk.errors:
            line(False, path, "block", e)
        if blk.errors:
            continue
        d = d_override or blk.d
        if d and not HEX40.match(d):
            line(False, path, "d", "not a 40-hex SHA: %r" % d)
            d = None

        env = dict(os.environ, REF=sha, B=sha, D=d or "")

        for (fpath, blob) in blk.frozen:
            actual = blob_at(sha, fpath, cwd)
            if actual is None:
                line(False, path, "frozen-blob " + fpath, "path absent at REF")
            elif actual != blob:
                line(False, path, "frozen-blob " + fpath,
                     "blob %s at REF, %s recorded" % (actual[:12], blob[:12]))
            else:
                line(True, path, "frozen-blob " + fpath, blob[:12])

        for row in blk.rows:
            rows_seen += 1
            ident = "row %s" % row.get("id", "?")
            probs = row_problems(row)
            if probs:
                line(False, path, ident, "; ".join(probs))
                continue
            scope = row["scope"]
            if scope == "D":
                if not d:
                    line(False, path, ident, "scope D but no `d:` recorded and no --d")
                elif not is_ancestor(d, sha, cwd):
                    line(False, path, ident, "D=%s is not an ancestor of REF" % d[:12])
                else:
                    line(True, path, ident, "D=%s is an ancestor of REF; drafting-time "
                         "fact not re-measured" % d[:12])
                continue
            if scope == "D->B" and not d:
                line(False, path, ident, "scope D->B but no `d:` recorded and no --d")
                continue
            if "$D" in row["check"] and not d:
                line(False, path, ident, "check references $D but D is unknown")
                continue
            try:
                rc, stdout = run_check(row["check"], env, cwd)
            except subprocess.TimeoutExpired:
                line(False, path, ident, "check timed out")
                continue
            ok = judge(row["expect"], rc, stdout)
            line(ok, path, ident, "scope %s, expect %s, exit %d, %d byte(s) of output"
                 % (scope, row["expect"], rc, len(stdout)))
    return fails, rows_seen


# --------------------------------------------------------------------------
# self-test: the mutation control
# --------------------------------------------------------------------------

FIXTURE_DIR = "verification/programmes/self-test/round-x"


def _sh(args, cwd):
    subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True)


def _commit(cwd, msg):
    _sh(["git", "add", "-A"], cwd)
    _sh(["git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q",
         "-m", msg], cwd)
    return git(["rev-parse", "HEAD"], cwd).strip()


def _write(cwd, rel, text):
    p = os.path.join(cwd, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(text)


def _control_plane(d, source_blob, with_failing):
    rows = [
        # a B-scoped tree condition that holds: no execution object exists
        '{"id": "no-exec-module", "scope": "B", "check": "git ls-tree -r --name-only '
        '$REF | grep -x lean/RoundX.lean", "expect": "empty"}',
        # a D-scoped name-freedom fact: not re-measured, ancestry only
        '{"id": "stem-free-at-D", "scope": "D", "check": "git grep -- RXQ $D", '
        '"expect": "empty"}',
        # a D->B provenance condition
        '{"id": "d-ancestor-of-b", "scope": "D->B", "check": "git merge-base '
        '--is-ancestor $D $REF", "expect": "exit0"}',
    ]
    if with_failing:
        # the Act 21 shape: a token that the control plane itself carries
        rows.append('{"id": "token-absent", "scope": "B", "check": "git grep -l -- '
                    'RXQ $REF", "expect": "empty"}')
    return "\n".join([
        "# Round X preregistration", "",
        "The stem is `RXQ`.", "",
        "```" + FENCE,
        "d: " + d,
        "merged: false",
        "frozen-blob: src/source.txt " + source_blob,
    ] + rows + ["```", ""])


def self_test():
    """Build a throwaway repository and check the verdicts, including that the
    tool FAILS on the failing row. A checker that cannot fail is not a control."""
    with tempfile.TemporaryDirectory() as tmp:
        _sh(["git", "init", "-q", "-b", "main"], tmp)
        _write(tmp, "src/source.txt", "pinned source\n")
        _write(tmp, "README.md", "drafting snapshot\n")
        d = _commit(tmp, "D")
        source_blob = blob_at(d, "src/source.txt", tmp)

        # 1. control plane with one failing B row: must FAIL exactly that row
        _write(tmp, FIXTURE_DIR + "/preregistration.md",
               _control_plane(d, source_blob, with_failing=True))
        m = _commit(tmp, "control plane, bad row")
        lines = []
        fails, rows = evaluate("M", m, tmp, out=lines.append)
        verdicts = {l.split("::")[1].split("--")[0].strip(): l.strip().startswith("PASS")
                    for l in lines if "::" in l}
        want = {"frozen-blob src/source.txt": True, "row no-exec-module": True,
                "row stem-free-at-D": True, "row d-ancestor-of-b": True,
                "row token-absent": False}
        for k, v in want.items():
            if verdicts.get(k) is not v:
                return False, "expected %s=%s, verdicts %s" % (k, v, verdicts)
        if fails != 1 or rows != 4:
            return False, "expected 1 failure over 4 rows, got %d over %d" % (fails, rows)

        # 2. same control plane without the failing row, in a fresh commit:
        #    every row PASSes, and the same code path serves mode B
        _write(tmp, FIXTURE_DIR + "/preregistration.md",
               _control_plane(d, source_blob, with_failing=False))
        b = _commit(tmp, "control plane, good")
        lines = []
        fails, rows = evaluate("B", b, tmp, out=lines.append)
        if fails != 0 or rows != 3:
            return False, "clean control plane: expected 0 failures over 3 rows, " \
                          "got %d over %d: %s" % (fails, rows, lines)

        # 3. frozen-blob mutation: the pinned source changes, the check FAILS
        _write(tmp, "src/source.txt", "drifted\n")
        b2 = _commit(tmp, "drift")
        lines = []
        fails, _ = evaluate("B", b2, tmp, out=lines.append)
        if fails != 1 or not any("frozen-blob" in l and l.strip().startswith("FAIL")
                                 for l in lines):
            return False, "frozen-blob drift was not reported: %s" % lines

        # 4. a D that is not an ancestor: the D row and the D->B row both FAIL
        lines = []
        bogus = "0" * 40
        fails, _ = evaluate("B", b, tmp, d_override=bogus, out=lines.append)
        if fails != 2:
            return False, "non-ancestor D: expected 2 failures, got %d: %s" % (fails, lines)

        # 5. no block-bearing file: a clean no-op
        lines = []
        fails, rows = evaluate("B", d, tmp, out=lines.append)
        if fails or rows or not any("nothing to evaluate" in l for l in lines):
            return False, "tree without a block was not a no-op: %s" % lines

        # 6. a row without a scope is a FAIL, not a skip (the pinned source is
        #    restored first so that this case isolates the unscoped row)
        _write(tmp, "src/source.txt", "pinned source\n")
        _write(tmp, FIXTURE_DIR + "/preregistration.md",
               _control_plane(d, source_blob, with_failing=False).replace(
                   '"scope": "B", ', ''))
        b3 = _commit(tmp, "unscoped row")
        lines = []
        fails, _ = evaluate("B", b3, tmp, out=lines.append)
        if fails != 1 or not any("scope must be" in l for l in lines):
            return False, "unscoped row was not rejected: %s" % lines
    return True, ""


# --------------------------------------------------------------------------

def main(argv):
    if "--self-test" in argv:
        ok, why = self_test()
        print("control_plane_base_check: self-test " + ("OK" if ok else "FAILED: " + why))
        return 0 if ok else 1

    def opt(name):
        return argv[argv.index(name) + 1] if name in argv and argv.index(name) + 1 < len(argv) else None

    mode, ref, d = opt("--mode"), opt("--ref"), opt("--d")
    repo = opt("--repo") or ROOT
    if mode not in ("M", "B") or not ref:
        print(__doc__.split("Usage:")[1].split("Exit 1")[0].strip())
        return 2
    try:
        fails, rows = evaluate(mode, ref, repo, d_override=d)
    except RuntimeError as e:
        print("control_plane_base_check: FAIL (%s)" % e)
        return 1
    if fails:
        print("control_plane_base_check: FAILED (%d failing line(s) over %d row(s), mode %s)"
              % (fails, rows, mode))
        return 1
    print("control_plane_base_check: OK (mode %s, %d row(s), no failure)" % (mode, rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
