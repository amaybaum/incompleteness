#!/usr/bin/env python3
"""controls.py -- the controls of native round ARP-2-QC21 (Q-C2-1). Preregistration r15, Appendix C.5; approved implementation under #1169 c.6778994857.

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
import io
import json
import os.path
import re
import subprocess
import sys
import tempfile
import zipfile

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
T0 = None  # Must be fixed from D main activity before F.
RECORDED_BRANCHES = (ROUND_BRANCH, DEV_BRANCH)  # Add design/confirmation/gate branches before F.
HOST_CALLS = 0
S_MAX_FLOOR = 100000
JOB_A = "Numerical probes / ARP-2-QC21 fixtures and stress"
JOB_B = "Numerical probes / ARP-2-QC21 exact decision (gated)"
STEP_B4 = "ARP-2-QC21 exact decision"
STEP_B3 = "ARP-2-QC21 approved commit and receipt"
STEP_B6 = "ARP-2-QC21 replay against the committed measurements"
STEP_A3 = "ARP-2-QC21 fixture decision"
STEP_A3B = "ARP-2-QC21 fixture output is fixture mode"
STEP_A7 = "ARP-2-QC21 stress output equals the pinned sha256"
STEP_A10 = "ARP-2-QC21 receipt absent"
GOVERNED_DIGEST = "1d195f938f5467d1549f7755bcafce2109abbfbcb57a7ff2243fa09a67e9982e"
ROUND_LINES = ["round ARP-2-QC21", "kind non-sealing", "record-directory " + RDIR]
GOVERNED_LINES = ["record AM " + RDIR, "record AM " + RECEIPT, "execution M " + WORKFLOW]

# Pin-table shape only. Values are read from the frozen preregistration, never embedded into this script.
PINS = {"qc21_check.py": None, "controls.py": None, "stress.json": None, "design-run.json": None,
        "gate-tests.json": None, "confirmation-run.json": None}
# Inputs at D (DS): path -> blob at D.
INPUTS = {
    "verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md": "51c24aeb7b42a915b8942462435fd9fe129861de",
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
    "tools/v3_verifier.py": "681c673734427cb9f316feee09b7c5ffba348004",
    "papers/Substratum.md": "e5c6f217fe689b7d25afb105feb4dad272f929cc",
    "verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md": "fb21999b0d45750a465dda742589f0af11575326",
    "verification/programmes/oi-qm/reconstruction/quarter-phase-feedback-20261107/RESULT.md": "a00b3b7f28992fd2c0010836d50e7c89ab158088",
    "verification/programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md": "9352d9da7da6a55a52e6ada235034219638b34d2",
    "verification/programmes/oi-qm/reconstruction/minacc-1-20261108/RESULT.md": "5adf76ebc8afa95cc51f45fb84c909b13876516c",
}
REQUIRED_SOURCE_INPUTS = {"RCH": {"path": None, "blob": None}, "DSN": {"path": None, "blob": None}}
S1_FILES = ("qc21_check.py", "controls.py", "evidence/design-run.json", "evidence/f-run/results.json",
            "evidence/confirmation-run.json", "evidence/confirmation-measurements.json", "evidence/gate-tests.json", "evidence/stress.json",
            "evidence/cone_k1_certificate.json", "evidence/cone_window_K2_certificate.json")
# r12a: the cone certificates, copied into the record directory at S1 and pinned by sha256.
STAB_CERTS = {"evidence/cone_k1_certificate.json":
              "e67199472530e6753eed86e991636a4fadb930b2b9c56e0456ec6b884cfeb644",
              "evidence/cone_window_K2_certificate.json":
              "f24a68d902a423018d15c4d92440970e5f17b202cc8b8ea3407ad11269e6ebaf"}
R12_STAB = True    # copied STAB certificates are required from the design stage onward
E_FILES = ("evidence/measurements.json", "evidence/s1-run/results.json", "evidence/order.json",
           "evidence/order-s1.json", "evidence/approvals.json", "result.md")

CHECKER_IMPORTS = {"fractions", "itertools", "json", "os", "sys"}
CONTROLS_IMPORTS = {"ast", "fractions", "hashlib", "io", "zipfile", "json", "os.path", "re", "subprocess", "sys", "tempfile"}
MOD_ATTRS = {"subprocess": {"run", "PIPE"}, "os.path": {"join", "isfile"}, "json": {"loads", "dumps"},
             "hashlib": {"sha256"}, "io": {"BytesIO"}, "zipfile": {"ZipFile"}, "re": {"fullmatch"}, "sys": {"argv", "exit", "stdout", "stderr"},
             "fractions": {"Fraction"}, "tempfile": {"TemporaryDirectory"}, "ast": None}
BANNED = {"getattr", "setattr", "delattr", "globals", "locals", "vars", "breakpoint", "help", "exec", "eval",
          "compile", "__import__"}
GIT_SUBCOMMANDS = {"rev-parse", "cat-file", "ls-tree", "rev-list", "merge-base", "diff-tree", "show"}
GIT_BAD = ("-c", "--config-env", "--exec-path", "-C", "--git-dir", "--work-tree", "--upload-pack", "--output",
           "--ext-diff", "--textconv", "--filters")
GH_EXTRA = {"--paginate", "-H", "Accept: application/vnd.github+json"}
GH_TEMPLATES = ("actions/runs?", "actions/runs/{DEC}", "actions/runs/{DEC}/attempts/{DEC}",
                "actions/runs/{DEC}/attempts/{DEC}/jobs?per_page=100", "actions/runs/{DEC}/artifacts",
                "actions/artifacts/{DEC}/zip", "issues/comments/{DEC}",
                "git/trees/{HEX40}?recursive=1", "git/trees/{HEX40}", "activity?ref=refs/heads/", "")
HELPERS = ("a_ok", "w_path", "root_check")
_C = r"(?!\.\.?(?:/|$))[A-Za-z0-9_.][A-Za-z0-9_.-]*"
A_OK_PATTERNS = (r"[0-9a-f]{40}", r"[1-9][0-9]{0,19}", r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z",
                 _C + r"(?:/" + _C + r")*", r"[0-9a-f]{40}:" + _C + r"(?:/" + _C + r")*")
T_CODE = ("import sys,json;sys.path.insert(0,'tools');import v3_verifier as v;r=v.Repo('.');"
          "a=v.control_plane(r,sys.argv[1],sys.argv[2]);"
          "print(json.dumps({'rdir':(a[0] or b'').decode(),'round':a[1],'kind':a[2],"
          "'digest':v.governed_digest(a[3]) if isinstance(a[3],list) else None,'codes':a[5]},sort_keys=True))")


class CaptureFailed(Exception):
    """Host capture is incomplete; retry without substituting an empty result."""


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
    global HOST_CALLS
    HOST_CALLS += 1
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
                            f"repos/amaybaum/incompleteness/actions/runs/{a_ok(vals[0])}/artifacts?per_page=100&page={a_ok(vals[1])}",
                            "-H", "Accept: application/vnd.github+json"], capture_output=True, text=True)
    elif path_kind == "artifact-zip":
        r = subprocess.run(["gh", "api", "--method", "GET",
                            f"repos/amaybaum/incompleteness/actions/artifacts/{a_ok(vals[0])}/zip",
                            "-H", "Accept: application/vnd.github+json"], capture_output=True)
    elif path_kind == "comment":
        r = subprocess.run(["gh", "api", "--method", "GET",
                            f"repos/amaybaum/incompleteness/issues/comments/{a_ok(vals[0])}",
                            "-H", "Accept: application/vnd.github+json"], capture_output=True, text=True)
    elif path_kind == "runs-dispatch":
        r = subprocess.run(["gh", "api", "--method", "GET",
                            f"repos/amaybaum/incompleteness/actions/runs?event={a_ok(run_class_dispatch())}&created="
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
    if path_kind == "artifact-zip":
        return True, r.stdout
    try:
        return True, json.loads(r.stdout)
    except (ValueError, TypeError):
        return False, "unparseable host response"


# ------------------------------------------------------------------------------------------------------------
# The frozen workflow splice (control W): verify.yml at the design run, 6', S1 and E equals D's verify.yml with
# exactly this splice.
# ------------------------------------------------------------------------------------------------------------
REF_KEY = "github.ref == 'refs/heads/research/arp2-qc21-20261108'"
RECEIPT_KEY = "hashFiles('verification/receipts/ARP-2-QC21.json') == ''"
SPLICE_B4_EXPR = ("${{ (github.event_name == 'workflow_dispatch' && github.run_attempt == '1' && " + REF_KEY + " && "
           + RECEIPT_KEY + ") && 'workflow_dispatch' || 'closed-or-other' }}")
SPLICE_B6_IF = ("${{ (github.event_name == 'workflow_dispatch' && github.run_attempt == '1' && " + REF_KEY + " && "
         + RECEIPT_KEY + ") }}")
SPLICE_JOB_B_IF = "${{ github.event_name == 'workflow_dispatch' && github.run_attempt == '1' && inputs.arp2qc21_decisive == true }}"
B3_RUN = ('test "$GITHUB_SHA" = "$ARP2QC21_SHA" && test "$GITHUB_REF" = refs/heads/research/arp2-qc21-20261108 '
          '&& test ! -e verification/receipts/ARP-2-QC21.json')
PY = "python3 -I -S -B "
SPLICE_ON_ANCHOR = "  workflow_dispatch:\n\njobs:\n"
SPLICE_ON_SPLICE = ("  workflow_dispatch:\n"
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
            "          name: arp2-qc21-" + {"fixtures.json": "fixtures", "stress.json": "stress", "measurements.json": "measurements"}[fname] + "\n"
            "          path: ${{ runner.temp }}/arp2-qc21/" + fname + "\n"
            "          if-no-files-found: error\n"
            "          retention-days: 90\n\n")


SPLICE_FROZEN_JOBS = (
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
    "          mkdir -p \"$RUNNER_TEMP/arp2-qc21\" && " + PY + CHECKER + " --event fixture > \"$RUNNER_TEMP/arp2-qc21/fixtures.json\"\n\n"
    "      - name: " + STEP_A3B + "\n"
    "        if: ${{ always() }}\n"
    "        run: " + PY + CONTROLS + " fixture-mode-check \"$RUNNER_TEMP/arp2-qc21/fixtures.json\"\n\n"
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
    "    if: " + SPLICE_JOB_B_IF + "\n"
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
    "          mkdir -p \"$RUNNER_TEMP/arp2-qc21\" && " + PY + CHECKER + " --event \"" + SPLICE_B4_EXPR + "\" --dispatch-sha \"$ARP2QC21_SHA\" > "
    "\"$RUNNER_TEMP/arp2-qc21/measurements.json\"\n\n"
    + upload("the measurements", "measurements.json") +
    "      - name: " + STEP_B6 + "\n"
    "        if: " + SPLICE_B6_IF + "\n"
    "        run: " + PY + CONTROLS + " replay \"$RUNNER_TEMP/arp2-qc21/measurements.json\"\n\n")
SPLICE_AGG_EDITS = (
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
    for old, new in ((SPLICE_ON_ANCHOR, SPLICE_ON_SPLICE), (JOB_ANCHOR, SPLICE_FROZEN_JOBS + JOB_ANCHOR)) + SPLICE_AGG_EDITS:
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
            r"actions/runs/\{V\}/attempts/\{V\}/jobs\?per_page=100(&page=\{V\})?", r"actions/runs/\{V\}/artifacts(\?per_page=100&page=\{V\})?",
            r"actions/artifacts/\{V\}/zip", r"issues/comments/\{V\}",
            r"git/trees/\{V\}\?recursive=1", r"git/trees/\{V\}", r"activity\?ref=refs/heads/\{V\}(&per_page=100&page=\{V\})?")
    return any(re.fullmatch(p, rest) for p in pats)


def zip_read_rules(tree):
    """Scoped in-memory reader: no mode change, extra member read, alias or resource escape."""
    errors = []
    constructors = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and dotted(node) == "zipfile.ZipFile":
            calls = [x for x in ast.walk(tree) if isinstance(x, ast.Call) and x.func is node]
            if len(calls) != 1:
                errors.append("ZIP: constructor escaped call position")
                continue
            call = calls[0]
            if len(call.args) != 1 or call.keywords:
                errors.append("ZIP: constructor arguments")
                continue
            buffer = call.args[0]
            if not (isinstance(buffer, ast.Call) and dotted(buffer.func) == "io.BytesIO"
                    and len(buffer.args) == 1 and not buffer.keywords):
                errors.append("ZIP: not an in-memory buffer")
            constructors.append(call)
    for fn in [x for x in tree.body if isinstance(x, ast.FunctionDef)]:
        for call in constructors:
            if not any(x is call for x in ast.walk(fn)):
                continue
            bindings = [x for x in ast.walk(fn) if isinstance(x, ast.withitem) and x.context_expr is call
                        and isinstance(x.optional_vars, ast.Name)]
            if len(bindings) != 1:
                errors.append("ZIP: resource must be locally scoped")
                continue
            target = bindings[0].optional_vars
            name = target.id
            allowed = {id(target)}
            for use in ast.walk(fn):
                if not isinstance(use, ast.Call) or not isinstance(use.func, ast.Attribute):
                    continue
                base = use.func.value
                if not isinstance(base, ast.Name) or base.id != name:
                    continue
                good = use.func.attr == "namelist" and not use.args and not use.keywords
                good = good or (use.func.attr == "read" and len(use.args) == 1 and not use.keywords
                                and isinstance(use.args[0], ast.Constant) and use.args[0].value == "measurements.json")
                if good:
                    allowed.add(id(base))
                else:
                    errors.append("ZIP: method/member")
            if any(isinstance(x, ast.Name) and x.id == name and id(x) not in allowed for x in ast.walk(fn)):
                errors.append("ZIP: resource alias/rebinding/escape")
    return sorted(set(errors))


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
    errs += zip_read_rules(tree)
    errs += run_class_string_sites(tree)
    return sorted(set(errs))


def run_class_string_sites(tree):
    """controls.py: the string constant "workflow_dispatch" occurs only in the run-classification functions
    (those named run_class_*, which derive-run, order and verdict use)."""
    errs, owners, splice_nodes = [], {}, set()
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            for item in ast.walk(node):
                owners[id(item)] = node.name
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            if node.targets[0].id.startswith("SPLICE_"):
                splice_nodes |= {id(item) for item in ast.walk(node.value)}
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and run_class_dispatch() in node.value:
            if id(node) not in splice_nodes and not str(owners.get(id(node))).startswith("run_class_"):
                errs.append("dispatch string outside admitted site")
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
    """Control B: exact mode/guard/registry/reference sites and deterministic collections."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return ["syntax"]
    errs = _dunder_ok(tree)
    imps = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            for alias in n.names:
                imps.add(alias.name)
                if alias.asname:
                    errs.append("import alias")
        if isinstance(n, ast.ImportFrom):
            imps.add(n.module)
            if n.module != "fractions" or [x.name for x in n.names] != ["Fraction"] or n.names[0].asname:
                errs.append("from-import")
    if imps != CHECKER_IMPORTS:
        errs.append("imports")
    owner = {}
    defs = {}
    for fn in tree.body:
        if isinstance(fn, ast.FunctionDef):
            defs[fn.name] = fn
            for n in ast.walk(fn):
                owner[id(n)] = fn.name
    consts = [n for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, str)
              and run_class_dispatch() in n.value]
    de = [n for n in tree.body if isinstance(n, ast.Assign) and len(n.targets) == 1
          and isinstance(n.targets[0], ast.Name) and n.targets[0].id == "DISPATCH_EVENT"]
    if len(consts) != 1 or len(de) != 1 or de[0].value is not consts[0]:
        errs.append("dispatch constant")
    for n in ast.walk(tree):
        if isinstance(n, ast.Name) and n.id == "DISPATCH_EVENT" and isinstance(n.ctx, ast.Load):
            if owner.get(id(n)) not in ("s_mode",) + GUARD_SELFTEST_FUNCS:
                errs.append("dispatch site")
        if isinstance(n, ast.Name) and n.id in BANNED:
            errs.append("banned " + n.id)
        if isinstance(n, ast.Attribute) and n.attr in ("system", "popen", "modules"):
            errs.append("attribute " + n.attr)
        if isinstance(n, (ast.Set, ast.SetComp)) or (isinstance(n, ast.Name) and n.id in ("set", "frozenset")):
            errs.append("unordered set")
    os_sites = [n for n in ast.walk(tree) if isinstance(n, ast.Name) and n.id == "os" and isinstance(n.ctx, ast.Load)]
    main_blocks = [n for n in tree.body if _is_main_guard(n)]
    main_nodes = {id(x) for block in main_blocks for x in ast.walk(block)}
    valid_os, kinds = set(), []
    for call in ast.walk(tree):
        if not isinstance(call, ast.Call) or not isinstance(call.func, ast.Name) or len(call.args) != 2 or call.keywords:
            continue
        arg, env = call.args
        if not (isinstance(arg, ast.Attribute) and arg.attr == "argv" and isinstance(arg.value, ast.Name) and arg.value.id == "sys"
                and isinstance(env, ast.Attribute) and env.attr == "environ" and isinstance(env.value, ast.Name) and env.value.id == "os"):
            continue
        if call.func.id == "s_mode" and owner.get(id(call)) == "s_refusal":
            valid_os.add(id(env.value)); kinds.append("refusal")
        elif call.func.id == "s_entry" and id(call) in main_nodes and owner.get(id(call)) is None:
            valid_os.add(id(env.value)); kinds.append("main")
    if len(main_blocks) != 1 or {id(x) for x in os_sites} != valid_os or sorted(kinds) != ["main", "refusal"]:
        errs.append("environment owner/caller/main sites")
    db = [n for n in tree.body if isinstance(n, ast.Assign) and len(n.targets) == 1
          and isinstance(n.targets[0], ast.Name) and n.targets[0].id == "DECISIVE_BUILDERS"]
    registry_sites = set()
    if len(db) != 1 or not isinstance(db[0].value, ast.Tuple) or \
            [x.id for x in db[0].value.elts if isinstance(x, ast.Name)] != list(builders) or \
            len(db[0].value.elts) != len(builders):
        errs.append("builder registry")
    else:
        registry_sites = {id(x) for x in db[0].value.elts}
    refusal_sites = set()
    for name in builders + ("s_decisive",):
        fn = defs.get(name)
        body = fn.body if fn else []
        if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str):
            body = body[1:]
        first = body[0] if body else None
        if not (isinstance(first, ast.Expr) and isinstance(first.value, ast.Call) and
                isinstance(first.value.func, ast.Name) and first.value.func.id == "s_refusal" and
                not first.value.args and not first.value.keywords):
            errs.append("first refusal " + name)
        else:
            refusal_sites.add(id(first.value.func))
    refusal = defs.get("s_refusal")
    if refusal is None or refusal.args.posonlyargs or refusal.args.args or refusal.args.vararg or refusal.args.kwarg or refusal.args.kwonlyargs or refusal.args.defaults or refusal.args.kw_defaults:
        errs.append("refusal signature")
    for n in ast.walk(tree):
        if isinstance(n, ast.Name) and n.id in builders and id(n) not in registry_sites:
            if owner.get(id(n)) != "s_decisive" or not isinstance(n.ctx, ast.Load):
                errs.append("builder reference")
        if isinstance(n, ast.Name) and n.id == "s_refusal" and id(n) not in refusal_sites:
            errs.append("refusal reference")
    sites = [owner.get(id(n)) for n in ast.walk(tree) if isinstance(n, ast.Name) and n.id == "s_decisive"]
    if sorted(map(str, sites)) != ["s_entry", "t_builder_refuses"]:
        errs.append("entry sites")
    tb = defs.get("t_builder_refuses")
    if tb is None or len(tb.body) != 1 or not isinstance(tb.body[0], ast.Try):
        errs.append("direct-refusal test form")
    else:
        tr = tb.body[0]
        call_ok = len(tr.body) == 1 and isinstance(tr.body[0], ast.Expr) and isinstance(tr.body[0].value, ast.Call)
        call_ok = call_ok and isinstance(tr.body[0].value.func, ast.Name) and tr.body[0].value.func.id == "s_decisive"
        call_ok = call_ok and not tr.body[0].value.args and not tr.body[0].value.keywords
        handler_ok = len(tr.handlers) == 1 and isinstance(tr.handlers[0].type, ast.Name)
        handler_ok = handler_ok and tr.handlers[0].type.id == "QC21Refusal" and tr.handlers[0].name is None
        if not (call_ok and handler_ok and tr.orelse and not tr.finalbody):
            errs.append("direct-refusal test form")
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
              "list", "dict", "isinstance"}
V_TYPE_NAMES = {"str"}
V_EXCEPTION_NAMES = {"ValueError", "TypeError", "KeyError", "IndexError", "ArithmeticError"}
V_FORBIDDEN = {"globals", "locals", "vars", "getattr", "setattr", "eval", "exec", "compile", "__import__"}


def indep_binding_errors(tree, vfuncs):
    """Check module bindings, including expressions evaluated when definitions are created."""
    errors, queue = [], list(tree.body)
    accepted = {id(fn) for fn in vfuncs}
    while queue:
        node = queue.pop(0)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name.startswith("v_") and id(node) not in accepted:
                errors.append("alternate verifier definition " + node.name)
            expressions = list(node.decorator_list) + list(node.args.defaults)
            expressions += [x for x in node.args.kw_defaults if x is not None]
            arguments = node.args.posonlyargs + node.args.args + node.args.kwonlyargs
            arguments += [x for x in (node.args.vararg, node.args.kwarg) if x is not None]
            expressions += [x.annotation for x in arguments if x.annotation is not None]
            if node.returns is not None:
                expressions.append(node.returns)
            queue.extend(expressions)
            # Function bodies create local bindings, not module bindings; C-INDEP scans verifier bodies.
            continue
        if isinstance(node, ast.ClassDef):
            if node.name.startswith("v_"):
                errors.append("verifier class binding " + node.name)
            queue.extend(node.bases + [x.value for x in node.keywords] + node.decorator_list)
            continue
        if isinstance(node, ast.Name) and isinstance(node.ctx, (ast.Store, ast.Del)) and node.id.startswith("v_"):
            errors.append("verifier module alias/rebinding " + node.id)
        if isinstance(node, ast.alias) and (node.asname or node.name).startswith("v_"):
            errors.append("verifier import alias/rebinding")
        if isinstance(node, ast.ExceptHandler) and node.name and node.name.startswith("v_"):
            errors.append("verifier exception binding")
        if isinstance(node, (ast.MatchAs, ast.MatchStar)) and node.name and node.name.startswith("v_"):
            errors.append("verifier pattern binding")
        if isinstance(node, ast.MatchMapping) and node.rest and node.rest.startswith("v_"):
            errors.append("verifier mapping binding")
        queue.extend(ast.iter_child_nodes(node))
    for node in ast.walk(tree):
        if isinstance(node, (ast.Global, ast.Nonlocal)) and any(name.startswith("v_") for name in node.names):
            errors.append("verifier global/nonlocal rebinding")
    return sorted(set(errors))


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
    vnames = {n.name for n in vfuncs}
    if len(vnames) != len(vfuncs):
        errs.append("duplicate verifier definition")
    errs += indep_binding_errors(tree, vfuncs)
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
                elif n.id in local or n.id in vnames or n.id in V_BUILTINS or n.id in V_EXCEPTION_NAMES or n.id in V_TYPE_NAMES:
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
                    if not (f.id in vnames or f.id in V_BUILTINS or f.id == "Fraction" or f.id in local):
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
    for src, names in ((src_checker, ("k_decide_c", "k_decide_levels")), (src_controls, ("decide_c", "decide_levels"))):
        tt = ast.parse(src)
        for fn in [n for n in tt.body if isinstance(n, ast.FunctionDef) and n.name in names]:
            for n in ast.walk(fn):
                if (isinstance(n, ast.Constant) and isinstance(n.value, str)
                        and re.fullmatch(r"(?s).*(?<![A-Za-z])STAB(?![A-Za-z]).*", n.value)) or \
                        (isinstance(n, ast.Name) and "STAB" in n.id.upper().split("_")) or \
                        (isinstance(n, ast.Attribute) and "STAB" in n.attr.upper().split("_")):
                    errs.append("%s references STAB (r12a: reported, never gating)" % fn.name)
        found = {n.name for n in tt.body if isinstance(n, ast.FunctionDef)} & set(names)
        if found != set(names):
            errs.append("C-IFACE: missing %s" % sorted(set(names) - found))
    for src, names in ((src_checker, ("k_decide_p", "k_decide_b", "k_decide_c", "k_decide_levels")),
                       (src_controls, ("decide_p", "decide_b", "decide_c", "decide_levels"))):
        for fn in [x for x in ast.parse(src).body if isinstance(x, ast.FunctionDef) and x.name in names]:
            for node in ast.walk(fn):
                if isinstance(node, ast.Constant) and node.value == "bp_equals_qmp":
                    errs.append(fn.name+" reads benchmark-only bp_equals_qmp")
                if isinstance(node, ast.Name) and node.id in ("bp_restricted_equals_qmp", "qm_restricted_run"):
                    errs.append(fn.name+" calls benchmark-only computation")
            if fn.name in ("k_decide_b", "decide_b"):
                roles = [x.comparators[0].value for x in ast.walk(fn) if isinstance(x, ast.Compare)
                         and isinstance(x.left, ast.Call) and x.left.args and isinstance(x.left.args[0], ast.Constant)
                         and x.left.args[0].value == "role" and len(x.comparators) == 1 and isinstance(x.comparators[0], ast.Constant)]
                if roles != ["B-P"]:
                    errs.append(fn.name+" must select only the B-P role")
    for fn in [x for x in ast.parse(src_controls).body if isinstance(x, ast.FunctionDef) and x.name.startswith("ada_")]:
        if any(isinstance(node, ast.Constant) and node.value == "bp_equals_qmp" for node in ast.walk(fn)):
            errs.append(fn.name+" reads benchmark-only bp_equals_qmp")
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
    """Independent controller rule: SG-1 and only B-P, never report-only verdicts."""
    try:
        if rec["controls_red"]:
            return "B-VOID", list(rec["controls_red"])
        bp_records = [entry for entry in rec["fragments"] if entry.get("role") == "B-P"]
        if len(bp_records) != 1:
            return "B-VOID", ["one-B-P-required"]
        bp = bp_records[0]
        settings = ["M00", "M01", "M02", "M10", "M11", "M12", "M20", "M21", "M22"]
        if bp.get("preps") != 32 or sorted(bp.get("lp_settings", [])) != settings:
            return "B-VOID", ["SG-1:32-preparations-nine-settings"]
        if bp.get("lp_reads_equal_acc") is not True or sorted(bp.get("acc", [])) != settings:
            return "B-VOID", ["lp_reads_equal_acc:B-P"]
        if bp.get("verified") is not True or bp.get("lp") not in ("feasible", "infeasible"):
            return "B-VOID", ["B-P:"+str(bp.get("lp")), "limitation:SG-2"]
        return ("B-CONTEXTUAL" if bp["lp"] == "infeasible" else "B-CLASSICALLY-IMITABLE"), []
    except (KeyError, TypeError, ValueError):
        return "B-VOID", ["missing-field"]


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


def fragment_controls(records):
    """Decisive C-CERT/C-BUDGET: withheld results are reported; only a leaked verdict makes the control red."""
    failures, leaked, over = [], [], []
    for record in records:
        named = str(record.get("name"))
        decided = record.get("lp") in ("feasible", "infeasible")
        if record.get("verified") is not True:
            failures.append(named)
            if decided:
                leaked.append(named)
        limits = record.get("budget_values", [])
        counters = [record.get(key) for key in ("pivots", "max_bits", "work")]
        excess = any(limit is not None and (not isinstance(value, int) or value > limit)
                     for value, limit in zip(counters, limits))
        caps = record.get("cap_values", [])
        sizes = [record.get(key) for key in ("n_extreme", "d", "c", "effects_before_reduction")]
        excess = excess or any(limit is not None and (not isinstance(value, int) or value > limit)
                               for value, limit in zip(sizes, caps))
        if decided and excess:
            over.append(named)
    return {"C-CERT": {"green": not leaked, "unverified": len(failures), "unverified_fragments": failures,
                        "given_verdict_without_certificate": leaked},
            "C-BUDGET": {"green": not over, "given_verdict_over_limit": over}}


def decide(m):
    """decide: VOID unless the measurements are decisive, complete and in schema, with no placeholder; else
    every token recomputed from the raw fields, and the checker's flags must agree (X)."""
    try:
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
        monitored = list(frs)+[x["completion_record"] for x in frs if isinstance(x.get("completion_record"), dict)]
        measured_controls = fragment_controls(monitored)
        b_red = list(f["controls_red"]["B"])
        b_red += [name for name, control in measured_controls.items() if not control["green"] and name not in b_red]
        b_tok, _ = decide_b({"controls_red": b_red, "fragments": frs})
        c_tok, _ = decide_c({"controls_red": f["controls_red"]["C"], "complete": True, "flags_agree": True,
                             "instances": m["C"]["instances"]})
        bp = [x for x in frs if x.get("role") == "B-P"]
        b_ctx = b_tok == "B-CONTEXTUAL"
        b_eq = bool(bp) and bp[0].get("lp_reads_equal_acc") is True
        lev = decide_levels(p_tok, b_ctx, b_eq, True, c_tok, m["REP_INV"]["reclassified"])
        attr = attr_value(m["P"]["arms"]["off"], m["P"]["arms"]["(w,0)"], m["P"]["arms"]["(w,w')"])
        agree = (p_tok == f["P"] and b_tok == f["B"] and c_tok == f["C"] and str(lev) == str(f["levels"]["level"])
                 and attr == m["P"]["ATTR"]["value"])
        out = {"P": p_tok, "B": b_tok, "C": c_tok, "level": lev, "ATTR": attr, "flags_agree": agree}
        if not agree:
            out["VOID"] = ["X: the checker's flags disagree with decide"]
        return out

    except (ValueError, TypeError, KeyError, IndexError, AttributeError):
        return {"VOID": ["malformed decisive record"]}


# ------------------------------------------------------------------------------------------------------------
# STAB-FALSE (r12a): each cone certificate's orbit rebuilt from its own fields, exactly; expected STAB = false
# ------------------------------------------------------------------------------------------------------------
CFGS = [(a, b, c, d) for a in (0, 1) for b in (0, 1) for c in (0, 1) for d in (0, 1)]   # (u0, v0, u1, v1)


def stab_fns(w):
    """(f_x, f_y, f_z) = (v0, u0 + v0 + u1 + v1, u0)."""
    return (w[1], (w[0] + w[1] + w[2] + w[3]) % 2, w[0])


def stab_qa():
    out = {"0": [Q(1, 16)] * 16}
    for a in range(3):
        for b in (0, 1):
            out["xyz"[a] + str(b)] = [Q(1, 8) if stab_fns(w)[a] == b else Q(0) for w in CFGS]
    return out


def stab_r(mu):
    return tuple(sum(p * (1 - 2 * stab_fns(w)[a]) for p, w in zip(mu, CFGS)) for a in range(3))


def stab_rank(rows):
    rows = [list(r) for r in rows]
    rank, col = 0, 0
    ncol = len(rows[0]) if rows else 0
    while rank < len(rows) and col < ncol:
        piv = next((i for i in range(rank, len(rows)) if rows[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        for i in range(rank + 1, len(rows)):
            if rows[i][col] != 0:
                f = rows[i][col] / rows[rank][col]
                rows[i] = [x - f * y for x, y in zip(rows[i], rows[rank])]
        rank += 1
        col += 1
    return rank


def stab_matrix(cert):
    """B from the certificate's fields: the explicit window form {K, q, B}, or the K = 1 form {q, P, G} with
    B delta_x = 8 q P(v(x)) l_x, l_x the product law with R = G(v)/P(v), v(x) = chi(x)."""
    if "B" in cert:
        return [[q(x) for x in row] for row in cert["B"]], int(cert["K"])
    qq = q(cert["q"])
    pp = {tuple(int(t) for t in k.split(",")): q(v) for k, v in cert["P"].items()}
    gg = {tuple(int(t) for t in k.split(",")): tuple(q(x) for x in v) for k, v in cert["G"].items()}
    chi = lambda w: tuple(1 - 2 * x for x in stab_fns(w))
    b = [[Q(0)] * 16 for _ in range(16)]
    for j, w in enumerate(CFGS):
        v = chi(w)
        if pp[v] == 0:
            continue
        r = tuple(g / pp[v] for g in gg[v])
        for i, x in enumerate(CFGS):
            cx = chi(x)
            pr = Q(1, 2)
            for a in range(3):
                pr *= (1 + r[a] * cx[a]) / 2
            b[i][j] += 8 * qq * pp[v] * pr
    return b, 1


def stab_unit_pair_fires(beta):
    """W-CL on beta (no ticks: the supplied branch is k = 0): the unit-modulus multiset is not a sub-multiset of a
    3x3 signed-permutation spectrum. Exact: rational roots removed, then the quadratic remainder tested."""
    a = beta
    tr = a[0][0] + a[1][1] + a[2][2]
    m2 = sum(a[i][i] * a[j][j] - a[i][j] * a[j][i] for i, j in ((0, 1), (0, 2), (1, 2)))
    det = (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
           + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
    poly = [Q(1), -tr, m2, -det]
    roots = []
    while len(poly) > 1:
        den = 1
        for c in poly:
            den = den * c.denominator // _igcd(den, c.denominator)
        ip = [int(c * den) for c in poly]
        cands = [Q(0)] if ip[-1] == 0 else sorted({Q(s * p, qq) for p in _idiv(ip[-1]) for qq in _idiv(ip[0])
                                                    for s in (1, -1)})
        root = None
        for r in cands:
            val = Q(0)
            for c in poly:
                val = val * r + c
            if val == 0:
                root = r
                break
        if root is None:
            break
        roots.append(root)
        new = [poly[0]]
        for c in poly[1:-1]:
            new.append(c + new[-1] * root)
        poly = new
    if len(poly) != 3:
        return False
    b, c = poly[1] / poly[0], poly[2] / poly[0]
    if c != 1 or not (-2 < b < 2) or b == 0:
        return False
    if b == 1:
        return -1 in roots
    if b == -1:
        return 1 in roots
    return True


def _igcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def _idiv(n):
    n = abs(n)
    out, i = set(), 1
    while i * i <= n:
        if n % i == 0:
            out |= {i, n // i}
        i += 1
    return sorted(out)


def stab_false_control(cert):
    """STAB-FALSE: the certificate's B as the branch (herald = the mass kept) on the seven QA laws, to its window
    K. Green when B >= 0 with column sums <= 1, HC(K), CONS(K), VAL(K) hold, W-CL fires, and STAB(K) is false."""
    b, k = stab_matrix(cert)
    sub = all(x >= 0 for row in b for x in row) and all(sum(b[i][j] for i in range(16)) <= 1 for j in range(16))
    fam = stab_qa()
    orbit, heralds = [fam], []
    for _ in range(k):
        nxt = {}
        for key, mu in orbit[-1].items():
            out = [sum(b[i][c] * mu[c] for c in range(16)) for i in range(16)]
            h = sum(out)
            heralds.append(h)
            if h == 0:
                return {"green": False, "reason": "herald 0"}
            nxt[key] = [x / h for x in out]
        orbit.append(nxt)
    hc = len(set(heralds)) == 1 and heralds[0] > 0
    alpha = stab_r(orbit[1]["0"])
    cols = [tuple(stab_r(orbit[1][ax + "0"])[i] - alpha[i] for i in range(3)) for ax in "xyz"]
    beta = [[cols[j][i] for j in range(3)] for i in range(3)]
    phi = lambda r: tuple(alpha[i] + sum(beta[i][c] * r[c] for c in range(3)) for i in range(3))
    cons = all(stab_r(orbit[j + 1][key]) == phi(stab_r(orbit[j][key])) for j in range(k) for key in fam)
    val = all(sum(x * x for x in stab_r(mu)) <= 1 for lev in orbit for mu in lev.values())
    wcl = stab_unit_pair_fires(beta)
    r_prev = stab_rank([mu for lev in orbit[:k] for mu in lev.values()])
    r_full = stab_rank([mu for lev in orbit for mu in lev.values()])
    stab = r_prev == r_full
    return {"green": sub and hc and cons and val and wcl and not stab, "K": k, "STAB": stab,
            "span_rank": [r_prev, r_full], "HC": hc, "CONS": cons, "VAL": val, "WCL": wcl}


def stab_false_check(root=RDIR):
    """Reads each pinned certificate copy, checks its sha256, and runs STAB-FALSE on it."""
    out = {}
    for rel, pin in sorted(STAB_CERTS.items()):
        path = root + rel
        if not os.path.isfile(path):
            out[rel] = {"green": False, "reason": "absent"}
            continue
        raw = read_bytes(path)
        if sha256_bytes(raw) != pin:
            out[rel] = {"green": False, "reason": "sha256"}
            continue
        out[rel] = stab_false_control(json.loads(raw))
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


def ada_statuses(measurements, decision):
    """Frozen ADA statuses from structured records; no quantum-comparison field is an input."""
    p, c = measurements["P"], measurements["C"]
    ablations, ab = p.get("ablate_p", {}), p.get("ab_p", {})
    rows = []
    for name, record in sorted(ablations.items()):
        status = "used, not varied"
        if name == "ABL-SA1c" and ab.get("universality_case") == "A fails and B succeeds" and record.get("pred_change") is True:
            status = "carrying the universality reading in this model"
        if name == "ABL-SA1b" and record.get("OLC", {}).get("joint") is True:
            status = "carries observer-level complementarity in this model"
        kind = record.get("kind", "dynamics" if name == "ABL-P3" else "reported")
        if name == "ABL-P3":
            status = "could not be ablated in this round (NR-16)"
        rows.append({"assumption": name, "status": status, "kind": kind,
                     "pred_change": record.get("pred_change"), "mech_change": record.get("mech_change"),
                     "access_only": record.get("access_only"), "dynamics_credit": record.get("dynamics_credit"),
                     "credit": "not credited with new dynamics" if kind in ("state restriction", "access restriction") else "as recorded"})
    controls = c.get("controls", {})
    affine_status = "used, not varied"
    if decision["C"] in ("C-EXPOSURE", "C-NONSTABILIZER") and controls.get("CC-NAT", {}).get("green") is True and controls.get("C-EMB", {}).get("green") is True:
        affine_status = "essential in this model"
    elif decision["C"] == "C-SURVIVAL":
        affine_status = "not sufficient to remove in this model"
    rows += [{"assumption": "L-AFF", "status": affine_status, "kind": "dynamics"},
             {"assumption": "L-HOLD", "status": "the record that suppresses is unread" if decision["P"] == "P-COMPLEMENTARITY" else "used, not varied"},
             {"assumption": "L-PORT", "status": "fixes B1"},
             {"assumption": "L-HET", "status": "used, not varied"},
             {"assumption": "L-CAL", "status": "used, not varied; REP-INV is reported separately"},
             {"assumption": "E-COMPL", "status": "reported", "CPL": {name: arm.get("CPL") for name, arm in p.get("arms", {}).items()}}]
    diagnostics = c.get("diagnostics_r5", {})
    herald_binding = [name for name, record in diagnostics.items() if record.get("herald_failure_non_octahedral_fit")]
    ball_binding = [name for name, record in diagnostics.items() if name in ("AND", "NAND", "OR", "NOR") and record.get("category") == "INVALID"]
    rows += [{"assumption": "L-HCONST (diagnostics)", "status": "binding" if herald_binding else "used, not varied", "rules": herald_binding},
             {"assumption": "E-BALL (diagnostics)", "status": "binding" if ball_binding else "used, not varied", "rules": ball_binding,
              "nonstab_valid": {name: diagnostics[name].get("nonstab_valid") for name in ball_binding}},
             {"assumption": "L-ISOT (diagnostics)", "status": "reported", "branches": {
                 name: {field: record.get(field) for field in ("nonisotropic_branches", "sharp_branches")} for name, record in diagnostics.items()}}]
    return rows


def ada_questions(measurements, decision):
    """The five frozen questions, per test/token, with the finite-model scope explicit."""
    result = {}
    for test in ("P", "B", "C"):
        token = decision[test]
        removal = "Only this model; outside this round's model, not established."
        counterexample = "None in the declared scope."
        if test == "P":
            removal = "The two A/B readings and ABL-SA1c's pred_change/mech_change/access_only fields are reported."
        elif test == "B":
            removal = "The first restoring completion with a verified model is reported; an undecided completion establishes no restoration."
        elif token == "C-EXPOSURE":
            removal = "In this model, for the listed instances on bounded orbits."
            counterexample = "A finite candidate satisfies VAL on O_K, HC, CONS and EMB only; the comparator's further requirements are untested (NR-6)."
        elif token == "C-NONSTABILIZER":
            removal = "Partly: valid non-stabilizer orbit laws; no non-Clifford fixed operation found in scope."
        elif token == "C-SURVIVAL":
            removal = "Not in this model."
        result[test] = {"token": token, "essential_assumptions": "From the ADA status rows above.",
                        "types": "From the frozen ledger; L-AFF, L-Q2 and L-N2 retain both native/imported readings.",
                        "removing_imported_assumption": removal, "counterexample": counterexample,
                        "scope": "Only this model. Irrational and approximate gates are outside every outcome; outside this round's model, not established."}
    return result


def make_note(m, d, f, s1, e):
    dec = decide(m)
    lines = ["# ARP-2-QC21 (Q-C2-1): result", "", FREEZE_DISCLOSURE, "",
             "- `D` = `%s`; `F` = `%s`; S1 = `%s`; `E` is this evidence commit, identified by the owner designation." % (d, f, s1), ""]
    if "VOID" in dec:
        lines += ["**Token:** `VOID`", "", "A required control failed, or the output was incomplete: "
                  + ", ".join(dec["VOID"]) + ". No reading is made. The measurements are preserved as produced.", ""]
        return "\n".join(lines) + "\n"
    lines += ["**Token line:** `"+token_line(m)+"`", "",
              "Any final-capture and E-stage approval/ratification checks remain required operational landing conditions. "
              "This enduring note makes no assertion that unretained host-time checks passed.", ""]
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
    if dec["B"] == "B-VOID":
        code_records = {"controls_red": m["flags"]["controls_red"]["B"], "fragments": m["B"]["fragments"]}
        codes = decide_b(code_records)[1]
        lines.append("A required B control failed, or B-P has no verified verdict within this round's frozen caps and budget: "
                     +", ".join(codes)+". No reading is made.")
        for fragment in m["B"]["fragments"]:
            if fragment.get("role") == "B-P" and fragment.get("lp") == "out_of_scope":
                lines.append("B-P exceeded "+", ".join(fragment.get("caps", ["the cap or budget"]))+
                             ". This is a limitation of this round's frozen resources, not a result about B-P.")
            if fragment.get("role") == "B-P" and fragment.get("lp") == "undecided":
                lines.append("B-P's certificate did not verify. This is a limitation of this round's method, not a result about B-P.")
    if dec["B"] == "B-CONTEXTUAL":
        lines.append(B_SCOPE.replace("{Acc}", "Acc(B-P)").replace("{typing}", "owner-typed candidate strengthened"))
    fragments = m["B"]["fragments"]
    completions = [record for record in fragments if record.get("role") == "completion"]
    for record in completions:
        lines.append("- Completion "+record["name"]+": "+str(record["lp"])+"; certificate verified "+str(record.get("verified"))+".")
    restored = [record["name"] for record in completions if record.get("lp") == "feasible" and record.get("verified") is True]
    if dec["B"] == "B-CONTEXTUAL":
        lines.append("First restoring completion: "+restored[0]+"." if restored else
                     "No completion in the frozen list restored a model within this round's frozen caps and budget: "+
                     ", ".join(record["name"]+" "+str(record["lp"]) for record in completions)+".")
    for record in fragments:
        if record.get("role") == "B-C":
            completion = record.get("completion_record", {})
            lines.append("- "+record["name"]+": "+str(record["lp"])+"; full-read completion "+str(completion.get("lp", "not attempted"))+
                         ("; imported for B-C." if record.get("restored_by_full") is True and record.get("lp") == "infeasible" else "; no UPR-BC label."))
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
    for row in ada_statuses(m, dec):
        lines.append("- "+canonical(row).strip())
    for test, questions in ada_questions(m, dec).items():
        lines.append("- "+test+": "+canonical(questions).strip())
    lines.append("Shared scaffolding untested here: P3, E-iso, N2, H-PREP, terminal screen, L-PATH and L-PORT.")
    return "\n".join(lines) + "\n"


# ------------------------------------------------------------------------------------------------------------
# stress-check, replay
# ------------------------------------------------------------------------------------------------------------
def freeze_budget_rule(stress, t5, t810):
    """C.8.1–2 mechanical resource selection; pure arithmetic on recorded design data only."""
    good, reason = stress_validate(stress)
    if not good:
        raise Refused("budget rule: "+reason)
    fragments = stress["fragments"]
    eligible = [x for x in fragments if x["class"] != "ST-BP"]
    if not eligible or any(x["certificate_verified"] is not True for x in eligible):
        raise Refused("budget rule: unverified general record")
    general = [3*max(x[key] for x in eligible) for key in ("pivots", "max_bits", "work")]
    work_total = stress["W_fix"]+stress["W_stress"]
    if work_total <= 0 or not isinstance(t5, int) or t5 < 0 or not isinstance(t810, int) or t810 < 0:
        raise Refused("budget rule: invalid durations or work")
    sigma = fractions.Fraction(t5, work_total)
    candidates = [x for x in fragments if x["class"] == "ST-BP" and x["over_maximum"] is False
                  and x["certificate_verified"] is True and x["verdict"] in ("feasible", "infeasible")
                  and type(x["c"]) is int and 0 <= x["c"] <= stress["S_max"]]
    candidates = sorted(candidates, key=lambda x: (-x["c"], (20261108, 1, 2).index(x["seed"])))
    reference, caps, bp_budget = None, [16, 16, 100000, 200], list(general)
    for record in candidates:
        proposed = [max(value, 3*record[key]) for value, key in zip(general, ("pivots", "max_bits", "work"))]
        bound = sigma*(proposed[2]+1203*general[2]+2*stress["W_fix"]+stress["W_stress"])+t810
        if bound <= 1200:
            reference, bp_budget = record["name"], proposed
            caps = [max(16, record["n_extreme"]), max(16, record["d"]), max(100000, record["c"]), 200]
            break
    bound = sigma*(bp_budget[2]+1203*general[2]+2*stress["W_fix"]+stress["W_stress"])+t810
    return {"general": general, "BP": bp_budget, "BP_caps": caps, "reference": reference,
            "sigma": str(sigma), "timeout_lhs": str(bound), "timeout_pass": bound <= 1200,
            "timeout_minutes": 60, "reported_only_volume": 1203}


def stress_validate(data):
    try:
        if data["schema"] != "arp2-qc21-stress" or data["version"] != 2:
            return False, "schema"
        if data["seeds"] != [20261108, 1, 2] or type(data["S_max"]) is not int or data["S_max"] < 1:
            return False, "seeds/S_max"
        records, names = data["fragments"], []
        if not isinstance(records, list) or not records:
            return False, "fragments"
        wf, ws = 0, 0
        for record in records:
            if record["name"] in names:
                return False, "duplicate fragment"
            names.append(record["name"])
            if record["class"] not in ("ST-BP", "stress", "fixture"):
                return False, "fragment class"
            for key in ("pivots", "max_bits", "work"):
                if type(record[key]) is not int or record[key] < 0:
                    return False, "counter "+key
            if "decided_by" not in record:
                return False, "missing deciding step"
            if record["class"] == "ST-BP":
                if type(record["c"]) is not int or record["c"] < 0 or type(record["over_maximum"]) is not bool:
                    return False, "ST-BP count/flag type"
                if record["over_maximum"] != (record["c"] > data["S_max"]):
                    return False, "ST-BP maximum relation"
            if record["class"] == "ST-BP" and record["over_maximum"] is True:
                if record["c"] <= data["S_max"] or record["verdict"] != "out_of_scope" or record["certificate"] is not None:
                    return False, "invalid over_maximum"
                if record["reduction_verified"] is not True:
                    return False, "unverified reduction"
            elif record["certificate_verified"] is not True or record["verdict"] not in ("feasible", "infeasible"):
                return False, "unverified "+record["name"]
            if record["class"] == "fixture":
                wf += record["work"]
            else:
                ws += record["work"]
        if [data["W_fix"], data["W_stress"]] != [wf, ws]:
            return False, "work totals"
        if sorted(x["seed"] for x in records if x["class"] == "ST-BP") != [1, 2, 20261108]:
            return False, "ST-BP instances"
        if sorted(x["seed"] for x in records if x["class"] == "stress") != [1, 2, 20261108]:
            return False, "SF-2 instances"
    except (ValueError, TypeError, KeyError, IndexError):
        return False, "malformed stress record"
    return True, "schema verified"


def stress_check(path, pin):
    raw = read_bytes(path)
    try:
        data = json.loads(raw)
    except (ValueError, TypeError):
        return False, "unparseable"
    good, reason = stress_validate(data)
    if not good:
        return False, reason
    digest = sha256_bytes(raw)
    return (True if pin is None else digest == pin), digest


def replay_compare(fresh_bytes, committed_bytes):
    """B6: compares files only. The committed measurements carry S1's dispatch input, so the one field
    parameters.dispatch_sha is set aside on both sides before the byte comparison of canonical JSON."""
    try:
        a, b = json.loads(fresh_bytes), json.loads(committed_bytes)
    except (ValueError, TypeError):
        return False
    if not isinstance(a, dict) or not isinstance(b, dict):
        return False
    if not isinstance(a.get("parameters"), dict) or not isinstance(b.get("parameters"), dict):
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
    if not v3_working_copy_ok():
        return ["DS: working v3_verifier differs from its exact pinned D object; T not started"]
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


def code_b(commit, pins=None):
    errors = []
    if pins is None:
        pins = frozen_pins(git_show(commit, PREREG))
    if pins is None:
        return ["B: missing/invalid frozen pin table"]
    for name, path, scan in (("qc21_check.py", CHECKER, static_checker), ("controls.py", CONTROLS, static_controls)):
        pin = pins.get(name)
        source = git_show(commit, path)
        if not isinstance(pin, str) or not re.fullmatch(r"[0-9a-f]{40}", pin) or git_blob(commit, path) != pin:
            errors.append("B: exact script blob "+name)
        digest = pins.get(name+".sha256")
        if source is None:
            errors.append("B: missing "+name)
            continue
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest) or sha256_bytes(source) != digest:
            errors.append("B: script sha256 "+name)
        text = source.decode()
        errors += ["B: "+name+": "+error for error in scan(text)]
        if name == "qc21_check.py":
            errors += ["B: C-EXACT: "+error for error in c_exact(text)]
            errors += ["B: C-INDEP: "+error for error in c_indep(text)]
    checker, controller = git_show(commit, CHECKER), git_show(commit, CONTROLS)
    if checker is not None and controller is not None:
        errors += ["B: C-IFACE: "+error for error in c_iface(checker.decode(), controller.decode())]
    return errors


def code_w(commit):
    wt = git_show(commit, WORKFLOW)
    dt = git_show(D_SHA, WORKFLOW)
    if wt is None or dt is None:
        return ["W: unreadable"]
    return [] if check_w(wt.decode("utf-8"), dt.decode("utf-8")) else ["W: verify.yml is not D's with the frozen splice"]


def code_ds():
    errors = []
    for path, blob in INPUTS.items():
        if not isinstance(blob, str) or not re.fullmatch(r"[0-9a-f]{40}", blob) or git_blob(D_SHA, path) != blob:
            errors.append("DS: exact D input pin "+path)
    for name, record in REQUIRED_SOURCE_INPUTS.items():
        path, blob = record.get("path"), record.get("blob")
        if not isinstance(path, str) or not isinstance(blob, str) or not re.fullmatch(r"[0-9a-f]{40}", blob):
            errors.append("DS: "+name+" main source path/blob not supplied")
        elif git_blob(D_SHA, path) != blob:
            errors.append("DS: "+name+" not at D's exact pin")
    return errors


def check_mode(commit, frozen, stage):
    """Validate the frozen chain and records; capture failure propagates rather than becoming scientific VOID."""
    errors = code_ds()
    if errors or not v3_working_copy_ok():
        return errors+["DS: control T not started before exact verifier-byte check"]
    errors += code_t(D_SHA, frozen)
    pins = frozen_pins(git_show(frozen, PREREG))
    if stage is None:
        errors += code_g(D_SHA, frozen, {PREREG})
        raw = git_show(frozen, PREREG)
        if raw is None:
            errors.append("P: no frozen preregistration")
        elif pending_unbackticked(raw.decode()):
            errors.append("P: unbackticked PENDING fields remain")
        additional, records = freeze_checks(frozen, commit)
        return errors+additional
    if stage not in ("S1", "E", "W"):
        return errors+["T: unknown stage"]
    if pins is None:
        return errors+["P: frozen pins absent"]
    if stage == "S1":
        if git_parents(commit) != [frozen]:
            errors.append("T: S1 must be a single-parent child of F")
        errors += code_g(frozen, commit, {RDIR+name for name in S1_FILES}|{WORKFLOW})
        errors += code_b(commit, pins)+code_w(commit)
        for name in S1_FILES:
            if git_show(commit, RDIR+name) is None:
                errors.append("R: S1 file missing "+name)
        additional, records = freeze_checks(frozen, commit)
        return errors+additional
    if stage == "W":
        errors += code_g(frozen, commit, {RDIR+name for name in S1_FILES+E_FILES}|{WORKFLOW, RDIR+"evidence/void-run.json"})
        if git_show(commit, WORKFLOW) != git_show(frozen, WORKFLOW):
            errors.append("W: halt commit did not restore F workflow")
        return errors
    parents = git_parents(commit)
    if parents is None or len(parents) != 1:
        return errors+["T: E must be single-parent"]
    s1 = parents[0]
    if git_parents(s1) != [frozen]:
        errors.append("T: E parent is not the S1 child of F")
    errors += code_g(s1, commit, {RDIR+name for name in E_FILES})
    errors += code_b(commit, pins)+code_w(commit)
    for name in E_FILES:
        if git_show(commit, RDIR+name) is None:
            errors.append("R: E file missing "+name)
    measurement = git_show(commit, MEAS)
    if measurement is None:
        return errors+["R: missing measurements"]
    try:
        data = json.loads(measurement)
        decision = decide(data)
        if "VOID" in decision:
            errors.append("X: "+str(decision["VOID"]))
        confirmation = git_show(commit, RDIR+"evidence/confirmation-measurements.json")
        if confirmation is None or canonical(json.loads(confirmation).get("fixtures")) != canonical(data.get("fixtures")):
            errors.append("C-STATELESS: supplied confirmation fixtures differ (no archive-authenticity claim)")
        note = git_show(commit, RDIR+"result.md")
        expected = make_note(data, D_SHA, frozen, s1, commit).encode()
        if note != expected:
            errors.append("V: regenerated note differs")
        if note is not None and s4_hits(note.decode()):
            errors.append("V: forbidden S4 assertion")
        for name in ("evidence/order.json", "evidence/order-s1.json"):
            capture = json.loads(git_show(commit, RDIR+name))
            if capture.get("schema") != "arp2-qc21-order" or capture.get("version") != 1 or capture.get("violations"):
                errors.append("R: invalid/violating "+name)
        run_class_approvals(json.loads(git_show(commit, RDIR+"evidence/approvals.json")))
    except (ValueError, TypeError, KeyError, IndexError, AttributeError, Refused):
        errors.append("R/X/V: malformed evidence record")
    return errors


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


def run_class_expected_conclusions(jobs, event, workflow):
    """Strict owner-approved B1 structured-host check against D's frozen workflow."""
    if event not in ("pull_request", "workflow_dispatch") or not isinstance(jobs, list):
        return ["B1 invalid event/jobs"]
    if isinstance(workflow, bytes):
        try:
            workflow = workflow.decode("utf-8")
        except UnicodeDecodeError:
            return ["B1 unreadable workflow"]
    if not isinstance(workflow, str):
        return ["B1 missing workflow"]
    a42 = "Numerical probes / A42 exclusion (${{ matrix.part }})"
    keep = "ARP-1-MARC keep the measurements"
    reports = "KTRANS-SEP-2 axiom reports within the three axioms"
    marker = "KTRANS-SEP-2 marker complete reports with an axiom outside the three"
    required = (
        "  probes_a42_exclusion:\n    name: " + a42 +
        "\n    if: ${{ github.event_name == 'workflow_dispatch' }}",
        "      - name: " + keep +
        "\n        if: ${{ always() && github.event_name == 'workflow_dispatch' }}",
        "      - name: " + reports + "\n        id: ktrans_sep2_axioms",
        "      - name: " + marker +
        "\n        if: ${{ !cancelled() && steps.ktrans_sep2_axioms.outputs.reports == 'complete-nonstandard' }}")
    if any(workflow.count(block) != 1 for block in required):
        return ["B1 changed frozen workflow condition"]
    section = re.search(r"(?s)\n  probes_a42_exclusion:\n(.*?)\n  probes_foundations:", workflow)
    matrix = re.search(r"part: (\[[^\]]+\])", section.group(1)) if section else None
    parts = ("paths", "r5", "n18:0", "n18:1", "n18:2", "dfs:0", "dfs:1", "dfs:2",
             "dfs:3", "dfs:4", "dfs:5", "sathr", "cubes:0", "cubes:1", "cubes:2")
    try:
        if matrix is None or tuple(ast.literal_eval(matrix.group(1))) != parts:
            return ["B1 changed matrix"]
    except (ValueError, SyntaxError, TypeError):
        return ["B1 invalid matrix"]
    baseline = re.findall(r"(?m)^    name: ([^\n]+)$", workflow)
    if len(baseline) != len(set(baseline)) or a42 not in baseline:
        return ["B1 invalid job identity list"]
    expected = [x for x in baseline if x != a42] + [JOB_A, JOB_B]
    expected += ([a42] if event == "pull_request" else
                 [a42.replace("${{ matrix.part }}", part) for part in parts])
    names = [j.get("name") if isinstance(j, dict) else None for j in jobs]
    errors = []
    if sorted(str(x) for x in names) != sorted(expected):
        errors.append("B1 missing/duplicate/extra job or A42 matrix shard")
    found = {keep: [], reports: [], marker: []}
    for job in jobs:
        if not isinstance(job, dict):
            errors.append("B1 malformed job")
            continue
        name = job.get("name")
        skipped = event == "pull_request" and name in (a42, JOB_B)
        if job.get("conclusion") != ("skipped" if skipped else "success"):
            errors.append("B1 wrong job conclusion " + str(name))
        steps = job.get("steps")
        if skipped:
            if steps not in (None, []):
                errors.append("B1 skipped job has steps " + str(name))
            continue
        if not isinstance(steps, list):
            errors.append("B1 missing job steps " + str(name))
            continue
        for i, step in enumerate(steps):
            if not isinstance(step, dict):
                errors.append("B1 malformed step " + str(name))
                continue
            sn = step.get("name")
            if sn in found:
                found[sn].append((name, i, step.get("conclusion")))
            expected_step = ("skipped" if sn == marker or
                             (sn == keep and event == "pull_request") else "success")
            if step.get("conclusion") != expected_step:
                errors.append("B1 wrong step conclusion " + str(sn))
    for name in found:
        if len(found[name]) != 1:
            errors.append("B1 missing/duplicate required step " + name)
    if len(found[reports]) == 1 and len(found[marker]) == 1:
        rep, mark = found[reports][0], found[marker][0]
        if rep[0] != mark[0] or rep[1] >= mark[1] or rep[2] != "success" or mark[2] != "skipped":
            errors.append("B1 KTRANS reports/marker relation")
    return errors


def run_class_absent_or_skipped(x):
    return x is None or x.get("conclusion") == "skipped"


def run_class_host_void(jobs):
    """C.6: an approved dispatch in which B4 never ran: job B absent, B4 absent, or B4 skipped."""
    jb = run_class_job(jobs, JOB_B)
    return jb is None or run_class_absent_or_skipped(run_class_step(jb, STEP_B4))


def run_class_binding_errors(entry, run, jobs, meas_dispatch_sha=None):
    """C.3, including the S1/E distinction and the expressly weaker host-VOID case."""
    errors = []
    try:
        stage, sha = entry["stage"], run["head_sha"]
        body = entry["quoted_words"]
        if stage not in ("S1", "E") or not run_class_word(body, sha) or not run_class_word(body, stage):
            errors.append("quoted commit/stage")
        if entry["head_sha"] != sha or entry["run_id"] != run["run_id"]:
            errors.append("entry/run identity")
        if (entry["approval_author"], entry["author_association"]) != OWNER:
            errors.append("approval author")
        created, edited, started = entry["approval_created_at"], entry["approval_updated_at"], run["created_at"]
        for stamp in (created, edited, started):
            run_class_time_value(stamp)
        if created >= started or (edited != created and edited >= started):
            errors.append("prior approval/edited-comment rule")
        if entry["run_attempt"] != 1 or run["run_attempt"] != 1 or run["event"] != run_class_dispatch():
            errors.append("event/attempt")
        if run.get("path") != WORKFLOW:
            errors.append("attesting workflow")
        if run_class_host_void(jobs):
            return errors
        job = run_class_job(jobs, JOB_B)
        b3 = run_class_step(job, STEP_B3)
        if job is None or b3 is None or b3.get("conclusion") != "success":
            errors.append("B3 not success")
        if stage == "S1" and meas_dispatch_sha != sha:
            errors.append("S1 measurements dispatch_sha")
    except (KeyError, TypeError, ValueError, Refused):
        errors.append("entry incomplete")
    return errors


def run_class_rule(att, approved, gate_tests, recorded_commits, nondispatch_records=None, order_s1=None):
    """C.3 classification reads actual completed job/step conclusions, never artifact mode claims."""
    key = (att["run_id"], att["run_attempt"])
    approvals = {(entry["run_id"], entry["run_attempt"]) for entry in approved}
    gates = {entry["run_id"] for entry in gate_tests}
    if att.get("attempt_status") != "completed":
        return "capture-not-completed"
    if key in approvals and key[1] == 1:
        return None
    if key[0] in gates and key[1] == 1:
        b4 = run_class_step(run_class_job(att["jobs"], JOB_B), STEP_B4)
        return None if run_class_absent_or_skipped(b4) else "gate-test B4 ran"
    if key[1] >= 2 and ((key[0], 1) in approvals or key[0] in gates):
        return None if run_class_absent_or_skipped(run_class_job(att["jobs"], JOB_B)) else "rerun job B not skipped"
    if att["event"] != run_class_dispatch() and att["head_sha"] in recorded_commits:
        ja, jb = run_class_job(att["jobs"], JOB_A), run_class_job(att["jobs"], JOB_B)
        if not run_class_absent_or_skipped(jb) or not run_class_absent_or_skipped(run_class_step(jb, STEP_B4)):
            return "non-dispatch job B/B4 ran"
        a3, marker = run_class_step(ja, STEP_A3), run_class_step(ja, STEP_A3B)
        if not run_class_absent_or_skipped(a3) and (marker is None or marker.get("conclusion") != "success"):
            return "started A3 without fixture-mode marker"
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


def run_class_pages(kind, field, values):
    """Complete one paginated listing, with stable counts and unique identities."""
    out, seen, expected, page = [], {}, None, 1
    while True:
        ok, data = gh_get(kind, *values, str(page))
        if not ok or not isinstance(data, dict):
            return None
        count, items = data.get("total_count"), data.get(field)
        if isinstance(count, bool) or not isinstance(count, int) or count < 0 or not isinstance(items, list):
            return None
        if expected is None:
            expected = count
        if count != expected:
            return None
        for item in items:
            ident = item.get("id") if isinstance(item, dict) else None
            if isinstance(ident, bool) or not isinstance(ident, int) or ident <= 0 or ident in seen:
                return None
            seen[ident] = True
            out.append(item)
        if len(out) > expected:
            return None
        if len(out) == expected:
            return out
        if not items:
            return None
        page += 1


def run_class_time_value(stamp):
    """UTC seconds from year 1; integer calendar conversion only, no external clock."""
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", stamp):
        raise Refused("UTC timestamp")
    year, month, day = int(stamp[:4]), int(stamp[5:7]), int(stamp[8:10])
    hour, minute, second = int(stamp[11:13]), int(stamp[14:16]), int(stamp[17:19])
    leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    months = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not (1 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= months[month-1]
            and 0 <= hour < 24 and 0 <= minute < 60 and 0 <= second < 60):
        raise Refused("UTC calendar")
    y = year - 1
    days = 365*y + y//4 - y//100 + y//400 + sum(months[:month-1]) + day - 1
    return ((days*24 + hour)*60 + minute)*60 + second


def run_class_time_text(value):
    days, seconds = divmod(value, 86400)
    lo, hi = 1, 10000
    while hi-lo > 1:
        mid = (lo+hi)//2
        y = mid-1
        if 365*y + y//4 - y//100 + y//400 <= days:
            lo = mid
        else:
            hi = mid
    y = lo-1
    days -= 365*y + y//4 - y//100 + y//400
    leap = lo % 4 == 0 and (lo % 100 != 0 or lo % 400 == 0)
    months = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = 1
    while days >= months[month-1]:
        days -= months[month-1]
        month += 1
    return "%04d-%02d-%02dT%02d:%02d:%02dZ" % (lo, month, days+1, seconds//3600,
                                                  seconds//60 % 60, seconds % 60)


def run_class_run_listing(kind, start, stop):
    """Partition saturated time windows; never interpret a capped listing as complete."""
    left, right = run_class_time_value(start), run_class_time_value(stop)
    if left > right:
        return None
    todo, runs, slices = [(left, right)], {}, []
    while todo:
        a, b = todo.pop(0)
        sa, sb = run_class_time_text(a), run_class_time_text(b)
        ok, first = gh_get(kind, sa, sb, "1")
        if not ok or not isinstance(first, dict):
            return None
        count = first.get("total_count")
        if isinstance(count, bool) or not isinstance(count, int) or count < 0:
            return None
        if count >= 1000:
            if a == b:
                return None
            mid = (a+b)//2
            todo[0:0] = [(a, mid), (mid+1, b)]
            continue
        listed = run_class_pages(kind, "workflow_runs", (sa, sb))
        if listed is None or len(listed) != count:
            return None
        slices.append({"window": [sa, sb], "total_count": count, "listed": len(listed)})
        for run in listed:
            if run.get("id") in runs or not sa <= run.get("created_at", "") <= sb:
                return None
            if not re.fullmatch(r"[0-9a-f]{40}", run.get("head_sha", "")):
                return None
            runs[run["id"]] = run
    return {"runs": list(runs.values()), "slices": slices}


def run_class_remote_tree(sha):
    """Read every tree blob; a truncated recursive response requires a complete subtree walk."""
    ok, tree = gh_get("tree-recursive", a_ok(sha))
    if not ok or not isinstance(tree, dict) or not isinstance(tree.get("tree"), list):
        return None
    if tree.get("truncated") is False:
        return {x["path"]: x["sha"] for x in tree["tree"] if x.get("type") == "blob"}
    if tree.get("truncated") is not True:
        return None
    out, queue = {}, [("", sha)]
    while queue:
        prefix, current = queue.pop(0)
        ok, part = gh_get("tree", a_ok(current))
        if not ok or not isinstance(part, dict) or part.get("truncated") is not False or not isinstance(part.get("tree"), list):
            return None
        for entry in part["tree"]:
            name, blob, kind = entry.get("path"), entry.get("sha"), entry.get("type")
            if not isinstance(name, str) or not re.fullmatch(r"[0-9a-f]{40}", blob or ""):
                return None
            if kind == "tree":
                queue.append((prefix+name+"/", blob))
            elif kind == "blob":
                out[prefix+name] = blob
            elif kind != "commit":
                return None
    return out


def run_class_artifact_binding(run_id, head_sha, expected=None):
    """S1 binding: full listing, exact identity/digest/member list, in-memory read only."""
    artifacts = run_class_pages("artifacts", "artifacts", (a_ok(str(run_id)),))
    if artifacts is None:
        return None
    matching = [x for x in artifacts if x.get("name") == "arp2-qc21-measurements"]
    if len(matching) != 1:
        return {"valid": False, "reason": "artifact name is absent or ambiguous"}
    artifact = matching[0]
    identity = artifact.get("workflow_run")
    if not isinstance(identity, dict) or identity.get("id") != run_id or identity.get("head_sha") != head_sha:
        return {"valid": False, "reason": "artifact run identity"}
    if artifact.get("expired") is not False or not isinstance(artifact.get("expires_at"), str):
        return {"valid": False, "reason": "expired or incomplete artifact"}
    digest = artifact.get("digest")
    if not isinstance(digest, str) or not re.fullmatch(r"sha256:[0-9a-f]{64}", digest):
        return {"valid": False, "reason": "artifact digest missing"}
    ok, blob = gh_get("artifact-zip", a_ok(str(artifact["id"])))
    if not ok:
        return {"valid": False, "reason": "archive unavailable"} if run_class_api_missing(blob) else None
    if not isinstance(blob, bytes) or sha256_bytes(blob) != digest[7:]:
        return {"valid": False, "reason": "archive digest mismatch"}
    try:
        with zipfile.ZipFile(io.BytesIO(blob)) as archive:
            members = archive.namelist()
            if members != ["measurements.json"]:
                return {"valid": False, "reason": "archive members"}
            measurements = archive.read("measurements.json")
        json.loads(measurements)
    except Exception:
        return {"valid": False, "reason": "unreadable archive"}
    record = {"id": artifact["id"], "name": artifact["name"], "digest": digest,
              "workflow_run": {"id": run_id, "head_sha": head_sha}, "expires_at": artifact["expires_at"],
              "members": members}
    if expected is not None and record != expected:
        return {"valid": False, "reason": "binding record changed"}
    return {"valid": True, "record": record, "measurements": measurements}


def run_class_comment(comment_id):
    ok, comment = gh_get("comment", a_ok(str(comment_id)))
    if not ok:
        return {"id": int(comment_id), "missing": True} if run_class_api_missing(comment) else None
    if not isinstance(comment, dict) or comment.get("id") != int(comment_id):
        return None
    return comment


def run_class_approval_entry(comment_id, run, stage):
    """Read the actual owner comment; do not trust executor-supplied quoted words or identity."""
    comment = run_class_comment(comment_id)
    if comment is None:
        return None
    return {"run_id": run["id"], "run_attempt": 1, "head_sha": run["head_sha"], "stage": stage,
            "approval_comment_id": int(comment_id), "approval_created_at": comment.get("created_at"),
            "approval_updated_at": comment.get("updated_at"),
            "approval_author": (comment.get("user") or {}).get("login"),
            "author_association": comment.get("author_association"), "quoted_words": comment.get("body")}


def run_class_designation_errors(comment, sha, first_time=None, digests=(), stage="F"):
    errors = []
    if not isinstance(comment, dict):
        return ["missing designation"]
    if ((comment.get("user") or {}).get("login"), comment.get("author_association")) != OWNER:
        errors.append("designation author")
    body = comment.get("body")
    if not re.fullmatch(r"[0-9a-f]{40}", sha) or not run_class_word(body, sha) or not run_class_word(body, stage):
        errors.append("designation commit/stage")
    if first_time is not None:
        try:
            for field in ("created_at", "updated_at"):
                stamp = comment[field]
                run_class_time_value(stamp)
                if stamp >= first_time:
                    errors.append("designation does not precede first execution")
        except (TypeError, KeyError, Refused):
            errors.append("designation timestamp")
    if any(not run_class_word(body, digest) for digest in digests):
        errors.append("designation digest")
    return errors


def run_class_fixture_mode(record):
    """The A3b structural marker; computes no fixture or decision."""
    if not isinstance(record, dict) or record.get("schema") != "arp2-qc21-measurements" or record.get("version") != 1:
        return False
    if record.get("mode") != "fixture" or record.get("complete") is not False:
        return False
    # Match the declared schema's full decisive shape, not only its mode label.
    for field in ("P", "P_controls", "C", "REP_INV"):
        if record.get(field) != "placeholder":
            return False
    b, budget, flags = record.get("B"), record.get("budget"), record.get("flags")
    if not isinstance(b, dict) or not isinstance(budget, dict) or not isinstance(flags, dict):
        return False
    if b.get("bp_equals_qmp") != "placeholder" or b.get("B1") != "placeholder":
        return False
    fragments = b.get("fragments")
    if not isinstance(fragments, list) or [x.get("name") for x in fragments if isinstance(x, dict)] != ["B-P", "A-of-B"]:
        return False
    if any(not isinstance(x, dict) or x.get("lp") != "placeholder" for x in fragments):
        return False
    if budget.get("respected") != "placeholder" or any(flags.get(x) != "placeholder" for x in ("P", "B", "C", "levels")):
        return False
    allowed = {"schema", "version", "mode", "complete", "parameters", "P", "P_controls", "REP_INV", "B", "C",
               "fixtures", "controls", "budget", "flags"}
    if set(record) != allowed:
        return False
    return True


def derive_run(run_id, bind_s1=False):
    """Every attempt, every jobs/artifacts page; optional S1 binding before E is committed."""
    ok, run = gh_get("run", a_ok(str(run_id)))
    if not ok or not isinstance(run, dict) or run.get("id") != int(run_id):
        return None
    count = run.get("run_attempt")
    if isinstance(count, bool) or not isinstance(count, int) or count < 1:
        return None
    record = {"run_id": run["id"], "head_sha": run.get("head_sha"), "event": run.get("event"),
              "created_at": run.get("created_at"), "status": run.get("status"), "conclusion": run.get("conclusion"),
              "run_attempt": count, "head_branch": run.get("head_branch"), "path": run.get("path"),
              "workflow_id": run.get("workflow_id"),
              "pull_requests": run.get("pull_requests"), "attempts": []}
    for number in range(1, count+1):
        ok, attempt = gh_get("attempt", str(run_id), str(number))
        jobs = run_class_pages("jobs", "jobs", (str(run_id), str(number)))
        if not ok or not isinstance(attempt, dict) or jobs is None:
            return None
        if attempt.get("run_attempt") != number or attempt.get("head_sha") != record["head_sha"]:
            return None
        record["attempts"].append({"run_id": run["id"], "run_attempt": number,
                                   "status": attempt.get("status"), "attempt_status": attempt.get("status"),
                                   "run_started_at": attempt.get("run_started_at"),
                                   "conclusion": attempt.get("conclusion"), "created_at": attempt.get("created_at"),
                                   "head_sha": attempt["head_sha"], "event": run.get("event"), "jobs": jobs,
                                   "path": run.get("path"), "workflow_id": run.get("workflow_id")})
    artifacts = run_class_pages("artifacts", "artifacts", (str(run_id),))
    if artifacts is None:
        return None
    record["artifacts"] = artifacts
    if bind_s1:
        binding = run_class_artifact_binding(run["id"], run["head_sha"])
        if binding is None:
            return None
        record["s1_binding"] = binding.get("record") if binding.get("valid") else binding
    ok, fresh = gh_get("run", str(run_id))
    if not ok or not isinstance(fresh, dict) or fresh.get("run_attempt") != count or fresh.get("head_sha") != record["head_sha"]:
        return None
    return record


def order_capture(t_repo, t0, now, branches):
    """Complete event/attempt inventory; no forbidden/missing result is interpreted as empty."""
    start_calls = HOST_CALLS
    capture = {"queries": [], "runs": {}, "activity": {}, "capture_time": now}
    for kind, start in (("runs-dispatch", t_repo), ("runs-all", t0)):
        listing = run_class_run_listing(kind, start, now)
        if listing is None:
            return None
        capture["queries"].append({"kind": kind, "window": [start, now], "slices": listing["slices"]})
        for run in listing["runs"]:
            if kind == "runs-all" and run.get("event") == run_class_dispatch():
                continue
            full = derive_run(str(run["id"]))
            if full is None:
                return None
            capture["runs"][str(run["id"])] = full
    for branch in branches:
        page, entries, seen = 1, [], {}
        while True:
            ok, items = gh_get("activity", a_ok(branch), str(page))
            if not ok or not isinstance(items, list):
                return None
            for entry in items:
                ident = entry.get("id") if isinstance(entry, dict) else None
                if ident is None or ident in seen:
                    return None
                seen[ident] = True
                entries.append(entry)
            if not items:
                break
            page += 1
        capture["activity"][branch] = entries
    capture["call_count"] = HOST_CALLS-start_calls
    return capture

def run_class_word(body, word):
    """Full token, not a prefix or a substring of a different commit/stage/digest."""
    if not isinstance(body, str) or not isinstance(word, str) or not word:
        return False
    # SHA/stage/digest arguments have already been restricted to letters, digits and hyphens.
    return re.fullmatch(r"(?s).*(?<![A-Za-z0-9_])"+word+r"(?![A-Za-z0-9_]).*", body) is not None


def run_class_branch_commits(branches, frozen):
    """Read all recorded branch commits; no fetch, mutation or silent missing branch."""
    commits = {}
    for branch in branches:
        result = subprocess.run(["git", "rev-list", "--end-of-options", a_ok("refs/heads/"+branch)],
                                capture_output=True, text=True)
        if result.returncode != 0:
            return None
        for sha in result.stdout.splitlines():
            if not re.fullmatch(r"[0-9a-f]{40}", sha):
                return None
            commits[sha] = True
    if not git_has(frozen) or not git_has(D_SHA):
        return None
    return commits


def run_class_run_success(run, stage):
    """Exact dispatch attestation; PR-only skips are never allowed at S1/E."""
    errors = []
    if not isinstance(run, dict) or not run.get("attempts"):
        return [stage+": missing run"]
    attempt = run["attempts"][0]
    if (run.get("path") != WORKFLOW or run.get("event") != run_class_dispatch()
            or attempt.get("run_attempt") != 1 or attempt.get("conclusion") != "success"):
        errors.append(stage+": workflow/event/attempt/conclusion")
    errors += run_class_expected_conclusions(attempt.get("jobs"), "workflow_dispatch", git_show(D_SHA, WORKFLOW))
    return errors

def run_class_approvals(data):
    if not isinstance(data, dict) or data.get("schema") != "arp2-qc21-approvals" or data.get("version") != 1:
        raise Refused("approvals schema")
    entries = data.get("entries")
    if not isinstance(entries, list):
        raise Refused("approvals entries")
    ids, runs = set(), set()
    for entry in entries:
        key = (entry["run_id"], entry["run_attempt"])
        if entry["approval_comment_id"] in ids or key in runs or entry["run_attempt"] != 1:
            raise Refused("reused approval or run identity")
        if entry["stage"] not in ("S1", "E") or not re.fullmatch(r"[0-9a-f]{40}", entry["head_sha"]):
            raise Refused("approval stage/head")
        ids.add(entry["approval_comment_id"]); runs.add(key)
    return entries


def run_class_refresh_entry(entry, record, dispatch_sha=None):
    first = record["attempts"][0]
    actual = run_class_approval_entry(entry["approval_comment_id"], {"id": record["run_id"], "head_sha": record["head_sha"]}, entry["stage"])
    if actual is None:
        raise CaptureFailed("approval comment capture failed")
    errors = []
    if actual != entry:
        errors.append("approval entry differs from actual comment")
    errors += run_class_binding_errors(actual, first, first["jobs"], dispatch_sha)
    return actual, errors


def run_class_e_entry(e_sha, comment_id, capture_time):
    """The shared e-entry/verdict builder, one unique attempt-one dispatch per approval comment."""
    ok, repo = gh_get("repo")
    if not ok or not isinstance(repo, dict):
        raise CaptureFailed("repository capture failed")
    comment = run_class_comment(comment_id)
    if comment is None:
        raise CaptureFailed("approval comment capture failed")
    listing = run_class_run_listing("runs-dispatch", comment["created_at"], capture_time)
    if listing is None:
        raise CaptureFailed("E dispatch inventory failed")
    matching = []
    for run in listing["runs"]:
        if run.get("head_sha") == e_sha and run.get("path") == WORKFLOW and run.get("created_at") > comment["created_at"]:
            matching.append(run)
    # Prior E approvals passed to verdict disambiguate retakes by ordered comment/run intervals.
    matching = sorted(matching, key=lambda item: (item["created_at"], item["id"]))
    if not matching:
        raise Refused("no E dispatch after approval")
    record = derive_run(str(matching[0]["id"]))
    if record is None or not record.get("attempts") or record["attempts"][0].get("attempt_status") != "completed":
        raise CaptureFailed("E run capture incomplete")
    entry = run_class_approval_entry(comment_id, matching[0], "E")
    errors = run_class_binding_errors(entry, record["attempts"][0], record["attempts"][0]["jobs"])
    return {"entry": entry, "entry_sha256": sha256_bytes(json.dumps(entry, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()), "errors": errors, "run": record}


def run_class_gate_errors(data, confirmation_head=None):
    """Re-read every gate-test attempt; executor-supplied expectations cannot weaken frozen cases."""
    if not isinstance(data, dict) or data.get("schema") != "arp2-qc21-gate-tests" or data.get("version") != 1:
        return ["gate-test schema"]
    entries = data.get("entries")
    if not isinstance(entries, list):
        return ["gate-test entries"]
    required = ["GT-B3", "GT-REF", "GT-RERUN", "GT-PLAIN", "GT-PR", "GT-ACT", "GT-LIST"]
    if sorted(item.get("name", "") for item in entries) != sorted(required):
        return ["gate-test frozen names"]
    errors = []
    for entry in entries:
        name = entry["name"]
        if name == "GT-ACT":
            ok, activity = gh_get("activity", a_ok(entry["branch"]), "1")
            if not ok or not isinstance(activity, list):
                raise CaptureFailed("GT-ACT host capture failed")
            if not any(item.get("id") == entry["activity_id"] and item.get("activity_type") == "force_push" for item in activity):
                errors.append("GT-ACT force movement absent")
            continue
        if name == "GT-PR":
            run_ids = entry.get("run_ids")
            if not isinstance(run_ids, list) or len(run_ids) != 2 or len(set(run_ids)) != 2:
                errors.append("GT-PR needs one pull_request and one push")
                continue
            records = [derive_run(str(ident)) for ident in run_ids]
            if any(record is None for record in records):
                raise CaptureFailed("GT-PR capture failed")
            if sorted(record["event"] for record in records) != ["pull_request", "push"]:
                errors.append("GT-PR event pair")
            for record in records:
                first = record["attempts"][0]
                if first.get("attempt_status") != "completed":
                    raise CaptureFailed("GT-PR attempt incomplete")
                if not run_class_absent_or_skipped(run_class_job(first["jobs"], JOB_B)):
                    errors.append("GT-PR job B not skipped")
            continue
        record = derive_run(str(entry["run_id"]))
        if record is None:
            raise CaptureFailed("gate run capture failed")
        if name == "GT-LIST":
            tree = run_class_remote_tree(entry["deleted_tree_sha"])
            if tree is None:
                raise CaptureFailed("GT-LIST deleted workflow tree unreadable")
            if record.get("workflow_id") != entry["workflow_id"] or entry["workflow_path"] in tree:
                errors.append("GT-LIST deleted-workflow witness")
            listing = run_class_run_listing("runs-all", record["created_at"], record["created_at"])
            if listing is None:
                raise CaptureFailed("GT-LIST runs-list capture failed")
            if not any(item["id"] == record["run_id"] for item in listing["runs"]):
                errors.append("GT-LIST run absent from repository listing")
            continue
        index = 2 if name == "GT-RERUN" else 1
        if name == "GT-RERUN" and entry["run_id"] != next(item["run_id"] for item in entries if item["name"] == "GT-B3"):
            errors.append("GT-RERUN does not re-run GT-B3")
        attempts = [attempt for attempt in record["attempts"] if attempt["run_attempt"] == index]
        if len(attempts) != 1 or attempts[0].get("attempt_status") != "completed":
            raise CaptureFailed("gate attempt incomplete")
        attempt = attempts[0]
        if confirmation_head is not None:
            actual_tree = run_class_remote_tree(record["head_sha"])
            expected_tree = run_class_remote_tree(confirmation_head)
            if actual_tree is None or expected_tree is None:
                raise CaptureFailed("gate/confirmation tree capture failed")
            if actual_tree != expected_tree:
                errors.append(name+": tree differs from confirmation")
        ja, jb = run_class_job(attempt["jobs"], JOB_A), run_class_job(attempt["jobs"], JOB_B)
        b3, b4, b6 = run_class_step(jb, STEP_B3), run_class_step(jb, STEP_B4), run_class_step(jb, STEP_B6)
        if not run_class_absent_or_skipped(b4) or not run_class_absent_or_skipped(b6):
            errors.append(name+": B4/B6 ran")
        if name in ("GT-B3", "GT-REF"):
            if jb is None or jb.get("conclusion") != "failure" or b3 is None or b3.get("conclusion") != "failure":
                errors.append(name+": B3 did not fail")
        elif not run_class_absent_or_skipped(jb):
            errors.append(name+": job B not skipped")
        if ja is None or ja.get("conclusion") != "success":
            errors.append(name+": job A not green")
        if record.get("head_branch") == ROUND_BRANCH:
            errors.append(name+": gate is on the round branch")
        if "approval_comment_id" not in entry:
            errors.append(name+": prior gate authorization absent")
        else:
            comment = run_class_comment(entry["approval_comment_id"])
            if comment is None:
                raise CaptureFailed("gate approval capture failed")
            if ((comment.get("user") or {}).get("login"), comment.get("author_association")) != OWNER:
                errors.append(name+": gate owner")
            before = attempt.get("run_started_at") if name == "GT-RERUN" else record["created_at"]
            if not isinstance(before, str) or comment.get("created_at", "Z") >= before or comment.get("updated_at", "Z") >= before:
                errors.append(name+": gate prior authorization")
            if not run_class_word(comment.get("body"), record["head_sha"]) or not run_class_word(comment.get("body"), name):
                errors.append(name+": gate authorization scope")
    return errors


def run_class_gate_attempts(data):
    records = []
    for item in data["entries"]:
        if "run_id" in item:
            records.append(item)
        for ident in item.get("run_ids", []):
            records.append({"run_id": ident, "name": item["name"]})
    return records


def run_class_api_missing(error):
    """Classify only an explicit missing-resource status; all other failures remain failed captures."""
    if isinstance(error, dict):
        return error.get("status") in (404, 410)
    return isinstance(error, str) and re.fullmatch(r"(?s).*[ (]HTTP (404|410)[)].*", error) is not None


def s_max_errors(preregistration, checker_value, stress_value):
    matches = []
    for line in preregistration.splitlines():
        text = line.strip()
        if text.startswith("- **`S_max`** = "):
            matches.append(text[len("- **`S_max`** = "):])
    if len(matches) != 1 or not re.fullmatch(r"[0-9]+", matches[0]):
        return ["P: S_max missing, duplicate or nondecimal"]
    value = int(matches[0])
    if type(checker_value) is not int or type(stress_value) is not int or value != checker_value or value != stress_value:
        return ["P: S_max three-way equality"]
    return [] if value >= S_MAX_FLOOR and value > 0 else ["P: S_max floor"]


def run_class_first_execution(runs, frozen):
    first = None
    for run in runs:
        sha = run["head_sha"]
        if run.get("head_branch") == ROUND_BRANCH and sha != frozen:
            if not git_has(sha):
                raise CaptureFailed("execution ancestry unavailable")
            if git_is_ancestor(frozen, sha):
                first = min(first, run["created_at"]) if first else run["created_at"]
    return first



def run_class_order(config, final=False):
    """Capture then classify every required event and attempt, with actual comments and complete trees."""
    if T0 is None:
        raise Refused("T0 is not frozen from D's main activity entry")
    first_call = HOST_CALLS
    frozen, capture_time = a_ok(config["F"]), a_ok(config["capture_time"])
    pins = frozen_pins(git_show(frozen, PREREG))
    if pins is None or not re.fullmatch(r"[0-9a-f]{40}", pins.get("qc21_check.py", "")):
        raise Refused("pinned checker absent")
    ok, repository = gh_get("repo")
    if not ok or not isinstance(repository, dict):
        raise CaptureFailed("repository capture failed")
    capture = order_capture(repository["created_at"], T0, capture_time, RECORDED_BRANCHES)
    if capture is None:
        raise CaptureFailed("repository event/attempt/activity capture failed")
    commits = run_class_branch_commits(RECORDED_BRANCHES, frozen)
    if commits is None:
        raise CaptureFailed("recorded branch ancestry unreadable")
    approvals = run_class_approvals(config["approvals"])
    gate_errors = run_class_gate_errors(config["gate_tests"])
    gate_entries = run_class_gate_attempts(config["gate_tests"])
    violations, trees, records = list(gate_errors), {}, []
    first_execution = None
    for sha in commits:
        tree = git_tree_blobs(sha)
        workflow = git_show(sha, WORKFLOW)
        if tree is None or workflow is None:
            raise CaptureFailed("recorded commit tree unreadable")
        text = workflow.decode()
        bearing = pins["qc21_check.py"] in tree.values() or any(name in text for name in (JOB_A, JOB_B, STEP_B4))
        if bearing and not git_is_ancestor(D_SHA, sha):
            violations.append("checker-bearing recorded commit predates D: "+sha)
    for record in capture["runs"].values():
        sha = record["head_sha"]
        if sha not in trees:
            if git_has(sha):
                tree = git_tree_blobs(sha)
                if tree is None:
                    raise CaptureFailed("local tree capture failed")
                trees[sha] = {"source": "local", "blobs": tree}
            else:
                tree = run_class_remote_tree(sha)
                if tree is None:
                    raise CaptureFailed("API tree capture failed")
                trees[sha] = {"source": "api", "blobs": tree}
        for attempt in record["attempts"]:
            if not run_class_checker_bearing(attempt["jobs"], trees[sha]["blobs"], pins["qc21_check.py"]):
                continue
            if attempt.get("attempt_status") != "completed":
                raise CaptureFailed("checker-bearing attempt still pending")
            reason = run_class_rule(attempt, approvals, gate_entries, commits)
            if reason is not None:
                violations.append({"run_id": attempt["run_id"], "run_attempt": attempt["run_attempt"], "reason": reason})
            if attempt["event"] != run_class_dispatch():
                ja, jb = run_class_job(attempt["jobs"], JOB_A), run_class_job(attempt["jobs"], JOB_B)
                records.append({"run_id": attempt["run_id"], "run_attempt": attempt["run_attempt"], "head_sha": sha,
                                "event": attempt["event"], "attempt_status": attempt["attempt_status"],
                                "jobB_conclusion": jb.get("conclusion") if jb else None,
                                "B4_conclusion": (run_class_step(jb, STEP_B4) or {}).get("conclusion"),
                                "A3_conclusion": (run_class_step(ja, STEP_A3) or {}).get("conclusion"),
                                "A3b_conclusion": (run_class_step(ja, STEP_A3B) or {}).get("conclusion"),
                                "fixtures_artifact_digest": [a.get("digest") for a in record["artifacts"] if a.get("name") == "arp2-qc21-fixtures"]})
    refreshed = []
    for entry in approvals:
        run = capture["runs"].get(str(entry["run_id"]))
        if run is None:
            violations.append("approved run absent from complete capture")
            continue
        actual, errors = run_class_refresh_entry(entry, run, config.get("S1"))
        refreshed.append(actual)
        violations += ["approval "+str(entry["approval_comment_id"])+": "+error for error in errors]
    for entries in capture["activity"].values():
        violations += run_class_activity_violations(entries)
    first_execution = run_class_first_execution(list(capture["runs"].values()), frozen)
    designation = run_class_comment(config["F_designation_comment_id"])
    if designation is None:
        raise CaptureFailed("F designation capture failed")
    if first_execution is None:
        raise Refused("first post-F execution run not found")
    violations += run_class_designation_errors(designation, frozen, first_execution)
    capture.update({"schema": "arp2-qc21-order", "version": 1, "F": frozen, "T0": T0,
                    "final_capture": final, "trees": trees, "nondispatch": records, "approvals": refreshed,
                    "F_designation": designation, "first_execution_created_at": first_execution,
                    "violations": violations, "call_count": HOST_CALLS-first_call, "operational_condition_only": True})
    return capture


def frozen_pins(raw):
    """Pins live in F's preregistration, avoiding a self-referential controls.py blob constant."""
    if raw is None:
        return None
    try:
        text = raw.decode() if isinstance(raw, bytes) else raw
        blocks = fenced(text, "qc21-implementation-pins")
        if len(blocks) != 1:
            return None
        data = json.loads("\n".join(blocks[0]))
        if data.get("schema") != "arp2-qc21-pins" or data.get("version") != 1:
            return None
        pins = dict(data["blobs"])
        pins.update(data["sha256"])
        for name in ("qc21_check.py", "controls.py"):
            pins[name+".sha256"] = data["script_sha256"][name]
        if set(pins) != set(PINS) | {"qc21_check.py.sha256", "controls.py.sha256"}:
            return None
        return pins
    except (ValueError, TypeError, KeyError, AttributeError):
        return None


def v3_working_copy_ok():
    """Compare actual working bytes to the pinned D object before the only Python subprocess starts."""
    path = "tools/v3_verifier.py"
    pin = INPUTS.get(path)
    if not isinstance(pin, str) or not re.fullmatch(r"[0-9a-f]{40}", pin) or git_blob(D_SHA, path) != pin:
        return False
    source = git_show(D_SHA, path)
    try:
        return source is not None and read_bytes(path) == source
    except OSError:
        return False


def checker_literals(source):
    values = {}
    for node in ast.parse(source).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            if name in ("P_MAX", "B_MAX", "W_MAX", "BP_P_MAX", "BP_B_MAX", "BP_W_MAX", "BP_CAP_GENERATORS",
                        "BP_CAP_D", "BP_CAP_FACET_SUBSETS", "BP_CAP_EFFECTS", "S_MAX", "CAP_GENERATORS", "CAP_D",
                        "CAP_FACET_SUBSETS", "CAP_EFFECTS", "SOURCE_BASE"):
                values[name] = ast.literal_eval(node.value)
    return values


def run_class_design_record_errors(record, pins, confirmation=False):
    errors = []
    if record.get("event") != "pull_request" or record.get("path") != WORKFLOW:
        errors.append("design/confirmation event or workflow")
    if not record.get("attempts") or record["attempts"][0].get("conclusion") != "success":
        return errors+["design/confirmation attempt one not green"]
    pull_requests = record.get("pull_requests")
    if not isinstance(pull_requests, list) or len(pull_requests) != 1:
        errors.append("synthetic merge missing unique PR identity")
    else:
        pr = pull_requests[0]
        if pr.get("base", {}).get("sha") != D_SHA or pr.get("head", {}).get("sha") != record.get("head_sha"):
            errors.append("synthetic merge base/head binding")
        if not git_is_ancestor(D_SHA, record["head_sha"]):
            errors.append("design/confirmation head does not descend from D")
    attempt = record["attempts"][0]
    errors += run_class_expected_conclusions(attempt.get('jobs'), 'pull_request', git_show(D_SHA, WORKFLOW))
    ja = run_class_job(attempt["jobs"], JOB_A)
    for name in (STEP_A3, STEP_A3B, STEP_A7):
        if (run_class_step(ja, name) or {}).get("conclusion") != "success":
            errors.append("design/confirmation required marker "+name)
    errors += code_w(record["head_sha"])
    if confirmation:
        errors += code_b(record["head_sha"], pins)
    return errors


def freeze_checks(frozen, record_commit):
    errors = []
    raw = git_show(frozen, PREREG)
    pins = frozen_pins(raw)
    if pins is None:
        return ["P: frozen pin table missing/invalid"], None
    for key, value in pins.items():
        width = 40 if key in ("qc21_check.py", "controls.py") else 64
        if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{"+str(width)+r"}", value):
            errors.append("P: unresolved pin "+key)
    records = {}
    for name in ("stress.json", "design-run.json", "gate-tests.json", "confirmation-run.json"):
        data = git_show(record_commit, RDIR+"evidence/"+name)
        if data is None and record_commit == frozen:
            try:
                data = read_bytes(RDIR+"evidence/"+name)
            except OSError:
                data = None
        if data is None:
            errors.append("R: missing "+name)
            continue
        if sha256_bytes(data) != pins.get(name):
            errors.append("P: evidence pin "+name)
        try:
            records[name] = json.loads(data)
        except (ValueError, TypeError):
            errors.append("R: unparseable "+name)
    for name in ("design-run.json", "confirmation-run.json"):
        record = records.get(name)
        if not isinstance(record, dict):
            continue
        actual = derive_run(str(record["run_id"]))
        if actual is None:
            raise CaptureFailed("design/confirmation host re-derivation failed")
        if canonical(record) != canonical(actual):
            errors.append("R: "+name+" disagrees with host re-derivation")
        errors += run_class_design_record_errors(actual, pins, name == "confirmation-run.json")
    confirmation = records.get("confirmation-run.json")
    stress = records.get("stress.json")
    design = records.get("design-run.json")
    if confirmation and stress and design:
        source = git_show(confirmation["head_sha"], CHECKER)
        if source is None:
            errors.append("P: confirmation checker unreadable")
        else:
            literals = checker_literals(source.decode())
            if literals.get("SOURCE_BASE") != D_SHA:
                errors.append("P: execution source is not bound to the authorized round D")
            errors += s_max_errors(raw.decode(), literals.get("S_MAX"), stress.get("S_max"))
            ja = run_class_job(design["attempts"][0]["jobs"], JOB_A)
            stress_step = run_class_step(ja, "ARP-2-QC21 stress")
            a8 = run_class_step(ja, "ARP-2-QC21 checker self-test")
            a9 = run_class_step(ja, "ARP-2-QC21 control mutation tests")
            if any(step is None for step in (stress_step, a8, a9)):
                errors.append("P: design timing steps missing")
            else:
                durations = [run_class_time_value(step["completed_at"])-run_class_time_value(step["started_at"])
                             for step in (stress_step, a8, a9)]
                selected = freeze_budget_rule(stress, durations[0], durations[1]+durations[2])
                actual_general = [literals.get(key) for key in ("P_MAX", "B_MAX", "W_MAX")]
                actual_bp = [literals.get(key) for key in ("BP_P_MAX", "BP_B_MAX", "BP_W_MAX")]
                actual_caps = [literals.get(key) for key in ("BP_CAP_GENERATORS", "BP_CAP_D", "BP_CAP_FACET_SUBSETS", "BP_CAP_EFFECTS")]
                if [actual_general, actual_bp, actual_caps] != [selected["general"], selected["BP"], selected["BP_caps"]]:
                    errors.append("P: constants differ from mechanical budget/cap recomputation")
                if not selected["timeout_pass"]:
                    errors.append("P: exact timeout test fails")
                records["recomputed_resource_rule"] = selected
    if "gate-tests.json" in records:
        errors += run_class_gate_errors(records["gate-tests.json"], confirmation.get("head_sha") if confirmation else None)
    for name, digest in STAB_CERTS.items():
        data = git_show(record_commit, RDIR+name)
        if data is None or sha256_bytes(data) != digest:
            errors.append("P: mandatory STAB certificate "+name)
    return errors, records


def run_class_retakes(entries, records, retakes, attesters):
    """A host-VOID replacement requires its posted immutable record and a later fresh owner decision."""
    errors = []
    pairs = {(x["replaced_run_id"], x["replacement_run_id"]): x for x in retakes}
    for stage in ("S1", "E"):
        ordered = sorted([entry for entry in entries if entry["stage"] == stage],
                         key=lambda entry: (records[str(entry["run_id"])]["created_at"], entry["run_id"]))
        if not ordered or ordered[-1]["run_id"] != attesters[stage]:
            errors.append(stage+": last authorized dispatch is not the attester")
            continue
        for old, new in zip(ordered, ordered[1:]):
            old_run, new_run = records[str(old["run_id"])], records[str(new["run_id"])]
            if not run_class_host_void(old_run["attempts"][0]["jobs"]):
                errors.append("checker outcome cannot be retaken")
                continue
            retake = pairs.get((old["run_id"], new["run_id"]))
            if retake is None or old["run_id"] == new["run_id"]:
                errors.append("fresh retake decision absent")
                continue
            posted = run_class_comment(retake["void_record_comment_id"])
            decision = run_class_comment(retake["decision_comment_id"])
            if posted is None or decision is None:
                raise CaptureFailed("retake provenance capture failed")
            try:
                blocks = fenced(posted["body"], "json")
                if len(blocks) != 1:
                    raise ValueError("one posted void record")
                raw = canonical(json.loads("\n".join(blocks[0]))).encode()
                if json.loads(raw) != old_run or sha256_bytes(raw) != retake["void_record_sha256"]:
                    errors.append("posted void record not bound to actual host record")
                if not run_class_word(posted["body"], retake["void_record_sha256"]):
                    errors.append("posted void digest absent")
                if not (posted["updated_at"] < decision["created_at"] < new_run["created_at"]
                        and decision["updated_at"] < new_run["created_at"]):
                    errors.append("retake decision/record order")
                if ((decision.get("user") or {}).get("login"), decision.get("author_association")) != OWNER:
                    errors.append("retake decision owner")
                if not run_class_word(decision["body"].lower(), "retake") or not run_class_word(decision["body"], new["head_sha"]):
                    errors.append("retake decision does not identify fresh dispatch")
            except (ValueError, TypeError, KeyError):
                errors.append("malformed retake provenance")
    return errors


def token_line(measurements):
    result = decide(measurements)
    if "VOID" in result:
        return None
    return "%s %s %s level %s" % (result["P"], result["B"], result["C"], result["level"])


def run_class_verdict(config):
    """Complete final host-time gate. Captures fail separately; round-level failures alone yield VOID."""
    try:
        frozen, s1, evidence = a_ok(config["F"]), a_ok(config["S1"]), a_ok(config["E"])
        errors = check_mode(evidence, frozen, "E")
        measurement_bytes = git_show(evidence, MEAS)
        if measurement_bytes is None:
            return {"verdict": "VERDICT VOID", "errors": errors+["missing measurements"]}
        measurements = json.loads(measurement_bytes)
        committed_order_bytes = git_show(evidence, RDIR+"evidence/order.json")
        approval_bytes = git_show(evidence, RDIR+"evidence/approvals.json")
        gate_bytes = git_show(evidence, RDIR+"evidence/gate-tests.json")
        s1_bytes = git_show(evidence, RDIR+"evidence/s1-run/results.json")
        if any(value is None for value in (committed_order_bytes, approval_bytes, gate_bytes, s1_bytes)):
            return {"verdict": "VERDICT VOID", "errors": errors+["missing required committed evidence"]}
        approvals = run_class_approvals(json.loads(approval_bytes))
        if any(entry["stage"] != "S1" for entry in approvals):
            errors.append("pre-E committed entries contain another stage")
        ids = config["E_approval_comment_ids"]
        if not isinstance(ids, list) or not ids or len(set(ids)) != len(ids):
            errors.append("missing/reused E approval comment ids")
            ids = []
        e_results = [run_class_e_entry(evidence, ident, config["capture_time"]) for ident in ids]
        e_entries = [result["entry"] for result in e_results]
        for result in e_results:
            errors += result["errors"]
        all_entries = run_class_approvals({"schema": "arp2-qc21-approvals", "version": 1, "entries": approvals+e_entries})
        order_config = dict(config, approvals={"schema": "arp2-qc21-approvals", "version": 1, "entries": all_entries},
                            gate_tests=json.loads(gate_bytes))
        capture = run_class_order(order_config)
        errors += capture["violations"]
        s1_run = capture["runs"].get(str(config["S1_run_id"]))
        e_run = capture["runs"].get(str(config["E_run_id"]))
        if s1_run is None or e_run is None:
            errors.append("attesting runs missing from complete inventory")
        else:
            if s1_run["head_sha"] != s1 or e_run["head_sha"] != evidence:
                errors.append("attesting exact heads")
            if s1_run["event"] != run_class_dispatch() or e_run["event"] != run_class_dispatch():
                errors.append("attesting events")
            errors += run_class_run_success(s1_run, "S1")+run_class_run_success(e_run, "E")
            stored = json.loads(s1_bytes)
            if stored.get("run_id") != s1_run["run_id"] or stored.get("head_sha") != s1:
                errors.append("committed S1 run identity")
            expected = stored.get("s1_binding")
            if not isinstance(expected, dict) or "id" not in expected:
                errors.append("committed S1 binding absent")
            else:
                binding = run_class_artifact_binding(s1_run["run_id"], s1, expected)
                if binding is None:
                    raise CaptureFailed("S1 artifact capture failed; retry without shortening inventory")
                if binding.get("valid") is not True or not replay_compare(binding.get("measurements", b"null"), measurement_bytes):
                    errors.append("S1 archive/committed measurements binding")
            errors += run_class_retakes(all_entries, capture["runs"], config.get("retakes", []),
                                       {"S1": s1_run["run_id"], "E": e_run["run_id"]})
        designation = run_class_comment(config["E_designation_comment_id"])
        if designation is None:
            raise CaptureFailed("E designation capture failed")
        order_digest = sha256_bytes(committed_order_bytes)
        errors += run_class_designation_errors(designation, evidence, digests=[order_digest]+[x["entry_sha256"] for x in e_results], stage="E")
        committed = json.loads(committed_order_bytes)
        if committed.get("violations") or committed.get("F") != frozen:
            errors.append("committed order provenance")
        line = token_line(measurements)
        note = git_show(evidence, RDIR+"result.md")
        expected_note = make_note(measurements, D_SHA, frozen, s1, evidence).encode()
        if line is None or note != expected_note:
            errors.append("note regeneration/token/schema agreement")
        return {"verdict": "VERDICT "+line if not errors else "VERDICT VOID", "errors": errors,
                "capture": capture, "E_entries": [{"entry": x["entry"], "entry_sha256": x["entry_sha256"]} for x in e_results],
                "E_designation": designation, "order_sha256": order_digest,
                "scope": "Required operational landing condition; no enduring assertion about unretained host checks."}

    except (Refused, OSError, ValueError, TypeError, KeyError, IndexError, AttributeError) as error:
        return {"verdict": "VERDICT VOID", "errors": ["invalid round evidence: "+str(error)]}


def verdict_mode(meas, expected_token_line, ratified_sha, order_sha, s1_run, e_run, capture_violations):
    """Pure final predicate retained for synthetic tests; real CLI uses run_class_verdict's host checks."""
    errors = []
    if ratified_sha != order_sha:
        errors.append("designation digest")
    errors += run_class_run_success(s1_run, "S1")+run_class_run_success(e_run, "E")
    if capture_violations:
        errors.append("capture violations")
    line = token_line(meas)
    if line is None or line != expected_token_line:
        errors.append("token/schema/flags agreement")
    return ("VERDICT "+line) if not errors else "VERDICT VOID", errors


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
    bad_role = chk.replace('f.get("role") == "B-P"', 'f.get("role") == "A-of-B"', 1)
    ck("C-IFACE rejects report-only B selector", bad_role != chk and bool(c_iface(bad_role, own)))
    bad_comparison = chk.replace('def k_decide_levels(rec):', 'def k_decide_levels(rec):\n    x = rec.get("bp_equals_qmp")', 1)
    ck("C-IFACE rejects comparator in levels", bool(c_iface(bad_comparison, own)))
    bad_ada = own+'\ndef ada_bad(m):\n    return m["B"]["bp_equals_qmp"]\n'
    ck("C-IFACE rejects comparator in ADA", bool(c_iface(chk, bad_ada)))
    helpers = "\ndef a_ok(x):\n    return x\n\ndef w_path(t, n):\n    return n\n\ndef root_check():\n    return 0\n"
    for name, snip in BYP.items():
        ck("control B fails " + name, static_controls(snip + helpers) != [])
    ck("control B rejects an unvalidated gh f-string", static_controls(
        "import subprocess\nsubprocess.run(['gh','api','--method','GET',f'repos/amaybaum/incompleteness/issues/comments/{x}'])"+helpers) != [])
    ck("control B passes a clean snippet", static_controls(
        "import subprocess\nsubprocess.run(['git', 'rev-parse', '--verify', '--end-of-options', a_ok(x)])" + helpers) == [])
    muts = {
        "a second dispatch constant": chk.replace("ROUND_REF = ", "X_EV = \"workflow_" + "dispatch\"\nROUND_REF = ", 1),
        "alias in a self-test": chk.replace("def t_misc():\n", "def t_misc():\n    b = s_build_p\n", 1),
        "second self-test referencing the gated entry": chk.replace("def t_misc():\n",
                                                                    "def t_misc():\n    x = s_decisive\n", 1),
        "t_builder_refuses extra statement": chk.replace("def t_builder_refuses():\n",
                                                         "def t_builder_refuses():\n    pass\n", 1),
        "globals()[...]": chk.replace("def t_misc():\n", "def t_misc():\n    globals()['s_build_p']()\n", 1),
        "getattr(...)": chk.replace("def t_misc():\n", "def t_misc():\n    getattr(sys, 'x')\n", 1),
        "dunder walk": chk.replace("def t_misc():\n", "def t_misc():\n    ().__class__\n", 1),
        "third os site": chk.replace("def t_misc():\n", "def t_misc():\n    s_mode([], os.environ)\n", 1),
        "builder without refusal": chk[:chk.index("def s_build_c(")] + chk[chk.index("def s_build_c("):].replace("    s_refusal()\n", "", 1),
        "positional-only refusal": chk.replace("def s_refusal():", "def s_refusal(unused=0, /):", 1),
        "aliased set": chk.replace("def t_misc():\n", "def t_misc():\n    collection_type = set\n    collection_type()\n", 1),
        "relocated main environment": chk.replace("status, text = s_entry(sys.argv, os.environ)",
            "status, text = s_entry(sys.argv, {})", 1).replace("def t_misc():\n", "def t_misc():\n    s_mode([], os.environ)\n", 1),
    }
    for name, src in muts.items():
        ck("name rules fail: " + name, src != chk and static_checker(src) != [])
    alias = chk.replace("def v_unique(values):", "v_shared = ordered_unique\n\ndef v_unique(values):\n    return v_shared(values)", 1)
    ck("M-INDEP prefixed module alias", alias != chk and c_indep(alias) != [])
    default_alias = chk + "\ndef s_bind(_=(v_unique := ordered_unique)):\n    pass\n"
    ck("M-INDEP definition-time alias", default_alias != chk and c_indep(default_alias) != [])
    for name, mutant in (("mode", own.replace("zipfile.ZipFile(io.BytesIO(blob))", "zipfile.ZipFile(io.BytesIO(blob), 'w')", 1)),
                         ("path", own.replace("zipfile.ZipFile(io.BytesIO(blob))", "zipfile.ZipFile('path')", 1)),
                         ("member", own.replace('archive.read("measurements.json")', 'archive.read("other.json")', 1))):
        ck("ZIP mutation " + name, mutant != own and static_controls(mutant) != [])
    ck("M-INDEP direct call", c_indep(chk.replace("def v_rank(rows):\n", "def v_rank(rows):\n    s_rank(rows)\n", 1)) != [])
    ck("M-INDEP default argument", c_indep(chk.replace("def v_rank(rows):", "def v_rank(rows, x=s_decide):", 1)) != [])
    ck("M-INDEP nested lambda", c_indep(chk.replace("def v_rank(rows):\n",
                                                    "def v_rank(rows):\n    f = lambda: s_rank(rows)\n", 1)) != [])
    ck("C-EXACT float literal", c_exact(chk.replace("CAP_D = 16", "CAP_D = 16.0", 1)) != [])
    ck("C-EXACT '/' outside the helper", c_exact(chk.replace("def fstr(x):\n", "def fstr(x):\n    y = 1 / 2\n", 1)) != [])
    ck("C-IFACE mutation (carrier slot into the screen input)",
       c_iface(chk.replace('if r["kept"] and r["port"] == 0) / tot', 'if r["kept"] and r["carrier"][0] == 0) / tot')
               .replace('r["kept"] and r["port"] == 0), tot)', 'r["kept"] and r["carrier"][0] == 0), tot)', 1), own) != [])
    ck("C-IFACE mutation (decide-c reads STAB)", c_iface(chk.replace(
        'def k_decide_c(rec):\n', 'def k_decide_c(rec):\n    _ = rec.get("STAB")\n', 1), own) != [])
    ck("C-IFACE mutation (decide-levels reads STAB)", c_iface(chk, own.replace(
        'def decide_levels(p_tok, b_ctx, b_eq, acc_owner, c_tok, imported):\n',
        'def decide_levels(p_tok, b_ctx, b_eq, acc_owner, c_tok, imported):\n    _ = "STAB"\n', 1)) != [])
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
        "event key (B4)": ("(github.event_name == '" + run_class_dispatch() + "' && github.run_attempt == '1' && " + REF_KEY,
                           "(github.run_attempt == '1' && " + REF_KEY),
        "attempt key (B6)": ("github.run_attempt == '1' && " + REF_KEY + " && " + RECEIPT_KEY + ") }}",
                             REF_KEY + " && " + RECEIPT_KEY + ") }}"),
        "ref key (B4/B6)": (" && " + REF_KEY, ""),
        "receipt key (B4/B6)": (" && " + RECEIPT_KEY + ")", ")"),
        "job B if": ("    if: " + SPLICE_JOB_B_IF + "\n", ""),
        "job B if: decisive input": (" && inputs.arp2qc21_decisive == true", ""),
        "B3": ("        run: " + B3_RUN + "\n", "        run: 'true'\n"),
        "B3 ref key": (' && test "$GITHUB_REF" = refs/heads/research/arp2-qc21-20261108', ""),
        "A3 literal": (" --event fixture >", " --event \"$X\" >"),
        "A3b marker": ("      - name: "+STEP_A3B+"\n", "      - name: wrong marker\n"),
        "A3b always": ("        if: ${{ always() }}\n", ""),
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
                              "lp_reads_equal_acc": True, "preps": 32,
                              "lp_settings": ["M"+a+b for a in ("0", "1", "2") for b in ("0", "1", "2")],
                              "acc": ["M"+a+b for a in ("0", "1", "2") for b in ("0", "1", "2")]}]},
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
        dict(synthetic_meas()["B"]["fragments"][0], lp="feasible")]})[0]
       == "B-CLASSICALLY-IMITABLE")
    for role in ("A-of-B", "completion", "B-C"):
        for outcome in ("out_of_scope", "undecided"):
            mm = synthetic_meas()
            mm["B"]["fragments"].append({"name": "reported", "role": role, "lp": outcome, "verified": False})
            ck("report-only "+role+" "+outcome, decide(mm).get("B") == "B-CONTEXTUAL")
    mm = synthetic_meas()
    mm["B"]["fragments"][0]["preps"] = 16
    mm["flags"].update({"B": "B-VOID", "levels": {"level": 1}})
    ck("SG-1 rejects sixteen preps, preserves Level 1", decide(mm).get("B") == "B-VOID" and decide(mm).get("level") == 1)
    for outcome in ("undecided", "out_of_scope"):
        mm = synthetic_meas()
        mm["B"]["fragments"][0].update({"lp": outcome, "verified": False})
        mm["flags"].update({"B": "B-VOID", "levels": {"level": 1}})
        ck("B-P "+outcome+" leaves Level 1", decide(mm).get("level") == 1 and "VOID" not in decide(mm))
    mm = synthetic_meas()
    mm["B"]["fragments"][0]["lp"] = "feasible"
    mm["flags"].update({"B": "B-CLASSICALLY-IMITABLE", "C": "C-VOID", "levels": {"level": 1}})
    mm["flags"]["controls_red"]["C"] = ["C-DET"]
    ck("C-VOID preserves Level 1", decide(mm).get("C") == "C-VOID" and decide(mm).get("level") == 1)
    for defect in ("certificate", "budget"):
        mm = synthetic_meas()
        reported = {"name": "reported", "role": "A-of-B", "lp": "feasible", "verified": True}
        if defect == "certificate":
            reported["verified"] = False
        else:
            reported.update({"budget_values": [1, 1, 1], "pivots": 2, "max_bits": 1, "work": 1})
        mm["B"]["fragments"].append(reported)
        mm["flags"].update({"B": "B-VOID", "levels": {"level": 1}})
        ck("leaked report-only verdict "+defect, decide(mm).get("B") == "B-VOID")
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


def synthetic_stress():
    """Fabricated record metadata only: no seeded laws or solver invocation."""
    records = []
    for seed in (20261108, 1, 2):
        for kind, role in (("SF-1", "ST-BP"), ("SF-2", "stress")):
            records.append({"name": kind+"/"+str(seed), "class": role, "seed": seed,
                            "verdict": "feasible", "decided_by": 2, "pivots": 1, "max_bits": 2, "work": 3,
                            "certificate_verified": True, "certificate": {}, "over_maximum": False,
                            "n_distinct": 4, "n_extreme": 4, "d": 2, "c": 4, "reduction_verified": True})
    records.append({"name": "synthetic-fixture", "class": "fixture", "seed": None,
                    "verdict": "feasible", "decided_by": 2, "pivots": 2, "max_bits": 3, "work": 4,
                    "certificate_verified": True, "certificate": {}, "over_maximum": False})
    return {"schema": "arp2-qc21-stress", "version": 2, "seeds": [20261108, 1, 2],
            "S_max": 100000, "fragments": records, "W_fix": 4, "W_stress": 18}


def selftest_files():
    good = synthetic_stress()
    ck("stress schema synthetic", stress_validate(good)[0])
    for flag, count in ((False, 100001), (True, 4)):
        bad = json.loads(canonical(good))
        bad["fragments"][0].update({"over_maximum": flag, "c": count})
        ck("ST-BP bilateral maximum "+str(flag), not stress_validate(bad)[0])
    missing_step = json.loads(canonical(good))
    del missing_step["fragments"][-1]["decided_by"]
    ck("stress requires C-SYM deciding step", not stress_validate(missing_step)[0])
    selected = freeze_budget_rule(good, 1, 0)
    ck("budget exact general maxima", selected["general"] == [6, 9, 12])
    ck("budget stable seed-order tie", selected["reference"] == "SF-1/20261108")
    ck("budget report-only volume", selected["reported_only_volume"] == 1203)
    ck("budget fallback timeout fails without added budget", freeze_budget_rule(good, 100, 0)["timeout_pass"] is False)
    a = canonical(synthetic_meas()).encode()
    b = canonical(synthetic_meas(parameters={"dispatch_sha": "1"*40})).encode()
    ck("replay compares with only dispatch_sha omitted", replay_compare(a, b))
    ck("replay changed complete flag", not replay_compare(a, canonical(synthetic_meas(complete=False)).encode()))
    ck("replay malformed bytes", not replay_compare(a, b"{"))


def selftest_runs():
    yes = {"name": JOB_B, "conclusion": "success", "steps": [{"name": STEP_B3, "conclusion": "success"},
                                                               {"name": STEP_B4, "conclusion": "success"}]}
    skip = {"name": JOB_B, "conclusion": "skipped", "steps": []}
    marker = {"name": JOB_A, "conclusion": "failure", "steps": [{"name": STEP_A3, "conclusion": "failure"},
                                                                   {"name": STEP_A3B, "conclusion": "success"}]}
    att = {"run_id": 1, "run_attempt": 1, "head_sha": "a"*40, "path": WORKFLOW,
           "created_at": "2026-11-10T01:00:00Z", "event": run_class_dispatch(), "attempt_status": "completed", "jobs": [yes]}
    entry = {"run_id": 1, "run_attempt": 1, "head_sha": "a"*40, "stage": "S1", "approval_comment_id": 10,
             "approval_created_at": "2026-11-10T00:00:00Z", "approval_updated_at": "2026-11-10T00:00:00Z",
             "approval_author": OWNER[0], "author_association": OWNER[1], "quoted_words": "Authorize S1 "+"a"*40}
    ck("approval exact S1", run_class_binding_errors(entry, att, att["jobs"], "a"*40) == [])
    ck("E binding does not compare to S1 dispatch input", run_class_binding_errors(dict(entry, stage="E", quoted_words="Authorize E "+"a"*40), att, att["jobs"], "b"*40) == [])
    for key, value in (("approval_created_at", "2026-11-10T02:00:00Z"),
                       ("approval_updated_at", "2026-11-10T02:00:00Z"), ("approval_author", "other"),
                       ("author_association", "MEMBER"), ("quoted_words", "Authorize S1 "+"b"*40)):
        ck("approval rejects "+key, bool(run_class_binding_errors(dict(entry, **{key: value}), att, att["jobs"], "a"*40)))
    ck("host VOID permits failed B3", run_class_binding_errors(entry, att, [{"name": JOB_B, "conclusion": "failure",
            "steps": [{"name": STEP_B3, "conclusion": "failure"}, {"name": STEP_B4, "conclusion": "skipped"}]}], "a"*40) == [])
    ck("missing B4 conclusion is checker outcome", not run_class_host_void([dict(yes, conclusion="timed_out", steps=[{"name": STEP_B4, "conclusion": None}])]))
    approved = [entry]
    ck("approved first attempt", run_class_rule(att, approved, [], {}) is None)
    ck("rerun B skipped", run_class_rule(dict(att, run_attempt=2, jobs=[skip]), approved, [], {}) is None)
    ck("rerun B started", run_class_rule(dict(att, run_attempt=2), approved, [], {}) is not None)
    passive = dict(att, event="pull_request", jobs=[marker, skip])
    ck("red A3 fixture mode is permitted", run_class_rule(passive, [], [], {"a"*40: True}) is None)
    missing = dict(marker, steps=[{"name": STEP_A3, "conclusion": "failure"}])
    ck("started A3 missing marker violates", run_class_rule(dict(passive, jobs=[missing, skip]), [], [], {"a"*40: True}) is not None)
    ck("A3 never started", run_class_rule(dict(passive, jobs=[skip]), [], [], {"a"*40: True}) is None)
    ck("pending record is not a completed verdict", run_class_rule(dict(passive, attempt_status="queued"), [], [], {"a"*40: True}) == "capture-not-completed")
    ck("unapproved dispatch", run_class_rule(att, [], [], {}) is not None)
    designation = {"id": 9, "user": {"login": OWNER[0]}, "author_association": OWNER[1],
                   "created_at": "2026-11-10T00:00:00Z", "updated_at": "2026-11-10T00:00:00Z", "body": "Designate F "+"f"*40}
    ck("F designation precedes execution", run_class_designation_errors(designation, "f"*40, att["created_at"]) == [])
    ck("F wrong commit", bool(run_class_designation_errors(designation, "e"*40, att["created_at"])))
    ck("F wrong stage", bool(run_class_designation_errors(dict(designation, body="Designate E "+"f"*40), "f"*40, att["created_at"])))
    ck("F post-run edit", bool(run_class_designation_errors(dict(designation, updated_at="2026-11-10T02:00:00Z"), "f"*40, att["created_at"])))
    ck("E designation missing digest", bool(run_class_designation_errors(dict(designation, body="Designate E "+"e"*40), "e"*40, digests=["1"*64], stage="E")))
    ck("activity force move", bool(run_class_activity_violations([{"activity_type": "force_push"}])))


def selftest_stab():
    res = stab_false_check()
    present = [rel for rel, r in res.items() if r.get("reason") != "absent"]
    if R12_STAB or present:
        for rel, r in sorted(res.items()):
            ck("STAB-FALSE on " + rel, r["green"])
    bad = {"q": "1/2", "P": {k: "0" for k in ("1,1,1", "1,1,-1", "1,-1,1", "1,-1,-1", "-1,1,1", "-1,1,-1",
                                             "-1,-1,1", "-1,-1,-1")}, "G": {}}
    ident = {"K": 1, "q": "1", "B": [["1" if i == j else "0" for j in range(16)] for i in range(16)]}
    r = stab_false_control(ident)
    ck("STAB-FALSE is not green on the identity branch (STAB true)", r["STAB"] is True and not r["green"])
    ck("STAB-FALSE rejects a zero branch", not stab_false_control(bad)["green"])


def self_test():
    del LOG[:]
    selftest_git()
    selftest_static()
    selftest_w()
    selftest_decide()
    selftest_files()
    selftest_runs()
    selftest_stab()
    bad = [n for n, okv in LOG if not okv]
    for n, okv in LOG:
        sys.stdout.write("%s %s\n" % ("PASS" if okv else "FAIL", n))
    sys.stdout.write("%d checks, %d failed\n" % (len(LOG), len(bad)))
    return 0 if not bad else 1


def control_main(argv):
    """Read-only CLI. All outputs go to stdout; the executor retains them using explicit redirects."""
    try:
        root_check()
        if len(argv) < 2:
            raise Refused("mode required")
        mode = argv[1]
        if mode == "--self-test":
            return self_test()
        if mode == "fixture-mode-check":
            record = json.loads(read_bytes(argv[2]))
            good = run_class_fixture_mode(record)
            sys.stdout.write(canonical({"fixture_mode": good}))
            return 0 if good else 1
        if mode == "stress-check":
            pins = frozen_pins(read_bytes(PREREG))
            pin = pins.get("stress.json") if pins else None
            good, info = stress_check(argv[2], pin)
            sys.stdout.write(canonical({"stress_check": good, "sha256_or_reason": info, "pin_present": pin is not None}))
            return 0 if good else 1
        if mode == "replay":
            if not os.path.isfile(MEAS):
                sys.stdout.write('{"replay":"not-applicable"}\n')
                return 0
            return 0 if replay_compare(read_bytes(argv[2]), read_bytes(MEAS)) else 3
        if mode == "decide":
            result = decide(json.loads(read_bytes(argv[2] if len(argv)>2 else MEAS)))
            sys.stdout.write(canonical(result))
            return 1 if "VOID" in result else 0
        if mode == "note":
            data = json.loads(read_bytes(argv[2]))
            sys.stdout.write(make_note(data, D_SHA, a_ok(argv[3]), a_ok(argv[4]), a_ok(argv[5])))
            return 0
        if mode == "derive-run":
            record = derive_run(a_ok(argv[2]), "--s1-binding" in argv)
            if record is None:
                raise Refused("derive-run capture failed")
            sys.stdout.write(canonical(record))
            return 0
        if mode == "e-entry":
            if "--capture-time" not in argv:
                raise Refused("explicit UTC --capture-time required")
            stamp = a_ok(argv[argv.index("--capture-time")+1])
            result = run_class_e_entry(a_ok(argv[2]), a_ok(argv[3]), stamp)
            sys.stdout.write(canonical({"entry": result["entry"], "entry_sha256": result["entry_sha256"], "errors": result["errors"]}))
            return 1 if result["errors"] else 0
        if mode in ("order", "verdict"):
            config = json.loads(read_bytes(argv[2]))
            if mode == "order":
                result = run_class_order(config, "--final" in argv)
                sys.stdout.write(canonical(result))
                return 1 if result["violations"] else 0
            result = run_class_verdict(config)
            sys.stdout.write(canonical(result)+result["verdict"]+"\n")
            return 1 if result["verdict"] == "VERDICT VOID" else 0
        if mode == "check":
            commit = a_ok(argv[2])
            frozen = a_ok(argv[argv.index("--freeze")+1])
            stage = argv[argv.index("--stage")+1] if "--stage" in argv else None
            errors = check_mode(commit, frozen, stage)
            output = {"check": "FAIL" if errors else "PASS", "errors": errors}
            if stage == "S1":
                if "--capture-config" not in argv:
                    raise Refused("S1 requires --capture-config for its repository-wide order-s1 capture")
                config = json.loads(read_bytes(argv[argv.index("--capture-config")+1]))
                capture = run_class_order(config)
                output["order_s1"] = capture
                output["errors"] += capture["violations"]
                output["check"] = "FAIL" if output["errors"] else "PASS"
            sys.stdout.write(canonical(output))
            return 1 if output["errors"] else 0
        raise Refused("unknown mode")
    except (CaptureFailed, Refused, OSError, ValueError, TypeError, KeyError, IndexError, AttributeError) as error:
        sys.stdout.write(canonical({"capture": "FAILED", "reason": str(error), "retry_after_completion_or_access_recovery": True}))
        return 3 if len(argv)>1 and argv[1] == "replay" else 2


def main(argv):
    return control_main(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
