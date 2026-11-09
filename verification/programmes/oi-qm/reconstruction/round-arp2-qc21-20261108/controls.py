#!/usr/bin/env python3
"""controls.py -- the controls of native round ARP-2-QC21 (Q-C2-1). Preregistration r11b, Appendix C.5.

Modes: check <commit> --freeze F [--stage S1|E|W], decide [m.json], note [m.json], replay <fresh.json>,
stress-check <stress.json>, derive-run <run_id> <attempt>, order [--final], verdict, --self-test.
Codes: T (chain and blocks), G (paths), R (record files by stage), B (blobs, allowlists, C-EXACT, C-INDEP, the
guard's node-form rules), W (verify.yml as a whole file), DS (inputs and drift), X (schema and flags), V (note
regeneration and S4), P (no unbackticked PENDING under --freeze; evidence pins).

It runs at the top of the repository's work tree (the root check) and starts no process other than read-only
git, GET-only `gh api` and control T's frozen command. It writes no file outside a self-test temporary directory.
Exact arithmetic only (Fraction)."""
import ast
import fractions
import hashlib
import json
import os.path
import re
import subprocess
import sys
import tempfile

ROUND = "ARP-2-QC21"
RDIR = "verification/programmes/oi-qm/reconstruction/round-arp2-qc21-20261108/"
RECEIPT = "verification/receipts/ARP-2-QC21.json"
WORKFLOW = ".github/workflows/verify.yml"
D_SHA = "fd539e150759a6ea51ab279aeeac80fc06050ade"
ROUND_BRANCH = "research/arp2-qc21-20261108"
DEV_BRANCH = "draft/arp2-qc21-dev"
BRANCHES_LINE = "arp2-qc21 branches: round research/arp2-qc21-20261108; dev draft/arp2-qc21-dev"
CHECKER = RDIR + "qc21_check.py"
CONTROLS = RDIR + "controls.py"
PREREG = RDIR + "preregistration.md"
MEAS = RDIR + "evidence/measurements.json"
OWNER = ("amaybaum", "OWNER")
JOB_A = "Numerical probes / ARP-2-QC21 fixtures and stress"
JOB_B = "Numerical probes / ARP-2-QC21 exact decision (gated)"
STEP_B4 = "ARP-2-QC21 exact decision"
STEP_B3 = "ARP-2-QC21 approved commit and receipt"
STEP_B6 = "ARP-2-QC21 replay against the committed measurements"
STEP_A3 = "ARP-2-QC21 fixture decision"
STEP_A7 = "ARP-2-QC21 stress output equals the pinned sha256"
STEP_A10 = "ARP-2-QC21 receipt absent"
GOVERNED_DIGEST = "1d195f938f5467d1549f7755bcafce2109abbfbcb57a7ff2243fa09a67e9982e"
ROUND_LINES = ["round ARP-2-QC21", "kind non-sealing", "record-directory " + RDIR]
GOVERNED_LINES = ["record AM " + RDIR, "record AM " + RECEIPT, "execution M " + WORKFLOW]

# Pins (PENDING until the design run, C.7): blobs of the scripts, the stress output, the records.
PINS = {"qc21_check.py": None, "controls.py": None, "stress.json": None, "design-run.json": None,
        "gate-tests.json": None, "confirmation-run.json": None}
# Inputs at D (DS): path -> blob at D.
INPUTS = {
    "verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md": "51c24aeb",
    "verification/receipts/ARP-1-MARC.json": "f4f2b06b40f1dcb91d4c0f2f020688be422b7bc8",
    "verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/preregistration.md":
        "af7c4f228393ecaa9d334d50410e3c87d6faf80e",
    "verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/result.md":
        "6fb623273c4db9aec5fd9ca0cfc80bd923076ece",
    "verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/evidence/measurements.json":
        "f4a783aafcb44953231e6e4566a1e93bb71ba21f",
    "verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/marc_check.py":
        "38d6f67559b6641590b3baf126b2247e97a4e28c",
    "verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/controls.py":
        "5e6318896ffe274bf5cca7dbcb2cb537b1bad4a1",
    "tools/v3_verifier.py": None,
}
S1_FILES = ("qc21_check.py", "controls.py", "evidence/design-run.json", "evidence/f-run/results.json",
            "evidence/confirmation-run.json", "evidence/confirmation-measurements.json", "evidence/gate-tests.json")
E_FILES = ("evidence/measurements.json", "evidence/s1-run/results.json", "evidence/order.json",
           "evidence/order-s1.json", "result.md")

CHECKER_IMPORTS = {"fractions", "itertools", "json", "os", "sys"}
CONTROLS_IMPORTS = {"ast", "fractions", "hashlib", "json", "os.path", "re", "subprocess", "sys", "tempfile"}
MOD_ATTRS = {"subprocess": {"run", "PIPE"}, "os.path": {"join", "isfile"}, "json": {"loads", "dumps"},
             "hashlib": {"sha256"}, "re": {"fullmatch"}, "sys": {"argv", "exit", "stdout", "stderr"},
             "fractions": {"Fraction"}, "tempfile": {"TemporaryDirectory"}, "ast": None}
BANNED = {"getattr", "setattr", "delattr", "globals", "locals", "vars", "breakpoint", "help", "exec", "eval",
          "compile", "__import__"}
GIT_SUBCOMMANDS = {"rev-parse", "cat-file", "ls-tree", "rev-list", "merge-base", "diff-tree", "show"}
GIT_BAD = ("-c", "--config-env", "--exec-path", "-C", "--git-dir", "--work-tree", "--upload-pack", "--output",
           "--ext-diff", "--textconv", "--filters")
GH_EXTRA = {"--paginate", "-H", "Accept: application/vnd.github+json"}
GH_TEMPLATES = ("actions/runs?", "actions/runs/{DEC}", "actions/runs/{DEC}/attempts/{DEC}",
                "actions/runs/{DEC}/attempts/{DEC}/jobs?per_page=100", "actions/runs/{DEC}/artifacts",
                "git/trees/{HEX40}?recursive=1", "git/trees/{HEX40}", "activity?ref=refs/heads/", "")
HELPERS = ("a_ok", "w_path", "root_check")
_C = r"(?!\.\.?(?:/|$))[A-Za-z0-9_.][A-Za-z0-9_.-]*"
A_OK_PATTERNS = (r"[0-9a-f]{40}", r"[1-9][0-9]{0,19}", r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z",
                 _C + r"(?:/" + _C + r")*", r"[0-9a-f]{40}:" + _C + r"(?:/" + _C + r")*")
T_CODE = ("import sys,json;sys.path.insert(0,'tools');import v3_verifier as v;r=v.Repo('.');"
          "a=v.control_plane(r,sys.argv[1],sys.argv[2]);"
          "print(json.dumps({'rdir':(a[0] or b'').decode(),'round':a[1],'kind':a[2],"
          "'digest':v.governed_digest(a[3]) if isinstance(a[3],list) else None,'codes':a[5]},sort_keys=True))")


class Refused(Exception):
    """A validator or the root check refused."""


def a_ok(x):
    """The frozen validator: re.fullmatch against exactly one frozen pattern, else it raises."""
    if not isinstance(x, str) or not any(re.fullmatch(p, x) for p in A_OK_PATTERNS):
        raise Refused("a_ok: %r" % (x,))
    return x


def w_path(td, name):
    """The single write-path helper: a literal file name joined under a self-test temporary directory."""
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", name):
        raise Refused("w_path: %r" % (name,))
    return os.path.join(td, name)


def root_check():
    """The entry refuses, exit 2, unless it runs at the top of the repository's work tree."""
    r = subprocess.run(["git", "rev-parse", "--show-prefix"], capture_output=True, text=True)
    if r.returncode != 0 or r.stdout != "\n":
        raise Refused("not at the repository root")


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def canonical(o):
    return json.dumps(o, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n"


def read_bytes(path):
    with open(path, "rb") as fh:
        return fh.read()


def read_text(path):
    with open(path, "r") as fh:
        return fh.read()


def git_show(commit, path):
    """The bytes of path at commit, or None."""
    r = subprocess.run(["git", "show", "--no-textconv", "--no-ext-diff", "--end-of-options",
                        a_ok(commit + ":" + path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def git_blob(commit, path):
    r = subprocess.run(["git", "rev-parse", "--verify", "--end-of-options", a_ok(commit + ":" + path)],
                       capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def git_commit(spec):
    r = subprocess.run(["git", "rev-parse", "--verify", "--end-of-options", a_ok(spec)],
                       capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def git_parents(commit):
    r = subprocess.run(["git", "rev-list", "--parents", "-n", "1", "--end-of-options", a_ok(commit)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return None
    return r.stdout.split()[1:]


def git_is_ancestor(a, b):
    r = subprocess.run(["git", "merge-base", "--is-ancestor", "--end-of-options", a_ok(a), a_ok(b)],
                       capture_output=True, text=True)
    return r.returncode == 0


def git_has(commit):
    r = subprocess.run(["git", "cat-file", "-e", "--end-of-options", a_ok(commit)], capture_output=True)
    return r.returncode == 0


def git_tree_blobs(commit):
    """{path: blob} for every blob in commit's tree."""
    r = subprocess.run(["git", "ls-tree", "-r", "--full-tree", "--end-of-options", a_ok(commit)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return None
    out = {}
    for line in r.stdout.splitlines():
        meta, path = line.split("\t", 1)
        parts = meta.split()
        if parts[1] == "blob":
            out[path] = parts[2]
    return out


def git_delta(a, b):
    """[(status, path)] of the change from a to b."""
    r = subprocess.run(["git", "diff-tree", "--no-textconv", "--no-ext-diff", "-r", "--no-renames", "--name-status",
                        "--end-of-options", a_ok(a), a_ok(b)], capture_output=True, text=True)
    if r.returncode != 0:
        return None
    return [tuple(line.split("\t", 1)) for line in r.stdout.splitlines() if line]


def gh_get(path_kind, *vals):
    """GET-only `gh api` over the frozen templates; returns (ok, parsed JSON or error text)."""
    if path_kind == "run":
        r = subprocess.run(["gh", "api", "--method", "GET",
                            f"repos/amaybaum/incompleteness/actions/runs/{a_ok(vals[0])}",
                            "-H", "Accept: application/vnd.github+json"], capture_output=True, text=True)
    elif path_kind == "attempt":
        r = subprocess.run(["gh", "api", "--method", "GET",
                            f"repos/amaybaum/incompleteness/actions/runs/{a_ok(vals[0])}/attempts/{a_ok(vals[1])}",
                            "-H", "Accept: application/vnd.github+json"], capture_output=True, text=True)
    elif path_kind == "jobs":
        r = subprocess.run(["gh", "api", "--method", "GET",
                            f"repos/amaybaum/incompleteness/actions/runs/{a_ok(vals[0])}/attempts/{a_ok(vals[1])}"
                            f"/jobs?per_page=100&page={a_ok(vals[2])}",
                            "-H", "Accept: application/vnd.github+json"], capture_output=True, text=True)
    elif path_kind == "artifacts":
        r = subprocess.run(["gh", "api", "--method", "GET",
                            f"repos/amaybaum/incompleteness/actions/runs/{a_ok(vals[0])}/artifacts",
                            "-H", "Accept: application/vnd.github+json"], capture_output=True, text=True)
    elif path_kind == "runs-dispatch":
        r = subprocess.run(["gh", "api", "--method", "GET",
                            f"repos/amaybaum/incompleteness/actions/runs?event=workflow_dispatch&created="
                            f"{a_ok(vals[0])}..{a_ok(vals[1])}&per_page=100&page={a_ok(vals[2])}",
                            "-H", "Accept: application/vnd.github+json"], capture_output=True, text=True)
    elif path_kind == "runs-all":
        r = subprocess.run(["gh", "api", "--method", "GET",
                            f"repos/amaybaum/incompleteness/actions/runs?created="
                            f"{a_ok(vals[0])}..{a_ok(vals[1])}&per_page=100&page={a_ok(vals[2])}",
                            "-H", "Accept: application/vnd.github+json"], capture_output=True, text=True)
    elif path_kind == "tree-recursive":
        r = subprocess.run(["gh", "api", "--method", "GET",
                            f"repos/amaybaum/incompleteness/git/trees/{a_ok(vals[0])}?recursive=1",
                            "-H", "Accept: application/vnd.github+json"], capture_output=True, text=True)
    elif path_kind == "tree":
        r = subprocess.run(["gh", "api", "--method", "GET",
                            f"repos/amaybaum/incompleteness/git/trees/{a_ok(vals[0])}",
                            "-H", "Accept: application/vnd.github+json"], capture_output=True, text=True)
    elif path_kind == "activity":
        r = subprocess.run(["gh", "api", "--method", "GET",
                            f"repos/amaybaum/incompleteness/activity?ref=refs/heads/{a_ok(vals[0])}"
                            f"&per_page=100&page={a_ok(vals[1])}",
                            "-H", "Accept: application/vnd.github+json"], capture_output=True, text=True)
    elif path_kind == "repo":
        r = subprocess.run(["gh", "api", "--method", "GET", "repos/amaybaum/incompleteness",
                            "-H", "Accept: application/vnd.github+json"], capture_output=True, text=True)
    else:
        raise Refused("gh template")
    if r.returncode != 0:
        return False, r.stderr
    return True, json.loads(r.stdout)


# ------------------------------------------------------------------------------------------------------------
# The frozen workflow splice (control W): verify.yml at the design run, 6', S1 and E equals D's verify.yml with
# exactly this splice.
# ------------------------------------------------------------------------------------------------------------
REF_KEY = "github.ref == 'refs/heads/research/arp2-qc21-20261108'"
RECEIPT_KEY = "hashFiles('verification/receipts/ARP-2-QC21.json') == ''"
B4_EXPR = ("${{ (github.event_name == 'workflow_dispatch' && github.run_attempt == '1' && " + REF_KEY + " && "
           + RECEIPT_KEY + ") && 'workflow_dispatch' || 'closed-or-other' }}")
B6_IF = ("${{ (github.event_name == 'workflow_dispatch' && github.run_attempt == '1' && " + REF_KEY + " && "
         + RECEIPT_KEY + ") }}")
JOB_B_IF = "${{ github.event_name == 'workflow_dispatch' && github.run_attempt == '1' && inputs.arp2qc21_decisive == true }}"
B3_RUN = ('test "$GITHUB_SHA" = "$ARP2QC21_SHA" && test "$GITHUB_REF" = refs/heads/research/arp2-qc21-20261108 '
          '&& test ! -e verification/receipts/ARP-2-QC21.json')
PY = "python3 -I -S -B "
ON_ANCHOR = "  workflow_dispatch:\n\njobs:\n"
ON_SPLICE = ("  workflow_dispatch:\n"
             "    inputs:\n"
             "      arp2qc21_decisive:\n"
             "        description: 'ARP-2-QC21: the decisive dispatch (owner-approved only)'\n"
             "        type: boolean\n"
             "        default: false\n"
             "      arp2qc21_sha:\n"
             "        description: 'ARP-2-QC21: the approved commit (full id)'\n"
             "        type: string\n"
             "        default: ''\n"
             "\njobs:\n")
JOB_ANCHOR = "  probes:\n    name: Numerical probes\n"


def upload(name, fname):
    return ("      - name: ARP-2-QC21 keep " + name + "\n"
            "        uses: actions/upload-artifact@v4\n"
            "        with:\n"
            "          name: arp2-qc21-" + name.split()[-1] + "\n"
            "          path: ${{ runner.temp }}/arp2-qc21/" + fname + "\n"
            "          if-no-files-found: error\n"
            "          retention-days: 90\n\n")


FROZEN_JOBS = (
    "  probes_arp2qc21:\n"
    "    name: " + JOB_A + "\n"
    "    runs-on: ubuntu-latest\n"
    "    timeout-minutes: 60\n"
    "    steps:\n"
    "      - uses: actions/checkout@v4\n"
    "        with:\n"
    "          fetch-depth: 0\n\n"
    "      - uses: actions/setup-python@v5\n"
    "        with:\n"
    "          python-version: '3.11'\n\n"
    "      - name: " + STEP_A3 + "\n"
    "        run: |\n"
    "          mkdir -p \"$RUNNER_TEMP/arp2-qc21\"\n"
    "          " + PY + CHECKER + " --event fixture > \"$RUNNER_TEMP/arp2-qc21/fixtures.json\"\n\n"
    + upload("the fixture output", "fixtures.json") +
    "      - name: ARP-2-QC21 stress\n"
    "        run: " + PY + CHECKER + " --stress > \"$RUNNER_TEMP/arp2-qc21/stress.json\"\n\n"
    + upload("the stress output", "stress.json") +
    "      - name: " + STEP_A7 + "\n"
    "        run: " + PY + CONTROLS + " stress-check \"$RUNNER_TEMP/arp2-qc21/stress.json\"\n\n"
    "      - name: ARP-2-QC21 checker self-test\n"
    "        run: " + PY + CHECKER + " --self-test\n\n"
    "      - name: ARP-2-QC21 control mutation tests\n"
    "        run: " + PY + CONTROLS + " --self-test\n\n"
    "      - name: " + STEP_A10 + "\n"
    "        if: ${{ " + RECEIPT_KEY + " }}\n"
    "        run: 'true'\n\n"
    "  probes_arp2qc21_decisive:\n"
    "    name: " + JOB_B + "\n"
    "    if: " + JOB_B_IF + "\n"
    "    runs-on: ubuntu-latest\n"
    "    timeout-minutes: 60\n"
    "    env:\n"
    "      ARP2QC21_SHA: ${{ inputs.arp2qc21_sha }}\n"
    "    steps:\n"
    "      - uses: actions/checkout@v4\n"
    "        with:\n"
    "          fetch-depth: 0\n\n"
    "      - uses: actions/setup-python@v5\n"
    "        with:\n"
    "          python-version: '3.11'\n\n"
    "      - name: " + STEP_B3 + "\n"
    "        run: " + B3_RUN + "\n\n"
    "      - name: " + STEP_B4 + "\n"
    "        run: |\n"
    "          mkdir -p \"$RUNNER_TEMP/arp2-qc21\"\n"
    "          " + PY + CHECKER + " --event \"" + B4_EXPR + "\" --dispatch-sha \"$ARP2QC21_SHA\" > "
    "\"$RUNNER_TEMP/arp2-qc21/measurements.json\"\n\n"
    + upload("the measurements", "measurements.json") +
    "      - name: " + STEP_B6 + "\n"
    "        if: " + B6_IF + "\n"
    "        run: " + PY + CONTROLS + " replay \"$RUNNER_TEMP/arp2-qc21/measurements.json\"\n\n")
AGG_EDITS = (
    (", probes_arp1marc]\n", ", probes_arp1marc, probes_arp2qc21, probes_arp2qc21_decisive]\n"),
    ("          ARP1MARC_RESULT: ${{ needs.probes_arp1marc.result }}\n",
     "          ARP1MARC_RESULT: ${{ needs.probes_arp1marc.result }}\n"
     "          ARP2QC21_RESULT: ${{ needs.probes_arp2qc21.result }}\n"
     "          ARP2QC21D_RESULT: ${{ needs.probes_arp2qc21_decisive.result }}\n"),
    ("          echo \"arp1marc=${ARP1MARC_RESULT}\"\n",
     "          echo \"arp1marc=${ARP1MARC_RESULT}\"\n"
     "          echo \"arp2qc21=${ARP2QC21_RESULT}\"\n"
     "          echo \"arp2qc21_decisive=${ARP2QC21D_RESULT}\"\n"),
    ("          test \"${ARP1MARC_RESULT}\" = success\n",
     "          test \"${ARP1MARC_RESULT}\" = success\n"
     "          test \"${ARP2QC21_RESULT}\" = success\n"
     "          test \"${ARP2QC21D_RESULT}\" = success -o \"${ARP2QC21D_RESULT}\" = skipped\n"))


def splice(d_text):
    """D's verify.yml with the frozen splice; None if an anchor is not found exactly once."""
    t = d_text
    for old, new in ((ON_ANCHOR, ON_SPLICE), (JOB_ANCHOR, FROZEN_JOBS + JOB_ANCHOR)) + AGG_EDITS:
        if t.count(old) != 1:
            return None
        t = t.replace(old, new)
    return t


def check_w(commit_text, d_text):
    """W: verify.yml as a whole file equals D's verify.yml with the frozen splice."""
    want = splice(d_text)
    return want is not None and commit_text == want


# ------------------------------------------------------------------------------------------------------------
# Control B: the node-form rules, checked by AST on every node of each script
# ------------------------------------------------------------------------------------------------------------
def dotted(n):
    out = []
    while isinstance(n, ast.Attribute):
        out.append(n.attr)
        n = n.value
    if isinstance(n, ast.Name):
        out.append(n.id)
        return ".".join(reversed(out))
    return None


def _is_lit(e):
    return isinstance(e, ast.Constant) and isinstance(e.value, str)


def _is_aok(e):
    return isinstance(e, ast.Call) and isinstance(e.func, ast.Name) and e.func.id == "a_ok"


def _is_main_guard(node):
    return (isinstance(node, ast.If) and isinstance(node.test, ast.Compare) and isinstance(node.test.left, ast.Name)
            and node.test.left.id == "__name__" and len(node.test.comparators) == 1
            and isinstance(node.test.comparators[0], ast.Constant) and node.test.comparators[0].value == "__main__")


def _dunder_ok(tree):
    """No name or attribute of the form __*__ other than the single `if __name__ == "__main__":`."""
    errs = []
    guards = [n for n in tree.body if _is_main_guard(n)]
    allowed = {id(g.test.left) for g in guards}
    if len(guards) > 1:
        errs.append("dunder: main guard twice")
    for n in ast.walk(tree):
        if isinstance(n, ast.Name) and re.fullmatch(r"__\w+__", n.id) and id(n) not in allowed:
            errs.append("dunder name " + n.id)
        if isinstance(n, ast.Attribute) and re.fullmatch(r"__\w+__", n.attr):
            errs.append("dunder attribute " + n.attr)
    return errs


def _gh_template_ok(js):
    """A gh path: an f-string or literal whose literal text reduces, with a_ok values replaced, to a frozen
    template under repos/amaybaum/incompleteness."""
    if _is_lit(js):
        txt = js.value
    elif isinstance(js, ast.JoinedStr):
        parts = []
        for v in js.values:
            if _is_lit(v):
                parts.append(v.value)
            elif isinstance(v, ast.FormattedValue) and _is_aok(v.value):
                parts.append("{V}")
            else:
                return False
        txt = "".join(parts)
    else:
        return False
    if txt == "repos/amaybaum/incompleteness":
        return True
    if not txt.startswith("repos/amaybaum/incompleteness/"):
        return False
    rest = txt[len("repos/amaybaum/incompleteness/"):]
    pats = (r"actions/runs\?[a-z0-9_=&.{}V]*", r"actions/runs/\{V\}", r"actions/runs/\{V\}/attempts/\{V\}",
            r"actions/runs/\{V\}/attempts/\{V\}/jobs\?per_page=100(&page=\{V\})?", r"actions/runs/\{V\}/artifacts",
            r"git/trees/\{V\}\?recursive=1", r"git/trees/\{V\}", r"activity\?ref=refs/heads/\{V\}(&per_page=100&page=\{V\})?")
    return any(re.fullmatch(p, rest) for p in pats)


def static_controls(src):
    """Control B on controls.py: imports, attributes, forbidden names, the frozen helpers, call position,
    open modes, process starts, git and gh forms, control T's exception."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return ["syntax"]
    errs = _dunder_ok(tree)
    call_funcs = {id(n.func) for n in ast.walk(tree) if isinstance(n, ast.Call)}
    top_defs = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]
    for h in HELPERS:
        all_defs = [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
                    and n.name == h]
        if top_defs.count(h) != 1 or len(all_defs) != 1:
            errs.append("c'': helper %s not bound exactly once by a top-level def" % h)
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            for a in n.names:
                if a.name not in CONTROLS_IMPORTS or a.asname:
                    errs.append("a: import " + a.name)
        elif isinstance(n, ast.ImportFrom):
            errs.append("a: from-import")
        if isinstance(n, ast.Name):
            if n.id in BANNED:
                errs.append("c: banned " + n.id)
            if n.id in HELPERS and not isinstance(n.ctx, ast.Load):
                errs.append("c'': helper bound " + n.id)
            if n.id in ("open", "subprocess") and not isinstance(n.ctx, ast.Load):
                errs.append("c': rebind " + n.id)
            if n.id == "open" and id(n) not in call_funcs:
                errs.append("c': open not in call position")
        if isinstance(n, ast.Attribute):
            d = dotted(n)
            if d == "subprocess.run" and id(n) not in call_funcs:
                errs.append("c': subprocess.run not in call position")
            if d:
                head = d.split(".")[0]
                if head == "os":
                    if not (d == "os.path" or d.startswith("os.path.")):
                        errs.append("b: attribute " + d)
                    elif d.startswith("os.path.") and d.split(".")[2] not in MOD_ATTRS["os.path"]:
                        errs.append("b: attribute " + d)
                elif head in MOD_ATTRS and MOD_ATTRS[head] is not None and "." in d:
                    if d.split(".")[1] not in MOD_ATTRS[head]:
                        errs.append("b: attribute " + d)
        if isinstance(n, (ast.ClassDef,)) and n.name in HELPERS:
            errs.append("c'': helper class")
        if isinstance(n, ast.ExceptHandler) and n.name in HELPERS + ("open", "subprocess"):
            errs.append("c'': except-as binds " + n.name)
        if isinstance(n, (ast.MatchAs, ast.MatchStar)) and n.name in HELPERS:
            errs.append("c'': match capture")
        if isinstance(n, ast.MatchMapping) and n.rest in HELPERS:
            errs.append("c'': match capture")
        if isinstance(n, ast.alias) and (n.asname or n.name) in HELPERS:
            errs.append("c'': import alias")
        if isinstance(n, (ast.Global, ast.Nonlocal)) and set(n.names) & set(HELPERS + ("open", "subprocess")):
            errs.append("c'': global/nonlocal")
        if isinstance(n, ast.arg) and n.arg in HELPERS + ("open", "subprocess"):
            errs.append("c'': argument binds " + n.arg)
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and n.name in ("open", "subprocess"):
            errs.append("c': rebind by def")
        if isinstance(n, ast.Call):
            f = dotted(n.func)
            for arg in list(n.args) + [k.value for k in n.keywords]:
                if dotted(arg) == "subprocess.run" or (isinstance(arg, ast.Name) and arg.id == "open"):
                    errs.append("c': passed as an argument")
            if f == "w_path":
                nm = n.args[1] if len(n.args) > 1 else None
                if not (_is_lit(nm) and re.fullmatch(r"[A-Za-z0-9_.-]+", nm.value)):
                    errs.append("d: w_path name not a slash-free literal")
            if f == "open":
                mode = n.args[1] if len(n.args) > 1 else next((k.value for k in n.keywords if k.arg == "mode"), None)
                m = mode.value if isinstance(mode, ast.Constant) else None
                p = n.args[0] if n.args else None
                if m in ("r", "rb"):
                    pass
                elif m in ("w", "wb") and isinstance(p, ast.Call) and dotted(p.func) == "w_path":
                    pass
                else:
                    errs.append("d: open mode")
            if f == "subprocess.run":
                errs += _run_form(n)
    for n in ast.walk(tree):
        if isinstance(n, (ast.Return, ast.Assign, ast.AnnAssign, ast.AugAssign, ast.NamedExpr)):
            val = n.value
            if val is not None and (dotted(val) == "subprocess.run" or (isinstance(val, ast.Name) and val.id == "open")):
                errs.append("c': stored or returned")
        if isinstance(n, (ast.List, ast.Tuple, ast.Set, ast.Dict)):
            elts = list(n.keys) + list(n.values) if isinstance(n, ast.Dict) else n.elts
            if any(e is not None and (dotted(e) == "subprocess.run" or (isinstance(e, ast.Name) and e.id == "open"))
                   for e in elts):
                errs.append("c': in a container")
        if isinstance(n, (ast.FunctionDef, ast.Lambda)):
            defaults = n.args.defaults + [d for d in n.args.kw_defaults if d is not None]
            if any(dotted(d) == "subprocess.run" or (isinstance(d, ast.Name) and d.id == "open") for d in defaults):
                errs.append("c': default value")
    errs += _dispatch_string_sites(tree)
    return sorted(set(errs))


def _dispatch_string_sites(tree):
    """controls.py: the string constant "workflow_dispatch" occurs only in the run-classification functions
    (those named run_class_*, which derive-run, order and verdict use)."""
    errs = []
    owners = {}
    for fn in tree.body:
        if isinstance(fn, ast.FunctionDef):
            for n in ast.walk(fn):
                owners[id(n)] = fn.name
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value == run_class_dispatch():
            if not str(owners.get(id(n))).startswith("run_class_"):
                errs.append("workflow_dispatch outside the run-classification functions")
    return errs


def run_class_dispatch():
    """The run-classification event name."""
    return "workflow_dispatch"


def _run_form(n):
    errs = []
    for k in n.keywords:
        if k.arg not in ("capture_output", "check", "text"):
            errs.append("e: keyword " + str(k.arg))
    if not n.args or not isinstance(n.args[0], ast.List) or len(n.args) != 1:
        return errs + ["e: not a list display"]
    el = n.args[0].elts
    if not el or not _is_lit(el[0]):
        return errs + ["e: variable first element"]
    head = el[0].value
    vals = [e.value if _is_lit(e) else None for e in el]
    if head == "git":
        if not all(_is_lit(e) or _is_aok(e) for e in el):
            errs.append("f: git element form")
        if len(vals) < 2 or vals[1] not in GIT_SUBCOMMANDS:
            errs.append("f: git subcommand")
        if any(v is not None and v.startswith(GIT_BAD) for v in vals):
            errs.append("f: git option")
        if len(vals) > 1 and vals[1] in ("show", "diff-tree") and not {"--no-textconv", "--no-ext-diff"} <= set(vals):
            errs.append("f: show/diff-tree without --no-textconv --no-ext-diff")
        ai = [i for i, e in enumerate(el) if _is_aok(e)]
        if ai:
            if "--end-of-options" not in vals or vals.index("--end-of-options") > ai[0]:
                errs.append("f: --end-of-options")
            else:
                j = vals.index("--end-of-options")
                if not all(_is_aok(e) for e in el[j + 1:]):
                    errs.append("f: element after --end-of-options")
            if len(vals) > 1 and vals[1] == "rev-parse" and "--verify" not in vals:
                errs.append("f: rev-parse without --verify")
    elif head == "gh":
        if vals[1:4] != ["api", "--method", "GET"] or len(el) < 5 or not _gh_template_ok(el[4]):
            errs.append("g: gh form")
        if any(not (_is_lit(e) and e.value in GH_EXTRA) for e in el[5:]):
            errs.append("g: gh extra element")
    elif head == "python3":
        if not (vals[:4] == ["python3", "-I", "-S", "-c"] and len(el) == 7 and _is_lit(el[4]) and el[4].value == T_CODE
                and _is_aok(el[5]) and _is_aok(el[6])):
            errs.append("h: control T's command")
    else:
        errs.append("e: argv0 " + str(head))
    return errs


GUARD_SELFTEST_FUNCS = ("t_mguard_checker", "t_builder_refuses")


def static_checker(src, builders=("s_build_p", "s_build_repinv", "s_build_b", "s_build_c")):
    """Control B on qc21_check.py: imports; "workflow_dispatch" once, as DISPATCH_EVENT; DISPATCH_EVENT only in
    s_mode and M-GUARD's self-test functions; os at exactly two sites, each `os.environ` passed whole to s_mode;
    each registered builder referenced only in its own def, DECISIVE_BUILDERS and s_decisive, with the refusal
    as its first statement; s_decisive only at the default entry and in t_builder_refuses, whose body is the
    stated try form; no forbidden names; no dunder beyond the main guard."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return ["syntax"]
    errs = _dunder_ok(tree)
    imps = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            for a in n.names:
                imps.add(a.name)
                if a.asname:
                    errs.append("import alias")
        if isinstance(n, ast.ImportFrom):
            imps.add(n.module)
            if n.module != "fractions" or [a.name for a in n.names] != ["Fraction"] or n.names[0].asname:
                errs.append("from-import")
    if imps != CHECKER_IMPORTS:
        errs.append("imports %s" % sorted(imps))
    owner = {}
    for fn in tree.body:
        if isinstance(fn, ast.FunctionDef):
            for n in ast.walk(fn):
                owner[id(n)] = fn.name
    consts = [n for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, str)
              and run_class_dispatch() in n.value]
    de = [n for n in tree.body if isinstance(n, ast.Assign) and len(n.targets) == 1
          and isinstance(n.targets[0], ast.Name) and n.targets[0].id == "DISPATCH_EVENT"]
    if len(consts) != 1 or len(de) != 1 or de[0].value is not consts[0]:
        errs.append("workflow_dispatch not exactly once as DISPATCH_EVENT")
    for n in ast.walk(tree):
        if isinstance(n, ast.Name) and n.id == "DISPATCH_EVENT" and isinstance(n.ctx, ast.Load):
            if owner.get(id(n)) not in ("s_mode",) + GUARD_SELFTEST_FUNCS:
                errs.append("DISPATCH_EVENT outside s_mode and M-GUARD")
        if isinstance(n, ast.Name) and n.id in BANNED:
            errs.append("banned " + n.id)
        if isinstance(n, ast.Attribute) and n.attr in ("system", "popen", "modules"):
            errs.append("attribute " + n.attr)
    os_sites = [n for n in ast.walk(tree) if isinstance(n, ast.Name) and n.id == "os" and isinstance(n.ctx, ast.Load)]
    env_ok = 0
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ("s_mode", "run_entry") \
                and len(n.args) == 2:
            a = n.args[1]
            if isinstance(a, ast.Attribute) and a.attr == "environ" and isinstance(a.value, ast.Name) and a.value.id == "os":
                env_ok += 1
    if len(os_sites) != 2 or env_ok != 2:
        errs.append("os not at exactly two sites as os.environ passed whole to s_mode")
    db = [n for n in tree.body if isinstance(n, ast.Assign) and len(n.targets) == 1
          and isinstance(n.targets[0], ast.Name) and n.targets[0].id == "DECISIVE_BUILDERS"]
    if len(db) != 1 or not isinstance(db[0].value, ast.Tuple) or \
            [e.value for e in db[0].value.elts if isinstance(e, ast.Constant)] != list(builders):
        errs.append("DECISIVE_BUILDERS not the frozen list")
    defs = {fn.name: fn for fn in tree.body if isinstance(fn, ast.FunctionDef)}
    for b in builders + ("s_decisive",):
        fn = defs.get(b)
        if fn is None:
            errs.append("missing " + b)
            continue
        first = fn.body[0]
        if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant) and isinstance(first.value.value, str):
            first = fn.body[1] if len(fn.body) > 1 else None
        if not (isinstance(first, ast.Expr) and isinstance(first.value, ast.Call)
                and isinstance(first.value.func, ast.Name) and first.value.func.id == "s_refusal"
                and len(first.value.args) == 1 and isinstance(first.value.args[0], ast.Constant)
                and first.value.args[0].value == b):
            errs.append("refusal is not the first statement of " + b)
    for n in ast.walk(tree):
        if isinstance(n, ast.Name) and n.id in builders:
            if owner.get(id(n)) != "s_decisive" or not isinstance(n.ctx, ast.Load):
                errs.append("builder %s referenced outside s_decisive" % n.id)
        if isinstance(n, ast.Name) and n.id == "s_decisive":
            if owner.get(id(n)) not in ("run_entry", "t_builder_refuses") or not isinstance(n.ctx, ast.Load):
                errs.append("s_decisive referenced outside the entry and t_builder_refuses")
    sd_sites = [owner.get(id(n)) for n in ast.walk(tree) if isinstance(n, ast.Name) and n.id == "s_decisive"]
    if sorted(sd_sites) != ["run_entry", "t_builder_refuses"]:
        errs.append("s_decisive sites %s" % sorted(map(str, sd_sites)))
    tb = defs.get("t_builder_refuses")
    if tb is None or len(tb.body) != 1 or not isinstance(tb.body[0], ast.Try):
        errs.append("t_builder_refuses not a single try statement")
    else:
        tr = tb.body[0]
        call_ok = (len(tr.body) == 1 and isinstance(tr.body[0], ast.Expr) and isinstance(tr.body[0].value, ast.Call)
                   and isinstance(tr.body[0].value.func, ast.Name) and tr.body[0].value.func.id == "s_decisive"
                   and not tr.body[0].value.args and not tr.body[0].value.keywords)
        h_ok = (len(tr.handlers) == 1 and isinstance(tr.handlers[0].type, ast.Name)
                and tr.handlers[0].type.id == "QC21Refusal" and tr.handlers[0].name is None)
        if not (call_ok and h_ok and tr.orelse and not tr.finalbody):
            errs.append("t_builder_refuses form")
    for fn in defs.values():
        if fn.name.startswith("t_") and fn.name != "t_builder_refuses":
            for n in ast.walk(fn):
                if isinstance(n, ast.Name) and n.id == "s_decisive":
                    errs.append("second self-test function references the gated entry")
    return sorted(set(errs))


# C-EXACT and C-INDEP (AST scans of qc21_check.py)
def c_exact(src):
    tree = ast.parse(src)
    hits = []
    owner = {}
    for fn in ast.walk(tree):
        if isinstance(fn, ast.FunctionDef):
            for n in ast.walk(fn):
                owner.setdefault(id(n), fn.name)
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex)):
            hits.append("float literal")
        if isinstance(n, ast.Name) and n.id in ("float", "complex"):
            hits.append("float call")
        if isinstance(n, (ast.Import, ast.ImportFrom)):
            names = [a.name for a in n.names] + ([n.module] if isinstance(n, ast.ImportFrom) else [])
            if "math" in names or "cmath" in names:
                hits.append("math import")
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Div) and owner.get(id(n)) != "q_div":
            hits.append("'/' outside the Fraction helper")
        if isinstance(n, ast.AugAssign) and isinstance(n.op, ast.Div):
            hits.append("'/=' outside the Fraction helper")
    return hits


V_BUILTINS = {"len", "range", "sum", "min", "max", "abs", "sorted", "enumerate", "zip", "all", "any", "int", "tuple",
              "list", "dict", "set", "isinstance"}
V_FORBIDDEN = {"globals", "locals", "vars", "getattr", "setattr", "eval", "exec", "compile", "__import__"}


def c_indep(src):
    """C-INDEP: inside every v_* function (body, defaults, decorators, nested functions and lambdas), calls target
    only v_* functions, Fraction, json.loads, itertools.combinations, the whitelisted builtins, or attribute calls
    on local variables; every module-level name referenced is a v_* function or a whitelisted name."""
    tree = ast.parse(src)
    module_names = set()
    for n in tree.body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            module_names.add(n.name)
        elif isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    module_names.add(t.id)
        elif isinstance(n, (ast.Import, ast.ImportFrom)):
            for a in n.names:
                module_names.add((a.asname or a.name).split(".")[0])
    errs = []
    vfuncs = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name.startswith("v_")]
    if not vfuncs:
        errs.append("no verifier")
    for fn in vfuncs:
        local = set()
        for n in ast.walk(fn):
            if isinstance(n, ast.arg):
                local.add(n.arg)
            if isinstance(n, ast.Name) and isinstance(n.ctx, (ast.Store, ast.Del)):
                local.add(n.id)
            if isinstance(n, (ast.FunctionDef, ast.Lambda)) and n is not fn:
                if isinstance(n, ast.FunctionDef):
                    local.add(n.name)
        for n in ast.walk(fn):
            if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load):
                if n.id in V_FORBIDDEN:
                    errs.append("%s: forbidden %s" % (fn.name, n.id))
                elif n.id in local or n.id.startswith("v_") or n.id in V_BUILTINS:
                    pass
                elif n.id in ("Fraction", "json", "itertools"):
                    pass
                elif n.id in module_names:
                    errs.append("%s: module-level name %s" % (fn.name, n.id))
                else:
                    errs.append("%s: name %s" % (fn.name, n.id))
            if isinstance(n, ast.Call):
                f = n.func
                if isinstance(f, ast.Name):
                    if not (f.id.startswith("v_") or f.id in V_BUILTINS or f.id == "Fraction" or f.id in local):
                        errs.append("%s: call %s" % (fn.name, f.id))
                elif isinstance(f, ast.Attribute):
                    d = dotted(f)
                    if d in ("json.loads", "itertools.combinations"):
                        pass
                    elif isinstance(f.value, ast.Name) and f.value.id in local:
                        pass
                    elif isinstance(f.value, (ast.Subscript, ast.Call)):
                        errs.append("%s: attribute call on a non-local value" % fn.name)
                    else:
                        errs.append("%s: call %s" % (fn.name, d))
                else:
                    errs.append("%s: computed call" % fn.name)
            if isinstance(n, ast.Attribute) and re.fullmatch(r"__\w+__", n.attr):
                errs.append("%s: dunder" % fn.name)
    return sorted(set(errs))


def c_iface(src_checker, src_controls):
    """C-IFACE (static part): P's screen input reads only the registered port; decide-p references neither ATTR
    nor the SH-0 and SH-K fields (only through the Adm_B loop)."""
    errs = []
    t = ast.parse(src_checker)
    fns = {n.name: n for n in t.body if isinstance(n, ast.FunctionDef)}
    arec = fns.get("p_arm_record")
    if arec is None:
        errs.append("p_arm_record missing")
    else:
        sof = [n for n in ast.walk(arec) if isinstance(n, ast.FunctionDef) and n.name == "s_of"]
        keys = {n.slice.value for f in sof for n in ast.walk(f) if isinstance(n, ast.Subscript)
                and isinstance(n.slice, ast.Constant) and isinstance(n.slice.value, str)}
        if not sof or not keys <= {"port", "w", "kept"} or "port" not in keys:
            errs.append("P's screen input reads %s" % sorted(keys))
    for src, name in ((src_checker, "k_decide_p"), (src_controls, "decide_p")):
        tt = ast.parse(src)
        f = [n for n in tt.body if isinstance(n, ast.FunctionDef) and n.name == name]
        if not f:
            errs.append(name + " missing")
            continue
        for n in ast.walk(f[0]):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (
                    n.value in ("shk", "sh0", "SH-0", "SH-K", "ATTR", "attr") or "(w,w')" in n.value
                    or "(0,w')" in n.value):
                errs.append("%s reads a sham-specific or attribution field: %s" % (name, n.value))
            if isinstance(n, ast.Name) and n.id in ("k_attr", "attr_value", "NAME_SHK", "NAME_SH0"):
                errs.append("%s references %s" % (name, n.id))
    return errs


# ------------------------------------------------------------------------------------------------------------
# decide: the frozen decision rules, recomputed here from the raw fields (independently of the checker)
# ------------------------------------------------------------------------------------------------------------
Q = fractions.Fraction


def q(x):
    if isinstance(x, int) and not isinstance(x, bool):
        return Q(x)
    if isinstance(x, str):
        if "/" in x:
            a, b = x.split("/")
            return Q(int(a), int(b))
        return Q(int(x))
    raise ValueError("not a rational: %r" % (x,))


def decide_p(rec):
    """Decision rule P (first match): reads the class, each member's V, D, NONABS, SPI, the off and on arms and
    the P controls."""
    try:
        adm, arms, red = rec["adm"], rec["arms"], rec["controls_red"]
        v_off = q(arms[rec["off"]]["V"])
        d_on = q(arms[rec["on"]]["D"])
        vals = {a: (q(arms[a]["V"]), q(arms[a]["D"]), arms[a]["NONABS"], arms[a]["SPI"]) for a in adm}
    except (KeyError, TypeError, ValueError):
        return "P-VOID", ["missing-field"]
    if red:
        return "P-VOID", list(red)
    bad = [a for a in adm if vals[a][2] is not True or vals[a][3] is not True]
    if bad:
        return "P-VOID", bad
    if v_off == 0:
        return "P-NO-FRINGES", []
    if d_on == 0:
        return "P-NO-RECORD", []
    rws = [a for a in adm if vals[a][1] > 0 and vals[a][0] >= v_off]
    if rws:
        return "P-RECORD-WITHOUT-SUPPRESSION", rws
    return "P-COMPLEMENTARITY", []


def attr_value(off, on, shk):
    try:
        ok_rec = q(on["D"]) > 0 and q(on["V"]) < q(off["V"])
        ok_sham = q(shk["D"]) == 0 and canonical(shk["K"]) == canonical(on["K"])
        retain = q(shk["V"]) == q(off["V"])
    except (KeyError, TypeError, ValueError):
        return "undefined"
    if not (ok_rec and ok_sham):
        return "undefined"
    return "attributable to which-path recording" if retain else "not attributable"


def decide_b(rec):
    try:
        red, frs = rec["controls_red"], rec["fragments"]
    except (KeyError, TypeError):
        return "B-VOID", ["missing-field"]
    if red:
        return "B-VOID", list(red)
    codes = []
    for f in frs:
        if f.get("lp") not in ("feasible", "infeasible") or f.get("verified") is not True:
            codes.append(str(f.get("name")))
        if f.get("role") in ("B-P", "B-C") and f.get("lp_reads_equal_acc") is not True:
            codes.append("lp_reads_equal_acc:" + str(f.get("name")))
    if codes:
        return "B-VOID", codes
    if any(f.get("role") in ("B-P", "B-C") and f["lp"] == "infeasible" for f in frs):
        return "B-CONTEXTUAL", []
    return "B-CLASSICALLY-IMITABLE", []


def decide_c(rec):
    try:
        if rec["controls_red"] or rec["complete"] is not True or rec["flags_agree"] is not True:
            return "C-VOID", list(rec["controls_red"]) or ["incomplete-or-flags"]
        inst = rec["instances"]

        def conj(i, k):
            return all(i[f][k] is True for f in ("HC", "CONS", "VAL")) and i["WCL"] is True and i["ABL"] is True \
                and i["EMB"] is True

        if any(conj(i, "12") for i in inst):
            return "C-EXPOSURE", []
        if any(conj(i, "6") and not conj(i, "12") for i in inst):
            return "C-SIZE-DEPENDENT", []
        if any(i["HC"]["12"] and i["VAL"]["12"] and i["WOCT"]["12"] and i["ABL"] and i["EMB"] for i in inst):
            return "C-NONSTABILIZER", []
    except (KeyError, TypeError):
        return "C-VOID", ["missing-field"]
    return "C-SURVIVAL", []


def decide_levels(p_tok, b_ctx, b_eq, acc_owner, c_tok, imported):
    withheld = set()
    for i in imported:
        if i in ("L-PATH", "L-PORT"):
            withheld |= {1, 2}
        if i in ("L-CAL", "L-UPRIME"):
            withheld |= {3}
    l1 = p_tok == "P-COMPLEMENTARITY" and 1 not in withheld
    l2 = l1 and b_ctx and b_eq and acc_owner and 2 not in withheld
    l3 = l2 and c_tok == "C-EXPOSURE" and 3 not in withheld
    return 3 if l3 else 2 if l2 else 1 if l1 else "none"


MEAS_TOP = ("schema", "version", "mode", "complete", "parameters", "P", "P_controls", "REP_INV", "B", "C",
            "fixtures", "controls", "budget", "flags")


def schema_errors(m):
    errs = []
    if not isinstance(m, dict):
        return ["not an object"]
    for k in MEAS_TOP:
        if k not in m:
            errs.append("missing " + k)
    if m.get("schema") != "arp2-qc21-measurements" or m.get("version") != 1:
        errs.append("schema/version")
    if m.get("mode") not in ("decisive", "fixture"):
        errs.append("mode")
    return errs


def decide(m):
    """decide: VOID unless the measurements are decisive, complete and in schema, with no placeholder; else
    every token recomputed from the raw fields, and the checker's flags must agree (X)."""
    errs = schema_errors(m)
    if errs:
        return {"VOID": errs}
    reasons = []
    if m["mode"] != "decisive":
        reasons.append("mode")
    if m["complete"] is not True:
        reasons.append("complete")
    frs = m["B"].get("fragments", []) if isinstance(m["B"], dict) else []
    if any(f.get("lp") == "placeholder" for f in frs) or m["P"] == "placeholder" or m["C"] == "placeholder":
        reasons.append("placeholder")
    if reasons:
        return {"VOID": reasons}
    f = m["flags"]
    p_rec = {"adm": m["P"]["decide_p_inputs"]["adm"], "arms": m["P"]["arms"], "off": "off",
             "on": m["P"]["decide_p_inputs"]["on"], "controls_red": f["controls_red"]["P"]}
    p_tok, _ = decide_p(p_rec)
    b_tok, _ = decide_b({"controls_red": f["controls_red"]["B"], "fragments": frs})
    c_tok, _ = decide_c({"controls_red": f["controls_red"]["C"], "complete": True, "flags_agree": True,
                         "instances": m["C"]["instances"]})
    bp = [x for x in frs if x.get("role") == "B-P"]
    b_ctx = bool(bp) and bp[0]["lp"] == "infeasible"
    b_eq = bool(bp) and bp[0].get("lp_reads_equal_acc") is True
    lev = decide_levels(p_tok, b_ctx, b_eq, True, c_tok, m["REP_INV"]["reclassified"])
    attr = attr_value(m["P"]["arms"]["off"], m["P"]["arms"]["(w,0)"], m["P"]["arms"]["(w,w')"])
    agree = (p_tok == f["P"] and b_tok == f["B"] and c_tok == f["C"] and str(lev) == str(f["levels"]["level"])
             and attr == m["P"]["ATTR"]["value"])
    out = {"P": p_tok, "B": b_tok, "C": c_tok, "level": lev, "ATTR": attr, "flags_agree": agree}
    if not agree:
        out["VOID"] = ["X: the checker's flags disagree with decide"]
    return out


# ------------------------------------------------------------------------------------------------------------
# note: result.md from the measurements, with the frozen texts; S4
# ------------------------------------------------------------------------------------------------------------
FREEZE_DISCLOSURE = (
    "P's construction-B token, P-COMPLEMENTARITY, was derived on paper before the freeze (AP1 §4.5 with SA-1(c); AP1 "
    "Lemma 3) and evaluated before the freeze by the writer's probe (`probes-r8/p_native.py`, `72c4db13…`) and the "
    "reviewer's probes (`review/probes-r6/p_arms_indep.py`, `1e351a74…`; `review/probes-r8/adm_closure.py`, "
    "`479a10c2…`). The CI evaluation reproduces that derivation under frozen controls. It is a consistency check "
    "(§A.23), not a novel confrontation, and under item L(i) Level 1's condition was known before the freeze.")
LEVEL1_TEXT = ("Level 1 here records that the run reproduces a known paper construction (AP1 §4.5 with SA-1(c); AP1 "
               "Lemma 3) under frozen controls. It is a consistency check, not a new derivation and not an "
               "independently generated mechanism.")
LEVEL3_TEXT = ("Level 3 here joins B-P (P's two-path apparatus) with C-EXPOSURE (the U′ gadget), two unrelated "
               "instances")
OWNER_LEVELS = ("… reaching Level 2 does not automatically establish Level 3, and even Level 3 does not establish full "
                "equivalence.")
WITNESS_PRINCIPLE = ("failure to construct a witness is not proof that no witness exists, unless a theorem "
                     "establishes that impossibility within a clearly stated scope.")
OWNER_STANDARD = ("Conversely, relaxing an assumption is not sufficient by itself. The resulting model must still "
                  "produce valid probabilities, observable quantum predictions and consistent behavior across "
                  "repeated experiments.")
OWNER_CASE = "If both A and B reproduce quantum behavior, observational incompleteness may not be necessary for that result."
CONSTR_B = ("construction B (the OI substratum plus the observational-incompleteness principles named in the ledger, "
            "each identified and tested separately)")
COMMON_CLAUSE = (
    "This concerns the finite models of this round: for P, one carrier cell with phase, arm and screen cells under the "
    "class-N step of " + CONSTR_B + " with supplied arming; for B, the stated fragments; for C, the ring `Z_3` with the "
    "four non-affine symmetric rules in a gadget, detectors realized by meters under the rule of " + CONSTR_B + ", the "
    "seven QA sources, the 150 rounds and at most 12 compositions. It is conditional on P2, N2, H-PREP, NNB (for "
    "`Λ_{y,b}`), P3 arming, E-iso, the supplied registration, the held unread cells, the refilled mediators, and the "
    "imported identifications of path, port and U′. Nothing here concerns larger systems, other alphabets, other "
    "identifications, a second system, or a physically sourced apparatus.")
B_SCOPE = (
    "No preparation- and measurement-noncontextual model exists over this fragment's own operational equivalences, "
    "read over the whole access class {Acc} ({typing}). Every OI table is generated by a configuration model, so this "
    "is a degenerate pairing on the configurations: it is relative to an access class whose reads do not span them. It "
    "does not exclude classical models in which those equivalences fail ontically: classical registers with unread "
    "parities, classical fields with intensity-normalized single-event detection, or OI's own configuration model.")
NO_OUTCOME = [
    "No outcome is a universal statement. None adopts a non-affine rule or a candidate strengthened principle, changes "
    "the status of A5, P1, P2, N2, H-PREP, NNB or any manuscript claim, or establishes a mechanism that reproduces QM.",
    "P-COMPLEMENTARITY is at most Level 1, and P's table has noncontextual classical models, construction B among them.",
    "No single suppression is assigned to path recording rather than disturbance, in any theory: dephasing is an "
    "equally valid explanation of each.",
    "Whether an arm leaves a path-correlated record is relative to access.",
    "Complementarity over construction B's class rests on SA-1(c), which is posited, not derived. Its existence "
    "reading holds in `A_P` as well.",
    "No substratum-only P is posed.",
    "B-CONTEXTUAL is relative to the fragment's own equivalences and to its `Acc`.",
    "C-EXPOSURE is a finite witness on bounded orbits through U′'s functionals.",
    "Every probability is rational. Nothing bears on irrational or approximate gates."]
S4_PHRASES = ("native protection", "is a theorem", "theorem-level", "proves", "proved", "never", "permanently",
              "in general", "for every observer", "physically justified", "establishes QM", "quantum mechanism",
              " iff ", "if and only if", "is equivalent to", "exactly when", "should not be read",
              "observed to be due", "quantum behaviour", "quantum behavior established", "proves quantum",
              "genuinely quantum", "native OI", "attributed to path recording", "excludes classical",
              "is due to recording", "caused by recording", "attributed to recording")
OWNER_QUOTES = (WITNESS_PRINCIPLE, OWNER_STANDARD, OWNER_CASE, OWNER_LEVELS)


def s4_hits(text):
    t = text
    for qt in OWNER_QUOTES:
        t = t.replace(qt, "")
    return [p for p in S4_PHRASES if p in t]


def fmt(x):
    return "null" if x is None else str(x)


def p_text(m, tok, lst):
    a = m["P"]["arms"]
    off, on, sh0, shk = a["off"], a["(w,0)"], a["(0,w')"], a["(w,w')"]
    ab = m["P"]["ab_p"]
    attr = m["P"]["ATTR"]["value"]
    if tok == "P-COMPLEMENTARITY":
        er_on, er_k = on["eraser"], shk["eraser"]
        return (
            "In " + CONSTR_B + " of P, with two phase settings, a known bit `φ ∈ {0, 1}` added to the read functional, "
            "the screen port follows `x + φ` with the marker off (`V = " + fmt(off["V"]) + "`); with single-path "
            "sources it is uniform. With the marker on, the held, unread marker carries a validated path record (`D = "
            + fmt(on["D"]) + "`) and `V = " + fmt(on["V"]) + "`. Over the admissible arm class of construction B ("
            + ", ".join(m["P"]["decide_p_inputs"]["adm"]) + "), every arm that records the path also disturbs the phase "
            "(kernel " + canonical(on["K"]).strip() + ") and suppresses the fringes: complementarity holds over that "
            "class. Each suppression is equally explained by the accompanying disturbance. The disturbance alone, with "
            "no path-correlated record, gives `V = " + fmt(shk["V"]) + "`; the coupling alone, with no disturbance, "
            "gives `V = " + fmt(sh0["V"]) + "`. What the construction adds is that, in its admissible class, no record "
            "exists without that disturbance. This rests on SA-1(c), a posited principle. Whether an arm leaves a "
            "path-correlated record is relative to access: the dephasing arm's `D = 0` holds because its second slot is "
            "unknown under N2. Erasure: sorting by the marker's conjugate slot gives conditional `V = "
            + canonical(er_on.get("cell0.slot0")).strip() + "`; sorting the dephasing arm by its noise value gives "
            "conditional `V = " + canonical(er_k.get("cell0.slot0")).strip() + "`; unsorted, `V = "
            + fmt(er_on.get("unsorted")) + "`. The table has noncontextual classical models, among them a classical "
            "wave with a polarization-type marker and construction B itself. This result excludes no classical "
            "explanation. A/B: existence, " + ab["existence_case"] + "; universality, " + ab["universality_case"]
            + ". Attribution (`ATTR`, a separate validated field, not part of the token): " + attr + ". In this model, "
            "as in QM and classical waves, the kick-matched sham suppresses in every case in which the marker does, so "
            "the suppression is not attributable to which-path recording. This was disclosed before the freeze. Level "
            "1, where awarded, records that the run reproduces a known paper construction; it is not a new derivation "
            "or an independently generated mechanism.")
    ab_s = " A/B: existence, " + ab["existence_case"] + "; universality, " + ab["universality_case"] + "."
    if tok == "P-RECORD-WITHOUT-SUPPRESSION":
        return ("In construction B of P, the admissible arms " + ", ".join(lst) + " record the path (`D = "
                + ", ".join(fmt(a[x]["D"]) for x in lst) + "`) and leave the fringes (`V = "
                + ", ".join(fmt(a[x]["V"]) for x in lst) + "`). Complementarity fails over this class." + ab_s)
    if tok == "P-NO-FRINGES":
        return ("With the marker off the screen shows no two-setting interference (`V = " + fmt(off["V"]) + "`). No "
                "complementarity relation is reported in this model.")
    if tok == "P-NO-RECORD":
        return ("The on arm leaves no validated path record (`D = " + fmt(on["D"]) + "`). No complementarity relation "
                "is reported in this model.")
    return "A required P control or validation check failed: " + ", ".join(lst) + ". No reading is made."


C_TEXTS = {
    "C-EXPOSURE": ("For {inst}, the gadget composed up to 12 times acts on the detector records (U′'s three "
                   "functionals, read by meters under the rule of " + CONSTR_B + ") as one fixed affine operation "
                   "whose unit-modulus spectrum is not that of any Clifford-class map, with a constant herald, every "
                   "orbit law inside the calibrated Bloch ball, supplies in the class `N_sup` and forward "
                   "conditioning. The identical gadget with the rule made affine, or idle (a change of dynamics), "
                   "shows no such operation. With `reg = none` on the same `(g, m, k)` the witness {ca}; "
                   "record-dependent conditioning {cond} part of the origin. B's status of this instance: {b}. "
                   "Composition alongside a second system, read and update statistics beyond the three detectors, and "
                   "every branch's validity as a quantum instrument are not tested here."),
    "C-SIZE-DEPENDENT": ("For {inst}, the operation is fixed on the detector records over 6 compositions and not over "
                         "12: the K = 12 conjunction fails."),
    "C-NONSTABILIZER": ("No gadget acts as a non-Clifford fixed operation within scope. For {inst}, orbit laws reach "
                        "calibrated record coordinates inside the ball and outside the octahedron."),
    "C-SURVIVAL": ("Within this scope no non-affine gadget yields a non-Clifford fixed operation or a non-stabilizer "
                   "valid orbit law on the detector records. This is a scoped finite search, exhaustive within its "
                   "scope; it is not an impossibility statement. The witness principle: \"" + WITNESS_PRINCIPLE + "\""),
    "C-VOID": "A required C control failed: {codes}. No reading is made."}


def make_note(m, d, f, s1, e):
    dec = decide(m)
    lines = ["# ARP-2-QC21 (Q-C2-1): result", "", FREEZE_DISCLOSURE, "",
             "- `D` = `%s`; `F` = `%s`; S1 = `%s`; `E` = `%s`." % (d, f, s1, e), ""]
    if "VOID" in dec:
        lines += ["**Token:** `VOID`", "", "A required control failed, or the output was incomplete: "
                  + ", ".join(dec["VOID"]) + ". No reading is made. The measurements are preserved as produced.", ""]
        return "\n".join(lines) + "\n"
    p_rec = {"adm": m["P"]["decide_p_inputs"]["adm"], "arms": m["P"]["arms"], "off": "off", "on": "(w,0)",
             "controls_red": m["flags"]["controls_red"]["P"]}
    p_tok, p_list = decide_p(p_rec)
    lines += ["## P", "", "**Token:** `%s`" % p_tok, "", FREEZE_DISCLOSURE + " " + p_text(m, p_tok, p_list), "",
              "**ATTR** (validation layer, printed beside the token): " + dec["ATTR"] + ".", ""]
    lines += ["**Ablations** (`pred_change`, `mech_change`, `access_only`; `dynamics_credit` beside them):", ""]
    for name, r in sorted(m["P"]["ablate_p"].items()):
        lines.append("- %s: token %s; pred_change %s; mech_change %d cells; access_only %s; dynamics_credit %s."
                     % (name, r.get("token"), r.get("pred_change"), len(r.get("mech_change", [])),
                        r.get("access_only"), r.get("dynamics_credit")))
    if m["P"]["ab_p"]["existence_case"] == "both succeed":
        lines += ["", OWNER_CASE]
    lines += ["", "## B", "", "**Token:** `%s`" % dec["B"], ""]
    if dec["B"] == "B-CONTEXTUAL":
        lines.append(B_SCOPE.replace("{Acc}", "Acc(B-P)").replace("{typing}", "owner-typed candidate strengthened"))
    lines += ["", "## C", "", "**Token:** `%s`" % dec["C"], ""]
    lines.append(C_TEXTS[dec["C"]].replace("{inst}", ", ".join(m["C"].get("flagged", [])) or "none")
                 .replace("{codes}", ", ".join(m["flags"]["controls_red"]["C"])).replace("{ca}", "is reported")
                 .replace("{cond}", "is reported as").replace("{b}", dec["B"]))
    lines += ["", "## Levels", "", "**Level:** %s" % dec["level"], ""]
    if dec["level"] != "none":
        lines.append(LEVEL1_TEXT)
    if dec["level"] == 3:
        lines.append(LEVEL3_TEXT + ".")
    lines += [OWNER_LEVELS, "", "## Representation ledger (REP-INV)", ""]
    for k, v in sorted(m["REP_INV"]["P"].items()):
        lines.append("- %s: %s" % (k, "invariant" if v == "invariant" else "changed: " + ", ".join(v)))
    lines.append("- reclassified as imported: %s" % (", ".join(m["REP_INV"]["reclassified"]) or "none"))
    lines += ["", "## What no outcome shows", ""] + ["- " + x for x in NO_OUTCOME]
    lines += ["", "## ADA", "", OWNER_STANDARD, "", COMMON_CLAUSE, ""]
    return "\n".join(lines) + "\n"


# ------------------------------------------------------------------------------------------------------------
# stress-check, replay
# ------------------------------------------------------------------------------------------------------------
def stress_check(path, pin):
    """A7: schema v2, every fragment certificate-verified, and (when a pin exists) sha256 equals the pin."""
    raw = read_bytes(path)
    try:
        s = json.loads(raw)
    except ValueError:
        return False, "unparseable"
    if s.get("schema") != "arp2-qc21-stress" or s.get("version") != 2:
        return False, "schema"
    frs = s.get("fragments")
    if not isinstance(frs, list) or not frs:
        return False, "fragments"
    for fr in frs:
        for k in ("verdict", "decided_by", "pivots", "max_bits", "work", "certificate_verified"):
            if k not in fr:
                return False, "field " + k
        if fr["certificate_verified"] is not True:
            return False, "unverified " + str(fr.get("name"))
    if not isinstance(s.get("W_fix"), int) or not isinstance(s.get("W_stress"), int):
        return False, "totals"
    h = sha256_bytes(raw)
    return (True if pin is None else h == pin), h


def replay_compare(fresh_bytes, committed_bytes):
    """B6: compares files only. The committed measurements carry S1's dispatch input, so the one field
    parameters.dispatch_sha is set aside on both sides before the byte comparison of canonical JSON."""
    try:
        a, b = json.loads(fresh_bytes), json.loads(committed_bytes)
    except ValueError:
        return False
    a.get("parameters", {}).pop("dispatch_sha", None)
    b.get("parameters", {}).pop("dispatch_sha", None)
    return canonical(a).encode() == canonical(b).encode()


# ------------------------------------------------------------------------------------------------------------
# check: T, G, R, B, W, DS, X, V, P
# ------------------------------------------------------------------------------------------------------------
def fenced(text, info):
    lines = text.split("\n")
    out, i = [], 0
    while i < len(lines):
        if lines[i] == "```" + info:
            j = i + 1
            while j < len(lines) and lines[j] != "```":
                j += 1
            out.append(lines[i + 1:j])
            i = j + 1
        else:
            i += 1
    return out


def pending_unbackticked(text):
    hits = []
    for n, line in enumerate(text.split("\n"), 1):
        parts = line.split("`")
        bare = "".join(parts[i] for i in range(0, len(parts), 2))
        if "PENDING" in bare:
            hits.append(n)
    return hits


def code_t(d, f):
    """T: the v3 control plane at F (via control T's frozen command) and the frozen blocks."""
    errs = []
    r = subprocess.run(["python3", "-I", "-S", "-c", "import sys,json;sys.path.insert(0,'tools');import v3_verifier as v;r=v.Repo('.');a=v.control_plane(r,sys.argv[1],sys.argv[2]);print(json.dumps({'rdir':(a[0] or b'').decode(),'round':a[1],'kind':a[2],'digest':v.governed_digest(a[3]) if isinstance(a[3],list) else None,'codes':a[5]},sort_keys=True))", a_ok(d), a_ok(f)], capture_output=True, text=True)
    if r.returncode != 0:
        return ["T: control T's command failed"]
    cp = json.loads(r.stdout)
    if cp["codes"]:
        errs.append("T: control-plane codes %s" % cp["codes"])
    if cp["round"] != ROUND or cp["kind"] != "non-sealing" or cp["rdir"] != RDIR:
        errs.append("T: round block")
    if cp["digest"] != GOVERNED_DIGEST:
        errs.append("T: governed digest %s" % cp["digest"])
    pre = git_show(f, PREREG)
    if pre is None:
        return errs + ["T: no preregistration at F"]
    t = pre.decode("utf-8")
    rb = fenced(t, "v3-round")
    gb = fenced(t, "v3-governed-paths")
    if len(rb) != 1 or [x for x in rb[0] if x.strip()] != ROUND_LINES:
        errs.append("T: round lines")
    if len(gb) != 1 or [x for x in gb[0] if x.strip()] != GOVERNED_LINES:
        errs.append("T: governed lines")
    if BRANCHES_LINE not in t.split("\n"):
        errs.append("T: branches line")
    return errs


def code_g(base, head, allowed):
    """G: the change from base to head touches only the allowed paths."""
    delta = git_delta(base, head)
    if delta is None:
        return ["G: unreadable delta"]
    return ["G: %s %s" % (st, p) for st, p in delta if p not in allowed]


def code_b(commit):
    errs = []
    for name, path, fn in (("qc21_check.py", CHECKER, static_checker), ("controls.py", CONTROLS, static_controls)):
        blob = git_blob(commit, path)
        if PINS[name] is not None and blob != PINS[name]:
            errs.append("B: blob %s" % name)
        src = git_show(commit, path)
        if src is None:
            errs.append("B: missing " + name)
            continue
        errs += ["B: %s: %s" % (name, e) for e in fn(src.decode("utf-8"))]
        if name == "qc21_check.py":
            text = src.decode("utf-8")
            errs += ["B: C-EXACT: " + e for e in c_exact(text)]
            errs += ["B: C-INDEP: " + e for e in c_indep(text)]
    ck, ct = git_show(commit, CHECKER), git_show(commit, CONTROLS)
    if ck is not None and ct is not None:
        errs += ["B: C-IFACE: " + e for e in c_iface(ck.decode("utf-8"), ct.decode("utf-8"))]
    return errs


def code_w(commit):
    wt = git_show(commit, WORKFLOW)
    dt = git_show(D_SHA, WORKFLOW)
    if wt is None or dt is None:
        return ["W: unreadable"]
    return [] if check_w(wt.decode("utf-8"), dt.decode("utf-8")) else ["W: verify.yml is not D's with the frozen splice"]


def code_ds():
    errs = []
    for path, blob in INPUTS.items():
        got = git_blob(D_SHA, path)
        if got is None or (blob is not None and not got.startswith(blob)):
            errs.append("DS: %s" % path)
    return errs


def check_mode(commit, f, stage):
    errs = []
    if stage is None:
        errs += code_t(D_SHA, f) + code_g(D_SHA, f, {PREREG}) + code_ds()
        pre = git_show(f, PREREG)
        if pre is not None:
            hits = pending_unbackticked(pre.decode("utf-8"))
            if hits:
                errs.append("P: unbackticked PENDING at lines %s" % hits[:20])
        if PINS["stress.json"] is None:
            errs.append("P: no stress pin")
        return errs
    errs += code_t(D_SHA, f)
    if stage == "S1":
        if git_parents(commit) != [f]:
            errs.append("T: S1 is not a single-parent child of F")
        errs += code_g(f, commit, {RDIR + x for x in S1_FILES} | {WORKFLOW})
        errs += code_b(commit) + code_w(commit)
    elif stage == "E":
        par = git_parents(commit)
        if par is None or len(par) != 1:
            errs.append("T: E is not a single-parent commit")
        else:
            errs += code_g(par[0], commit, {RDIR + x for x in E_FILES})
            errs += code_b(commit) + code_w(commit)
        mb = git_show(commit, MEAS)
        if mb is None:
            errs.append("R: no measurements at E")
        else:
            m = json.loads(mb)
            dec = decide(m)
            if "VOID" in dec:
                errs.append("X: %s" % dec["VOID"])
            conf = git_show(commit, RDIR + "evidence/confirmation-measurements.json")
            if conf is None or canonical(json.loads(conf).get("fixtures")) != canonical(m.get("fixtures")):
                errs.append("C-STATELESS: the fixtures section differs from the confirmation run's")
            note = git_show(commit, RDIR + "result.md")
            if note is not None:
                if s4_hits(note.decode("utf-8")):
                    errs.append("V: S4 %s" % s4_hits(note.decode("utf-8")))
            else:
                errs.append("R: no result.md")
    elif stage == "W":
        errs += code_g(f, commit, {RDIR + x for x in S1_FILES + E_FILES} | {WORKFLOW, RDIR + "evidence/void-run.json"})
    return errs


# ------------------------------------------------------------------------------------------------------------
# Runs, evidence, approvals (C.3): the run-classification functions. Pure rules over host records, and readers.
# ------------------------------------------------------------------------------------------------------------
def run_class_checker_bearing(jobs, tree_blobs, checker_blob):
    """(i) by name: a job named JOB_A or JOB_B, or a step named STEP_B4; (ii) by blob: the head_sha tree carries
    the pinned checker blob at any path. Conclusions are not consulted."""
    for j in jobs:
        if j.get("name") in (JOB_A, JOB_B):
            return True
        if any(s.get("name") == STEP_B4 for s in j.get("steps") or []):
            return True
    return checker_blob is not None and checker_blob in tree_blobs.values()


def run_class_job(jobs, name):
    m = [j for j in jobs if j.get("name") == name]
    return m[0] if m else None


def run_class_step(job, name):
    if job is None:
        return None
    m = [s for s in job.get("steps") or [] if s.get("name") == name]
    return m[0] if m else None


def run_class_absent_or_skipped(x):
    return x is None or x.get("conclusion") == "skipped"


def run_class_host_void(jobs):
    """C.6: an approved dispatch in which B4 never ran: job B absent, B4 absent, or B4 skipped."""
    jb = run_class_job(jobs, JOB_B)
    return jb is None or run_class_absent_or_skipped(run_class_step(jb, STEP_B4))


def run_class_binding_errors(entry, run, jobs, meas_dispatch_sha):
    """The approval entry bound to its run (re-anchored on the owner's quoted commit; E5) and the edited-comment
    rule (R10-B5). Fail-closed: a missing field is an error."""
    errs = []
    try:
        quoted = entry["quoted_words"]
        sha = run["head_sha"]
        if sha not in quoted or entry["stage"] not in quoted:
            errs.append("quoted words do not name the commit and the stage")
        if entry["approval_created_at"] >= run["created_at"]:
            errs.append("approval does not precede the run")
        if not (entry["approval_updated_at"] == entry["approval_created_at"]
                or entry["approval_updated_at"] < run["created_at"]):
            errs.append("approval comment edited after its run")
        if (entry["approval_author"], entry.get("author_association")) != OWNER:
            errs.append("approval author")
        if run.get("run_attempt") != 1 or entry["run_attempt"] != 1:
            errs.append("attempt")
        if run.get("event") != run_class_dispatch():
            errs.append("event")
        jb = run_class_job(jobs, JOB_B)
        b3 = run_class_step(jb, STEP_B3)
        if jb is None or b3 is None or b3.get("conclusion") != "success":
            errs.append("B3 not success")
        if meas_dispatch_sha != sha:
            errs.append("measurements' dispatch_sha")
    except (KeyError, TypeError):
        errs.append("entry incomplete")
    return errs


def run_class_rule(att, approved, gate_tests, recorded_commits, nondispatch_records, order_s1):
    """The rule (C.3): every checker-bearing attempt is (a) an approved entry's attempt 1, (b) a gate-test entry,
    (c) an attempt >= 2 of (a) or (b) whose job B is absent or skipped, or (d) a non-dispatch attempt at a
    recorded-branch commit satisfying the no-unapproved-F1 rule. Returns None (compliant) or a violation."""
    key = (att["run_id"], att["run_attempt"])
    is_disp = att["event"] == run_class_dispatch()
    approved_ids = {(e["run_id"], e["run_attempt"]) for e in approved}
    gate_ids = {e["run_id"] for e in gate_tests}
    if key in approved_ids and att["run_attempt"] == 1:
        return None
    if att["run_id"] in gate_ids and att["run_attempt"] == 1:
        if not run_class_absent_or_skipped(run_class_step(run_class_job(att["jobs"], JOB_B), STEP_B4)):
            return "gate-test run in which B4 ran"
        return None
    if att["run_attempt"] >= 2 and ((att["run_id"], 1) in approved_ids or att["run_id"] in gate_ids):
        if run_class_absent_or_skipped(run_class_job(att["jobs"], JOB_B)):
            return None
        return "re-run attempt with job B not skipped"
    if not is_disp and att["head_sha"] in recorded_commits:
        rec = nondispatch_records.get(key) or order_s1.get(key)
        if rec is None:
            return "no record (artifact missing and not in order-s1.json)"
        jb = run_class_job(att["jobs"], JOB_B)
        if not run_class_absent_or_skipped(jb) or not run_class_absent_or_skipped(run_class_step(jb, STEP_B4)):
            return "job B or B4 ran in a non-dispatch run"
        if rec.get("fixtures_mode") != "fixture":
            return "fixtures_mode is not fixture"
        return None
    return "unapproved checker-bearing attempt"


def run_class_slice_ok(pages):
    """total_count read from page 1 and equal on every page; listed count equals it and is below 1000."""
    if not pages:
        return False
    tc = pages[0].get("total_count")
    if any(p.get("total_count") != tc for p in pages):
        return False
    listed = sum(len(p.get("workflow_runs") or []) for p in pages)
    return listed == tc and tc < 1000


def run_class_activity_violations(entries):
    return [e for e in entries if e.get("activity_type") in ("force_push", "branch_deletion")]


def derive_run(run_id):
    """derive-run: the run, every attempt and its jobs (every page), and its artifacts' sha256 from the artifacts
    API (the digest field), as structured JSON. A failed read makes the capture failed (exit 1), never a pass."""
    ok, run = gh_get("run", str(run_id))
    if not ok:
        return None
    rec = {"run_id": run["id"], "head_sha": run["head_sha"], "event": run["event"], "created_at": run["created_at"],
           "run_attempt": run["run_attempt"], "head_branch": run.get("head_branch"), "attempts": []}
    for n in range(1, run["run_attempt"] + 1):
        ok, att = gh_get("attempt", str(run_id), str(n))
        if not ok:
            return None
        jobs, page = [], 1
        while True:
            ok, js = gh_get("jobs", str(run_id), str(n), str(page))
            if not ok:
                return None
            jobs += [{"name": j["name"], "conclusion": j.get("conclusion"),
                      "steps": [{"name": s["name"], "conclusion": s.get("conclusion"),
                                 "started_at": s.get("started_at"), "completed_at": s.get("completed_at")}
                                for s in j.get("steps") or []]} for j in js.get("jobs", [])]
            if len(jobs) >= js.get("total_count", 0) or not js.get("jobs"):
                break
            page += 1
        rec["attempts"].append({"run_attempt": n, "conclusion": att.get("conclusion"), "jobs": jobs,
                                "event": run["event"], "head_sha": run["head_sha"], "run_id": run["id"]})
    ok, arts = gh_get("artifacts", str(run_id))
    if not ok:
        return None
    rec["artifacts"] = [{"name": a["name"], "artifact_sha256": (a.get("digest") or "").replace("sha256:", ""),
                         "expired": a.get("expired")} for a in arts.get("artifacts", [])]
    return rec


def order_capture(t_repo, t0, now, branches):
    """order: the repository-wide enumeration (set (1) dispatches over [T_repo, now]; set (2) every other event over
    [T0, now]), every page, total_count checked per slice; the activity of each recorded branch. Returns the
    structured capture or None (failed capture, to be retried)."""
    cap = {"queries": [], "runs": {}, "activity": {}}
    for kind, a in (("runs-dispatch", t_repo), ("runs-all", t0)):
        pages, page = [], 1
        while True:
            ok, pg = gh_get(kind, a, now, str(page))
            if not ok:
                return None
            pages.append(pg)
            if not pg.get("workflow_runs") or sum(len(p["workflow_runs"]) for p in pages) >= pg.get("total_count", 0):
                break
            page += 1
        if not run_class_slice_ok(pages):
            return None
        cap["queries"].append({"kind": kind, "window": [a, now], "total_count": pages[0]["total_count"],
                               "listed": sum(len(p["workflow_runs"]) for p in pages)})
        for p in pages:
            for r in p["workflow_runs"]:
                if kind == "runs-all" and r["event"] == run_class_dispatch():
                    continue
                cap["runs"][str(r["id"])] = {"head_sha": r["head_sha"], "event": r["event"],
                                             "run_attempt": r["run_attempt"]}
    for b in branches:
        ents, page = [], 1
        while True:
            ok, pg = gh_get("activity", b, str(page))
            if not ok:
                return None
            if not pg:
                break
            ents += pg
            page += 1
        cap["activity"][b] = [{"activity_type": e.get("activity_type"), "after": e.get("after"),
                               "timestamp": e.get("timestamp")} for e in ents]
    return cap


def verdict_mode(meas, token_line, ratified_sha, order_sha, s1_run, e_run, capture_violations):
    """verdict: VERDICT <token> only when every condition holds; else VERDICT VOID (exit 1)."""
    errs = []
    if ratified_sha != order_sha:
        errs.append("designation of E does not ratify order.json's sha256")
    for lab, run in (("S1", s1_run), ("E", e_run)):
        att = run["attempts"][0] if run and run.get("attempts") else None
        if att is None or att["conclusion"] != "success":
            errs.append(lab + ": attempt 1 not success")
            continue
        for j in att["jobs"]:
            if j["conclusion"] != "success":
                errs.append(lab + ": job " + j["name"])
            for s in j["steps"]:
                if j["name"] in (JOB_A, JOB_B) and s["conclusion"] != "success":
                    errs.append(lab + ": step " + s["name"])
    if capture_violations:
        errs.append("capture violations: %s" % capture_violations)
    dec = decide(meas)
    if "VOID" in dec:
        errs.append("decide VOID")
    tok = "%s %s %s level %s" % (dec.get("P"), dec.get("B"), dec.get("C"), dec.get("level"))
    if token_line != tok:
        errs.append("the note's token line differs")
    return ("VERDICT " + tok) if not errs else "VERDICT VOID", errs


# ------------------------------------------------------------------------------------------------------------
# Self-test
# ------------------------------------------------------------------------------------------------------------
LOG = []


def ck(name, cond):
    LOG.append((name, bool(cond)))


K = "GITHUB_EVENT_NAME=x GITHUB_RUN_ATTEMPT=1 python3 -I q.py --event x"
BYP = {
    "BYP-1": "import subprocess\nsubprocess.run(['git','-c','alias.q=!x','q'])",
    "BYP-2": "import subprocess\nsubprocess.run(['gh','api','repos/o/r/actions/workflows/v/dispatches','--input','b'])",
    "BYP-3a": "import subprocess\nsubprocess.run(['gh','api','--method=POST','repos/o/r/x'])",
    "BYP-3b": "import subprocess\nsubprocess.run(['gh','api','-XPOST','repos/o/r/x'])",
    "BYP-4": "import subprocess\nsubprocess.run(['gh','api','graphql','--input','q.json'])",
    "BYP-5": "import os.path\nos.path.os.system('x')",
    "BYP-6a": "import subprocess\nsubprocess.os.system('x')",
    "BYP-6b": "import tempfile\ntempfile._os.system('x')",
    "BYP-7": "import sys\nsys.modules['os'].system('x')",
    "BYP-8": "import subprocess\ngetattr(subprocess, 'Po'+'pen')(['x'])",
    "BYP-9": "import subprocess as s\ns.Popen(['x'])",
    "BYP-10": "from subprocess import Popen\nPopen(['x'])",
    "BYP-11": "c = ().__class__.__base__.__subclasses__()",
    "BYP-12": "import subprocess\nopen('/site/z.pth','w').write('x')\nsubprocess.run(['python3','-I','-c','F','D','F'])",
    "BYP-13": "import subprocess\np = subprocess.run\np(['sh', '-c', %r])" % K,
    "BYP-14": "import subprocess\nlist(map(subprocess.run, [['sh', '-c', %r]]))" % K,
    "BYP-15": "o = open\no('/site/z.pth', 'w').write('import os')",
    "BYP-16": "import subprocess\nsubprocess.run(['git','show','--no-textconv','--no-ext-diff','-s','main'], cwd='v/x')",
    "BYP-17a": "import subprocess\nsubprocess.run(['git','show','--no-textconv','--no-ext-diff','--ext-diff','HEAD'])",
    "BYP-17b": "import subprocess\nsubprocess.run(['git','show','--no-textconv','--no-ext-diff','--textconv','HEAD'])",
    "BYP-18": "import subprocess\nsubprocess.run(['git','show','--no-textconv','--no-ext-diff',a_ok(x),'--end-of-options',a_ok(y)])",
    "pending_deployments": "import subprocess\nsubprocess.run(['gh','api','--method','POST','repos/amaybaum/incompleteness/actions/runs/1/pending_deployments'])",
    "template": "import subprocess\nsubprocess.run(['gh','api','--method','GET','repos/amaybaum/incompleteness/actions/workflows'])",
    "BYP-19": "import subprocess\nsubprocess.run(['git','cat-file','--filters','--end-of-options',a_ok(x)])",
    "BYP-20a": "a_ok = str\na_ok('x')",
    "BYP-20b": "w_path = str\nw_path('x')",
    "BYP-21": "help(1)",
    "BYP-23": "(a_ok := str)",
    "BYP-24": "match x:\n    case a_ok:\n        pass",
    "BYP-25": "try:\n    pass\nexcept E as w_path:\n    pass",
    "BYP-26": "class a_ok:\n    pass",
    "BYP-23r": "(root_check := str)",
    "w_path non-literal": "import tempfile\nopen(w_path(td, name), 'w')",
    "w_path slash": "import tempfile\nopen(w_path(td, 'a/b.pth'), 'w')",
    "import qc22_check": "import qc22_check\nqc22_check.main()",
    "computed path": "import subprocess\nsubprocess.run([x, 'show'])",
    "run-time list": "import subprocess\nsubprocess.run(argv)",
    "os.system": "import os\nos.system('x')",
    "gh -X POST": "import subprocess\nsubprocess.run(['gh','api','-X','POST','repos/o/r'])",
    "gh workflow run": "import subprocess\nsubprocess.run(['gh','workflow','run','verify.yml'])",
    "git subcommand": "import subprocess\nsubprocess.run(['git','config','--list'])",
    "git push": "import subprocess\nsubprocess.run(['git','push'])",
}


def selftest_static():
    own = read_text(CONTROLS)
    chk = read_text(CHECKER)
    ck("control B on controls.py", static_controls(own) == [])
    if static_controls(own):
        ck("control B on controls.py details: %s" % static_controls(own)[:5], False)
    ck("control B on qc21_check.py", static_checker(chk) == [])
    if static_checker(chk):
        ck("control B on qc21_check.py details: %s" % static_checker(chk)[:5], False)
    ck("C-EXACT on qc21_check.py", c_exact(chk) == [])
    ck("C-INDEP on qc21_check.py", c_indep(chk) == [])
    ck("C-IFACE static", c_iface(chk, own) == [])
    helpers = "\ndef a_ok(x):\n    return x\n\ndef w_path(t, n):\n    return n\n\ndef root_check():\n    return 0\n"
    for name, snip in BYP.items():
        ck("control B fails " + name, static_controls(snip + helpers) != [])
    ck("control B passes a clean snippet", static_controls(
        "import subprocess\nsubprocess.run(['git', 'rev-parse', '--verify', '--end-of-options', a_ok(x)])" + helpers) == [])
    muts = {
        "a second workflow_dispatch": chk.replace("ROUND_REF = ", "X_EV = \"workflow_" + "dispatch\"\nROUND_REF = ", 1),
        "alias in a self-test": chk.replace("def t_misc():\n", "def t_misc():\n    b = s_build_p\n", 1),
        "second self-test referencing the gated entry": chk.replace("def t_misc():\n",
                                                                    "def t_misc():\n    x = s_decisive\n", 1),
        "t_builder_refuses extra statement": chk.replace("def t_builder_refuses():\n",
                                                         "def t_builder_refuses():\n    pass\n", 1),
        "globals()[...]": chk.replace("def t_misc():\n", "def t_misc():\n    globals()['s_build_p']()\n", 1),
        "getattr(...)": chk.replace("def t_misc():\n", "def t_misc():\n    getattr(sys, 'x')\n", 1),
        "dunder walk": chk.replace("def t_misc():\n", "def t_misc():\n    ().__class__\n", 1),
        "third os site": chk.replace("def t_misc():\n", "def t_misc():\n    s_mode([], os.environ)\n", 1),
        "builder without refusal": chk.replace('    s_refusal("s_build_c")\n', "", 1),
    }
    for name, src in muts.items():
        ck("name rules fail: " + name, src != chk and static_checker(src) != [])
    ck("M-INDEP direct call", c_indep(chk.replace("def v_rank(rows):\n", "def v_rank(rows):\n    s_rank(rows)\n", 1)) != [])
    ck("M-INDEP default argument", c_indep(chk.replace("def v_rank(rows):", "def v_rank(rows, x=s_decide):", 1)) != [])
    ck("M-INDEP nested lambda", c_indep(chk.replace("def v_rank(rows):\n",
                                                    "def v_rank(rows):\n    f = lambda: s_rank(rows)\n", 1)) != [])
    ck("C-EXACT float literal", c_exact(chk.replace("CAP_D = 16", "CAP_D = 16.0", 1)) != [])
    ck("C-EXACT '/' outside the helper", c_exact(chk.replace("def fstr(x):\n", "def fstr(x):\n    y = 1 / 2\n", 1)) != [])
    ck("C-IFACE mutation (carrier slot into the screen input)",
       c_iface(chk.replace('if r["kept"] and r["port"] == 0) / tot', 'if r["kept"] and r["carrier"][0] == 0) / tot')
               .replace('r["kept"] and r["port"] == 0), tot)', 'r["kept"] and r["carrier"][0] == 0), tot)', 1), own) != [])
    ck("C-IFACE mutation (decide-p reads the sham)", c_iface(chk, own.replace(
        'def decide_p(rec):\n', 'def decide_p(rec):\n    _ = rec.get("shk")\n', 1)) != [])


def selftest_git():
    root_check()
    head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    ck("git rev-parse HEAD gives 40 hex", re.fullmatch(r"[0-9a-f]{40}", head) is not None)
    ck("git rev-parse --verify --end-of-options (output is the commit)", git_commit(head) == head)
    ck("git cat-file -e", git_has(head))
    blobs = git_tree_blobs(head)
    ck("git ls-tree -r (output lists the checker)", blobs is not None and CHECKER in blobs)
    par = git_parents(head)
    ck("git rev-list --parents (output parses)", par is not None)
    ck("git merge-base --is-ancestor", git_is_ancestor(head, head))
    ck("git diff-tree (output empty for X..X)", git_delta(head, head) == [])
    ck("git show (output is the file)", git_show(head, CHECKER) is not None)
    ck("git rev-parse blob", git_blob(head, CHECKER) == (blobs or {}).get(CHECKER))
    for bad in ("--output=x", "-x", "a=b", "../x", "x y", "", "a/../b"):
        try:
            a_ok(bad)
            ck("a_ok raises on " + repr(bad), False)
        except Refused:
            ck("a_ok raises on " + repr(bad), True)
    for good in (head, "123", "2026-11-09T08:00:00Z", RDIR + "x.json", head + ":" + CHECKER):
        ck("a_ok accepts " + good[:20], a_ok(good) == good)


def selftest_w():
    dt = git_show(D_SHA, WORKFLOW)
    if dt is None:
        ck("W: D's verify.yml readable", False)
        return
    d = dt.decode("utf-8")
    sp = splice(d)
    ck("W: the splice applies to D's verify.yml", sp is not None)
    if sp is None:
        return
    ck("W: the spliced file passes", check_w(sp, d))
    removals = {
        "event key (B4)": ("(github.event_name == 'workflow_dispatch' && github.run_attempt == '1' && " + REF_KEY,
                           "(github.run_attempt == '1' && " + REF_KEY),
        "attempt key (B6)": ("github.run_attempt == '1' && " + REF_KEY + " && " + RECEIPT_KEY + ") }}",
                             REF_KEY + " && " + RECEIPT_KEY + ") }}"),
        "ref key (B4/B6)": (" && " + REF_KEY, ""),
        "receipt key (B4/B6)": (" && " + RECEIPT_KEY + ")", ")"),
        "job B if": ("    if: " + JOB_B_IF + "\n", ""),
        "job B if: decisive input": (" && inputs.arp2qc21_decisive == true", ""),
        "B3": ("        run: " + B3_RUN + "\n", "        run: 'true'\n"),
        "B3 ref key": (' && test "$GITHUB_REF" = refs/heads/research/arp2-qc21-20261108', ""),
        "A3 literal": (" --event fixture >", " --event \"$X\" >"),
        "A10 marker": ("      - name: " + STEP_A10 + "\n", "      - name: ARP-2-QC21 other\n"),
    }
    for name, (old, new) in removals.items():
        mut = sp.replace(old, new, 1)
        ck("W fails without " + name, mut != sp and not check_w(mut, d))


def synthetic_meas(**over):
    def arm(v, dd, k=None):
        return {"V": v, "D": dd, "K": k or [["1", "0"], ["0", "1"]], "NONABS": True, "SPI": True,
                "eraser": {"cell0.slot0": {"0": "1", "1": "1"}, "unsorted": "0"}}
    unif = [["1/2", "1/2"], ["1/2", "1/2"]]
    arms = {"off": arm("1", "0"), "(w,0)": arm("0", "1", unif), "(0,w')": arm("1", "0"), "(w,w')": arm("0", "0", unif),
            "(w,1)": arm("0", "1", unif), "(1,w')": arm("1", "0")}
    m = {"schema": "arp2-qc21-measurements", "version": 1, "mode": "decisive", "complete": True,
         "parameters": {"dispatch_sha": "0" * 40},
         "P": {"arms": arms, "decide_p_inputs": {"adm": sorted(arms), "on": "(w,0)"},
               "ATTR": {"value": "not attributable"}, "ab_p": {"existence_case": "both succeed",
                                                               "universality_case": "A fails and B succeeds"},
               "ablate_p": {}},
         "P_controls": {}, "REP_INV": {"reclassified": [], "P": {}},
         "B": {"fragments": [{"name": "B-P", "role": "B-P", "lp": "infeasible", "verified": True,
                              "lp_reads_equal_acc": True}]},
         "C": {"instances": [], "flagged": []}, "fixtures": {}, "controls": {}, "budget": {},
         "flags": {"P": "P-COMPLEMENTARITY", "B": "B-CONTEXTUAL", "C": "C-SURVIVAL", "levels": {"level": 2},
                   "controls_red": {"P": [], "B": [], "C": []}}}
    for k, v in over.items():
        m[k] = v
    return m


def selftest_decide():
    m = synthetic_meas()
    dec = decide(m)
    ck("decide: tokens and agreement", dec.get("P") == "P-COMPLEMENTARITY" and dec.get("B") == "B-CONTEXTUAL"
       and dec.get("C") == "C-SURVIVAL" and dec.get("level") == 2 and dec.get("flags_agree"))
    for cond in ("mode", "complete", "placeholder"):
        mm = synthetic_meas()
        if cond == "mode":
            mm["mode"] = "fixture"
        elif cond == "complete":
            mm["complete"] = False
        else:
            mm["B"]["fragments"][0]["lp"] = "placeholder"
        ck("M-MODE VOID on " + cond, "VOID" in decide(mm))
    mm = synthetic_meas()
    mm["flags"]["P"] = "P-NO-RECORD"
    ck("X: disagreeing flags give VOID", "VOID" in decide(mm))
    ck("decide: schema error VOID", "VOID" in decide({"schema": "x"}))
    arms = synthetic_meas()["P"]["arms"]
    rec = {"adm": sorted(arms), "arms": arms, "off": "off", "on": "(w,0)", "controls_red": []}
    ck("decide-p COMPLEMENTARITY", decide_p(rec)[0] == "P-COMPLEMENTARITY")
    r2 = json.loads(canonical(rec))
    r2["arms"]["(w,1)"]["V"] = "1"
    ck("decide-p RECORD-WITHOUT-SUPPRESSION", decide_p(r2)[0] == "P-RECORD-WITHOUT-SUPPRESSION")
    r2 = json.loads(canonical(rec))
    r2["arms"]["(w,0)"]["D"] = "0"
    ck("decide-p NO-RECORD", decide_p(r2)[0] == "P-NO-RECORD")
    r2 = json.loads(canonical(rec))
    r2["arms"]["off"]["V"] = "0"
    ck("decide-p NO-FRINGES", decide_p(r2)[0] == "P-NO-FRINGES")
    r2 = json.loads(canonical(rec))
    r2["arms"]["off"]["SPI"] = False
    ck("decide-p VOID (SPI)", decide_p(r2)[0] == "P-VOID")
    ck("decide-p VOID (control red)", decide_p(dict(rec, controls_red=["PL-SPI"]))[0] == "P-VOID")
    ck("decide-b VOID (out_of_scope)", decide_b({"controls_red": [], "fragments": [
        {"name": "x", "role": "A-of-B", "lp": "out_of_scope", "verified": False}]})[0] == "B-VOID")
    ck("decide-b IMITABLE", decide_b({"controls_red": [], "fragments": [
        {"name": "x", "role": "B-P", "lp": "feasible", "verified": True, "lp_reads_equal_acc": True}]})[0]
       == "B-CLASSICALLY-IMITABLE")
    t = {"6": True, "12": True}
    fl = {"6": False, "12": False}
    inst = {"HC": t, "CONS": t, "VAL": t, "WOCT": fl, "WCL": True, "ABL": True, "EMB": True}
    base = {"controls_red": [], "complete": True, "flags_agree": True}
    ck("decide-c EXPOSURE", decide_c(dict(base, instances=[inst]))[0] == "C-EXPOSURE")
    ck("decide-c SIZE-DEPENDENT", decide_c(dict(base, instances=[dict(inst, CONS={"6": True, "12": False})]))[0]
       == "C-SIZE-DEPENDENT")
    ck("decide-c NONSTABILIZER", decide_c(dict(base, instances=[dict(inst, WCL=False, WOCT=t)]))[0] == "C-NONSTABILIZER")
    ck("decide-c SURVIVAL", decide_c(dict(base, instances=[dict(inst, WCL=False)]))[0] == "C-SURVIVAL")
    ck("decide-c VOID", decide_c(dict(base, controls_red=["C-DET"], instances=[]))[0] == "C-VOID")
    ck("levels: representation rule", decide_levels("P-COMPLEMENTARITY", True, True, True, "C-EXPOSURE",
                                                    ["L-PATH"]) == "none")
    ck("levels: L-UPRIME withholds 3", decide_levels("P-COMPLEMENTARITY", True, True, True, "C-EXPOSURE",
                                                     ["L-UPRIME"]) == 2)
    ck("ATTR three values", attr_value({"V": "1"}, {"V": "0", "D": "1", "K": [1]}, {"V": "1", "D": "0", "K": [1]})
       == "attributable to which-path recording" and attr_value({"V": "1"}, {"V": "0", "D": "1", "K": [1]},
                                                              {"V": "0", "D": "0", "K": [1]}) == "not attributable"
       and attr_value({"V": "1"}, {"V": "0", "D": "1", "K": [1]}, {"V": "0", "D": "1", "K": [1]}) == "undefined")
    note = make_note(m, D_SHA, "f" * 40, "1" * 40, "e" * 40)
    ck("note: no S4 hit", s4_hits(note) == [])
    ck("note: the freeze disclosure leads", note.split("\n")[2] == FREEZE_DISCLOSURE)
    ck("note: Level-1 sentence printed", LEVEL1_TEXT in note)
    ck("S4 catches a planted phrase", s4_hits(note + " This is caused by recording.") != [])
    ck("note: VOID text for a fixture record", "**Token:** `VOID`" in make_note(synthetic_meas(mode="fixture"),
                                                                               D_SHA, "f" * 40, "1" * 40, "e" * 40))


def selftest_files():
    with tempfile.TemporaryDirectory() as td:
        good = {"schema": "arp2-qc21-stress", "version": 2, "W_fix": 1, "W_stress": 2,
                "fragments": [{"name": "SF-1", "verdict": "feasible", "decided_by": 2, "pivots": 0, "max_bits": 0,
                               "work": 0, "certificate_verified": True}]}
        with open(w_path(td, "stress.json"), "w") as fh:
            fh.write(canonical(good))
        ok, h = stress_check(w_path(td, "stress.json"), None)
        ck("stress-check records without a pin", ok)
        ok2, _ = stress_check(w_path(td, "stress.json"), h)
        ok3, _ = stress_check(w_path(td, "stress.json"), "0" * 64)
        ck("stress-check compares against the pin", ok2 and not ok3)
        bad = dict(good)
        bad["fragments"] = [dict(good["fragments"][0], certificate_verified=False)]
        with open(w_path(td, "stress-bad.json"), "w") as fh:
            fh.write(canonical(bad))
        ck("stress-check rejects an unverified fragment", not stress_check(w_path(td, "stress-bad.json"), None)[0])
    a = canonical(synthetic_meas()).encode()
    b = canonical(synthetic_meas(parameters={"dispatch_sha": "1" * 40})).encode()
    c = canonical(synthetic_meas(complete=False)).encode()
    ck("replay: equal up to dispatch_sha", replay_compare(a, b))
    ck("replay: a change is a mismatch", not replay_compare(a, c))


def selftest_runs():
    jobs_ok = [{"name": JOB_A, "conclusion": "success", "steps": []},
               {"name": JOB_B, "conclusion": "success", "steps": [{"name": STEP_B3, "conclusion": "success"},
                                                                 {"name": STEP_B4, "conclusion": "success"}]}]
    jobs_skip = [{"name": JOB_A, "conclusion": "success", "steps": []},
                 {"name": JOB_B, "conclusion": "skipped", "steps": []}]
    ck("checker-bearing by name", run_class_checker_bearing(jobs_skip, {}, None))
    ck("checker-bearing by blob", run_class_checker_bearing([], {"x/qc21_check.py": "b" * 40}, "b" * 40))
    ck("not checker-bearing", not run_class_checker_bearing([{"name": "other", "steps": []}], {"a": "c"}, "b" * 40))
    ck("host VOID: job B absent", run_class_host_void(jobs_skip[:1]))
    ck("host VOID: B4 skipped", run_class_host_void([{"name": JOB_B, "steps": [{"name": STEP_B4,
                                                                                "conclusion": "skipped"}]}]))
    ck("not host VOID", not run_class_host_void(jobs_ok))
    run = {"head_sha": "a" * 40, "created_at": "2026-11-10T10:00:00Z", "run_attempt": 1, "event": run_class_dispatch()}
    entry = {"quoted_words": "approve S1 at " + "a" * 40, "stage": "S1", "approval_created_at": "2026-11-10T09:00:00Z",
             "approval_updated_at": "2026-11-10T09:00:00Z", "approval_author": "amaybaum",
             "author_association": "OWNER", "run_attempt": 1}
    ck("binding holds", run_class_binding_errors(entry, run, jobs_ok, "a" * 40) == [])
    ck("binding: edited after the run", run_class_binding_errors(
        dict(entry, approval_updated_at="2026-11-10T11:00:00Z"), run, jobs_ok, "a" * 40) != [])
    ck("binding: comment after the run", run_class_binding_errors(
        dict(entry, approval_created_at="2026-11-10T11:00:00Z", approval_updated_at="2026-11-10T11:00:00Z"),
        run, jobs_ok, "a" * 40) != [])
    ck("binding: other commit quoted", run_class_binding_errors(dict(entry, quoted_words="S1 " + "b" * 40), run,
                                                                jobs_ok, "a" * 40) != [])
    ck("binding: missing field fails closed", run_class_binding_errors({}, run, jobs_ok, "a" * 40) != [])
    att = lambda rid, n, ev, sha, jobs: {"run_id": rid, "run_attempt": n, "event": ev, "head_sha": sha, "jobs": jobs}
    appr = [{"run_id": 1, "run_attempt": 1}]
    gates = [{"run_id": 2}]
    rec_commits = {"c" * 40}
    nd = {(3, 1): {"fixtures_mode": "fixture"}}
    disp = run_class_dispatch()
    ck("rule (a)", run_class_rule(att(1, 1, disp, "a" * 40, jobs_ok), appr, gates, rec_commits, nd, {}) is None)
    ck("rule (b)", run_class_rule(att(2, 1, disp, "a" * 40, jobs_skip), appr, gates, rec_commits, nd, {}) is None)
    ck("rule (b): B4 ran in a gate test", run_class_rule(att(2, 1, disp, "a" * 40, jobs_ok), appr, gates,
                                                         rec_commits, nd, {}) is not None)
    ck("rule (c)", run_class_rule(att(1, 2, disp, "a" * 40, jobs_skip), appr, gates, rec_commits, nd, {}) is None)
    ck("rule (c): re-run with job B", run_class_rule(att(1, 2, disp, "a" * 40, jobs_ok), appr, gates, rec_commits,
                                                     nd, {}) is not None)
    ck("rule (d)", run_class_rule(att(3, 1, "pull_request", "c" * 40, jobs_skip), appr, gates, rec_commits, nd,
                                  {}) is None)
    ck("rule (d): artifact missing, not in order-s1", run_class_rule(att(4, 1, "push", "c" * 40, jobs_skip), appr,
                                                                     gates, rec_commits, nd, {}) is not None)
    ck("rule (d): covered by order-s1", run_class_rule(att(4, 1, "push", "c" * 40, jobs_skip), appr, gates,
                                                       rec_commits, nd, {(4, 1): {"fixtures_mode": "fixture"}}) is None)
    ck("unapproved dispatch is a violation", run_class_rule(att(5, 1, disp, "a" * 40, jobs_ok), appr, gates,
                                                            rec_commits, nd, {}) is not None)
    ck("commit outside the recorded branches", run_class_rule(att(6, 1, "push", "d" * 40, jobs_skip), appr,
                                                              gates, rec_commits, nd, {}) is not None)
    ck("slice ok", run_class_slice_ok([{"total_count": 2, "workflow_runs": [1]}, {"total_count": 2,
                                                                                 "workflow_runs": [2]}]))
    ck("slice: total_count mismatch fails", not run_class_slice_ok([{"total_count": 2, "workflow_runs": [1]},
                                                                    {"total_count": 3, "workflow_runs": [2]}]))
    ck("slice: listed count short fails", not run_class_slice_ok([{"total_count": 3, "workflow_runs": [1]}]))
    ck("activity: force_push is a violation", run_class_activity_violations([{"activity_type": "force_push"}]) != [])


def self_test():
    del LOG[:]
    selftest_git()
    selftest_static()
    selftest_w()
    selftest_decide()
    selftest_files()
    selftest_runs()
    bad = [n for n, okv in LOG if not okv]
    for n, okv in LOG:
        sys.stdout.write("%s %s\n" % ("PASS" if okv else "FAIL", n))
    sys.stdout.write("%d checks, %d failed\n" % (len(LOG), len(bad)))
    return 0 if not bad else 1


def main(argv):
    try:
        root_check()
    except Refused:
        sys.stderr.write("refused: run at the top of the repository's work tree\n")
        return 2
    if len(argv) < 2:
        sys.stderr.write("usage: controls.py <mode> ...\n")
        return 2
    mode = argv[1]
    if mode == "--self-test":
        return self_test()
    if mode == "stress-check":
        ok, info = stress_check(argv[2], PINS["stress.json"])
        sys.stdout.write(("recorded (no pin yet): " if PINS["stress.json"] is None else "sha256: ") + info + "\n")
        return 0 if ok else 1
    if mode == "replay":
        if not os.path.isfile(MEAS):
            sys.stdout.write("no committed measurements (stage S1): nothing to compare\n")
            return 0
        return 0 if replay_compare(read_bytes(argv[2]), read_bytes(MEAS)) else 1
    if mode == "decide":
        m = json.loads(read_bytes(argv[2] if len(argv) > 2 else MEAS))
        out = decide(m)
        sys.stdout.write(canonical(out))
        return 1 if "VOID" in out else 0
    if mode == "note":
        m = json.loads(read_bytes(argv[2]))
        sys.stdout.write(make_note(m, D_SHA, a_ok(argv[3]), a_ok(argv[4]), a_ok(argv[5])))
        return 0
    if mode == "check":
        commit = a_ok(argv[2])
        f = a_ok(argv[argv.index("--freeze") + 1]) if "--freeze" in argv else None
        stage = argv[argv.index("--stage") + 1] if "--stage" in argv else None
        if f is None or stage not in (None, "S1", "E", "W"):
            return 2
        errs = check_mode(commit, f, stage)
        for e in errs:
            sys.stdout.write(e + "\n")
        sys.stdout.write("CHECK %s\n" % ("PASS" if not errs else "FAIL"))
        return 0 if not errs else 1
    if mode == "derive-run":
        rec = derive_run(a_ok(argv[2]))
        if rec is None:
            sys.stdout.write("capture failed\n")
            return 1
        sys.stdout.write(canonical(rec))
        return 0
    if mode in ("order", "verdict"):
        sys.stdout.write("%s: the capture inputs (T_repo, T0, the approval entries, the gate-test entries, the "
                         "recorded branches' commits) are PENDING until the round PR is opened\n" % mode)
        return 1
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
